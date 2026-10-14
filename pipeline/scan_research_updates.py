from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urldefrag, urljoin, urlsplit, urlunsplit
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FEEDS_PATH = PROJECT_ROOT / "src" / "lib" / "content" / "research-feeds.json"
UPDATES_PATH = PROJECT_ROOT / "src" / "lib" / "content" / "research-updates.json"
MAX_FEED_ITEMS = 30
MAX_STORED_ITEMS = 200
MAX_SEEN_KEYS = 2000
MAX_PAGE_ITEMS = 40
MAX_WORKERS = 5
CONTENT_PATH_HINTS = {
    "article",
    "articles",
    "blog",
    "chart",
    "charts",
    "comment",
    "insight",
    "insights",
    "memo",
    "news",
    "perspectives",
    "publication",
    "publications",
    "research",
    "report",
    "story",
    "teaser",
}


class PlainTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


class ListingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.href: str | None = None
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a" and self.href is None:
            self.href = dict(attrs).get("href")
            self.parts = []

    def handle_data(self, data: str) -> None:
        if self.href is not None:
            self.parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.href is not None:
            self.links.append((self.href, " ".join(self.parts)))
            self.href = None
            self.parts = []


def plain_text(value: str) -> str:
    parser = PlainTextParser()
    parser.feed(unescape(value))
    return " ".join(" ".join(parser.parts).split())


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def child_text(element: ET.Element, names: set[str]) -> str:
    for child in element:
        if local_name(child.tag) in names:
            return " ".join(child.itertext()).strip()
    return ""


def item_link(element: ET.Element) -> str:
    for child in element:
        if local_name(child.tag) == "link":
            href = child.attrib.get("href", "").strip()
            if href:
                return href
            return (child.text or "").strip()
    return ""


def iso_datetime(value: str) -> str | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        try:
            parsed = parsedate_to_datetime(value)
        except (TypeError, ValueError, OverflowError):
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc).isoformat()


def parse_feed(feed_bytes: bytes, source_id: str) -> list[dict[str, str | None]]:
    root = ET.fromstring(feed_bytes)
    entries = [element for element in root.iter() if local_name(element.tag) in {"item", "entry"}]
    items: list[dict[str, str | None]] = []

    for entry in entries[:MAX_FEED_ITEMS]:
        title = plain_text(child_text(entry, {"title"}))
        url = item_link(entry)
        if not title or not url.startswith(("https://", "http://")):
            continue

        identifier = child_text(entry, {"guid", "id"}) or url
        summary = plain_text(child_text(entry, {"description", "summary", "encoded", "content"}))
        published_at = iso_datetime(child_text(entry, {"pubdate", "published", "updated", "date"}))
        items.append(
            {
                "key": f"{source_id}:{identifier}",
                "sourceId": source_id,
                "title": title,
                "url": url,
                "publishedAt": published_at,
                "detectedAt": None,
                "summary": summary[:600],
            }
        )
    return items


