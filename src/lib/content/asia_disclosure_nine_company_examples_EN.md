# A Taxonomy of Asian Disclosure Systems: Nine Worked Examples

## Applying the framework to Samsung Electronics, SK hynix, Samsung Electro-Mechanics, Kioxia, Tokyo Electron, Advantest, TSMC, MediaTek and ASE

> **Purpose.** The taxonomy piece and its detailed edition describe five disclosure systems in the abstract. This document runs the framework end to end on nine real semiconductor companies, three per market, so that every concept (source routing, earnings clock, ownership regimes, obligation type, supply-chain matching, rule registry) has a concrete instance.
>
> **How to read it.** Each company gets the same template. Where a number would come from a live filing (a threshold applied to this year's revenue, a holder's exact percentage, a specific filing date), it is shown as `[value]` or given as an approximate range and flagged. Identifiers and calendars are stated from public knowledge as of 13 September 2026 and should be verified against the source before use.
>
> **As-of date:** 13 September 2026. Personal research, not investment advice. *Claude Opus 5 and Claude Fable 5.1 (Anthropic) assisted under the author's direction; all judgments and errors are the author's own.*

---

## 1. The nine companies and why these nine

| Market | Company | Role in the chain | Why it is a good test case |
|---|---|---|---|
| 🇰🇷 | Samsung Electronics (삼성전자) | Memory, foundry, devices | Largest issuer; preliminary two-line print; FTC group disclosure; supply-contract threshold so high it never files one |
| 🇰🇷 | SK hynix (SK하이닉스) | Memory (DRAM, HBM, NAND) | Capex event filings for fabs; named short positions; SK group disclosure |
| 🇰🇷 | Samsung Electro-Mechanics (삼성전기) | MLCC, camera modules, substrates | Mid-size large corporation where supply-contract filings actually occur; Samsung group |
| 🇯🇵 | Kioxia Holdings (キオクシア) | NAND | Recent IPO (December 2024) so short history; large-holder sell-down filings; March fiscal year |
| 🇯🇵 | Tokyo Electron (東京エレクトロン) | Wafer fab equipment | Textbook EDINET + TDnet company; forecast revisions; buybacks; cross-shareholdings |
| 🇯🇵 | Advantest (アドバンテスト) | Test equipment | Frequent forecast revisions in the AI test cycle; buybacks |
| 🇹🇼 | TSMC (台積電) | Foundry | Monthly revenue; quarterly call with guidance; NYSE ADR so MOPS and EDGAR both apply |
| 🇹🇼 | MediaTek (聯發科) | Fabless SoC | TSMC customer; monthly revenue; guidance on call; no ADR |
| 🇹🇼 | ASE Technology Holding (日月光投控) | OSAT (packaging and test) | NYSE ADR plus a Shanghai-listed subsidiary (USI, 环旭电子), so three disclosure regimes touch one group |

The set covers memory (Samsung, SK hynix, Kioxia), equipment (TEL, Advantest), foundry (TSMC), fabless (MediaTek), packaging (ASE) and components (SEMCO), which means real supply-chain relationships exist between the rows.

---

## 2. Entity master

| Company | Local listing | Code | Other listings | Fiscal year end | Native regulator IDs to capture |
|---|---|---|---|---|---|
| Samsung Electronics | KRX KOSPI | 005930 | GDRs (London, Luxembourg) | December | DART `corp_code`; KRX issuer code |
| SK hynix | KRX KOSPI | 000660 | GDRs | December | DART `corp_code` |
| Samsung Electro-Mechanics | KRX KOSPI | 009150 | none material | December | DART `corp_code` |
| Kioxia Holdings | TSE Prime | 285A | none | March | EDINET code (assigned at listing, December 2024); TDnet issuer code |
| Tokyo Electron | TSE Prime | 8035 | none (ADR OTC only) | March | EDINET code; TDnet issuer code |
| Advantest | TSE Prime | 6857 | none (ADR OTC only) | March | EDINET code; TDnet issuer code |
| TSMC | TWSE | 2330 | NYSE ADR (TSM), SEC registrant | December | MOPS company ID; SEC CIK |
| MediaTek | TWSE | 2454 | none | December | MOPS company ID |
| ASE Technology Holding | TWSE | 3711 | NYSE ADR (ASX), SEC registrant; subsidiary USI listed on SSE (601231) | December | MOPS company ID; SEC CIK; SSE code for the subsidiary |

Three of the nine are SEC registrants or have a listed Chinese subsidiary. That is the first practical lesson: "Taiwan company" does not mean "Taiwan sources only". TSMC and ASE furnish Form 6-K to EDGAR for the same monthly revenue and quarterly results they post on MOPS, and file an annual Form 20-F.

