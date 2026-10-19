from __future__ import annotations

from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from html import escape
import json
import os
from pathlib import Path
import smtplib
from zoneinfo import ZoneInfo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = Path(os.environ.get("RESEARCH_UPDATES_PATH", PROJECT_ROOT / ".state" / "research-updates.json"))
PREVIEW_PATH = Path(os.environ.get("NEWSLETTER_PREVIEW_PATH", Path("newsletter-preview.html")))
HONG_KONG = ZoneInfo("Asia/Hong_Kong")


def parse_datetime(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def current_week_items(
    items: list[dict[str, str | None]], checked_at: str
) -> list[dict[str, str | None]]:
    reference = parse_datetime(checked_at) or datetime.now(timezone.utc)
    local_reference = reference.astimezone(HONG_KONG)
    week_start = local_reference.replace(hour=0, minute=0, second=0, microsecond=0)
    week_start -= timedelta(days=week_start.weekday())
    week_end = week_start + timedelta(days=7)
    current_items = []
    for item in items:
        item_date = parse_datetime(item.get("publishedAt") or item.get("detectedAt") or "")
        if item_date is not None and week_start <= item_date.astimezone(HONG_KONG) < week_end:
            current_items.append(item)
    return current_items


def render_newsletter(items: list[dict[str, str | None]], checked_at: str) -> tuple[str, str, str]:
    reference = parse_datetime(checked_at) or datetime.now(timezone.utc)
    week_start = reference.astimezone(HONG_KONG).date()
    week_start -= timedelta(days=week_start.weekday())
    date_label = f"Week of {week_start.isoformat()}"
    subject = f"ASMR Research Digest | {date_label}"
    entries_html = "\n".join(
        "<li><a href=\"{url}\">{title}</a><p>{source} · {date}</p></li>".format(
            url=escape(item["url"] or "", quote=True),
            title=escape(item["title"] or ""),
            source=escape(item["sourceId"]),
            date=escape((item.get("publishedAt") or item.get("detectedAt") or "Date unavailable")[:10]),
        )
        for item in items
    )
    plain_entries = "\n".join(
        f"- {item.get('title', '')} ({item.get('sourceId', '')})\n  {item.get('url', '')}"
        for item in items
    )
    html_body = (
        "<!doctype html><html><body><main style=\"max-width:680px;margin:0 auto;"
        "font:16px/1.5 Arial,sans-serif;color:#202421\">"
        f"<h1>ASMR Research Digest</h1><p>{escape(date_label)} · "
        f"{len(items)} new items</p><ul>{entries_html}</ul>"
        "<p>Titles and links only. Read each publisher’s original page for full content.</p>"
        "</main></body></html>"
    )
    text_body = f"ASMR Research Digest | {date_label}\n\n{plain_entries}\n\nTitles and links only."
    return subject, html_body, text_body


def main() -> None:
    report = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    checked_at = report.get("lastCheckedAt") or datetime.now(timezone.utc).isoformat()
    pending_items = report.get("pendingItems", [])
    items = current_week_items(pending_items, checked_at)
    if len(items) != len(pending_items):
        report["pendingItems"] = items
        STATE_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not items:
        print("No current-week research items; no newsletter generated.")
        return

    subject, html_body, text_body = render_newsletter(items, checked_at)
    PREVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    PREVIEW_PATH.write_text(html_body, encoding="utf-8")
    print(f"Newsletter preview created: {PREVIEW_PATH} ({len(items)} items)")

    host = os.environ.get("SMTP_HOST")
    username = os.environ.get("SMTP_USERNAME")
    password = os.environ.get("SMTP_PASSWORD")
    recipients = [
        address.strip()
        for address in os.environ.get("NEWSLETTER_TO", "").replace(";", ",").split(",")
        if address.strip()
    ]
    if not all((host, username, password, recipients)):
        print("Email not sent: configure SMTP_HOST, SMTP_USERNAME, SMTP_PASSWORD, and NEWSLETTER_TO.")
        return

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = os.environ.get("SMTP_FROM") or username
    message["To"] = ", ".join(recipients)
    message.set_content(text_body)
    message.add_alternative(html_body, subtype="html")

    port = int(os.environ.get("SMTP_PORT") or "587")
    if port == 465:
        with smtplib.SMTP_SSL(host, port, timeout=30) as server:
            server.login(username, password)
            server.send_message(message)
    else:
        with smtplib.SMTP(host, port, timeout=30) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(message)

    report["pendingItems"] = []
    STATE_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Newsletter sent to {len(recipients)} recipient(s).")


if __name__ == "__main__":
    main()
