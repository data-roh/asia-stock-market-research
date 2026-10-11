# A Taxonomy of Asian Disclosure Systems: Detailed Edition

## Korea, Japan, China and Taiwan, benchmarked against US EDGAR, with rule-level detail and a data architecture

> **Purpose.** This is the long-form companion to the Asia Stock Review piece *A Taxonomy of Asian Disclosure Systems*. The newsletter states the conclusions. This edition shows the rules behind them, corrects the places where the newsletter's shorthand was legally too broad, and lays out the schema, signals and quality controls needed to turn five disclosure systems into one point-in-time research database.
>
> **As-of date:** 12 September 2026. Rules, thresholds, APIs and taxonomies change. A production system should version the rulebook and the source metadata rather than hard-code anything below.
>
> *Claude Opus 5 and Claude Fable 5.1 (Anthropic) assisted with research, tables and editing under the author's direction; all judgments and errors are the author's own. Personal research, unrelated to the author's day job. Not investment advice.*

---

## 1. Executive conclusion

The thesis holds: **normalize the economic event, preserve the original source.** Korea, Japan, Mainland China, Taiwan and the US all disclose earnings, financing, ownership, corporate actions and material events. They do so through different legal layers, document types, taxonomies, time rules and interfaces. A cross-market system should never use a local filing name as its primary data model.

The architecture summary also holds:

| Market | Architecture | What that means in practice |
|---|---|---|
| 🇰🇷 Korea | Integrated discovery and API ecosystem centred on DART / OpenDART | One search surface and one API, even though the legal obligations come from the FSC / FSS, KRX rules and the Fair Trade Commission separately |
| 🇯🇵 Japan | Two-system model: EDINET (statutory) + TDnet (exchange timely disclosure) | You need both; neither is complete alone |
| 🇨🇳 China | Distributed: CSRC rules + exchange rules and publication + portals and data services | No single DART analogue; SSE, SZSE, BSE and CNINFO are all first-class sources |
| 🇹🇼 Taiwan | Central MOPS platform + unusually rich TWSE / TPEx structured APIs | The easiest market to turn into a database, with mandatory monthly operating data |
| 🇺🇸 US | Single statutory archive (EDGAR) with no separate exchange filing taxonomy | World-class developer platform; the event menu for operational events is more principles-based than in Asia |

Ten places where the short version needed tightening, all now reflected in the newsletter and in this edition:

1. **Taiwan large-holder threshold.** The Article 43-1 substantial-shareholding threshold is more than 5%, not 10%, effective 10 May 2024. A separate Article 25 regime covers directors, supervisors, officers and holders above 10%, with monthly reporting. These are different systems and must be modelled as two concepts.
2. **Japan buyback execution.** The canonical monthly Self-Share Purchase Status Report (自己株券買付状況報告書) is a statutory EDINET filing under the FIEA. TDnet also carries resolutions and progress or completion notices. "Monthly, TDnet" alone was incomplete.
3. **Japan guidance revisions.** Not every change in guidance triggers a filing. Timely disclosure becomes mandatory when the exchange's forecast-revision criteria are met: roughly 10% for sales and 30% for profit items, with edge cases for small profits, sign changes and range forecasts. Publishing a forecast at all is expected practice under the earnings-report format rather than a legal requirement, and nearly every company does it.
4. **Taiwan material information.** It is not merely a "materiality judgment". TWSE's Procedures for Verification and Disclosure of Material Information contain an enumerated list of events with quantitative tests plus residual materiality clauses. Important contracts are one enumerated category.
5. **China regulator correspondence.** Chinese exchanges publish inquiry letters and issuer responses. This is not the SEC comment-letter process, but it is a major public research dataset.
6. **Korea supply-contract threshold.** "A fixed percentage" is correct in direction but market-specific: the current KOSPI handbook uses 5% of prior-year sales (2.5% for large corporations); KOSDAQ filings cite 10%.
7. **Korea ex-ante trade plans.** Korea has a pre-trade disclosure regime: officers and major shareholders planning a trade of 1% or more of the shares, or KRW 5 billion or more, report the plan about 30 days ahead. The short version had credited only China and Taiwan with ex-ante insider disclosure.
8. **"Materiality vs numeric thresholds."** Too binary. All five systems mix enumerated events, quantitative tests, qualitative materiality and residual clauses. The difference is degree and event granularity.
9. **CNINFO positioning.** CNINFO is a critical official portal, closely tied to the Shenzhen infrastructure and useful as a cross-market search layer, but it is not the single final publication node for all Mainland exchanges. The exchanges remain authoritative sources.
10. **EDGAR 5:30 p.m. rule.** Generally right, but there are submission-type exceptions. Store the actual acceptance timestamp and the filing date rather than coding a blanket time rule.

The strongest form of the argument is not "Asia discloses more than the US". It is this: **the five markets optimize public disclosure around different objects.** The US is exceptionally strong in standardized ownership reporting, filing-review correspondence and public-data infrastructure. Several Asian markets expose operational corporate events (contracts, forecast revisions, monthly revenue, pledges, group transactions, exchange inquiries) in forms that are unusually structured or frequent. The research edge comes from knowing which regime selects which events into the public record.

---

## 2. A five-layer model instead of a "DART equivalent"

The single most useful architectural move is to separate who makes the rule, who receives and distributes the document, what the document is called natively, what economic event it describes, and what feature you compute from it.

### Layer 1: legal and regulatory authority

| Market | Authorities |
|---|---|
| Korea | Financial Investment Services and Capital Markets Act; FSC / FSS administration; KRX listing and disclosure rules (KOSPI, KOSDAQ, KONEX); Fair Trade Commission group-disclosure rules |
| Japan | Financial Instruments and Exchange Act / FSA; JPX / TSE listing rules |
| China | Securities Law / CSRC regulations (currently the Information Disclosure Measures, Order No. 226, effective 1 July 2025); SSE, SZSE and BSE listing rules (SSE rules last revised April 2026) |
| Taiwan | Securities and Exchange Act / FSC; TWSE and TPEx listing and material-information rules |
| US | Securities Act, Exchange Act, SEC rules; NYSE / Nasdaq listing rules |

### Layer 2: submission and dissemination system

| Market | Systems |
|---|---|
| Korea | DART / OpenDART (FSS); KRX-originating disclosures surfaced through KIND and DART |
| Japan | EDINET (FSA) and TDnet (TSE) |
| China | SSE, SZSE and BSE disclosure systems; CNINFO and related services |
| Taiwan | MOPS; TWSE and TPEx systems and OpenAPIs |
| US | EDGAR; issuer and exchange news channels |

### Layer 3: source-native document taxonomy

사업보고서, 有価証券報告書, 年度报告, 年報, 10-K. This layer must be preserved because it carries legal provenance.

### Layer 4: cross-market economic-event taxonomy

`EARNINGS_RELEASE`, `GUIDANCE_REVISION`, `BUYBACK_AUTHORIZATION`, `BUYBACK_EXECUTION`, `MAJOR_CONTRACT`, `CAPEX`, `ASSET_ACQUISITION`, `LARGE_HOLDER_CHANGE`, `INSIDER_TRADE_PLAN`, `INSIDER_TRADE_EXECUTION`, `SHARE_PLEDGE`, `SHORT_POSITION`, `RUMOR_RESPONSE`, `EXCHANGE_INQUIRY`, `LITIGATION`, `DISTRESS`. This is the layer a PM, a quant researcher or an LLM should query.

### Layer 5: research features and signals