---

## 3. Source routing per company

| Company | Statutory | Timely / exchange | Structured API | Also |
|---|---|---|---|---|
| Samsung, SK hynix, SEMCO | DART (사업보고서, 분기·반기보고서, 주요사항보고서) | KRX via KIND and DART (수시공시, 공정공시, 조회공시) | OpenDART | FTC group disclosures (Samsung group, SK group) through DART; KRX daily flows and short data |
| Kioxia, TEL, Advantest | EDINET (有価証券報告書, 半期報告書, 大量保有, 自己株券買付状況報告書) | TDnet (決算短信, 業績予想の修正, buyback resolutions, 補足資料) | EDINET API v2; TDnet API (paid) | JPX short-position disclosure; weekly investor-type aggregates |
| TSMC, ASE | MOPS (財報, 年報, 重大訊息, 法說會 materials and audio) + EDGAR (6-K, 20-F) | TWSE material information | TWSE OpenAPI; SEC data.sec.gov | TWSE daily flows, margin, lending, foreign ownership; for ASE also SSE / CNINFO for USI |
| MediaTek | MOPS | TWSE material information | TWSE OpenAPI | TWSE daily flows and foreign ownership |

---

## 4. Company templates

Each template follows the same nine headings: identity and routing; periodic clock; earnings sequence; guidance regime; ownership and positioning; capital actions; operational events and the rules that select them; quirks; example tool calls.

### 4.1 Samsung Electronics (005930)

**Periodic clock.** December fiscal year. 사업보고서 by end of March; 분기보고서 and 반기보고서 within 45 days of quarter-end (mid-May, mid-August, mid-November).

**Earnings sequence.** The clearest example of Korea's two-season structure. A preliminary consolidated print (매출, 영업이익 only, no segment detail) arrives as a 공정공시 roughly one week after quarter-end, typically around the 7th to 8th of January, April, July and October. The detailed release with segment breakdown, the call, and the IR deck follow about three weeks later, at the end of the month. The quarterly report itself lands another two weeks after that. Three documents, three timestamps, one quarter.

**Guidance regime.** Samsung gives qualitative directional commentary on the call, not numeric targets, so there is little numeric 공정공시 guidance to capture. The preliminary print is the de facto guidance event for the market.

**Ownership and positioning.** Large-holder (5%) reports from the National Pension Service, Samsung Life and the Samsung C&T group are the relevant 대량보유상황보고서 filers, with change reports on 1pp moves. Officer and major-shareholder ownership reports and, since the regime was introduced, ex-ante trade plans for trades of 1% or KRW 5 billion or more apply to the founding family's holdings. Foreign ownership is published daily by KRX along with foreign, institutional and retail net buying. Short positions of 0.5% or more are disclosed with the holder's name; Samsung is a routine name in that table.

**Capital actions.** Buyback programs are announced as 자기주식취득 결정 (board resolution, size, period), executed through trust or direct purchase, and closed with a 결과보고서; cancellations are separate 소각 filings. Quarterly dividends are 현금배당결정 filings.

**Operational events.** The supply-contract rule shows how thresholds scale with size. Samsung is a 대규모법인, so the KOSPI threshold is 2.5% of prior-year revenue. On revenue of roughly `[KRW 300 trillion]` that is a `[~KRW 7.5 trillion]` contract, so Samsung essentially never files a 단일판매·공급계약 disclosure even though its suppliers file them constantly. CAPEX for new fabs appears, if at all, through 신규시설투자 filings and periodic-report MD&A rather than a dedicated event. FTC group disclosures capture intra-group transactions with Samsung affiliates.

**Quirks.** Frequent 조회공시 subject (M&A rumors, production rumors); the "미확정" answer is itself an event. Annual report human-capital tables give headcount, tenure and salary by gender and division.

**Example calls.**
```text
get_earnings(005930, period=2026Q3)        -> preliminary (Oct ~7) + detailed (Oct ~30) + 분기보고서 (Nov ~14)
get_large_holders(005930)                  -> DART 대량보유 filings, purpose field
get_short_positions(005930)                -> KRX named positions >= 0.5%
get_flows(005930, window=30d)              -> KRX daily foreign / institutional / retail
get_major_contracts(005930)                -> expected: none (threshold too high); return NO_FILING_EXPECTED
```

### 4.2 SK hynix (000660)

**Periodic clock.** December fiscal year; same statutory deadlines as Samsung.

**Earnings sequence.** SK hynix does not publish a separate two-line preliminary. Results arrive as a 공정공시 on the call day, roughly three to four weeks after quarter-end (late January, April, July, October), followed by the 분기보고서. So for SK hynix the first number and the detailed number are the same event.

