"""Generate or send a validated daily digest of verified new research."""

from __future__ import annotations

from datetime import datetime, timezone
from email.message import EmailMessage
from html import escape
import json
import os
from pathlib import Path
import smtplib
import ssl
from zoneinfo import ZoneInfo

from verify_research_updates import official_host


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "src/lib/content/research-radar.json"
SOURCES_PATH = ROOT / "data/institutional_sources.json"
STATE_PATH = Path(os.environ.get("RESEARCH_RADAR_EMAIL_STATE", ROOT / ".state/research-radar-email.json"))
PREVIEW_DIR = Path(os.environ.get("RESEARCH_RADAR_EMAIL_PREVIEW", ROOT / "output/email_preview"))
ARCHIVE_DIR = ROOT / "output/daily"
SITE_URL = "https://data-roh.github.io/asia-stock-market-research/research-radar/"
HKT = ZoneInfo("Asia/Hong_Kong")


def collect_ready_items(radar: dict, domains_by_source: dict[str, list[str]], sent_ids: set[str]) -> list[dict]:
    ready = []
    seen = set()
    for item in radar.get("institutional", []):
        verification = item.get("verification") or {}
        article_id = item.get("id")
        url = item.get("url", "")
        if (
            verification.get("status") != "VERIFIED_NEW"
            or not article_id
            or article_id in sent_ids
            or article_id in seen
            or not item.get("title")
            or not official_host(url, domains_by_source.get(item.get("sourceId", ""), []))
        ):
            continue
        seen.add(article_id)
        ready.append(item)
    return sorted(
        ready,
        key=lambda item: (
            item.get("researchPriority") or 0,
            item.get("asiaRelevance") or 0,
            item.get("publishedAt") or "",
        ),
        reverse=True,
    )


def render_digest(items: list[dict], digest_date: str, radar: dict) -> tuple[str, str, str]:
    day_id = f"daily-{digest_date}"
    date_label = datetime.strptime(digest_date, "%Y-%m-%d").strftime("%d %b %Y").lstrip("0")
    top = [item for item in items if (item.get("researchPriority") or 0) >= 80]
    asia = [item for item in items if (item.get("asiaRelevance") or 0) >= 70 and item not in top]
    top_ids = {item["id"] for item in top + asia}
    other = [item for item in items if item["id"] not in top_ids]
    text = [f"Institutional Research Radar | {len(items)} new verified articles | {date_label}", ""]
    html_parts = [
        "<main style='max-width:760px;margin:auto;padding:20px;font:15px/1.6 Arial,sans-serif;color:#183344'>",
        f"<p style='color:#087f78;font-size:12px;font-weight:bold'>ASMR · RESEARCH RADAR</p><h1>Institutional Research Radar</h1><p>{escape(date_label)} · {len(items)} new verified articles</p>",
    ]

    def add_section(title: str, rows: list[dict], detailed: bool) -> None:
        if not rows:
            return
        text.extend([title.upper(), ""])
        html_parts.append(f"<h2 style='margin-top:30px'>{escape(title)}</h2>")
        for item in rows:
            excerpt = item.get("excerpt", "").strip()
            source = item.get("institution") or item.get("sourceName") or item.get("sourceId", "Institution")
            summary_line = excerpt or "Summary unavailable; review the original source."
            text.extend([
                f"{source} — {item['title']}",
                f"Published: {item.get('publishedAt') or 'Unknown'} | Confidence: {(item.get('verification') or {}).get('confidence', 'LOW')}",
                f"Asia relevance: {item.get('asiaRelevance', 'Unknown')} | Priority: {item.get('researchPriority', 'Unknown')}",
                f"Publisher description: {summary_line}",
            ])
            if detailed and item.get("topics"):
                text.append(f"Topics: {' · '.join(item['topics'])}")
            text.append(f"Official source: {item['url']}")
            html_parts.append(
                "<article style='margin:18px 0;padding:16px;border:1px solid #d8e1df'>"
                f"<p style='margin:0;color:#087f78;font-size:12px;font-weight:bold'>{escape(source)}</p>"
                f"<h3 style='margin:6px 0'><a style='color:#183344' href='{escape(item['url'], quote=True)}'>{escape(item['title'])}</a></h3>"
                f"<p style='margin:4px 0;color:#667a84;font-size:12px'>Published: {escape(item.get('publishedAt') or 'Unknown')} · "
                f"Verification: {(item.get('verification') or {}).get('confidence', 'LOW')} · "
                f"Asia relevance: {item.get('asiaRelevance', 'Unknown')}/100 · Priority: {item.get('researchPriority', 'Unknown')}/100</p>"
                f"<p>{escape(summary_line)}</p>"
                + (f"<p style='font-size:12px;color:#667a84'>Topics: {escape(' · '.join(item.get('topics', [])))}</p>" if detailed and item.get("topics") else "")
                + "</article>"
            )
            text.append("")

    add_section("Top reads", top, True)
    add_section("Asia-relevant", asia, True)
    add_section("Other new research", other, False)
    successful = sum(1 for check in radar.get("sourceChecks", []) if check.get("ok"))
    failed = sum(1 for check in radar.get("sourceChecks", []) if not check.get("ok"))
    text.extend([
        "RUN SUMMARY",
        f"Sources checked: {len(radar.get('sourceChecks', []))}",
        f"Successful: {successful} | Failed: {failed}",
        f"New verified articles in digest: {len(items)}",
        f"Research Radar: {SITE_URL}",
        "",
        "Publisher descriptions are metadata, not generated summaries. Always check the original article.",
    ])
    html_parts.append(
        f"<h2>Run summary</h2><p>Sources checked: {len(radar.get('sourceChecks', []))} · "
        f"Successful: {successful} · Failed: {failed}</p><p><a href='{SITE_URL}'>Open Research Radar</a></p>"
        "<p style='color:#667a84;font-size:12px'>Publisher descriptions are metadata, not generated summaries. Always check the original article.</p></main>"
    )
    return day_id, "\n".join(text), "\n".join(html_parts)