Contract value over prior-year revenue; new guidance over old guidance; buyback executed over authorized; pledged shares over controller holdings; monthly revenue surprise; filing delay; correction count; cross-counterparty disclosure lag.

The rule: **never throw away the source-native filing, and never expose source complexity to the research user unless they ask for it.**

---

## 3. Korea: the integrated discovery and API benchmark

### 3.1 What is integrated, and what is not

OpenDART's disclosure-search API exposes ten top-level types: A Periodic, B Major Issues, C Issuance, D Equity, E Other, F External Audit, G Funds, H Asset-Backed Securitization, I Exchange Disclosure, J Fair Trade Commission Disclosure. The response also flags whether a document falls under KOSPI, KOSDAQ, KONEX, bond-market or KFTC authority, and marks amended or withdrawn documents. That metadata is unusually valuable for a normalized event store.

"One ecosystem" does not mean "one legal regime". A KRX timely-disclosure rule and a KFTC business-group disclosure have different legal bases, triggers and enforcement even though the investor discovers both from the same environment. Statutory "major matter reports" (주요사항보고서) go to the FSS under the Capital Markets Act; event disclosures (수시공시) go to KRX under the listing rules; both are served through DART.

### 3.2 Periodic reporting

Annual business report within 90 days; semi-annual and quarterly reports within 45 days. OpenDART offers structured financial endpoints and XBRL source downloads. The engineering problems are consolidated versus separate statements, original reporting units, taxonomy versions, restated values, and aligning Korean fiscal periods with March-year-end Japan and calendar-year China and Taiwan.

### 3.3 Earnings: preliminary prints are a fair-disclosure filing

Preliminary earnings (영업(잠정)실적) travel through the fair-disclosure channel (공정공시), which is why they are voluntary: the rule says that anything given selectively to analysts must be filed publicly, not that a preliminary must be produced. The largest names publish a two-line consolidated print (sales, operating profit) about a week after quarter-end; most listed companies produce no preliminary at all, so their first number is the quarterly report up to 45 days later. Separately, when annual sales or profit changes 30% or more versus the prior year (15% for large corporations), a dedicated filing is required when the books close, before the annual report.

### 3.4 Three ownership regimes, not one

| Regime | Trigger | Deadline | Notes |
|---|---|---|---|
| Large shareholding (5% rule) | Crossing 5%; later 1 percentage-point change or material change of purpose | 5 business days | Encodes purpose of holding (management participation / general / simple investment); cooling-off period after a management-participation filing |
| Officer and major-shareholder ownership | Any change by officers or holders with 10%+ voting power or de facto influence | 5 days after the trade | Post-trade regime, separate from the 5% rule |
| **Ex-ante trade plan** | Planned trade by an officer or major shareholder of 1% or more of the securities, or KRW 5 billion or more, including relevant recent trades | About 30 days before the trading period starts | Conceptually different from the US Form 4; creates `INSIDER_TRADE_PLAN_EX_ANTE` and `INSIDER_TRADE_EXECUTION_POST` as two events |

Features from the trade-plan regime: planned amount over ADV, planned amount over insider holdings, cancellation and modification rate, execution versus plan, returns around plan announcement and execution window.

### 3.5 Positioning data the US does not publish

Net short positions of 0.5% or more are disclosed with the holder's name (Japan has the same rule; the US publishes aggregates). KRX publishes daily net buying by foreigners, institutions and retail for every stock (Taiwan does the same; Japan publishes weekly aggregates).

### 3.6 Supply contracts: thresholds by market

| Market | Threshold for a single sales / supply contract filing |
|---|---|
| KOSPI | 5% of prior-year sales; 2.5% for large corporations |
| KOSDAQ | 10% of recent fiscal-year sales |

Do not store one field `korea_supply_contract_threshold = 5%`. Store `market_segment`, `rule_version`, `issuer_large_corp_flag`, `threshold_type`, `threshold_value`, `threshold_denominator`. The correct research feature is `contract_value / rule_relevant_sales`, not contract value over market cap.

### 3.7 Contract confidentiality is not missing at random

Korea allows disclosure deferral for commercially sensitive terms, typically at the counterparty's request, with later correction when the deferral ends. A missing counterparty may mean the issuer legitimately withheld the field until a later date. Store `counterparty_disclosed_flag`, `deferral_flag`, `deferral_reason`, `deferral_expiry`, `counterparty_first_public_at`. This is essential for avoiding look-ahead bias when amended filings later reveal withheld information.

### 3.8 Inquiry disclosure and disclosure-quality penalties

The exchange can demand a public answer to a rumor or unexplained price move on a deadline of about a day (조회공시); the "confirmed / denied / undecided" reply is itself a filing and a tradeable event. The exchange also designates "unfaithful disclosure companies" (불성실공시법인) with penalty points that accumulate toward trading halts.

### 3.9 KFTC disclosures: the group-structure edge

Fair Trade Commission filings by designated large business groups cover large inter-affiliate transactions (with a board resolution and filing before execution), business-group status, ownership and control relationships, debt guarantees and related-party transactions. Do not compress this into a generic `RELATED_PARTY` field. Keep `BUSINESS_GROUP_DISCLOSURE`, `INTER_AFFILIATE_TRANSACTION`, `GROUP_OWNERSHIP_STRUCTURE`, `RELATED_PARTY_FINANCING`. Useful for holding-company discounts, succession and control analysis, intra-group funding stress and related-party support.

### 3.10 Data-engineering assessment

Strengths: integrated search taxonomy, good entity identifiers (corp_code), structured finance endpoints, XBRL source downloads, ownership and event APIs, explicit amendment markers, deep event disclosure. Weak points: the legal source is more fragmented than the API makes it look; thresholds vary by KRX market and issuer class; attachments and deferred fields complicate parsing; taxonomy versions and amended filings must be preserved; Korean labels and event subtypes need normalization.

---

## 4. Japan: EDINET and TDnet are complementary, not substitutes

### 4.1 The clean mental model

EDINET is statutory securities-law disclosure run by the FSA: annual securities report (有価証券報告書), semi-annual report (半期報告書), extraordinary report (臨時報告書), securities registration statement (有価証券届出書), large shareholding report (大量保有報告書), tender-offer statement (公開買付届出書), target opinion report (意見表明報告書), internal control report (内部統制報告書), and the self-share purchase status report (自己株券買付状況報告書).

TDnet is exchange timely disclosure run by TSE: earnings reports (決算短信), forecast and dividend revisions, share-repurchase resolutions and progress notices, issuance, M&A and reorganizations, fixed-asset actions, management changes, business and capital alliances, litigation and other timely disclosure, plus supplementary materials such as the earnings-briefing deck.

### 4.2 The 2024 quarterly reporting regime break

From 1 April 2024 the statutory quarterly securities report was abolished. Post-reform: annual and semi-annual statutory reports in EDINET; Q1 and Q3 earnings reporting, and the annual and Q2 earnings summaries, in the TDnet framework. A database spanning 2015 to 2026 needs a `jp_quarterly_regime_version` field because a "Q1 filing" before and after April 2024 does not come from the same legal path.

### 4.3 Guidance revisions: powerful, but threshold-based

Publishing a full-year forecast is not itself a legal requirement, but the 決算短信 format includes one and nearly every company provides it. Once published, TSE timely disclosure becomes mandatory when newly calculated figures diverge from the latest public forecast or reference result and the exchange's criteria are met: roughly ±10% for sales and ±30% for major profit measures, with small-profit exceptions, sign-change rules and range-forecast handling. Revisions are XBRL-tagged and filed the same day.