**Guidance regime.** Directional commentary on the call; numeric targets are rare, so 공정공시 guidance filings are infrequent.

**Ownership and positioning.** SK Square is the controlling holder and files 대량보유 reports; the National Pension Service is a 5% filer. SK hynix is among the most heavily shorted large caps in Korea, so the named 0.5% short table and its changes are directly relevant. Daily foreign net buying is a widely watched series.

**Capital actions.** Buybacks and dividends as above. SK hynix has used both quarterly dividends and treasury-share cancellations, each with its own filing.

**Operational events.** This is where SK hynix differs from Samsung. Fab investments are large relative to the company's balance sheet and have appeared as 신규시설투자 filings, for example the Cheongju M15X expansion and the Yongin cluster commitments. Those filings carry investment amount, purpose, period and funding source, which makes them the cleanest CAPEX event data in the nine-company set. Supply contracts: as a 대규모법인 the 2.5% threshold on `[~KRW 60+ trillion]` revenue is still large, so contract filings are rare; HBM supply arrangements with Nvidia or others do not appear as individual filings.

**Quirks.** SK group FTC disclosures capture intra-group funding and equity transactions (SK Square, SK Telecom links). Frequent 조회공시 target during HBM news cycles.

**Example calls.**
```text
get_capex(000660, since=2024-01-01)        -> DART 신규시설투자 filings with amount and period
get_short_positions(000660)                -> named positions; track changes around earnings
get_group_disclosures(000660)              -> FTC filings for SK group inter-affiliate transactions
get_earnings(000660, period=2026Q3)        -> single release ~Oct 23 to 30, then 분기보고서
```

### 4.3 Samsung Electro-Mechanics (009150)

**Periodic clock.** December fiscal year; same deadlines.

**Earnings sequence.** No preliminary print. Results as a 공정공시 with call in late January, April, July, October; 분기보고서 two weeks later. For a pipeline this is the "long tail" case even though SEMCO is a large company.

**Guidance regime.** Qualitative.

**Ownership and positioning.** Samsung Electronics is the controlling holder (large-holder filings); NPS is a 5% filer. Foreign ownership and daily flows from KRX.

**Capital actions.** Annual or semi-annual dividends; occasional buybacks.

**Operational events.** SEMCO is the Korean example where supply-contract filings can actually occur. It is a 대규모법인 (2.5%) with revenue around `[KRW 10 trillion]`, so a contract above `[~KRW 250 billion]` triggers a 단일판매·공급계약체결 filing with counterparty, value and term. Component contracts (MLCC, camera modules, FC-BGA substrates) occasionally cross that line, and the counterparty is often redacted at the customer's request ("북미 소재 고객사", "중화권 고객사"). CAPEX for new MLCC or substrate lines appears as 신규시설투자 when material.

**Quirks.** Samsung group FTC disclosures apply. This is the company in the set most likely to sit on the Korean side of the cross-market contract example in Section 6.

**Example calls.**
```text
get_major_contracts(009150, since=2023-01-01)  -> DART 단일판매·공급계약, with deferral flags on counterparty
get_capex(009150)                              -> 신규시설투자
get_earnings(009150, period=2026Q3)            -> single release late Oct
```

### 4.4 Kioxia Holdings (285A)

**Periodic clock.** March fiscal year, listed on TSE Prime on 18 December 2024. Annual 有価証券報告書 by end of June; 半期報告書 for the September half by mid-November; Q1 and Q3 only through the TDnet 決算短信 framework (there was never a statutory quarterly report for Kioxia because the statutory quarterly regime ended before its first full fiscal year).

**Earnings sequence.** One 決算短信 per quarter on TDnet at a fixed afternoon release time (Q1 results were published on 31 July 2026; the September quarter typically lands in early to mid November, December quarter in early to mid February, March quarter in mid May). The IR deck goes to TDnet as 補足資料. No preliminary; the 短信 is the full release with statements and forecast.

**Guidance regime.** Kioxia provides forecasts in the 決算短信 format. NAND pricing is volatile, so the ±10% sales / ±30% profit revision criteria are crossed relatively often, generating 業績予想の修正 filings on TDnet. Each is XBRL-tagged; the `sign_flip` feature matters for a company that has moved between loss and profit.

**Ownership and positioning.** The most instructive ownership case in the nine. Pre-IPO holders (the Bain Capital-led consortium, Toshiba with roughly a fifth of the shares as of late 2025, Hoya) sit above 5% and file 大量保有報告書 on EDINET, with 変更報告書 on each 1pp reduction. Post-lock-up sell-downs therefore leave a precise, dated trail in EDINET that does not exist for a US IPO of comparable structure. Institutions buying in file under the special reporting system with a lag, so the accumulation side is slower than the distribution side. Named short positions of 0.5% or more apply.

