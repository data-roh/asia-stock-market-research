# Research Radar

## What it does now

The Radar has two distinct layers:

1. `pipeline/scan_research_updates.py` discovers public candidates from the configured feeds and listing pages in `src/lib/content/research-feeds.json`.
2. `pipeline/verify_research_updates.py` uses Playwright/Chromium for newly discovered candidates in the Phase 1 set in `data/institutional_sources.json`. The scan persists a pending-verification queue, and ambiguous/access-failed candidates are retried up to three times. A candidate is marked `VERIFIED_NEW` only after the configured official listing contains its URL, the article page loads on an allowed publisher domain, and the visible article title matches the discovered title. Inaccessible or ambiguous results stay `POSSIBLE_NEW` or `UNVERIFIED`.

The verification record stores the status, confidence, checked time, official-domain check, listing match, article-page match, title match, visible date when available, canonical URL, extraction method and a content hash. Article text is processed transiently to count words and calculate the hash; full article text and HTML are not published or saved.

The public JSON remains `src/lib/content/research-radar.json`. Each completed verification run records its completion time and counts, including a real zero-candidate run. Before any run metadata is published, the page displays “Not run” rather than implying zero verified items. The Radar page reads the normalized dataset and offers time, source, topic, search and verification filters. Evidence is expandable per article. Source health is shown separately so a failed scan is not represented as an empty publication week.

## Phase 1 source set

The five representative sources are AQR, Citadel Securities, Man Group, Apollo and Oaktree. Their official listing URLs and allowed domains are declared in `data/institutional_sources.json`. This is a deliberately bounded browser-verification rollout, not a claim that every source in the library has been verified automatically.

The full source library is captured in `data/source_audit.csv`. Refresh it with:

```powershell
python pipeline/audit_research_sources.py
```

The audit makes a bounded public HTTP check and tries the existing static listing parser. `A` means a configured feed parsed successfully; `B` means static HTML candidates were found; `C` is a possible client-rendered page; `D` needs a custom parser or manual review; `E` means the automated request was denied or failed. The classification is a discovery-method snapshot, not a guarantee of complete coverage. Sitemap/API support, publication dates and pagination are left explicitly unchecked unless established.

## Article metadata and enrichment

Deterministic browser evidence controls verification. Topic tags, region tags, content type, Asia relevance, research priority and ASMR-candidate hints are heuristic metadata and must not be confused with verification confidence.

An excerpt is shown only when it comes from publisher metadata. It is labelled as a publisher description, not an AI-generated summary. No LLM provider or credentials are configured, so generated summaries and weekly cross-institution synthesis are not claimed. If reliable public metadata is absent, the page says that the description is unavailable instead of inventing one.

## Daily digest and email state

`pipeline/send_research_radar_digest.py` validates that every included item is `VERIFIED_NEW`, has a title and URL, and belongs to a configured official domain. It produces HTML and plain-text previews. Empty digests are skipped by default. Delivery is dry-run by default; to enable SMTP delivery, set the GitHub Actions repository variable `RESEARCH_RADAR_EMAIL_DRY_RUN` to `false` and configure the existing `SMTP_HOST`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, `SMTP_FROM`, and `NEWSLETTER_TO` secrets.

Successful sends record deterministic daily digest IDs and article IDs in the private `.state/research-radar-email.json` file, restored and saved through the Actions cache. A failed submission does not mark articles as sent. SMTP does not provide a universal idempotency key, so a process crash after a server accepts a message but before state is saved remains an unavoidable narrow duplicate-delivery window; the deterministic state prevents ordinary workflow retries after a completed send from resending it.

## Run and validate locally

```powershell
python pipeline/audit_research_sources.py
python pipeline/scan_research_updates.py
python pipeline/verify_research_updates.py
python pipeline/build_research_radar.py
$env:EMAIL_DRY_RUN = "true"
python pipeline/send_research_radar_digest.py
python -m unittest discover -s pipeline -p 'test_*.py'
npm.cmd run check
npm.cmd run lint
npm.cmd run build
```

The Actions workflow installs Playwright Chromium, performs the scan and verification, rebuilds the public JSON, creates a digest preview, and uploads the preview as a workflow artifact. Real sending remains opt-in.

## Known limitations and next phases

- Only the five Phase 1 sources receive automated browser verification. Other sources remain unverified unless separately configured.
- The generic discovery parser is not an authoritative source-specific adapter and may miss JavaScript-rendered content, pagination or PDFs. Never infer “no new research” solely from a zero-item result.
- Article-body extraction is measured but not summarized. A configured LLM provider, prompts, summary validation and weekly synthesis need to be designed and tested before generated analysis is enabled.
- The daily email uses publisher metadata excerpts and links to the original. It is not a substitute for reading the article.
- Expand source-specific adapters only after reviewing their source-audit results and regression fixtures.
