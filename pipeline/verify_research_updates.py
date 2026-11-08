"""Verify Phase 1 research candidates against official publisher pages."""

from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
from difflib import SequenceMatcher
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
SOURCES_PATH = ROOT / "data/institutional_sources.json"
OUTPUT_PATH = Path(os.environ.get("RESEARCH_UPDATES_PATH", ROOT / ".state/research-updates.json"))
RADAR_PATH = ROOT / "src/lib/content/research-radar.json"
TRACKING_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}
CHALLENGE_TERMS = ("captcha", "verify you are human", "access denied", "checking your browser")
ASIA_TERMS = {
    "asia": 30, "asian": 30, "japan": 25, "japanese": 25, "china": 25, "chinese": 25,
    "korea": 25, "korean": 25, "taiwan": 25, "india": 20, "hong kong": 20,
    "singapore": 20, "semiconductor": 15, "emerging markets": 10, "em asia": 10,
}
TOPIC_TERMS = {
    "Macro": ("econom", "inflation", "growth", "gdp", "monetary", "fiscal", "macro"),
    "Equities": ("equity", "equities", "stocks", "shares"),
    "Rates": ("rates", "yield", "bonds", "fixed income"),
    "Credit": ("credit", "spread", "default"),
    "FX": ("currency", "currencies", "exchange rate", "forex"),
    "Commodities": ("commodity", "commodities", "oil", "energy", "gold"),
    "Volatility": ("volatility", "options", "vix"),
    "Market Structure": ("market structure", "liquidity", "positioning", "flows", "market maker"),
    "Quant": ("quant", "systematic", "factor", "algorithmic", "machine learning"),
    "Private Markets": ("private equity", "private credit", "private markets", "real estate"),
    "Technology": ("technology", "artificial intelligence", " ai ", "semiconductor", "chip"),
}
CONTENT_TYPES = (
    ("Podcast", ("podcast", "listen to")),
    ("Outlook", ("outlook", "year ahead", "quarterly view")),
    ("Memo", ("memo", "letter to investors")),
    ("Report", ("report", "white paper", "research")),
    ("Market Commentary", ("market update", "market insights", "market commentary")),
)


def canonical_url(value: str) -> str:
    parts = urlsplit(value.strip())
    query = [
        (key, val) for key, val in parse_qsl(parts.query, keep_blank_values=True)
        if not key.lower().startswith("utm_") and key.lower() not in TRACKING_KEYS
    ]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), urlencode(query), ""))


def normalized_title(value: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value.casefold()).split())


def extract_article_id(source_id: str, title: str, url: str) -> str:
    value = "|".join((source_id, normalized_title(title), canonical_url(url)))
    return sha256(value.encode("utf-8")).hexdigest()


def official_host(url: str, domains: list[str]) -> bool:
    host = (urlsplit(url).hostname or "").lower()
    return any(host == domain.lower() or host.endswith("." + domain.lower()) for domain in domains)


def title_matches(candidate: str, actual: str) -> bool:
    left, right = normalized_title(candidate), normalized_title(actual)
    if not left or not right:
        return False
    return left in right or right in left or SequenceMatcher(None, left, right).ratio() >= 0.78


def classify(title: str, excerpt: str) -> tuple[list[str], list[str], int, str, str]:
    text = f" {title.casefold()} {excerpt.casefold()} "
    topics = [
        topic for topic, terms in TOPIC_TERMS.items()
        if any(term in text for term in terms)
    ]
    regions = [
        region for region, terms in (
            ("Asia", ("asia", "asian", "em asia")),
            ("China", ("china", "chinese")),
            ("Japan", ("japan", "japanese")),
            ("Korea", ("korea", "korean")),
            ("Taiwan", ("taiwan",)),
            ("India", ("india", "indian")),
            ("Hong Kong", ("hong kong",)),
            ("Singapore", ("singapore",)),
        )
        if any(term in text for term in terms)
    ]
    relevance = min(100, sum(weight for term, weight in ASIA_TERMS.items() if term in text))
    asmr_reason = ""
    if relevance >= 25:
        asmr_reason = "Direct Asia-market references may support a regional comparison in Asia Stock Market Review."
    elif any(topic in topics for topic in ("Market Structure", "Quant", "Equities", "Rates")):
        asmr_reason = "The market framework may be reusable for analysis of Asian markets."
    content_type = next(
        (label for label, terms in CONTENT_TYPES if any(term in text for term in terms)),
        "Research Article",
    )
    return topics, regions or ["Global"], relevance, asmr_reason, content_type