**Capital actions.** As a recent IPO, capital-return filings are limited; any future buyback would be a TDnet resolution plus monthly EDINET 自己株券買付状況報告書.

**Operational events.** New fab construction (Fab3 at Kitakami has been announced) surfaces as TDnet timely disclosure under fixed-asset acquisition criteria when the exchange's quantitative tests are met, and in the 有価証券報告書. The joint venture with Sandisk means related-party and JV disclosures are important. No Korean-style supply-contract filing exists; customer contracts do not appear as events.

**Quirks.** Short history: the first 有価証券報告書 covers FY March 2025, so cross-shareholding tables and human-capital data have at most two annual observations. The rule registry must mark `listing_date = 2024-12-18` so that backtests do not look for filings before it.

**Example calls.**
```text
get_large_holders(285A)                    -> EDINET 大量保有 + 変更報告書 chain for Bain, Toshiba, Hoya
get_guidance_changes(285A)                 -> TDnet 業績予想の修正 with revision pct and sign_flip
get_earnings(285A, period=FY2027Q2)        -> 決算短信 early-mid Nov 2026; 半期報告書 by mid Nov
get_capex(285A)                            -> TDnet fixed-asset disclosures; 有報 capital-expenditure section
```

### 4.5 Tokyo Electron (8035)

**Periodic clock.** March fiscal year. 有価証券報告書 by late June; 半期報告書 by mid-November; Q1 and Q3 via 決算短信 only.

**Earnings sequence.** 決算短信 roughly four weeks after quarter-end (late April to early May for the full year, late July to early August, late October to early November, late January to early February). Deck on TDnet. Call in Japanese with vendor transcripts.

**Guidance regime.** TEL publishes full-year forecasts and revises when WFE demand shifts cross the criteria. The `revision_number_fy` feature is useful: a second upward revision in a fiscal year is a different signal from a first.

**Ownership and positioning.** Large holders are mainly custodians and the parent-linked TEL trust structures; 大量保有 filings are less eventful than Kioxia's. The interesting ownership data are on the other side: TEL's own 有価証券報告書 lists its 政策保有株式 by name and reason, so the cross-shareholding unwind trade can be tracked from TEL's filings. Human-capital data (average salary, age, tenure, gender pay gap) also in the 有報.

**Capital actions.** TEL runs buybacks. The authorization is a TDnet resolution; execution appears monthly in the EDINET 自己株券買付状況報告書 with TDnet progress notices; retirement is a separate event. This is the reference case for the corrected buyback mapping.

**Operational events.** TEL is the Japanese counterparty in the Section 6 contract example. Japan has no dedicated major-contract category, so a large tool order from a Korean or Taiwanese fab does not generate a TEL filing; it appears only in aggregate as orders and backlog in the 決算短信 and deck. A business or capital alliance (業務提携・資本提携) would be a TDnet event, but a routine sales contract is not.

**Quirks.** TSE cost-of-capital list: TEL is a disclosing company. Weekly investor-type flow data only, no daily per-stock series.

**Example calls.**
```text
get_cross_shareholdings(8035)              -> 有報 政策保有株式 table, by name, with reason
get_buybacks(8035)                         -> TDnet authorization + EDINET monthly status + completion
get_guidance_changes(8035)                 -> TDnet revisions with threshold_crossing flag
get_major_contracts(8035)                  -> NO_FILING_EXPECTED (no Japanese category)
```

### 4.6 Advantest (6857)

**Periodic clock.** March fiscal year; same structure as TEL.

**Earnings sequence.** 決算短信 in late April, late July, late October, late January, with deck on TDnet.

**Guidance regime.** Advantest is the most active forecast reviser in the set. During the AI test-demand cycle it has revised full-year forecasts upward more than once within a fiscal year, each time as a TDnet 業績予想の修正 with tagged sales and profit figures. The `days_since_prior_guidance` and `revision_sequence` features are informative here.

**Ownership and positioning.** Custodian-heavy register; 大量保有 filings from large passive managers under the special reporting regime. Named short positions apply.

**Capital actions.** Regular buybacks with the TDnet-plus-EDINET pattern; dividend forecast revisions via 配当予想の修正.

**Operational events.** Like TEL, no contract filings; test-equipment orders from SK hynix (HBM test) or TSMC do not surface as events. Fixed-asset acquisitions above the criteria would be TDnet events.

**Quirks.** Because revisions are frequent, Advantest is the natural test case for the Japan guidance-revision momentum signal: sign of revision, magnitude versus threshold, and the market reaction on the same afternoon.