That allows features beyond a binary "guidance changed": `sales_revision_pct`, `operating_profit_revision_pct`, `ordinary_profit_revision_pct`, `net_income_revision_pct`, `sign_flip`, `crossed_mandatory_threshold`, `days_since_prior_guidance`, `revision_number_fy`.

### 4.4 TDnet access: public view versus institutional feed

The free TDnet viewing service displays 31 days of information; it is not an unlimited public historical database. JPX sells a server-based real-time feed, a TDnet API (five years of history), a database service and Snowflake distribution. Content: earnings information (summary PDF, full PDF, XBRL), forecast and dividend revisions (PDF + XBRL), other disclosures including issuance, stock options, buybacks and PR (PDF). Prototype research and an institutional historical feed are different products.

### 4.5 Buybacks: the correct source mapping

| Event | Source |
|---|---|
| `BUYBACK_AUTHORIZATION` | TDnet resolution and terms |
| `BUYBACK_MONTHLY_EXECUTION` | EDINET statutory self-share purchase status report (FIEA Art. 24-6), often with a TDnet progress notice |
| `BUYBACK_COMPLETION` | TDnet or related disclosure |
| `BUYBACK_CANCELLATION_OR_RETIREMENT` | Separate corporate-action event |

This is the clearest example of why source-native document identity and economic-event identity must be separate tables.

### 4.6 Large shareholding

Crossing 5% triggers a Large Shareholding Report within five business days; a later change of 1 percentage point or more triggers a Change Report within five business days. Qualifying institutional investors use a special reporting system with batched reference dates, so filing timestamps are not economically identical across holder types: activist accumulation shows up faster than passive accumulation.

### 4.7 Cross-shareholdings and human-capital data in the annual report

The 有価証券報告書 lists the company's strategic cross-shareholdings (政策保有株式) by name, with the stated reason for holding each (top holdings named). It also carries average salary, average age, average tenure, and since FY2023 the gender pay gap, female-manager ratio and male parental-leave rate. TSE's cost-of-capital initiative adds an exchange-maintained public list of which companies have disclosed an action plan on capital cost and share price.

### 4.8 EDINET API and taxonomy

EDINET API v2 (subscription key required) provides daily document lists and metadata, document retrieval by ID, XBRL packages, PDF, attachments, English files where available and XBRL-to-CSV where available. The EDINET taxonomy is broader than financial statements: the 2026 taxonomy includes document classes such as large-shareholding, tender-offer and self-share purchase status reports, and the FSA published a draft 2027 taxonomy on 11 September 2026 with sustainability-related work linked to the IFRS sustainability taxonomy. Store `taxonomy_name`, `taxonomy_version`, `namespace`, `concept_qname`, `effective_from`, `effective_to`. Never hard-code "Japanese XBRL tag = permanent concept".

### 4.9 Japan does use quantitative tests

Japan's timely-disclosure rules contain many quantitative "minor criteria" tests based on sales, profit, net assets or transaction size, alongside residual materiality. The correct comparison is not "numeric Asia versus principles-based Japan and US" but:

| Market | Rule style |
|---|---|
| Korea | Enumerated events + numerical tests + residual concepts |
| Japan | Enumerated events + numerical minor criteria + residual materiality |
| China | Enumerated statutory and exchange events + numerical tests + residual materiality |
| Taiwan | Enumerated material-information events + numerical tests + residual clauses |
| US | Form-item requirements + legal materiality + some quantitative tests in specific rules |

The difference is degree and event granularity.

---

## 5. Mainland China: the source hierarchy is part of the dataset

### 5.1 Start from the current CSRC rule

The Measures for the Administration of Information Disclosure by Listed Companies (CSRC Order No. 226) were promulgated 26 March 2025 and took effect 1 July 2025. At the CSRC layer, periodic reports are framed around annual and interim reports; material events require immediate disclosure.

### 5.2 Exchange rules add the operational filing universe

The SSE Stock Listing Rules (effective 24 April 2026) and their SZSE and BSE counterparts define detailed listed-company obligations, including Q1 and Q3 reports. Model `CSRC_RULE`, `EXCHANGE_RULE` and `DISCLOSURE_DOCUMENT` as separate objects, and store `rule_authority`, `rule_version`, `exchange`, `board`, `issuer_type`, because Main Board, STAR, ChiNext and BSE differ in implementation.

### 5.3 CNINFO: important, but not the whole topology

CNINFO (巨潮资讯) is a critical official disclosure and search platform, closely tied to the Shenzhen securities-information infrastructure, and highly useful as a unified retrieval layer. Keep `SSE`, `SZSE`, `BSE` and `CNINFO` as distinct source IDs: exchange sites are the authoritative dissemination and enforcement nodes, exchange-specific metadata and inquiry pages differ, a portal may normalize or mirror content, and source timestamp and URL lineage matter for event studies.

### 5.4 High-value event types

`EARNINGS_PREANNOUNCEMENT` (业绩预告), `EARNINGS_FLASH` (业绩快报), `BUYBACK` (股份回购), `HOLDER_INCREASE_DECREASE` (股东增减持, with the 15-trading-day advance plan for controllers and directors), `SHARE_PLEDGE_FREEZE` (股权质押/冻结), `MAJOR_ASSET_RESTRUCTURING` (重大资产重组), `MAJOR_INVESTMENT` (重大投资), `MAJOR_CONTRACT` (重大合同), `PROFIT_DISTRIBUTION` (利润分配), `LITIGATION_ARBITRATION` (重大诉讼/仲裁), `REGULATORY_PENALTY` (行政处罚), `RELATED_PARTY_TRANSACTION` (关联交易), `RISK_WARNING` (ST / *ST status events), `ABNORMAL_PRICE_MOVE` (股价异动公告).

### 5.5 Preannouncements are rule-driven, but not one universal threshold

SSE rules specify mandatory annual-performance preannouncements in situations such as an expected net loss, a turnaround from loss to profit, large profit changes (commonly around 50%), certain low-revenue or negative-profit conditions, and negative net assets. Deadlines and details are exchange, board and version dependent (annual by 31 January is the common case). Store `preannouncement_trigger_code`, `exchange`, `board`, `rule_version`, `mandatory_flag` rather than one generic threshold.

### 5.6 Exchange inquiry letters are public data

The SSE has a public regulatory-inquiry section (监管问询), and companies publish responses to information-disclosure inquiry letters; SZSE has parallel 问询函 and 关注函 flows. Event types: `EXCHANGE_INQUIRY_ISSUED`, `ISSUER_INQUIRY_RESPONSE`, `INQUIRY_FOLLOWUP`, `SELF_REGULATORY_MEASURE`, `DISCIPLINARY_ACTION`. Features: inquiry category, number of questions, accounting versus transaction versus governance focus, response delay, amendment after inquiry, auditor involvement, stock reaction, recurrence by issuer. Not identical to SEC staff comment letters, but the analytical parallel is real, and the Chinese letters arrive faster.

### 5.7 Management-attention data no other market has

Shenzhen-listed companies must post an investor-relations activity record (投资者关系活动记录表) within two trading days of meeting investors, including the names of attending funds and the Q&A; Shanghai encourages the same. Exchange-run Q&A platforms (互动易 in Shenzhen, 上证e互动 in Shanghai) let any investor ask a question that management must answer in writing. Annual results briefings (业绩说明会) are open to all investors online with records posted. Top-10 shareholders, including top-10 holders of float shares, are published every quarter.

### 5.8 China and XBRL

