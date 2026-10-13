from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FEEDS_PATH = PROJECT_ROOT / "src" / "lib" / "content" / "research-feeds.json"
UPDATES_PATH = PROJECT_ROOT / "src" / "lib" / "content" / "research-updates.json"
MAX_FEED_ITEMS = 30
MAX_STORED_ITEMS = 200
MAX_SEEN_KEYS = 2000


class PlainTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


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

    for feed in feed_config["feeds"]:
        source_id = feed["sourceId"]
        entries, error = fetch_feed(source_id, feed["feedUrl"])
        source_checks.append({"sourceId": source_id, "ok": error is None, "error": error})
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