**Example calls.**
```text
get_guidance_changes(6857, since=2024-04-01)  -> ordered revision chain with pct changes
get_buybacks(6857)                            -> authorization, monthly execution, completion
get_disclosure_timeline(6857, FY2027)         -> 決算短信 x4, revisions, dividend changes, 有報, 半期
```

### 4.7 TSMC (2330 / NYSE: TSM)

**Periodic clock.** December fiscal year. Taiwan: 年報 by end of March; quarterly 財報 within 45 days. US: Form 20-F annually in April; Form 6-K for everything material in between.

**Earnings sequence.** The richest earnings clock of the nine.
- Monthly revenue by the 10th of the following month, filed on MOPS and furnished to EDGAR on a 6-K the same day. Three prints per quarter, so the quarterly revenue is nearly known before the call.
- Quarterly results and investor conference (法說會) around the middle of January, April, July and October, on a Thursday afternoon Taiwan time. Slides and audio are uploaded to MOPS as required; the same materials are furnished on a 6-K.
- Quarterly 財報 within 45 days; 20-F in April with the audited statements.

**Guidance regime.** TSMC gives explicit next-quarter guidance on the call (revenue range in US dollars, gross margin range, operating margin range) and full-year capex and growth commentary. This is voluntary in Taiwan and not a structured filing, but because the call materials are on MOPS and the 6-K, the guidance text is in the disclosure archive. Guidance changes are therefore captured from the deck, not from a tagged revision as in Japan.

**Ownership and positioning.** The National Development Fund is the one holder above the Article 43-1 line and appears in the substantial-holder data. Directors, officers and >10% holders (there are none of the latter besides the Fund) report monthly under Article 25, with pledges. Foreign ownership, published daily by TWSE, is among the highest on the exchange; daily foreign, investment-trust and dealer net buying is the most watched flow series in Taiwan. On the US side, 13F filings show manager-side holdings of the ADR, which is the only manager-side view of any company in this set.

**Capital actions.** Quarterly cash dividends are approved by the board and announced as 重大訊息. The board's quarterly approval of capital appropriations (the capex budget tranche) is also a 重大訊息 and a 6-K, which makes TSMC's CAPEX one of the best-documented event streams in Asia.

**Operational events.** Overseas fab investments (Arizona, Kumamoto, Dresden) appear as board-approved capital appropriations and as 重大訊息 when they meet the enumerated tests. Customer contracts do not appear; TSMC does not name customers. Material litigation and regulatory matters are 重大訊息 and 6-K.

**Quirks.** Every material MOPS event has an EDGAR twin, usually within hours, which gives a clean measurement of cross-system publication lag. The audio of the earnings call is in MOPS, so the transcript can be regenerated from an official source rather than a vendor.

**Example calls.**
```text
get_monthly_operating_data(2330, months=12)    -> MOPS / TWSE API monthly revenue; 6-K twin
get_capex(2330)                                -> 重大訊息 board capital appropriations, quarterly
get_earnings(2330, period=2026Q3)              -> 法說會 ~Oct 15 to 16, slides + audio, 6-K
get_large_holders(2330)                        -> Art. 43-1 filers; Art. 25 monthly insiders
get_flows(2330, window=60d)                    -> TWSE daily three-institution net buying, foreign %
```

### 4.8 MediaTek (2454)

**Periodic clock.** December fiscal year; 年報 by end of March; quarterly 財報 within 45 days. No US registration.

**Earnings sequence.** Monthly revenue by the 10th. Quarterly results and 法說會 at the end of January, April, July and October, with slides and audio on MOPS.

**Guidance regime.** Numeric next-quarter guidance on the call (revenue range in NT dollars, gross margin, operating expense ratio) plus full-year directional commentary. As with TSMC, captured from the deck rather than a tagged filing.

**Ownership and positioning.** Foreign ownership published daily; no single holder above 5% besides possibly investment vehicles, so Article 43-1 activity is limited. Article 25 monthly insider and pledge table applies to the founder-chairman's holdings. Daily flows from TWSE.

**Capital actions.** Dividends approved by the board and disclosed as 重大訊息; MediaTek has paid both annual and interim dividends.

**Operational events.** MediaTek is the customer side of the TSMC relationship and a customer of ASE for packaging; none of those relationships generate contract filings on any side, which is exactly the selection-bias point. Material asset transactions and investments follow the enumerated 重大訊息 tests.

**Quirks.** The cleanest "monthly revenue as nowcast" case among fabless names: quarterly guidance is given at the end of month one of the quarter, and monthly revenue for months one, two and three then arrives on the 10th of the following months, so the guidance can be scored against official data three times before the next call.