XBRL exists in the exchange ecosystem, and SSE guidance requires exchange-provided tools for XBRL submission of periodic reports. But "XBRL exists" does not imply "one OpenDART-style public cross-exchange API". Build adapters by source (`cn_sse`, `cn_szse`, `cn_bse`, `cn_cninfo`, `cn_structured_data`, `cn_document_parser`) and normalize after ingestion.

### 5.9 The research edge is granularity plus enforcement metadata

Preannouncement-to-actual error; inquiry letter to restatement probability; shareholder pledge plus price drawdown; regulatory penalty recurrence; restructuring lifecycle; buyback execution rate; major-contract concentration; ST transitions; related-party transaction intensity. The source hierarchy and revision history are part of the alpha-generating dataset, not merely plumbing.

---

## 6. Taiwan: the highest-value public high-frequency fundamentals stack

### 6.1 The architecture

FSC / Securities and Exchange Act → MOPS central disclosure → TWSE / TPEx listing and material-information rules → TWSE / TPEx structured OpenAPI. Do not treat "Taiwan" as one exchange: store `market = TWSE | TPEX | emerging`.

### 6.2 Monthly operating status is a legal obligation

Securities and Exchange Act Article 36 requires issuers, subject to exceptions, to publicly announce and file the operating status for the preceding month within the first ten days of each calendar month. That is the legal foundation of the monthly revenue dataset and why it behaves like official alternative data. Some issuers (notably financial holding companies) add voluntary monthly self-assessed earnings (自結損益). Article 36 also sets Q1 to Q3 financial reports within 45 days of quarter-end and the annual report within the prescribed deadline; financial institutions and other special categories can differ.

### 6.3 Two holder regimes: 5% and 10%

| Regime | Trigger | Timing | Content |
|---|---|---|---|
| Article 43-1 substantial shareholding | Acquisition above 5% (lowered from 10%, effective 10 May 2024) | Initial declaration within 10 days; subsequent changes per prescribed rules | Public declaration via MOPS workflow |
| Article 25 insiders and major holders | Directors, supervisors, managerial officers, and holders above 10% | Report prior-month changes to the issuer by the 5th; issuer reports on the statutory timetable | Holdings and pledges (質權設定) monthly; planned transfers pre-declared 3 days before selling |

An API endpoint labelled "10%+ shareholders" reflects the Article 25 regime, not the large-holder threshold. Model `TW_SUBSTANTIAL_HOLDER_5PCT` and `TW_INSIDER_MAJOR_HOLDER_10PCT` separately.

### 6.4 Pledges as first-class ownership-risk data

Features: `pledged_shares`, `pledged_pct_of_holder_position`, `pledged_pct_of_company`, `new_pledge`, `released_pledge`, `pledge_acceleration`. Combined with price drawdown and ownership concentration, a useful controller-stress indicator.

### 6.5 Material information is enumerated, not purely discretionary

TWSE's Procedures for Verification and Disclosure of Material Information contain an extensive enumerated list: credit and default events, trading-method and listing changes, material transactions, important contracts, investments, production and business disruptions, litigation and regulatory events, governance and control events, with specific quantitative tests and residual materiality clauses, plus disclosure time limits. The English translation available in 2026 notes a 2026 amendment to Articles 6 and 11 and lags the Chinese text. Certain major events also require a press conference at the exchange (重大訊息說明記者會). For a large foundry, one supplier contract usually falls below the tests, which is why the Korean counterparty's filing often has no Taiwanese twin; that is `NO_FILING_EXPECTED`, not "not found".

### 6.6 Investor conferences are filings

For investor conferences (法說會) the slides and the audio recording must be uploaded to MOPS. Taiwan is the only compared market where the earnings call is literally in the disclosure archive.

### 6.7 Structured data and positioning

TWSE's OpenAPI / Swagger interface and TPEx's parallel API cover monthly revenue, financial statements, material information, shareholders, governance, ESG and more. Daily per-stock data include foreign, investment-trust and dealer net buying, margin and securities-lending balances, and foreign ownership percentage. Taiwan adopted XBRL from Q2 2010 and has required Inline XBRL for all public companies since Q1 2019. An annual regulator-run corporate-governance evaluation ranks every listed company into published tiers.

---

## 7. United States benchmark: keep it, use it carefully

### 7.1 EDGAR developer infrastructure

Free, unauthenticated JSON APIs at data.sec.gov (submissions history, company facts, XBRL frames), filing indexes, bulk data and full-text search. Every filing has an accession number; amendments carry a `/A` suffix; acceptance timestamps are recorded to the second. XBRL since 2009, iXBRL phased in 2019 to 2021. World-class public infrastructure.

### 7.2 Ownership is where the US is genuinely powerful

Form 13F: institutional managers above the threshold file holdings quarterly, generally within 45 days of quarter-end. Not a live portfolio, but a unique manager-level holdings panel. Schedule 13D / 13G: beneficial owners crossing 5%, with 13D now due within five business days. Forms 3/4/5: Form 4 within two business days, XML, transaction codes. Fair wording: the US has the strongest standardized public manager and insider ownership reporting among the five systems; Asian systems expose different variables, particularly pledges, control-family data, named short positions and daily flows.

### 7.3 Comment letters: excellent, with a Chinese parallel

SEC filing-review correspondence is released after the review process and is searchable as `UPLOAD` and `CORRESP`. The corrected comparison: US → SEC staff comment and review letters (delayed); CN → exchange inquiry letters and issuer responses (immediate). Not identical processes; both support textual and event-driven research.

### 7.4 Earnings release: the "furnished" nuance

A standard earnings release disclosed under Form 8-K Item 2.02 is generally furnished, not deemed filed for Section 18 purposes, unless the issuer alters that treatment. Guidance is voluntary under Reg FD constraints; the call and transcript are not filed; slides may be furnished under Item 7.01; filed financial statements arrive later in the 10-Q. Reg G requires reconciliation of non-GAAP numbers in the release.

### 7.5 Buybacks

The SEC's 2023 repurchase-rule modernization, which would have required daily data, was vacated effective 19 December 2023 and the prior regime (the quarterly Item 703 table with monthly detail) was restored by technical amendment. Authorization itself has no dedicated 8-K item.

### 7.6 Form 10-S: a future regime break, not current law

On 5 May 2026 the SEC proposed allowing companies to elect a semiannual Form 10-S in lieu of three 10-Qs. As of 12 September 2026 it is a proposal; 10-Qs remain required. A production database should track `rule_status = PROPOSED | ADOPTED | EFFECTIVE | VACATED`.

### 7.7 What the US does not require as discrete events

CAPEX commitments, supply contracts below the materiality line or in the ordinary course, production halts, monthly revenue, guidance, rumor responses. 8-K Item 1.01 covers material definitive agreements outside the ordinary course; Item 2.01 covers completed acquisitions and dispositions above a significance test; Item 4.02 is a clean restatement flag; Items 5.01, 5.02, 1.03 and 3.01 cover control change, executive change, bankruptcy and delisting notice.

---

## 8. Corrected cross-market event matrix

"Mandatory" always means subject to the relevant trigger, issuer type, venue and current rule. "None" means no standard mandatory category exists; the information may still appear in a periodic report or a voluntary release.

