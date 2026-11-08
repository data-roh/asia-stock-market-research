"""Audit the configured institutional research links and write a CSV snapshot."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import csv
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from scan_research_updates import parse_listing


ROOT = Path(__file__).resolve().parents[1]
SOURCES_FILE = ROOT / "src/lib/content/institutional-research.ts"
FEEDS_FILE = ROOT / "src/lib/content/research-feeds.json"
OUTPUT_FILE = ROOT / "data/source_audit.csv"
REPORT_FILE = ROOT / "docs/institutional_source_audit.md"
FIELDS = [
    "institution", "publication", "official_url", "listing_url", "rss_available",
    "rss_url", "sitemap_available", "api_or_json_endpoint", "server_rendered",
    "javascript_required", "browser_required", "publication_date_visible",
    "article_url_visible", "pagination_type", "access_restriction",
    "estimated_update_frequency", "recommended_collection_method", "confidence",
    "classification", "notes",
]
SOURCE_PATTERN = re.compile(
    r"\{ id: '([^']+)', name: '([^']+)', url: '([^']+)'.*?cadence: '([^']+)'"
)


def sources() -> list[dict[str, str]]:
    source_text = SOURCES_FILE.read_text(encoding="utf-8")
    feed_config = json.loads(FEEDS_FILE.read_text(encoding="utf-8"))
    feed_urls = {item["sourceId"]: item["feedUrl"] for item in feed_config.get("feeds", [])}
    page_urls = {item["sourceId"]: item["pageUrl"] for item in feed_config.get("pages", [])}
    items = []
    for source_id, name, url, cadence in SOURCE_PATTERN.findall(source_text):
        items.append({
            "id": source_id,
            "name": name,
            "url": url,
            "cadence": cadence,
            "feed_url": feed_urls.get(source_id, ""),
            "listing_url": page_urls.get(source_id, url),
        })
    return items


def inspect(source: dict[str, str]) -> dict[str, str]:
    listing_url = source["listing_url"]
    result = {
        "institution": source["name"].split(" · ")[0],
        "publication": source["name"].split(" · ", 1)[1] if " · " in source["name"] else source["id"],
        "official_url": source["url"],
        "listing_url": listing_url,
        "rss_available": "no",
        "rss_url": source["feed_url"],
        "sitemap_available": "not checked",
        "api_or_json_endpoint": "not checked",
        "server_rendered": "unknown",
        "javascript_required": "unknown",
        "browser_required": "unknown",
        "publication_date_visible": "not checked",
        "article_url_visible": "unknown",
        "pagination_type": "not checked",
        "access_restriction": "none observed",
        "estimated_update_frequency": source["cadence"],
        "recommended_collection_method": "official RSS/Atom" if source["feed_url"] else "official HTML listing",
        "confidence": "medium" if source["feed_url"] else "low",
        "notes": "",
    }
    if source["feed_url"]:
        rss_request = Request(
            source["feed_url"],
            headers={"User-Agent": "ASMRResearchSourceAudit/1.0", "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml"},
        )
        try:
            with urlopen(rss_request, timeout=12) as response:
                ET.fromstring(response.read(1_000_000))
            result["rss_available"] = "yes"
        except (HTTPError, TimeoutError, URLError, OSError, ET.ParseError, ValueError) as error:
            result["rss_available"] = "configured, check failed"
            result["notes"] = f"Configured feed check failed: {type(error).__name__}; "
    request = Request(
        listing_url,
        headers={
            "User-Agent": "ASMRResearchSourceAudit/1.0 (+https://data-roh.github.io/asia-stock-market-research/)",
            "Accept": "text/html,application/xhtml+xml,application/xml",
        },
    )
    try:
        with urlopen(request, timeout=15) as response:
            content_type = response.headers.get("Content-Type", "").lower()
            body = response.read(1_500_000)
            final_url = response.geturl()
            result["listing_url"] = final_url
            if "html" not in content_type:
                result["access_restriction"] = f"unexpected content type: {content_type or 'unknown'}"
                result["notes"] = "Live check succeeded but response was not HTML."
                result["recommended_collection_method"] = "custom adapter review"
                return result
            found = parse_listing(
                body, final_url, source["id"], datetime.now(timezone.utc).isoformat()
            )
            result["server_rendered"] = "yes" if found else "not established"
            result["article_url_visible"] = "yes" if found else "no static candidates"
            result["browser_required"] = "no" if found else "manual review"
            result["javascript_required"] = "unknown"
            script_count = len(re.findall(rb"<script\b", body, re.I))
            result["notes"] += (
                f"HTTP {response.status}; {len(found)} candidate links found by the current static parser; "
                f"{script_count} script tags in sampled HTML. "
                "Dates, pagination, RSS alternatives and client-side rendering were not exhaustively audited."
            )
            if found:
                result["confidence"] = "medium"
                if not source["feed_url"]:
                    result["recommended_collection_method"] = "official HTML listing; browser verification"
            else:
                result["confidence"] = "low"
                result["javascript_required"] = "possible" if script_count >= 15 else "unknown"
                result["browser_required"] = "possible" if script_count >= 15 else "manual review"
                result["recommended_collection_method"] = (
                    "browser rendering investigation" if script_count >= 15 else "source-specific parser/manual review"
                )
    except HTTPError as error:
        result["access_restriction"] = f"HTTP {error.code}"
        result["notes"] = "Automated access was denied or unavailable; this is not proof the public page is invalid."
        result["recommended_collection_method"] = "manual review; do not bypass access controls"
        result["confidence"] = "low"
    except (TimeoutError, URLError, OSError, ValueError) as error:
        result["access_restriction"] = type(error).__name__
        result["notes"] = f"Automated check failed: {str(error)[:160]}"
        result["recommended_collection_method"] = "manual review; retry before implementation"
        result["confidence"] = "low"
    return result


def category(row: dict[str, str]) -> str:
    if row["rss_available"] == "yes":
        return "A"
    if row["access_restriction"] != "none observed" and row["article_url_visible"] == "unknown":
        return "E"
    if row["article_url_visible"] == "yes":
        return "B"
    return "C" if row["javascript_required"] == "possible" else "D"


def main() -> None:
    all_sources = sources()
    with ThreadPoolExecutor(max_workers=6) as executor:
        rows = list(executor.map(inspect, all_sources))
    counts: dict[str, int] = {}
    for row in rows:
        label = category(row)
        counts[label] = counts.get(label, 0) + 1
        row["classification"] = label
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    checked_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_lines = [
        "# Institutional Source Audit",
        "",
        f"Audit snapshot: {checked_at} (UTC). Sources are taken from the Institutional Research Library.",
        "",
        f"Total listed sources: {len(rows)}.",
        "",
        "## Preliminary collection classification",
        "",
        "| Class | Sources | Meaning |",
        "|---|---:|---|",
        f"| A | {counts.get('A', 0)} | A configured RSS/Atom feed parsed successfully during this snapshot. |",
        f"| B | {counts.get('B', 0)} | Static HTML candidate links were found by the existing parser. |",
        f"| C | {counts.get('C', 0)} | JavaScript/browser rendering may be needed; confirm with a browser audit. |",
        f"| D | {counts.get('D', 0)} | No static candidate was extracted; a source-specific parser or manual review is needed. |",
        f"| E | {counts.get('E', 0)} | Automated access failed or was denied; retry or review manually without bypassing restrictions. |",
        "",
        "The generated CSV records live URL/feed checks and parser candidate counts. These are preliminary access and discovery observations, not proof of completeness or date accuracy. Sitemap, API, pagination and publication-date visibility remain unchecked. A zero-result scan is not evidence that a source published nothing.",
        "",
        "## Phase 1",
        "",
        "AQR, Citadel Securities, Man Group, Apollo and Oaktree are the representative sources configured for browser verification in `data/institutional_sources.json`. They are still subject to the same official-domain and article-page checks; access challenges are reported, never bypassed.",
        "",
        "## Refresh",
        "",
        "Run `python pipeline/audit_research_sources.py` to regenerate `data/source_audit.csv` and this report. Re-audit before treating any source as production-complete.",
    ]
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Audited {len(rows)} library sources: {counts}")


if __name__ == "__main__":
    main()
