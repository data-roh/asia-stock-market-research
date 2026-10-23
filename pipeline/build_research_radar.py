"""Build a public, source-linked research radar from public metadata only.

Run after scan_research_updates.py. No article/PDF content is downloaded or
summarized. A failed provider retains its previous public entries.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from html import unescape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "src/lib/content/research-radar.json"
UPDATES = Path(os.environ.get("RESEARCH_UPDATES_PATH", ROOT / ".state/research-updates.json"))
HKT = ZoneInfo("Asia/Hong_Kong")
TOPICS = {
    "asset pricing": "Asset pricing",
    "market microstructure": "Market microstructure",
    "portfolio optimization": "Portfolio construction",
    "algorithmic trading": "Trading systems",
    "financial machine learning": "Financial ML",
    "alternative data finance": "Alternative data",
}
TITLE_PATTERNS = {
    "asset pricing": r"asset pric|factor invest|factor model|equity risk premium|stock return|return predict|cross.sectional return",
    "market microstructure": r"market microstructure|financial microstructure|order book|limit order|market mak|market liquidity|trading liquidity|price impact|bid.ask|tick size|volatility and liquidity",
    "portfolio optimization": r"portfolio|asset allocation|risk parity|mean.variance",
    "algorithmic trading": r"algorithmic trad|trading strateg|trade execution|backtest|high.frequency trad",
    "financial machine learning": r"(?:machine learning|neural|deep learning|transformer|language model|\bllm\b).*(?:financ|market|stock|trad|invest|return)|(?:financ|market|stock|trad|invest|return).*(?:machine learning|neural|deep learning|transformer|language model|\bllm\b)",
    "alternative data finance": r"alternative data|satellite data|credit.card data|web traffic|transaction data|earnings.transcript",
}
GITHUB_QUERIES = [
    "topic:quantitative-finance", "topic:algorithmic-trading",
    "topic:backtesting", "topic:portfolio-optimization",
    "topic:market-microstructure", "topic:financial-machine-learning",
]
MAX_REPOS = 90
MAX_PAPERS = 80
MAX_INSTITUTIONAL = 300


def get_json(url: str, token: str = "") -> dict:
    headers = {"Accept": "application/json", "User-Agent": "ASMR-Research-Radar/1.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    with urlopen(Request(url, headers=headers), timeout=25) as response:
        return json.load(response)


def clean(value: str, limit: int = 260) -> str:
    return " ".join(unescape(re.sub(r"<[^>]*>", " ", value or "")).split())[:limit]


class DescriptionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.description = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "meta":
            return
        values = dict(attrs)
        key = (values.get("name") or values.get("property") or "").lower()
        if key in {"description", "og:description"} and not self.description:
            self.description = clean(values.get("content") or "", 220)


def page_description(url: str) -> str:
    try:
        request = Request(url, headers={"User-Agent": "ASMR-Research-Radar/1.0", "Accept": "text/html"})
        with urlopen(request, timeout=10) as response:
            if "html" not in response.headers.get("Content-Type", "").lower():
                return ""
            parser = DescriptionParser()
            parser.feed(response.read(250_000).decode("utf-8", errors="replace"))
            return parser.description
    except (OSError, ValueError):
        return ""


def date_from_crossref(value: dict) -> str | None:
    parts = value.get("date-parts", [[]])[0]
    if len(parts) >= 3:
        try:
            return datetime(*parts[:3], tzinfo=timezone.utc).isoformat()
        except (TypeError, ValueError):
            pass
    return None


def papers(now: datetime, previous: list[dict]) -> tuple[list[dict], list[str]]:
    found = {p["id"]: p for p in previous}
    errors = []
    since = (now - timedelta(days=21)).date().isoformat()
    for query, label in TOPICS.items():
        params = urlencode({
            "query.bibliographic": query,
            "filter": f"from-created-date:{since}",
            "sort": "created", "order": "desc", "rows": 40,
        })
        try:
            data = get_json(f"https://api.crossref.org/prefixes/10.2139/works?{params}")
            for work in data["message"]["items"]:
                doi = work.get("DOI", "").lower()
                if not re.fullmatch(r"10\.2139/ssrn\.\d+", doi):
                    continue
                title = clean((work.get("title") or [""])[0])
                if len(title) < 12 or not re.search(TITLE_PATTERNS[query], title, re.I):
                    continue
                paper_id = doi.rsplit(".", 1)[-1]
                created = date_from_crossref(work.get("created", {}))
                if not created:
                    continue
                old = found.get(doi, {})
                found[doi] = {
                    "id": doi, "title": title,
                    "url": f"https://papers.ssrn.com/sol3/papers.cfm?abstract_id={paper_id}",
                    "indexedAt": created,  # DOI registration, not necessarily SSRN posting.
                    "topics": sorted(set(old.get("topics", [])) | {label}),
                    "abstract": clean(work.get("abstract", ""), 220),
                }
        except (KeyError, OSError, ValueError) as error:
            errors.append(f"SSRN metadata ({query}): {str(error)[:120]}")
    ordered = sorted(found.values(), key=lambda p: p["indexedAt"], reverse=True)
    return ordered[:MAX_PAPERS], errors


def github(now: datetime, previous: list[dict]) -> tuple[list[dict], list[str]]:
    found = {r["id"]: r for r in previous}
    errors = []
    token = os.environ.get("GITHUB_TOKEN", "")
    since = (now - timedelta(days=14)).date().isoformat()
    for topic in GITHUB_QUERIES:
        # Include recent discoveries as well as established repos. Search's
        # stars sort is lifetime stars, never weekly star growth.
        for new_only in (False, True):
            q = f"{topic} fork:false archived:false"
            if new_only:
                q += f" created:>={since}"
            params = urlencode({"q": q, "sort": "stars", "order": "desc", "per_page": 20})
            try:
                data = get_json(f"https://api.github.com/search/repositories?{params}", token)
                for repo in data["items"]:
                    old = found.get(str(repo["id"]), {})
                    history = old.get("history", [])
                    today = now.astimezone(HKT).date().isoformat()
                    history = [point for point in history if point["date"] != today]
                    history.append({"date": today, "stars": repo["stargazers_count"]})
                    history = [point for point in history if point["date"] >= (now.astimezone(HKT).date() - timedelta(days=35)).isoformat()]
                    found[str(repo["id"])] = {
                        "id": str(repo["id"]), "name": repo["full_name"],
                        "url": repo["html_url"], "description": clean(repo.get("description") or ""),
                        "stars": repo["stargazers_count"], "createdAt": repo["created_at"],
                        "updatedAt": repo["pushed_at"], "history": history,
                    }
            except (KeyError, OSError, ValueError) as error:
                errors.append(f"GitHub ({topic}): {str(error)[:120]}")
    target = (now.astimezone(HKT).date() - timedelta(days=7)).isoformat()
    for repo in found.values():
        baseline = next((point for point in reversed(repo["history"]) if point["date"] <= target), None)
        repo["stars7d"] = repo["stars"] - baseline["stars"] if baseline else None
    ordered = sorted(found.values(), key=lambda r: (r["stars7d"] is not None, r["stars7d"] or 0, r["stars"]), reverse=True)
    return ordered[:MAX_REPOS], errors


def institutional(previous: list[dict]) -> tuple[list[dict], list[str]]:
    if not UPDATES.exists():
        return previous, ["Institutional scan state unavailable"]
    try:
        state = json.loads(UPDATES.read_text(encoding="utf-8"))
        items = state.get("items", [])
        good = []
        for item in items:
            url = item.get("url", "")
            if not url.startswith("https://") or not item.get("title"):
                continue
            good.append({
                "id": item.get("key") or url,
                "title": clean(item["title"]), "url": url,
                "sourceId": item.get("sourceId", ""),
                "publishedAt": item.get("publishedAt"),
                "detectedAt": item.get("detectedAt"),
                "excerpt": clean(item.get("summary") or "", 220),
            })
        merged = {item["id"]: item for item in previous}
        for item in good:
            old = merged.get(item["id"], {})
            if not item["excerpt"] and old.get("url") == item["url"]:
                item["excerpt"] = old.get("excerpt", "")
                if old.get("descriptionChecked"):
                    item["descriptionChecked"] = True
            merged[item["id"]] = item
        result = sorted(merged.values(), key=lambda x: x.get("publishedAt") or x.get("detectedAt") or "", reverse=True)
        candidates = [x for x in result[:18] if not x["excerpt"] and not x.get("descriptionChecked")]
        with ThreadPoolExecutor(max_workers=4) as executor:
            descriptions = list(executor.map(lambda x: page_description(x["url"]), candidates))
        for item, description in zip(candidates, descriptions):
            item["excerpt"] = description
            item["descriptionChecked"] = True
        return result[:MAX_INSTITUTIONAL], []
    except (OSError, ValueError) as error:
        return previous, [f"Institutional scan: {str(error)[:120]}"]


def weekly(now: datetime, data: dict) -> dict:
    local = now.astimezone(HKT)
    # The last completed Hong Kong Monday–Sunday period is stable all week.
    this_monday = local.date() - timedelta(days=local.weekday())
    start = this_monday - timedelta(days=7)
    end = this_monday
    def in_week(value: str | None) -> bool:
        try:
            return value is not None and start <= datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(HKT).date() < end
        except ValueError:
            return False
    institution = [x for x in data["institutional"] if in_week(x.get("publishedAt") or x.get("detectedAt"))][:12]
    paper = [x for x in data["ssrn"] if in_week(x.get("indexedAt"))][:8]
    repo = [x for x in data["github"] if (x.get("stars7d") or 0) > 0][:8]
    return {"start": start.isoformat(), "endExclusive": end.isoformat(),
            "institutionalIds": [x["id"] for x in institution],
            "ssrnIds": [x["id"] for x in paper],
            "githubIds": [x["id"] for x in repo]}


def main() -> None:
    now = datetime.now(timezone.utc)
    old = json.loads(OUTPUT.read_text(encoding="utf-8")) if OUTPUT.exists() else {}
    institutions, e1 = institutional(old.get("institutional", []))
    ssrn, e2 = papers(now, old.get("ssrn", []))
    repos, e3 = github(now, old.get("github", []))
    result = {"lastCheckedAt": now.isoformat(), "institutional": institutions,
              "ssrn": ssrn, "github": repos}
    result["weekly"] = weekly(now, result)
    result["sourceErrors"] = e1 + e2 + e3
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Radar: {len(institutions)} institutional, {len(ssrn)} SSRN, {len(repos)} GitHub; {len(result['sourceErrors'])} errors")


if __name__ == "__main__":
    main()