### 8.1 Periodic and earnings disclosure

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Annual report | 사업보고서 (DART, 90 days) | 有価証券報告書 (EDINET, 3 months) | 年度报告 (by Apr 30) | 年報 (MOPS, by Mar 31) | 10-K (60 to 90 days) |
| Semi-annual / interim | 반기보고서 (45 days) | 半期報告書 (EDINET) | 半年度报告 (by Aug 31) | 半年度財報 (45 days) | 10-Q Q2; optional Form 10-S proposed 2026 |
| Q1 / Q3 | 분기보고서 (45 days) | 決算短信 (TDnet); statutory quarterly report abolished April 2024 | 季度报告 (exchange rules; Q1 by Apr 30, Q3 by Oct 31) | 季報 (45 days) | 10-Q (40 to 45 days) |
| Preliminary / flash earnings | 영업(잠정)실적 공정공시 (voluntary; mainly large caps) | none (決算短信 is the full release) | 业绩快报 (optional) | 自結損益 (voluntary, monthly, mainly financials) | 8-K Item 2.02 (typically furnished) |
| Earnings early warning | 매출액·손익구조 30% (15%) 변동 (annual, ex post, mandatory) | 業績予想の修正 when criteria met (mandatory) | 业绩预告 on expected loss, turnaround or large change (mandatory; annual by Jan 31; details by board) | none | none (voluntary via 8-K 2.02 / 7.01) |
| Monthly revenue | none | none | none | 每月營收 by the 10th (Art. 36, mandatory; TWSE / TPEx API) | none |
| Guidance | 공정공시 if given (voluntary) | 決算短信 forecast (expected practice); revisions mandatory above ~10% sales / ~30% profit, XBRL | 业绩预告 | none | Voluntary, Reg FD |

### 8.2 Shareholder return and financing

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Buyback authorization | 자기주식취득 결정 | 自己株式取得 resolution (TDnet) | 股份回购 | 庫藏股 (board resolution with price range) | none (press release / 8-K 8.01) |
| Buyback execution | 자기주식취득결과보고서 | 自己株券買付状況報告書 (monthly, statutory, EDINET) + TDnet progress notices | 回购进展 | 庫藏股執行情形 | 10-Q / 10-K Item 703 (quarterly, monthly detail) |
| Treasury disposal / cancellation | 자기주식처분·소각 | 自己株式消却 | 回购股份注销 | 庫藏股註銷 | none |
| Dividend | 현금·현물배당결정 | 配当予想の修正 (TDnet, XBRL) | 利润分配 | 股利分派 | none (press release) |
| Equity issuance | 유상증자 | 有価証券届出書 (EDINET) / 新株発行 (TDnet) | 增发 / 配股 | 現金增資 | S-1 / S-3, 424B; 8-K 3.02 |
| Convertible / debt | 전환사채·신주인수권부사채 | 転換社債型新株予約権付社債 | 可转债 | 可轉換公司債 | 8-K 2.03 |
| Capital reduction | 감자 | 減資 | 减资 | 減資 | none |
| Tender offer | 공개매수 | 公開買付届出書 / 意見表明報告書 (EDINET) | 要约收购 | 公開收購 | Schedule TO / SC 14D-9 |

### 8.3 Ownership, positioning and control

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Large holder threshold | 5%; 1pp changes; 5 business days; purpose encoded | >5%; 1pp changes; 5 business days; institutions on special batched reporting | 5% (权益变动报告书) | >5% (Art. 43-1, since 10 May 2024; within 10 days) | 13D / 13G >5%; 13D within 5 business days |
| Company-side top holders | 사업보고서 5%+ holders | 有報 大株主 top 10 (semi-annual) | 前十大股东 + 前十大流通股东 (quarterly) | Art. 25 insiders and >10% holders (monthly) | Proxy, annual |
| Manager-side portfolios | none | none | none | none | Form 13F (quarterly, 45-day lag) |
| Insider trades, post | 임원·주요주주 소유상황보고서 (5 days) | via 大量保有 amendments; director disclosures | 股东增减持 | 內部人持股轉讓 (monthly table) | Forms 3/4/5 (Form 4: 2 business days, XML) |
| Insider trades, ex ante | 거래계획보고 (≥1% or ₩5bn; ~30 days before) | none | 减持预披露 (15 trading days before) | 事前申報 (3 days before) | none (10b5-1 plan adoption disclosed in periodic reports) |
| Short positions | ≥0.5% named | ≥0.5% named | none | aggregate lending, daily | aggregate only |
| Daily flows by investor type, per stock | yes (KRX) | weekly aggregate only | northbound (Stock Connect) | yes (TWSE / TPEx) | none |
| Share pledge | 담보제공 in large-holder report | not standardized | 股权质押/冻结 (discrete events) | Art. 25 monthly pledge table | proxy footnotes |
| Control change | 최대주주변경 | 親会社・主要株主の異動 (TDnet) | 控制权变更 | 董事長／總經理變動 | 8-K 5.01 |
| Management change | 대표이사변경 | 代表取締役の異動 (TDnet) | 董监高变动 | 經理人異動 | 8-K 5.02 |
| Related party / group | KFTC 대규모내부거래·기업집단 공시 (ex ante) | none | 关联交易 | 關係人交易 | 10-K Item 13 / DEF 14A |
| Cross-shareholdings | none | 政策保有株式 by name with reason (有報) | none | none | none |

### 8.4 Investment, operations and restructuring

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| CAPEX / new capacity | 신규시설투자 | 固定資産の取得 when criteria met (TDnet) | 重大投资 | 重大訊息 (asset acquisition tests) | none (MD&A narrative) |
| Asset acquisition / disposal | 유형자산·타법인주식 취득·처분 | 固定資産の譲渡 | 重大资产重组 / 出售 | 取得或處分資產 | 8-K 2.01 (completion, significance test); 2.06 impairment |
| Major contract | 단일판매·공급계약체결 (KOSPI 5% / 2.5%; KOSDAQ 10%; counterparty may be deferred) | no dedicated category; other TDnet categories and residual obligation | 重大合同 | Important contracts within enumerated material-information rules | 8-K 1.01 (material definitive agreement outside ordinary course) |
| M&A / spin-off | 합병·분할 | 合併・会社分割 (TDnet) | 重大资产重组 | 合併・分割 | 8-K 1.01; S-4; DEFM14A |
| Business / capital alliance | none | 業務提携・資本提携 (TDnet) | 战略合作 | 策略聯盟 | none unless material agreement |
| Production halt | 생산중단 | 操業停止 | 停产 | 停工 (enumerated) | none (8-K 8.01 voluntary) |
| Technology transfer | 기술도입·이전 | none | 技术转让 | 技術授權 | none |
| Rumor / price-move response | 조회공시 (exchange-demanded, ~1 day) | 報道に関するお知らせ (voluntary) | 股价异动公告 (mandatory at ~20% over 3 days) | 澄清媒體報導 (exchange-demanded) | none |

### 8.5 Risk, distress and regulator interaction

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Litigation | 소송등의 제기 | 訴訟の提起 (TDnet) | 重大诉讼/仲裁 | 重大訴訟 | 10-K Item 3 / 10-Q Part II; 8-K 8.01 voluntary |
| Regulatory action | 행정처분 | 行政処分 | 行政处罚 | 主管機關處分 | 8-K 8.01 / 10-K |
| Audit opinion | 감사보고서 | 監査報告書 | 审计意见 | 會計師查核意見 | 10-K; 8-K 4.01 auditor change |
| Restatement / non-reliance | 정정공시 | 訂正報告書 | 更正公告 | 重編 | 8-K 4.02 |
| Insolvency / risk status | 회생절차·부도 | 民事再生・会社更生 | 破产重整; ST / *ST ticker flag | 重整・破產 | 8-K 1.03; 3.01 |
| Regulator ↔ company correspondence | none as a public corpus | none as a public corpus | 问询函 / 关注函 + replies, public, immediate | none as a public corpus | SEC comment letters (UPLOAD / CORRESP), public, delayed |
| Disclosure-quality penalty | 불성실공시법인 지정 (public, points) | none | 监管函 / 公开谴责 | fines | none |