def fetch_feed(source_id: str, feed_url: str) -> tuple[list[dict[str, str | None]], str | None]:
    request = urllib.request.Request(
        feed_url,
        headers={
            "User-Agent": "ASMRResearchUpdates/1.0 (+https://data-roh.github.io/asia-stock-market-research/)",
            "Accept": "application/atom+xml, application/rss+xml, application/xml, text/xml, */*",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            items = parse_feed(response.read(), source_id)
        return items, None
    except (urllib.error.URLError, TimeoutError, ET.ParseError, ValueError) as error:
        return [], str(error)[:240]


def canonical_url(url: str) -> str:
    parts = urlsplit(urldefrag(url)[0])
    query = "&".join(
        part
        for part in parts.query.split("&")
        if part and not part.lower().startswith(("utm_", "fbclid=", "srnd=", "partnerref="))
    )
    return urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/"), query, ""))


def listing_item_url(href: str, page_url: str) -> str | None:
    candidate = canonical_url(urljoin(page_url, href.strip()))
    parsed = urlsplit(candidate)
    page = urlsplit(page_url)
    if parsed.scheme not in {"https", "http"} or parsed.hostname != page.hostname:
        return None
    if parsed.path.rstrip("/") == page.path.rstrip("/"):
        return None
    path_parts = [part.casefold() for part in parsed.path.split("/") if part]
    slug = path_parts[-1] if path_parts else ""
    if re.search(r"\.(?:pdf|xml|rss|jpg|jpeg|png|svg|webp)$", slug):
        return None
    has_date_prefix = len(path_parts) >= 4 and all(part.isdigit() for part in path_parts[-4:-1])
    if len(slug) < 20 or not ("-" in slug or "_" in slug or has_date_prefix):
        return None
    if slug in {
        "about-us",
        "contact-us",
        "privacy-policy",
        "terms-and-conditions",
        "terms-of-use",
        "login-userid",
        "my-subscriptions",
        "search-insights",
        "investment-capabilities",
    }:
        return None
    has_content_path = any(hint in part for part in path_parts[:-1] for hint in CONTENT_PATH_HINTS)
    is_top_level_article = len(path_parts) == 1 and len(slug) >= 32
    if not (has_content_path or has_date_prefix or is_top_level_article):
        return None
    return candidate


def parse_listing(page_bytes: bytes, page_url: str, source_id: str, detected_at: str) -> list[dict[str, str | None]]:
    parser = ListingParser()
    parser.feed(page_bytes.decode("utf-8", errors="replace"))
    items: list[dict[str, str | None]] = []
    seen_urls: set[str] = set()
    ignored_titles = {"read more", "learn more", "view all", "see all posts", "load more", "subscribe", "sign up"}

    for href, raw_title in parser.links:
        title = plain_text(raw_title).strip(" ·|\t\n")
        url = listing_item_url(href, page_url)
        if not url or len(title) < 16 or len(title) > 240 or title.casefold() in ignored_titles:
            continue
        path_end = urlsplit(url).path.rstrip("/").rsplit("/", 1)[-1].casefold()
        if path_end in {"about", "contact", "login", "register", "subscribe", "search", "privacy-policy", "terms-of-use"}:
            continue
        if url in seen_urls:
            continue
        seen_urls.add(url)
        items.append(
            {
                "key": f"{source_id}:{url}",
                "sourceId": source_id,
                "title": title,
                "url": url,
                "publishedAt": None,
                "detectedAt": detected_at,
                "summary": "",
            }
        )
        if len(items) >= MAX_PAGE_ITEMS:
            break
    return items


def fetch_listing(source_id: str, page_url: str, detected_at: str) -> tuple[list[dict[str, str | None]], str | None]:
    request = urllib.request.Request(
        page_url,
        headers={
            "User-Agent": "ASMRResearchUpdates/1.0 (+https://data-roh.github.io/asia-stock-market-research/)",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            final_url = response.geturl()
            items = parse_listing(response.read(), final_url, source_id, detected_at)
        return items, None
    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        return [], str(error)[:240]


def main() -> None:
    feed_config = json.loads(FEEDS_PATH.read_text(encoding="utf-8"))
    previous = json.loads(UPDATES_PATH.read_text(encoding="utf-8"))
    previous_seen = list(dict.fromkeys(previous.get("seen", [])))
    checked_at = datetime.now(timezone.utc).isoformat()
    seen = previous_seen.copy()
    seen_set = set(previous_seen)
    baselined_source_ids = set(previous.get("baselinedSourceIds", []))
    new_items: list[dict[str, str | None]] = []
    source_checks: list[dict[str, str | bool | None]] = []
    feed_ids = {feed["sourceId"] for feed in feed_config["feeds"]}
    sources_to_check = [
        ("rss", feed["sourceId"], feed["feedUrl"])
        for feed in feed_config["feeds"]
    ] + [
        ("listing", page["sourceId"], page["pageUrl"])
        for page in feed_config.get("pages", [])
        if page["sourceId"] not in feed_ids
    ]

    def check_source(source: tuple[str, str, str]) -> tuple[str, str, list[dict[str, str | None]], str | None]:
        method, source_id, source_url = source
        if method == "rss":
            entries, error = fetch_feed(source_id, source_url)
        else:
            entries, error = fetch_listing(source_id, source_url, checked_at)
        return method, source_id, entries, error

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        checked_sources = list(executor.map(check_source, sources_to_check))

    for method, source_id, entries, error in checked_sources:
        source_checks.append({"sourceId": source_id, "method": method, "ok": error is None, "error": error})
        needs_baseline = source_id not in baselined_source_ids
        for entry in entries:
            key = entry["key"]
            if key not in seen_set:
                seen_set.add(key)
                seen.append(key)
                if not needs_baseline:
                    new_items.append(entry)
        if error is None:
            baselined_source_ids.add(source_id)

    combined_items = new_items + previous.get("items", [])
    combined_items.sort(key=lambda item: item.get("publishedAt") or "", reverse=True)
    report = {
        "lastCheckedAt": checked_at,
        "sourceChecks": source_checks,
        "baselinedSourceIds": sorted(baselined_source_ids),
        "items": combined_items[:MAX_STORED_ITEMS],
        "seen": seen[-MAX_SEEN_KEYS:],
    }
    UPDATES_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Checked {len(source_checks)} feeds; {len(new_items)} new items.")
    for check in source_checks:
        status = "ok" if check["ok"] else f"failed: {check['error']}"
        print(f"{check['sourceId']}: {status}")


if __name__ == "__main__":
    main()