def article_evidence(page, candidate: dict, source: dict, listing_url: str, checked_at: str) -> dict:
    url = canonical_url(candidate.get("url", ""))
    evidence = {
        "status": "UNVERIFIED",
        "confidence": "LOW",
        "verifiedAt": checked_at,
        "officialDomain": official_host(url, source["officialDomains"]),
        "listingPageMatch": False,
        "articlePageMatch": False,
        "titleMatch": False,
        "dateFound": False,
        "canonicalUrl": url,
    }
    if not evidence["officialDomain"]:
        evidence["reason"] = "Article URL is outside the configured official domains."
        return evidence

    try:
        listing_response = page.goto(listing_url, wait_until="domcontentloaded", timeout=25000)
        if not official_host(page.url, source["officialDomains"]):
            evidence["reason"] = "Official listing redirected outside the configured publisher domains."
            return evidence
        listing_text = page.locator("body").inner_text(timeout=10000).casefold()
        if any(term in listing_text for term in CHALLENGE_TERMS):
            evidence["reason"] = "The publisher listing presented an access challenge."
            return evidence
        links = page.locator("a[href]").evaluate_all("(nodes) => nodes.map(a => ({href: a.href, text: a.innerText}))")
        candidate_url = canonical_url(url)
        evidence["listingPageMatch"] = any(canonical_url(link["href"]) == candidate_url for link in links)
        listing_accessible = listing_response is not None and listing_response.status < 400
        if not listing_accessible or not evidence["listingPageMatch"]:
            evidence["status"] = "POSSIBLE_NEW"
            evidence["reason"] = "Candidate was not found on an accessible official listing page."
            return evidence

        article_response = page.goto(url, wait_until="domcontentloaded", timeout=25000)
        if article_response is None or article_response.status >= 400:
            evidence["status"] = "POSSIBLE_NEW"
            evidence["reason"] = "Official article page did not return a successful response."
            return evidence
        if not official_host(page.url, source["officialDomains"]):
            evidence["status"] = "POSSIBLE_NEW"
            evidence["reason"] = "Article redirected outside the configured publisher domains."
            return evidence
        page.locator("body").wait_for(state="visible", timeout=10000)
        body_text = page.locator("body").inner_text(timeout=10000).casefold()
        if any(term in body_text for term in CHALLENGE_TERMS):
            evidence["status"] = "POSSIBLE_NEW"
            evidence["reason"] = "The publisher article presented an access challenge."
            return evidence
        heading = page.locator("h1").first
        actual_title = heading.inner_text(timeout=5000).strip() if heading.count() else ""
        if not actual_title:
            actual_title = page.locator('meta[property="og:title"]').get_attribute("content") or ""
        evidence["articlePageMatch"] = True
        evidence["titleMatch"] = title_matches(candidate.get("title", ""), actual_title)
        evidence["title"] = actual_title[:240]
        canonical = page.locator('link[rel="canonical"]').get_attribute("href")
        if canonical:
            canonical = canonical_url(urljoin(page.url, canonical))
            if not official_host(canonical, source["officialDomains"]):
                evidence["status"] = "POSSIBLE_NEW"
                evidence["reason"] = "The article canonical URL is outside the configured publisher domains."
                return evidence
            evidence["canonicalUrl"] = canonical
        date_locator = page.locator(
            'time[datetime], meta[property="article:published_time"], '
            'meta[name="date"], meta[itemprop="datePublished"]'
        ).first
        if date_locator.count():
            date_value = date_locator.get_attribute("datetime") or date_locator.get_attribute("content") or ""
            evidence["publishedAt"] = date_value[:40] or None
            evidence["dateFound"] = bool(date_value)
        description = page.locator('meta[property="og:description"], meta[name="description"]').first
        excerpt = description.get_attribute("content") if description.count() else ""
        evidence["excerpt"] = (excerpt or candidate.get("summary") or "")[:500]
        article_text = page.locator("article, main").first
        content = article_text.inner_text(timeout=5000) if article_text.count() else ""
        evidence["contentWordCount"] = len(content.split())
        evidence["contentHash"] = sha256(content.encode("utf-8")).hexdigest() if content else ""
        evidence["extractionMethod"] = "article_or_main_text" if content else "publisher_metadata"
        if not evidence["titleMatch"]:
            evidence["status"] = "POSSIBLE_NEW"
            evidence["reason"] = "Official article page title did not sufficiently match the discovered title."
            return evidence
        evidence["status"] = "VERIFIED_NEW"
        evidence["confidence"] = "HIGH" if evidence["dateFound"] else "MEDIUM"
        evidence["reason"] = "Official listing and article pages match the candidate."
        return evidence
    except (PlaywrightError, PlaywrightTimeoutError, ValueError) as error:
        evidence["status"] = "POSSIBLE_NEW"
        evidence["reason"] = f"Browser verification failed: {str(error)[:180]}"
        return evidence