---

## 9. Earnings: five clocks, five deliverables

| Step | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Early warning | 30% / 15% change filing at annual close | Forecast revision when criteria met | 业绩预告 on loss, turnaround or large change; annual by Jan 31 | Monthly revenue by the 10th | none |
| Preliminary | 잠정실적 (voluntary; large caps ~1 to 2 weeks after quarter; often sales and OP only) | none | 业绩快报 (optional; common on STAR / ChiNext) | 自結損益 (voluntary monthly) | none |
| Formal release | 분기보고서 / 사업보고서 | 決算短信 within 45 days (TSE asks for 30): statements + forecast, XBRL, fixed release time | 定期报告 by Apr 30 / Aug 31 / Oct 31 | 財報 within 45 days | Press release + 8-K 2.02 (furnished) |
| Statutory report | 사업보고서 90 days; 분기·반기 45 days | 有価証券報告書 3 months; Q1/Q3 not statutory | 年报 by Apr 30 (Q1 also by Apr 30) | 年報 by Mar 31 | 10-K 60 to 90 days; 10-Q 40 to 45 days |
| Investor briefing | Calls for large caps; IR 개최 notice on KIND; deck on company site | 決算説明会; deck on TDnet as 補足資料 | 业绩说明会 open to all; record posted | 法說會: slides and audio on MOPS (mandatory) | Call; transcript not filed; slides sometimes 8-K 7.01 |
| Who management met | none | none | 投资者关系活动记录表: fund names + Q&A within 2 days (Shenzhen mandatory) | none | none |

Where the IR deck lives: TDnet (Japan) and MOPS (Taiwan) are regulatory sources; Korea, China and the US require company-site collection. China compensates with meeting records and the retail Q&A stream; Korea with preliminary prints and daily flows.

---

## 10. Data access and machine-readability matrix

| Dimension | Korea | Japan | China | Taiwan | US |
|---|---|---|---|---|---|
| Central public discovery | Very strong | Split EDINET / TDnet | Fragmented | Very strong | Very strong |
| Public developer API | Strong OpenDART | Strong EDINET; TDnet full API paid | No single cross-exchange analogue | Strong TWSE / TPEx APIs | Strong free SEC APIs |
| XBRL / iXBRL | Strong | Strong | Meaningful but fragmented by source | Strong; iXBRL since Q1 2019 | Strong |
| Ownership structured | Strong (three regimes) | Strong large-holder | Strong but venue-complex | Strong, dual 5% / 10% regimes | Very strong |
| High-frequency official fundamentals | Moderate (preliminary prints, 30% rule) | Guidance revisions | Preannouncements, flash data | Monthly operating status | Limited |
| Timely operational event taxonomy | Very rich | Very rich TDnet | Very rich exchange ecosystem | Very rich material-information regime | Principles / form-item based |
| Free deep history | Good | EDINET good; TDnet public view 31 days | Fragmented | Good for many APIs | Excellent |
| Commercial institutional feed | Market vendors | Strong JPX paid products | Exchange-vendor ecosystem | MOPS push / vendors | Many vendors; raw SEC free |

Analytical scorecard (not official ratings):

| Dimension | KR | JP | CN | TW | US |
|---|---:|---:|---:|---:|---:|
| Central discovery | 5 | 3 | 2 | 5 | 5 |
| Public API convenience | 5 | 4 statutory / 2 timely | 2 to 3 | 5 | 5 |
| XBRL maturity | 5 | 5 | 4 | 5 | 5 |
| Operational event richness | 5 | 5 | 5 | 5 | 3 |
| Manager / insider holdings richness | 4 | 4 | 4 | 4 | 5 |
| High-frequency official fundamentals | 3 | 4 | 4 | 5 | 2 |
| Regulatory inquiry text | 3 | 3 | 5 | 3 | 5 |
| Easy point-in-time reconstruction | 4 | 4 | 2 to 3 | 4 | 5 |
| Prototype MCP suitability | 5 | 4 | 2 to 3 | 5 | 5 |

---

## 11. The ontology must encode obligation type, not only event type

For every event, store:

```text
event_type
event_subtype

obligation_type:
    MANDATORY_NUMERIC_TRIGGER
    MANDATORY_ENUMERATED_EVENT
    MANDATORY_MATERIALITY
    PERIODIC
    VOLUNTARY
    CORRECTIVE
    REGULATORY_RESPONSE

trigger_rule_id
trigger_metric
trigger_threshold
trigger_denominator
trigger_operator

source_authority
source_system
source_document_type
```

These are economically different even though all map to `MAJOR_CONTRACT`:

```text
Korea contract disclosed because the 10% KOSDAQ threshold was crossed
Taiwan contract disclosed because a material-information test was triggered
Japan company voluntarily announces a commercial alliance
US company files 8-K 1.01 because the agreement is material and outside the ordinary course
```

The selection mechanism affects signal bias.

---

## 12. Disclosure selection bias is a first-class research problem

Cross-country filing counts are not comparable. If Korea produces 500 major-contract announcements and Japan 80, that does not mean Korean companies sign more contracts. It may mean Korea has a dedicated numeric rule, Japan's is category-dependent, company size changes disclosure probability, and confidentiality rules differ. Model `P(disclosed | event, issuer, market, size, rule)`. The observed event dataset is a selected sample, and this matters most in supply-chain matching.

---

## 13. The supply-chain question: why the same contract appears on one side only

A single relationship (Korean supplier → Japanese equipment maker → Taiwanese foundry) can produce a mandatory Korea supply-contract filing, no dedicated Japan filing, a Taiwan material-information filing only if the rule is triggered, and a US filing only if a material definitive agreement falls within 8-K requirements. Therefore `no matching filing != no contract`.

Correct workflow:

1. Observe the source-side disclosed event.
2. Resolve the counterparty legal entity.
3. Map the counterparty to a listed parent and security.
4. Determine the counterparty's jurisdiction and rule set.
5. Calculate whether the event could plausibly trigger disclosure there.
6. Search the relevant filing categories.
7. Distinguish `NO_FILING_EXPECTED` from `FILING_EXPECTED_NOT_FOUND`.
8. Monitor later corrections, delayed disclosure and periodic-report mentions.

Once the event layer is shared, the cross-counterparty disclosure lag itself becomes a signal.

---

## 14. Point-in-time architecture: four clocks are necessary, six are better

Core clocks: `event_time`, `reporting_period_end`, `published_at`, `first_seen_at`.

Add `effective_at` (when the decision or legal effect becomes effective; a buyback approved today whose window opens next week) and `source_modified_at` (when the source system last changed the document or metadata; distinguishes an economic correction from a technical re-upload or metadata repair).

EDGAR illustrates the subtlety: filings accepted after 5:30 p.m. Eastern generally carry the next business day's filing date, with submission-type exceptions. Store acceptance timestamp and filing date separately; do not code a blanket rule.

---

## 15. Never overwrite corrections

Use an append-only document store:

```text
document_id
source_document_id
source_system
issuer_entity_id
filing_type_native
filing_type_normalized

published_at
first_seen_at
source_modified_at

is_amendment
amends_document_id
amendment_sequence
amendment_reason

raw_object_uri
raw_sha256
parser_version
```

A correction can change the amount, the counterparty, the contract end date, replace an attachment, disclose a previously deferred field, or fix a typo with no economic impact. So also store `amendment_materiality: TECHNICAL | TEXT_ONLY | ECONOMIC_VALUE_CHANGE | COUNTERPARTY_CHANGE | TIMING_CHANGE | SCOPE_CHANGE`. EDGAR's accession-number-plus-`/A` convention is a useful reference design; the Asian sources need the equivalent built on top.