**Example calls.**
```text
get_monthly_operating_data(2454, months=12)
get_earnings(2454, period=2026Q3)              -> 法說會 ~Oct 30; guidance for Q4 from deck
get_insider_activity(2454)                     -> Art. 25 monthly table; 事前申報 pre-declarations
```

### 4.9 ASE Technology Holding (3711 / NYSE: ASX / subsidiary SSE: 601231)

**Periodic clock.** December fiscal year. Taiwan and US as for TSMC (年報, quarterly 財報, 20-F, 6-K). The Shanghai-listed subsidiary USI (环旭电子) follows the Chinese clock: annual and Q1 by 30 April, interim by 31 August, Q3 by 31 October, with its own 业绩预告 obligations if profit swings meet the SSE criteria.

**Earnings sequence.** Monthly revenue by the 10th on MOPS with a 6-K twin. Quarterly results and 法說會 around the end of January, April, July and October. USI reports separately on SSE and CNINFO, so the group's China exposure has an independent, earlier-warning signal through USI's 业绩预告 and quarterly reports.

**Guidance regime.** ASE gives directional and sometimes numeric guidance on the call for its packaging and test business and for USI's EMS business; USI's Chinese filings add mandatory preannouncements.

**Ownership and positioning.** Article 43-1 substantial holders and Article 25 monthly insider and pledge table on the Taiwan side; 13F holdings of the ADR on the US side; for USI, the quarterly top-10 shareholder list (前十大股东) on SSE, which shows ASE's controlling stake and any Chinese institutional holders by name.

**Capital actions.** Dividends and buybacks as 重大訊息 and 6-K; USI's profit distribution as an SSE 利润分配 announcement.

**Operational events.** ASE is the OSAT for TSMC-produced and MediaTek-designed chips, so it sits on the receiving end of the relationships above without any contract filings. Its distinctive event stream is the China layer: USI's related-party transactions with the ASE group are 关联交易 announcements on SSE; any SSE inquiry letter (问询函) to USI and its reply is public; USI's institutional-meeting records (if held on the Shenzhen side of a dual structure, or voluntarily on SSE) and its 上证e互动 Q&A are searchable.

**Quirks.** One group, three regimes: Taiwan enumerated material information, US 6-K and 20-F, Chinese exchange rules for the subsidiary. The rule registry needs `parent_entity_id` links from USI to ASE so that a USI 业绩预告 can be surfaced as a group-level early warning.

**Example calls.**
```text
get_monthly_operating_data(3711)
get_earnings(3711, period=2026Q3)              -> 法說會 late Oct; 6-K
get_subsidiary_disclosures(3711)               -> USI (601231) on SSE / CNINFO: 业绩预告, 关联交易, 问询函
get_exchange_inquiries(601231)                 -> SSE inquiry letters and replies for USI
```

---

## 5. The quarter on one timeline

Illustrative calendar for the September 2026 quarter across the nine names. Dates are approximate patterns, not confirmed schedules.

| Approx. date | Event | Companies | Source |
|---|---|---|---|
| Oct 7 to 8 | Preliminary two-line print | Samsung Electronics | DART 공정공시 |
| Oct 10 | September monthly revenue (quarter now complete) | TSMC, MediaTek, ASE | MOPS + TWSE API; 6-K for TSMC, ASE |
| Oct 15 to 16 | Q3 results, call, Q4 guidance | TSMC | MOPS 法說會 (slides, audio) + 6-K |
| Oct 23 to 31 | Q3 results and call | SK hynix, SEMCO, Samsung (detailed), MediaTek, ASE | DART 공정공시; MOPS 法說會 |
| Late Oct to early Nov | FY3/27 Q2 決算短信, possible forecast revisions | TEL, Advantest | TDnet |
| Early to mid Nov | FY3/27 Q2 決算短信 | Kioxia | TDnet |
| Nov 10 | October monthly revenue (first look at Q4) | TSMC, MediaTek, ASE | MOPS |
| Nov ~14 | 분기보고서 (45-day deadline) | Samsung, SK hynix, SEMCO | DART |
| Nov ~14 | 半期報告書 (45-day deadline) | Kioxia, TEL, Advantest | EDINET |
| Nov ~14 | Q3 財報 (45-day deadline) | TSMC, MediaTek, ASE | MOPS |
| Rolling | Named short positions, daily flows | Korea and Taiwan names daily; Japan shorts | KRX, TWSE, JPX |
| Rolling | Buyback monthly status | TEL, Advantest (if active) | EDINET |
| Oct 31 | USI Q3 report | ASE subsidiary | SSE / CNINFO |