def verification_summary(candidates: list[dict], checked_at: str) -> dict:
    counts: dict[str, int] = {}
    for item in candidates:
        status = item.get("verification", {}).get("status", "UNVERIFIED")
        counts[status] = counts.get(status, 0) + 1
    return {
        "completedAt": checked_at,
        "candidateCount": len(candidates),
        "verifiedNewCount": counts.get("VERIFIED_NEW", 0),
        "verifiedExistingCount": counts.get("VERIFIED_EXISTING", 0),
        "needsReviewCount": counts.get("POSSIBLE_NEW", 0),
        "unverifiedCount": counts.get("UNVERIFIED", 0),
    }


def verification_candidates(state: dict, sources: dict) -> list[dict]:
    pending_keys = set(state.get("pendingVerificationKeys", []))
    return [
        item for item in state.get("items", [])
        if item.get("sourceId") in sources and item.get("key") in pending_keys
    ]


def main() -> None:
    config = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    sources = {item["sourceId"]: item for item in config["sources"]}
    if not OUTPUT_PATH.exists():
        raise FileNotFoundError(f"Research scan state not found: {OUTPUT_PATH}")
    state = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    checked_at = datetime.now(timezone.utc).isoformat()
    previous_radar = json.loads(RADAR_PATH.read_text(encoding="utf-8")) if RADAR_PATH.exists() else {}
    existing_verified_ids = {
        item["id"] for item in previous_radar.get("institutional", [])
        if item.get("verification", {}).get("status") in {"VERIFIED_NEW", "VERIFIED_EXISTING"}
    }
    existing_verified_urls = {
        canonical_url(item.get("url", "")) for item in previous_radar.get("institutional", [])
        if item.get("verification", {}).get("status") in {"VERIFIED_NEW", "VERIFIED_EXISTING"}
    }
    checks = {item["sourceId"]: item for item in state.get("sourceChecks", [])}

    candidates = verification_candidates(state, sources)
    if candidates:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.set_default_navigation_timeout(25000)
            for item in candidates:
                source = sources[item["sourceId"]]
                article_id = extract_article_id(item["sourceId"], item.get("title", ""), item.get("url", ""))
                is_existing = (
                    article_id in existing_verified_ids
                    or canonical_url(item.get("url", "")) in existing_verified_urls
                )
                evidence = article_evidence(page, item, source, source["listingUrl"], checked_at)
                if evidence["status"] == "VERIFIED_NEW" and is_existing:
                    evidence["status"] = "VERIFIED_EXISTING"
                    evidence["reason"] = "A matching article was already verified in the published radar history."
                evidence["articleId"] = article_id
                item["articleId"] = article_id
                item["verification"] = evidence
                item["verificationAttempts"] = item.get("verificationAttempts", 0) + 1
                item["firstSeenAt"] = item.get("firstSeenAt") or item.get("detectedAt") or checked_at
                item["publishedAt"] = evidence.get("publishedAt") or item.get("publishedAt")
                item["url"] = evidence.get("canonicalUrl") or item["url"]
                item["summary"] = evidence.get("excerpt") or item.get("summary", "")
                topics, regions, relevance, asmr_reason, content_type = classify(item.get("title", ""), item["summary"])
                item["topics"] = topics
                item["regions"] = regions
                item["asiaRelevance"] = relevance
                item["researchPriority"] = round(relevance * 0.7 + source["priority"] * 0.3)
                item["asmrCandidate"] = bool(asmr_reason)
                item["asmrReason"] = asmr_reason
                item["contentType"] = content_type
                item["summaryBasis"] = "official_metadata" if item["summary"] else "unavailable"
            browser.close()

    state["sourceChecks"] = list(checks.values())
    state["lastVerificationAt"] = checked_at
    state["verificationRun"] = verification_summary(candidates, checked_at)
    state["pendingVerificationKeys"] = [
        item["key"] for item in candidates
        if item.get("verification", {}).get("status") in {"POSSIBLE_NEW", "UNVERIFIED"}
        and item.get("verificationAttempts", 0) < 3
    ]
    OUTPUT_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Verification run: {state['verificationRun']}")


if __name__ == "__main__":
    main()