def send_email(subject: str, plain_text: str, html_body: str, recipients: list[str]) -> None:
    host = os.environ.get("SMTP_HOST")
    username = os.environ.get("SMTP_USERNAME")
    password = os.environ.get("SMTP_PASSWORD")
    sender = os.environ.get("SMTP_FROM") or username
    if not all((host, username, password, sender, recipients)):
        raise RuntimeError("Email delivery requires SMTP_HOST, SMTP_USERNAME, SMTP_PASSWORD, sender, and recipient configuration.")
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = ", ".join(recipients)
    message.set_content(plain_text)
    message.add_alternative(html_body, subtype="html")
    port = int(os.environ.get("SMTP_PORT") or "587")
    if port == 465:
        with smtplib.SMTP_SSL(host, port, timeout=30, context=ssl.create_default_context()) as server:
            server.login(username, password)
            server.send_message(message)
    else:
        with smtplib.SMTP(host, port, timeout=30) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(username, password)
            server.send_message(message)


def main() -> None:
    radar = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    source_registry = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    domains_by_source = {item["sourceId"]: item["officialDomains"] for item in source_registry["sources"]}
    names_by_source = {item["sourceId"]: item["institution"] for item in source_registry["sources"]}
    state = json.loads(STATE_PATH.read_text(encoding="utf-8")) if STATE_PATH.exists() else {
        "sentDigestIds": [], "sentArticleIds": [],
    }
    digest_date = datetime.now(HKT).date().isoformat()
    items = collect_ready_items(radar, domains_by_source, set(state.get("sentArticleIds", [])))
    for item in items:
        item["institution"] = names_by_source.get(item.get("sourceId", ""), item.get("sourceId", "Institution"))
    digest_id, text_body, html_body = render_digest(items, digest_date, radar)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    (PREVIEW_DIR / "daily.txt").write_text(text_body, encoding="utf-8")
    (PREVIEW_DIR / "daily.html").write_text(html_body, encoding="utf-8")
    if digest_id in state.get("sentDigestIds", []):
        print(f"Digest {digest_id} was already submitted; skipping.")
        return

    if not items and os.environ.get("SEND_EMPTY_DIGEST", "").lower() != "true":
        print(f"No verified unsent articles for {digest_id}; previews generated, no email sent.")
        return
    if os.environ.get("EMAIL_DRY_RUN", "true").lower() != "false":
        print(f"Dry run: generated preview for {digest_id} with {len(items)} verified article(s).")
        return

    recipients = [
        value.strip()
        for value in os.environ.get("NEWSLETTER_TO", "").replace(";", ",").split(",")
        if value.strip()
    ]
    send_email(
        f"Institutional Research Radar | {len(items)} New Verified Articles | {digest_date}",
        text_body,
        html_body,
        recipients,
    )
    state["sentDigestIds"] = list(dict.fromkeys(state.get("sentDigestIds", []) + [digest_id]))
    state["sentArticleIds"] = list(dict.fromkeys(
        state.get("sentArticleIds", []) + [item["id"] for item in items]
    ))
    state["lastDailyDigestAt"] = datetime.now(timezone.utc).isoformat()
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    (ARCHIVE_DIR / f"{digest_date}.md").write_text(text_body, encoding="utf-8")
    print(f"Digest {digest_id} submitted successfully.")


if __name__ == "__main__":
    main()
