# Asia Stock Market Research

Independent research on Asian markets, financial institutions and quantitative investing.

[Visit the live site](https://data-roh.github.io/asia-stock-market-research/)

Sample market data is illustrative only. This site is not investment advice.

# Research radar

The dedicated Research Radar tab (`/research-radar/`) shows a source-linked weekly reading list:
institutional updates, SSRN papers, and GitHub quant repositories. The existing
daily GitHub Action scans public research pages, runs
`pipeline/build_research_radar.py`, commits
`src/lib/content/research-radar.json`, then dispatches the existing Pages
deployment workflow. The explicit dispatch is needed because a push made with
`GITHUB_TOKEN` does not trigger another push workflow.
On Hong Kong Mondays, `pipeline/send_weekly_radar.py` prepares a weekly email
using the **existing** SMTP secrets and `NEWSLETTER_TO`. If they are unset, the
site still updates and an HTML email preview is saved as a workflow artifact.

To start immediately after merging, run **Daily Research Newsletter** through
GitHub Actions > Run workflow. The first GitHub run establishes the star baseline;
seven-day gains appear after seven days of snapshots. The SSRN feed uses Crossref
records for DOI prefix `10.2139` and selected title filters. It is a partial
discovery feed, not SSRN's discontinued Top Papers ranking. Its date is DOI
registration, which may differ from the SSRN posting date.

The weekly list is intentionally limited to titles, public excerpts, and source
links. It does not claim to have read an article or paper when only metadata is
available. Some publisher listing pages reject automated requests; those failures
are recorded by the existing scanner and do not block other sources. A failed
SSRN or GitHub request keeps previously collected public records.

Run locally with `python pipeline/scan_research_updates.py` followed by
`python pipeline/build_research_radar.py`, then `npm run validate`. Authenticated
GitHub Actions runs supply `GITHUB_TOKEN` to avoid the low anonymous search
limit. On each run the radar keeps at most 90 repositories, 80 papers and 300
institutional items; repository star snapshots are retained for 35 days.
