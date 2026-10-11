# Asia Stock Review: LinkedIn Carousel

## A Taxonomy of Asian Disclosure Systems: 5 Tables

*Five tables, five points each. Designed to be screenshot one per slide.*

**Intro**

A buyback is a buyback and a supply contract is a supply contract, whether the company is in Seoul, Tokyo, Shanghai, Taipei or New York. But the way each market makes companies disclose those events is different in every one: who requires the filing, where it lives, what it is called, and when it is stamped. I spent some time mapping the disclosure systems of Korea, Japan, China and Taiwan into a single framework and then put US EDGAR beside them as the benchmark. Two things surprised me. First, every market has rules that exist nowhere else, and most of them are the kind of thing an event-driven desk would build a signal around if it knew they existed. Second, the US, the market everyone treats as the standard for transparency, turns out to require the least disclosure of what a company is actually doing. The five tables below are the short version.

---

## Table 1. Same Question, Five Architectures

| Market | Architecture | Where filings live | In one line |
|---|---|---|---|
| 🇰🇷 Korea | Integrated hub | DART / OpenDART (+ KRX, FTC) | One system, one API, one taxonomy |
| 🇯🇵 Japan | Deliberately split | EDINET (statutory) + TDnet (exchange) | Two regimes; you need both |
| 🇨🇳 China | Three layers | CSRC writes rules → exchanges enforce and publish → CNINFO searches across them | No single "Chinese DART" |
| 🇹🇼 Taiwan | Central platform + open APIs | MOPS + TWSE / TPEx OpenAPI | Easiest to turn into a database |
| 🇺🇸 US | Single statutory system | SEC EDGAR (exchanges enforce via press release) | One regulator, no exchange filing taxonomy |

**Key points**

