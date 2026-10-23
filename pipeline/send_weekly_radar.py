"""Email the last completed week's public metadata digest on Hong Kong Mondays."""

from datetime import datetime
from email.message import EmailMessage
from html import escape
import json
import os
from pathlib import Path
import smtplib
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src/lib/content/research-radar.json"
HKT = ZoneInfo("Asia/Hong_Kong")


def main() -> None:
    if datetime.now(HKT).weekday() != 0:
        print("Weekly email runs on Hong Kong Mondays only.")
        return
    radar = json.loads(DATA.read_text(encoding="utf-8"))
    week = radar["weekly"]
    groups = [
        ("Institutional research", radar["institutional"], week["institutionalIds"]),
        ("SSRN papers (DOI metadata)", radar["ssrn"], week["ssrnIds"]),
        ("GitHub (observed 7-day star gain)", radar["github"], week["githubIds"]),
    ]
    text_parts = [f"ASMR Weekly Research Radar | {week['start']}"]
    html_parts = ["<main style='max-width:720px;font:16px/1.5 Arial,sans-serif;color:#202421'>",
                  f"<h1>ASMR Weekly Research Radar</h1><p>Week of {escape(week['start'])}</p>"]
    count = 0
    for label, entries, ids in groups:
        by_id = {item["id"]: item for item in entries}
        text_parts.append(f"\n{label}")
        html_parts.append(f"<h2>{escape(label)}</h2><ul>")
        for item_id in ids:
            item = by_id.get(item_id)
            if not item:
                continue
            count += 1
            title = item.get("title") or item.get("name") or "Untitled"
            excerpt = item.get("excerpt") or item.get("abstract") or item.get("description") or ""
            metric = f" (+{item['stars7d']} stars / 7d)" if item.get("stars7d") is not None else ""
            text_parts.append(f"- {title}{metric}\n  {excerpt}\n  {item['url']}")
            html_parts.append(f"<li><a href='{escape(item['url'], quote=True)}'>{escape(title)}</a>{escape(metric)}<p>{escape(excerpt)}</p></li>")
        html_parts.append("</ul>")
    disclaimer = "Public metadata and publisher excerpts only; verify claims and methods in the original. SSRN dates are DOI registration dates."
    text_parts.append(f"\n{disclaimer}")
    html_parts.append(f"<p>{escape(disclaimer)}</p></main>")
    preview = Path(os.environ.get("WEEKLY_PREVIEW_PATH", "weekly-radar-preview.html"))
    preview.parent.mkdir(parents=True, exist_ok=True)
    preview.write_text("\n".join(html_parts), encoding="utf-8")
    if not count:
        print("No weekly items; preview only.")
        return
    host = os.environ.get("SMTP_HOST")
    username = os.environ.get("SMTP_USERNAME")
    password = os.environ.get("SMTP_PASSWORD")
    recipients = [x.strip() for x in os.environ.get("NEWSLETTER_TO", "").replace(";", ",").split(",") if x.strip()]
    if not all((host, username, password, recipients)):
        print("Weekly preview created; configure existing SMTP secrets to receive email.")
        return
    message = EmailMessage()
    message["Subject"] = f"ASMR Weekly Research Radar | {week['start']}"
    message["From"] = os.environ.get("SMTP_FROM") or username
    message["To"] = ", ".join(recipients)
    message.set_content("\n".join(text_parts))
    message.add_alternative("\n".join(html_parts), subtype="html")
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
    print(f"Weekly radar sent to {len(recipients)} recipient(s).")


if __name__ == "__main__":
    main()