Two things the timeline makes visible. First, Taiwan's official data arrive first (September revenue on 10 October) and the memory makers' detailed numbers arrive last, so a Taiwan-to-Korea nowcast has a real information window. Second, Japan's fiscal calendar means "Q2" for TEL, Advantest and Kioxia is the same calendar quarter as "Q3" for everyone else; the `calendar_quarter_overlap` field is not optional.

---

## 6. The supply-chain example, with real names

Take a hypothetical but realistic chain: SEMCO sells FC-BGA substrates or MLCCs into a design that MediaTek fabs at TSMC and packages at ASE; SK hynix buys test equipment from Advantest and deposition tools from TEL; Kioxia buys tools from TEL. What would each side file?

| Relationship | Side A files? | Side B files? | Why |
|---|---|---|---|
| SEMCO → MediaTek (components) | SEMCO: yes, if the contract exceeds 2.5% of prior-year revenue (`[~KRW 250bn]`); counterparty likely redacted | MediaTek: only if the contract meets TWSE's enumerated tests, which a component purchase normally does not | KR numeric trigger vs TW enumerated tests |
| SK hynix → Advantest (test equipment order) | SK hynix: no (purchase, not sale; and below its own thresholds) | Advantest: no (Japan has no contract category) | Both sides `NO_FILING_EXPECTED`; visible only in Advantest orders and SK hynix capex aggregates |
| SK hynix fab investment (M15X, Yongin) | SK hynix: yes, 신규시설투자 with amount, period, funding | TEL: no; order appears in backlog | The Korean CAPEX filing is the only event-level document in the pair |
| Kioxia Fab3 construction → TEL tools | Kioxia: TDnet fixed-asset disclosure if quantitative criteria met; 有報 capex section | TEL: no | JP enumerated + numeric criteria on the buyer side only |
| MediaTek → TSMC (wafers) | MediaTek: no | TSMC: no; visible in TSMC monthly revenue and capacity commentary | Neither regime selects a foundry contract |
| TSMC → ASE (packaging) | TSMC: no | ASE: no; USI-level 关联交易 only for intra-ASE-group deals | Same |
| Samsung Electronics → any supplier | Samsung: no (2.5% of `[~KRW 300tn]`) | Supplier: often yes, if Samsung's order exceeds the supplier's threshold | The supplier's filing is the only public record of Samsung's procurement |

The last row is the general lesson: in Korea, the small company's filing is where the large company's activity becomes visible. A pipeline that indexes 단일판매·공급계약 filings by counterparty text ("삼성전자", "SK하이닉스", and redacted forms) reconstructs procurement flows that neither Samsung nor SK hynix ever files themselves.

Workflow applied to the SEMCO → MediaTek row:

1. Observe SEMCO 단일판매·공급계약체결 on DART (`obligation_type = MANDATORY_NUMERIC_TRIGGER`, `trigger_rule_id = KR_KOSPI_MAJOR_CONTRACT_2026`, `large_corp = true`).
2. Counterparty text: "대만 소재 고객사" (redacted) or "MediaTek Inc." (named). Store `counterparty_text_raw` and a resolution with confidence.
3. Map to MediaTek (2454, TW, TWSE).
4. Rule set on the Taiwan side: TWSE material-information procedures, enumerated tests.
5. Plausibility: a component purchase of `[KRW 250bn]` against MediaTek's revenue of `[NT$ 500bn+]` is far below any test → `NO_FILING_EXPECTED`.
6. Search MOPS 重大訊息 for MediaTek in the window anyway; record the null result with the expected-null label.
7. Monitor SEMCO's later 정정 filings for the deferral expiry that names the counterparty.

---

## 7. The nowcast example, with real names

The Taiwan monthly-revenue stack gives an official high-frequency read on the chain that feeds the Korean and Japanese names' later reports.

| Step | Data | Timing |
|---|---|---|
| 1 | TSMC, MediaTek, ASE monthly revenue | 10th of each month |
| 2 | Seasonality-adjusted YoY, 3M acceleration, quarter-to-date vs TSMC's own guidance range | Same day |
| 3 | Cross-read to Japanese equipment: TEL and Advantest forecast revisions (if any) and 決算短信 order commentary | Late April, July, October, January |
| 4 | Cross-read to Korean memory: Samsung preliminary (Oct ~7), SK hynix full release (late Oct) | Following month |
| 5 | Score: did the Taiwan composite lead the Korean prints? Did Advantest's upward revisions precede SK hynix's HBM commentary? | Quarterly |

The official monthly series doubles as the truth set for any alternative-data nowcast of the same companies.

---

## 8. Rule registry entries the nine companies need

