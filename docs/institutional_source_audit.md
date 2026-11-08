# Institutional Source Audit

Audit snapshot: 2026-11-08 (UTC). Sources are taken from the Institutional Research Library.

Total listed sources: 45.

## Preliminary collection classification

| Class | Sources | Meaning |
|---|---:|---|
| A | 1 | A configured RSS/Atom feed parsed successfully during this snapshot. |
| B | 32 | Static HTML candidate links were found by the existing parser. |
| C | 2 | JavaScript/browser rendering may be needed; confirm with a browser audit. |
| D | 3 | No static candidate was extracted; a source-specific parser or manual review is needed. |
| E | 7 | Automated access failed or was denied; retry or review manually without bypassing restrictions. |

The generated CSV records live URL/feed checks and parser candidate counts. These are preliminary access and discovery observations, not proof of completeness or date accuracy. Sitemap, API, pagination and publication-date visibility remain unchecked. A zero-result scan is not evidence that a source published nothing.

## Phase 1

AQR, Citadel Securities, Man Group, Apollo and Oaktree are the representative sources configured for browser verification in `data/institutional_sources.json`. They are still subject to the same official-domain and article-page checks; access challenges are reported, never bypassed.

## Refresh

Run `python pipeline/audit_research_sources.py` to regenerate `data/source_audit.csv` and this report. Re-audit before treating any source as production-complete.