- Every market answers the same investor questions (earnings, guidance, buybacks, holders, contracts), but the *architecture* is different in each.
- Japan physically separates statutory filings (audited annual report → EDINET) from timely disclosure (yesterday's buyback → TDnet). Miss one and you miss half the market.
- China splits "who writes the rule" (CSRC), "who enforces and publishes it" (SSE / SZSE / BSE) and "where you search across all of them" (CNINFO). The exchanges stay authoritative; the portal is a convenience layer.
- Korea's Fair Trade Commission filings, covering intra-group transactions inside the chaebol, are not a securities-law disclosure at all, and have no equivalent anywhere else.
- The US is the mirror image of Japan: the exchange layer is thin, and almost everything investable flows through one form, the 8-K.

---

## Table 2. What Only This Market Requires

| Market | Nobody else requires this |
|---|---|
| 🇰🇷 Korea | Exchange-demanded answers to rumors (조회공시) · Supply contracts above a revenue threshold (5% KOSPI, 2.5% large corps, 10% KOSDAQ), with counterparty · Insider trade plans filed 30 days *before* trading (≥1% or ₩5bn) · Short sellers ≥0.5% named · Daily foreign / institutional / retail flows per stock · Related-party deals disclosed *before* execution |
| 🇯🇵 Japan | Forecasts are near-universal and, once published, revisions are mandatory and XBRL-tagged above ~10% sales / ~30% profit · Cross-shareholdings listed by name with reason · TSE's public list of who has a cost-of-capital plan · Monthly statutory buyback status reports (EDINET) · IR deck filed on TDnet |
| 🇨🇳 China | Mandatory earnings preannouncement on expected loss, turnaround or large swing · Institutional meeting records with attendee fund names within 2 days · Exchange-run retail Q&A platforms · Insider sale plans published 15 trading days *before* selling · Top-10 holders every quarter |
| 🇹🇼 Taiwan | Monthly revenue by the 10th, via API · Earnings-call slides *and audio* filed on MOPS · >5% holder declarations since May 2024, plus a separate monthly insider / >10% table · Insider sales pre-declared 3 days ahead · Daily flows, margin, lending and foreign ownership per stock · Mandatory press conferences for major events |
| 🇺🇸 US | Manager-side portfolios (13F) · Insider trades in 2 days, XML (Form 4) · Clean restatement flag (8-K 4.02) · SEC comment letters public · Nothing filed on earnings day |

**Key points**

- Korea and Taiwan expose positioning and flows. Japan exposes guidance and cross-holdings. China exposes who management is talking to. The US exposes who owns the company.
- In Korea, China and Taiwan insiders must announce planned trades *in advance* (30 / 15 / 3 days), the opposite of the US Form 4, which reports two days *after*.
- Japan is the only market where changing guidance forces a structured filing the same day. Giving a forecast is expected practice rather than law, but once given it is binding. Everywhere else, guidance and its revision are voluntary.
- Shenzhen companies must publish, within two trading days, which funds visited them and what was asked. Your competitors' diligence trail is public.
- The US has the best ownership data in the world and almost no mandatory disclosure of what a company is operationally doing.

---

## Table 3. Earnings: Five Different Clocks

| Step | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Early warning | 30% / 15% change filing at annual close (mandatory, ex post) | Forecast revision above threshold (mandatory) | 业绩预告 on loss, turnaround or large swing (mandatory, by Jan 31) | Monthly revenue by 10th (mandatory) | none |
| Preliminary | 잠정실적: voluntary; large caps only, ~1 week after quarter, 2 lines | none | 业绩快报: optional | 自結損益: voluntary monthly | none |
| Formal release | Quarterly report, up to 45 days | 決算短信: full statements + new forecast, XBRL, one document | Periodic report by Apr 30 / Aug 31 / Oct 31 | 財報 within 45 days | Press release + 8-K 2.02 (*furnished*) |
| IR deck / call | Company site | **Deck filed on TDnet** | 业绩说明会 open to retail; record posted | **Deck + audio filed on MOPS** | Company site; transcript not filed |
| Who management met | none | none | **Fund names + Q&A within 2 days (Shenzhen)** | none | none |

**Key points**

- Korea has two earnings seasons: a handful of two-line preliminary prints in the first two weeks, then a long tail where the quarterly report itself is the first number.
- Japan puts release, financials and guidance in one XBRL document at a fixed time. The call is the least official part.
- China staggers information across three documents of different legal weight, and annual + Q1 reports share the April 30 deadline, so thousands of filings land in one week.
- Taiwan replaces the "preliminary" with three monthly revenue prints; the quarterly report mostly resolves margins. And the earnings call is literally in the disclosure archive.
- The US has the most calls and the fewest filings: the release is furnished, the deck is optional, the transcript is vendor-only, and the filed statements arrive weeks later.

---

## Table 4. Ownership and Positioning: Who Sees What

| Signal | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Manager-side portfolios | none | none | none | none | **13F, quarterly** |
| Company-side top holders | 5%+ holders | Top 10, semi-annual | **Top 10 (incl. float), quarterly** | >5% declarations; insiders and >10% monthly | Proxy, annual |
| Insider trades | **Plan 30 days *before*** + 5 days after | via 5% amendments | **Plan published 15 days *before*** | **Declared 3 days *before*** | **Form 4, 2 days after, XML** |
| Short positions | **≥0.5% named** | **≥0.5% named** | none | Aggregate lending | Aggregate |
| Daily flows per stock | **Yes** | Weekly aggregate | Northbound only | **Yes** | none |
| Share pledges | In 5% report | none | **Discrete event** | **Monthly table** | Proxy footnote |
| Cross-shareholdings | none | **By name, with reason** | none | none | none |

**Key points**

- Two philosophies: the US discloses from the *manager's* side (13F, every stock a fund holds); Asia discloses from the *company's* side (top-10 holders). You can see who owns a Chinese stock; you cannot see a Chinese fund's book.
- Named short positions ≥0.5% in Korea and Japan have no US equivalent; the US publishes aggregates only.
- Korea and Taiwan publish foreign / institutional / retail net buying for every stock every evening. Japan gives weekly aggregates; the US nothing.
- Share pledges (a controller using stock as loan collateral) are events in China and a monthly table in Taiwan, linking ownership data to financing stress.
- Japan's annual report lists strategic cross-shareholdings by name and reason. The entire unwind trade lives in that table.

---

## Table 5. Asia vs. EDGAR: Where the Edge Is

| Dimension | 🇺🇸 US | Asia (best market) |
|---|---|---|
| Ownership, manager-side | 13F | None |
| Insider trades | 2 days after | **KR / CN / TW: 30 / 15 / 3 days before** |
| Short positions | Aggregate | **KR / JP: ≥0.5% named** |
| Daily flows | None | **KR / TW: per stock** |
| Guidance | Voluntary | **JP: mandatory, tagged** |
| Monthly revenue | None | **TW: mandatory** |
| Earnings early warning | None | **CN: mandatory preannouncement** |
| Buyback execution | Quarterly, lagged | **JP: monthly statutory report** |
| Supply contracts | Materiality, no threshold | **KR: mandatory, with counterparty** |
| Rumor / price-move response | None | **KR / CN / TW: exchange-demanded** |
| Who management met | None | **CN: fund names + Q&A** |
| Earnings-call materials | Company site | **JP: deck filed; TW: deck + audio filed** |
| Restatements | **8-K 4.02, clean flag** | Less standardized |
| Regulator correspondence | Comment letters, delayed | **CN: inquiry letters, immediate** |
| Data access | **JSON APIs, full-text search** | KR / TW comparable; JP split; CN fragmented |

**Key points**

- The US discloses *who owns and runs the company* better than anyone. Asia discloses *what the company is doing, who is trading it, and who management is talking to* better than the US.
- The same supply contract can be a mandatory filing in Seoul, a rule-triggered but usually untriggered filing in Taipei, and no filing at all in Tokyo or New York. The asymmetry is itself information.
- A US event-driven playbook ported to Asia loses 13F and Form 4 but gains an entire layer of operational and positioning events with no US analogue.
- On buybacks, guidance, contracts and CAPEX, Asian data is simply better than US data.
- The build order: Korea → Taiwan → US → Japan EDINET → Japan TDnet → China. Normalize the event, preserve the source.

---

*Full piece: Asia Stock Review, "A Taxonomy of Asian Disclosure Systems." Personal research, not investment advice. Claude Opus 5 and Claude Fable 5.1 (Anthropic) assisted with research, tables and editing under the author's direction; all judgments and errors are the author's own.*