---

## 16. Entity resolution is harder than filing retrieval

Link issuer, security, listed parent, subsidiary, counterparty, business group and ultimate parent. Recommended keys:

```text
entity_id
legal_name_local
legal_name_en
former_names
country
incorporation_country
ultimate_parent_entity_id

KR corp_code
JP EDINET code
JP security code
CN exchange + stock code
TW market + stock code
US CIK
ISIN
LEI where available
```

For supply-chain matching, preserve the raw counterparty text after resolution: `counterparty_text_raw`, `counterparty_entity_id`, `resolution_method`, `resolution_confidence`, `resolution_asof`.

---

## 17. Financial-statement normalization: XBRL does not solve comparability

All five systems use structured reporting; "XBRL available" is not "the numbers are comparable". You still need concept mapping (`local_concept → canonical_concept`: `REVENUE`, `OPERATING_PROFIT`, `NET_INCOME_ATTRIBUTABLE_TO_PARENT`, `CAPEX`, `CASH`, `TOTAL_DEBT`), dimensional normalization (segments, continuing versus discontinued, consolidated versus separate), a fiscal calendar (`period_start`, `period_end`, `fiscal_year_label_native`, `fiscal_quarter_native`, `calendar_year`, `calendar_quarter_overlap`; a March-year-end Japanese FY2026 is not a calendar-year Taiwanese FY2026), and restatement vintage (`value`, `reported_at`, `document_id`, `version`; never keep only "latest revenue for FY2024"). Taxonomies differ: Korea and Taiwan tag against IFRS-based local taxonomies, Japan against its own, the US against US GAAP; "operating income" is not guaranteed to be the same concept.

---

## 18. Research signals that become possible after normalization

**Korea supply-contract surprise.** `contract_value / prior_year_sales`, `contract_value / market_cap`, `contract_duration`, `counterparty_repeat_flag`, `counterparty_country`, `disclosure_deferral_flag`, `amendment_count`, `cancellation_flag`. Question: does the market under-react when a contract is large relative to the supplier's sales but small relative to the customer's procurement base?

**Korea insider trade plans.** Planned amount over ADV and over holdings, cancellation rate, execution versus plan, returns around plan announcement and execution window.

**Japan guidance-revision momentum.** `sales_guidance_revision`, `op_profit_guidance_revision`, `net_income_guidance_revision`, `sign_flip`, `threshold_crossing`, `days_to_fy_end`, `revision_sequence`. Better than "upward versus downward".

**Japan cross-shareholding unwind.** Change in named strategic holdings after the TSE capital-cost list; who is on the other side.

**China preannouncement quality.** `preannouncement_midpoint`, `actual_result`, `forecast_error`, `range_width`, `revision_count`, `days_before_actual`, crossed with exchange inquiry, audit opinion, regulatory penalty and controlling-shareholder pledge.

**China management attention.** Institutional visit count and attendee mix from 投资者关系活动记录表 ahead of flash reports; Q&A platform volume and tone.

**Taiwan monthly revenue nowcast.** QTD revenue, seasonality-adjusted YoY, 3M acceleration, supplier and customer weighted composite, consensus-implied remaining month. Official monthly revenue serves as both predictive signal and truth set for evaluating alternative-data nowcasts.

**Buyback authorization-to-execution ratio, all markets.** `authorized_amount`, `executed_amount`, `executed_pct`, `time_to_first_purchase`, `time_to_completion`, `cancelled_amount`, `retired_shares`, `treasury_shares_resold`. Separates symbolic buybacks from real capital return.

**Ownership plus pledge stress (CN / TW primarily).** `controller_ownership`, `pledged_pct_of_controller_holdings`, `pledged_pct_of_company`, `price_drawdown`, `margin_call_proxy`, `new_pledge_velocity`.

**Inquiry-letter risk (CN and US).** `inquiry_topic`, `accounting_topic`, `M&A_topic`, `governance_topic`, `response_days`, `number_of_rounds`, `subsequent_amendment`, `subsequent_restated_financials`.

**Positioning (KR / JP / TW).** Named short-position changes; daily foreign and institutional flows versus event dates; Korea's 조회공시 and China's 股价异动公告 as event markers.

---

## 19. MCP design: expose semantic research tools, not source APIs

A cross-market service should route internally (KR → OpenDART / KIND; JP → EDINET + TDnet; CN → SSE / SZSE / BSE / CNINFO; TW → MOPS / TWSE / TPEx; US → EDGAR) and expose:

```text
resolve_entity()
search_disclosures()
get_disclosure()
get_document_text()
get_xbrl_facts()

get_financials()
get_earnings()
get_guidance_changes()
get_monthly_operating_data()

get_buybacks()
get_dividends()
get_issuance()

get_large_holders()
get_insider_activity()          # both ex-ante plans and post-trade reports
get_share_pledges()
get_short_positions()
get_flows()
get_control_changes()

get_major_contracts()
get_capex()
get_asset_transactions()
get_mna()

get_audit_events()
get_litigation()
get_regulatory_actions()
get_exchange_inquiries()
get_meeting_records()
get_distress_events()

get_disclosure_timeline()
```

Example routing: `get_guidance_changes(Toyota)` → JP → TDnet; `get_large_holders(Toyota)` → JP → EDINET; `get_buybacks(Toyota)` → JP → TDnet authorization + EDINET monthly status; `get_monthly_operating_data(TSMC)` → TW → TWSE / MOPS; `get_exchange_inquiries(Chinese issuer)` → CN → exchange inquiry pages; `get_major_contracts(KOSDAQ supplier)` → KR → KRX / DART event taxonomy with the 10% rule attached. The user should not need to know the topology. The Korean DART MCP project (github.com/chrisryugj/korean-dart-mcp) is a useful reference for compressing raw endpoints into a small analyst-friendly tool surface; the cross-market version adds jurisdiction-aware routing and rule-version-aware normalization.

---

## 20. Canonical schema

**`source_registry`:** `source_id`, `country`, `authority`, `source_system`, `source_role`, `official_flag`, `access_method`, `api_type`, `xbrl_flag`, `history_depth`, `license`, `redistribution_rights`, `latency_profile`, `timezone`, `language`.

**`entity_master`:** `entity_id`, `legal_name_local`, `legal_name_en`, `country`, `exchange`, `ticker`, `security_code`, `isin`, `lei`, `native_regulator_id`, `parent_entity_id`, `valid_from`, `valid_to`.

**`document`:** `document_id`, `source_id`, `native_document_id`, `entity_id`, `native_document_type`, `published_at`, `first_seen_at`, `source_modified_at`, `language`, `raw_uri`, `raw_hash`, `is_amendment`, `amends_document_id`.

**`event`:** `event_id`, `entity_id`, `event_type`, `event_subtype`, `obligation_type`, `trigger_rule_id`, `event_time`, `effective_at`, `currency`, `amount`, `shares`, `ownership_pct`, `counterparty_entity_id`, `counterparty_text_raw`, `confidence`.

**`event_document_bridge`:** `event_id`, `document_id`, `document_role` (`INITIAL_ANNOUNCEMENT`, `STATUTORY_FILING`, `CORRECTION`, `PROGRESS_UPDATE`, `REGULATORY_RESPONSE`, `COMPLETION`).

**`fact`:** `entity_id`, `concept_id`, `value`, `unit`, `period_start`, `period_end`, `instant_date`, `dimensions`, `document_id`, `reported_at`, `version`.