| rule_id | Applies to | Key parameters |
|---|---|---|
| KR_KOSPI_MAJOR_CONTRACT_2026 | Samsung, SK hynix, SEMCO | 5% of prior-year sales; 2.5% because all three are 대규모법인 |
| KR_LARGE_HOLDER_5PCT | all three | 5%; 1pp changes; 5 business days; purpose field |
| KR_INSIDER_TRADE_PLAN | all three | ≥1% or ≥KRW 5bn; ~30 days before |
| KR_SHORT_POSITION_PUBLIC | all three | ≥0.5% named |
| KR_FTC_GROUP_DISCLOSURE | all three | Samsung group, SK group |
| KR_PROFIT_CHANGE_30_15 | all three | 15% (large corporations) at annual close |
| JP_QUARTERLY_REGIME | Kioxia, TEL, Advantest | statutory Q1/Q3 abolished 2024-04-01 |
| JP_FORECAST_REVISION | Kioxia, TEL, Advantest | sales ±10% / profit ±30% criteria |
| JP_LARGE_HOLDER | Kioxia, TEL, Advantest | >5%; 5 business days; special reporting for institutions |
| JP_BUYBACK_STATUS | TEL, Advantest | monthly EDINET report; TDnet resolution and progress |
| JP_SHORT_POSITION_PUBLIC | all three | ≥0.5% named |
| JP_LISTING_DATE | Kioxia | 2024-12-18; no filings before |
| TW_MONTHLY_REVENUE_ART36 | TSMC, MediaTek, ASE | by the 10th |
| TW_LARGE_HOLDER_2024 | TSMC, MediaTek, ASE | >5% since 2024-05-10; 10 days |
| TW_INSIDER_ART25 | TSMC, MediaTek, ASE | monthly holdings and pledges; 3-day pre-declaration |
| TW_MATERIAL_INFO | TSMC, MediaTek, ASE | enumerated events with quantitative tests |
| TW_INVESTOR_CONFERENCE | TSMC, MediaTek, ASE | slides and audio on MOPS |
| US_6K_20F | TSMC, ASE | 6-K on material events; 20-F annual |
| US_13F | TSMC, ASE (ADRs) | manager-side quarterly holdings |
| CN_SSE_LISTING_RULES_2026 | USI (ASE subsidiary) | 业绩预告 triggers; quarterly top-10 holders; 关联交易 |

---

## 9. What a single cross-market query returns

**"Buybacks across the nine in the last twelve months."**

| Company | Authorization | Execution | Completion / retirement | Notes |
|---|---|---|---|---|
| Samsung | DART 자기주식취득 결정 | trust or direct; 결과보고서 | 소각 filing | one Korean chain, one source |
| SK hynix | same | same | same | |
| SEMCO | same if any | | | may be none |
| Kioxia | none expected (recent IPO) | | | `NO_FILING_EXPECTED` |
| TEL | TDnet resolution | EDINET monthly 自己株券買付状況報告書 + TDnet progress | TDnet completion; 消却 separate | two sources for one event |
| Advantest | same pattern | same | same | |
| TSMC | 重大訊息 board resolution (rare) | 執行情形 | 註銷 | plus 6-K |
| MediaTek | 重大訊息 if any | | | |
| ASE | 重大訊息 + 6-K | | | USI buybacks separately on SSE |

The answer is one table, but it was assembled from five systems with three different authorization-to-execution structures. That is the taxonomy doing its job.

**"Who owns them, and who is short."**

| Layer | Korea (3) | Japan (3) | Taiwan (3) |
|---|---|---|---|
| Company-side large holders | DART 대량보유 (5%) | EDINET 大量保有 (>5%) | MOPS Art. 43-1 (>5%) |
| Insiders | DART officer reports + ex-ante trade plans | via 大量保有 | Art. 25 monthly + pre-declarations |
| Manager-side | none | none | 13F for TSM and ASX ADRs only |
| Named shorts | KRX ≥0.5% | JPX ≥0.5% | none (aggregate lending) |
| Daily flows | KRX | none (weekly aggregate) | TWSE |
| Pledges | in 대량보유 | none | Art. 25 table |

---

## 10. Takeaway from the nine

- The same economic events (a quarter's earnings, a fab investment, a buyback, a large holder selling) exist for all nine companies. The number of documents, the sources, the timestamps and the obligation types differ in every case.
- Within one market the rules select differently by size: Samsung never files a supply contract, SEMCO sometimes does, and both are under the same 2.5% rule.
- Three of nine companies touch a second or third regime (TSMC and ASE via EDGAR, ASE via its Shanghai subsidiary), so entity resolution and parent links are not optional even for a nine-name universe.
- Taiwan's monthly revenue arrives first, Japan's forecast revisions arrive when thresholds are crossed, Korea's preliminary print arrives for one company only. A cross-market signal has to respect that order.

**Normalize the event. Preserve the source. Version the rule. Never overwrite history.**