---

## 21. Rule registry: the table most disclosure projects forget

```text
rule_id
country
market
authority
rule_name
rule_article
effective_from
effective_to

event_type
trigger_type
threshold_value
threshold_unit
denominator
deadline_rule
exceptions
source_url
```

Examples:

```text
KR_KOSPI_MAJOR_CONTRACT_2026
  event_type = MAJOR_CONTRACT; trigger_type = SALES_PERCENT
  threshold = 5%; large_corp_threshold = 2.5%

KR_KOSDAQ_MAJOR_CONTRACT_2026
  threshold = 10%

KR_INSIDER_TRADE_PLAN
  event_type = INSIDER_TRADE_PLAN; trigger = >=1% of securities OR >= KRW 5bn
  deadline_rule = ~30 days before trading period

JP_FORECAST_REVISION
  event_type = GUIDANCE_REVISION; trigger = sales +/-10% OR profit items +/-30%

JP_QUARTERLY_REGIME
  effective_from = 2024-04-01 (statutory Q1/Q3 abolished)

CN_CSRC_DISCLOSURE_MEASURES_226
  effective_from = 2025-07-01

TW_LARGE_HOLDER_2024
  event_type = LARGE_HOLDER_CROSSING; threshold = >5%; effective_from = 2024-05-10
  supersedes TW_LARGE_HOLDER_10PCT

US_FORM_10S
  rule_status = PROPOSED (2026-05-05)

US_DAILY_BUYBACK_DISCLOSURE
  rule_status = VACATED (2023-12-19)
```

This is how a 2026 rule is kept from contaminating a 2018 backtest.

---

## 22. Research-quality controls

| Control | Measure |
|---|---|
| Coverage | expected filings found / expected filings, by market and event type |
| Timeliness | `first_seen_at - published_at` |
| Parsing accuracy | golden set by event type |
| Entity-resolution precision | particularly counterparties |
| Amendment recall | every amendment linked to its original |
| Point-in-time correctness | no query as of date `t` can see a later document or version |
| Source redundancy | exchange copy and portal copy match |
| Rule-version integrity | every event carries the rule version in force on its published date |

---

## 23. Build order

1. **Korea:** define the ontology on the richest familiar event set, including the three ownership regimes and the KFTC layer.
2. **Taiwan:** test cross-market normalization on the OpenAPIs, monthly revenue, material-information events and the dual 5% / 10% holder regimes.
3. **US EDGAR:** validate that the ontology is not Asia-only; add ownership, comment-letter and rule-status concepts.
4. **Japan EDINET:** statutory, XBRL, large-holder, tender-offer, buyback-status and cross-shareholding layer.
5. **Japan TDnet:** timely earnings, guidance, dividend, buyback-authorization and corporate-action layer; decide early between the public 31-day view and the paid historical API.
6. **China:** add SSE, SZSE, BSE and CNINFO adapters after the common schema is stable, and treat inquiry letters, meeting records and Q&A platforms as a separate text pipeline.

China last is not about low value. It is rich enough to force source-specific complexity into the schema before the abstraction has matured.

---

## 24. Takeaway

The five markets optimize public disclosure around different objects. The US is exceptionally strong in standardized ownership, filing-review correspondence and public-data infrastructure. Korea and Taiwan expose positioning, flows and threshold-driven operational events. Japan exposes guidance, cross-holdings and monthly buyback execution. China exposes early earnings warnings, pledges, exchange inquiries and who management is talking to. The research edge comes from knowing which regime selects which events into the public record.

**Normalize the event. Preserve the source. Version the rule. Never overwrite history.**

---

## 25. Primary official sources

### Korea
- OpenDART disclosure search API and A to J taxonomy: https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DE001&apiId=AE00001
- DART large-shareholding guide: https://dart.fss.or.kr/info/main.do?menu=310
- DART officer / major-shareholder ownership guide: https://dart.fss.or.kr/info/main.do?menu=320
- DART ex-ante trade-plan reporting guide: https://dart.fss.or.kr/info/main.do?menu=340
- KRX KOSPI disclosure and listing handbook: https://kind.krx.co.kr/external/dst/reference/11635/
- KFTC large business-group disclosure overview: https://www.ftc.go.kr/eng/contents.do?key=786

### Japan
- FSA quarterly-report reform: https://www.fsa.go.jp/en/newsletter/weekly2024/581.html
- JPX forecast-revision disclosure FAQ: https://faq.jpx.co.jp/disclo/tse/web/knowledge6851.html
- JPX TDnet overview: https://www.jpx.co.jp/equities/listing/disclosure/tdnet/
- JPX TDnet API: https://www.jpx.co.jp/markets/paid-info-listing/tdnet/02.html
- FSA large-shareholding overview: https://www.fsa.go.jp/common/shinsei/tairyohoyu/summary/index.html
- EDINET API v2 specification: https://disclosure2dl.edinet-fsa.go.jp/guide/static/disclosure/download/ESE140206.pdf
- FSA EDINET taxonomy: https://www.fsa.go.jp/search/EDINET_Taxonomy_All.html
- 2027 EDINET taxonomy draft: https://www.fsa.go.jp/search/20260911.html

### Mainland China
- CSRC Order No. 226, Listed Company Information Disclosure Measures: https://www.csrc.gov.cn/csrc/c101953/c7547359/content.shtml
- SSE Stock Listing Rules, April 2026: https://www.sse.com.cn/lawandrules/sselawsrules2025/stocks/mainipo/c/c_20260424_10816589.shtml
- SSE regulatory inquiries: https://www.sse.com.cn/disclosure/credibility/supervision/inquiries/
- SSE regulatory measures: https://www.sse.com.cn/disclosure/credibility/supervision/measures/
- CNINFO: https://www.cninfo.com.cn/ and data services https://webapi.cninfo.com.cn/

### Taiwan
- Securities and Exchange Act, Article 36: https://law.fsc.gov.tw/EngLawContent.aspx?id=1331&lan=E
- Article 43-1 substantial-shareholding regulation: https://law.fsc.gov.tw/EngLawContent.aspx?id=2705
- TWSE explanation of the 5% threshold effective May 2024: https://twmonthly.twse.com.tw/front/content/8a81b9818f0ee6b4018f19c31cef0006?date=May+2024
- Article 25 insider / >10% holder regime: https://law.fsc.gov.tw/EngLawContent.aspx?id=2116&lan=E
- TWSE material-information rules: https://twse-regulation.twse.com.tw/m/en/LawContent.aspx?FID=FL007111
- TWSE OpenAPI: https://openapi.twse.com.tw/ and TPEx OpenAPI: https://www.tpex.org.tw/openapi/
- TWSE XBRL / iXBRL history: https://www.twse.com.tw/en/listed/xbrl.html

### United States
- SEC EDGAR APIs: https://www.sec.gov/search-filings/edgar-application-programming-interfaces
- SEC Form 13F FAQ: https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f
- SEC filing-review correspondence search: https://www.sec.gov/search-filings/edgar-search-assistance/how-search-edgar-correspondence
- SEC share-repurchase rule vacatur and technical amendments: https://www.sec.gov/rules-regulations/2024/03/s7-21-21
- SEC semiannual Form 10-S proposal: https://www.sec.gov/rules-regulations/2026/05/s7-2026-15
- SEC EDGAR filing-date guidance: https://www.sec.gov/submit-filings/filer-support-resources/how-do-i-guides/determine-status-my-filing

### Reference implementation
- Korean DART MCP: https://github.com/chrisryugj/korean-dart-mcp
