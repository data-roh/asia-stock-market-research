# Asia Stock Review

## A Taxonomy of Asian Disclosure Systems

### How Korea, Japan, China and Taiwan disclose, and how the US compares

*Korea has one system for everything. Japan has two. China has three layers. Taiwan has the best public data. And the US, the market everyone treats as the standard, actually requires companies to disclose the least about what they are doing.*

> *Claude Opus 5 and Claude Fable 5.1 (Anthropic) assisted with research, tables and editing under the author's direction; all judgments and errors are the author's own.*

---

This started with two simple questions.

First: a Korean chip-materials company files a supply contract on DART. The customers are a Japanese equipment maker and a Taiwanese foundry. Do those two companies have to disclose the same contract? If so, where, under what name, and how many days later? I knew where to look in Korea. I had no idea where to look in Tokyo or Taipei.

Second: I wanted to compare the official financial statements of a dozen semiconductor companies across the four markets: same line items, same periods, straight from the filings. Every market says it has structured financial data. None of them delivers it the same way.

The answer to both is the same. The economic event is identical everywhere. The disclosure system (who requires the filing, where it is published, what it is called, when it is stamped) is different in every market. You cannot ask the question until you understand the system.

So I mapped the four Asian systems into one framework, added US EDGAR for comparison, and wrote down where the edge is. This is for people who want to build the pipeline, not just read the filings.

> ⚠️ Personal research, unrelated to my day job. Not investment advice. All classifications and errors are mine.

---

## The Short Version: What Each Market Requires That the Others Don't

Before the full map, here is the part that surprised me most. Every market has a handful of disclosure rules that exist nowhere else, and most of them are the kind of thing an event-driven desk would build a signal around if it knew they existed.

### 🇰🇷 Korea

- **Inquiry disclosure (조회공시).** When a stock moves sharply or a rumor circulates, the exchange can demand a public answer within about a day. The company's "confirmed / denied / undecided" reply is itself a filing.
- **Supply contracts with a hard threshold.** Contracts above a fixed share of prior-year revenue (5% on KOSPI, 2.5% for large corporations, 10% on KOSDAQ) must be disclosed with counterparty, value and term. The counterparty can be redacted at its own request ("a European automaker"), and the redaction is itself visible. The redaction pattern is a signal.
- **Profit-shock filing.** When annual sales or profit changes by 30% or more versus the prior year (15% for large companies), a dedicated filing is required when the books close, before the annual report. Korea's version of China's preannouncement, but after the fact.
- **Insiders file a trade plan 30 days ahead.** Officers and major shareholders planning a trade of 1% or more of the shares, or KRW 5 billion or more, must report the plan about 30 days before the trading window opens. Korea has both an ex-ante plan report and the usual post-trade report.
- **Short sellers named in public.** Net short positions of 0.5% or more are disclosed with the holder's name. Japan has the same rule. The US publishes only aggregates.
- **Related-party deals disclosed before they happen.** Large intra-group transactions in chaebol need a board resolution and a Fair Trade Commission filing *before* execution.
- **Daily flows per stock.** The exchange publishes foreign / institutional / retail net buying for every stock every day. Taiwan does the same; Japan only gives weekly aggregates; the US nothing.
- **Employee data by gender.** Annual reports include headcount, average tenure and average salary, split by gender and division.
- **Public shaming list.** The exchange designates "unfaithful disclosure companies" (불성실공시법인) with penalty points that accumulate toward trading halts.

### 🇯🇵 Japan

- **Guidance revisions are mandatory above hard thresholds.** Publishing a full-year forecast is not a legal requirement, but the exchange's earnings-report format includes one and nearly every company provides it. Once published it is binding: if the forecast moves by roughly 10% on sales or 30% on profit, the company must file a tagged revision the same day. No other market forces guidance changes into a structured filing.
- **Cross-shareholdings listed by name.** The annual securities report lists the company's strategic holdings in other listed firms: top holdings, with the stated reason for owning each one. The entire cross-shareholding unwind trade lives in this table.
- **The exchange keeps a public list of who has a capital-efficiency plan.** Under TSE's cost-of-capital initiative, companies disclose an action plan on capital cost and share price, and the exchange publishes which companies have and haven't. A regulator-run pressure list.
- **Monthly buyback status reports.** Execution is reported every month through a statutory EDINET filing (自己株券買付状況報告書), with TDnet progress and completion notices on top. Not once a quarter.
- **The IR deck is a filing.** Earnings-briefing materials are posted to TDnet as supplementary documents alongside the earnings report.
- **Institutions get a slower large-holder clock.** Ordinary 5% holders file within 5 business days; qualifying institutions use a batched "special report" with a lag of up to several weeks. Activist accumulation shows up faster than passive accumulation.
- **Human-capital data.** Average salary, average age, average tenure, and since FY2023 the gender pay gap, female-manager ratio and male parental-leave rate, all in the annual report.

### 🇨🇳 China

- **Three earnings clocks.** A mandatory preannouncement when net profit is expected to swing 50% or more, or flip sign (annual by January 31); an optional flash report; then the formal periodic report. No other market has a mandatory early warning with a numeric trigger.
- **Institutional meeting records with attendee names.** After meeting investors (site visits, calls, roadshows), Shenzhen-listed companies must post a record within two trading days, including the names of the funds that attended and the Q&A. Shanghai encourages the same. Your competitors' diligence trail is public.
- **Retail Q&A platforms run by the exchange.** On 互动易 (Shenzhen) and 上证e互动 (Shanghai), any investor can ask a question and management answers in writing. Timestamped, searchable, and a large, free NLP corpus.
- **Insiders pre-announce sales.** Controlling shareholders and directors must publish a selling plan (size, price range, window) 15 trading days before selling. An ex-ante Form 4.
- **Abnormal-move announcements.** A cumulative move of about 20% in three days forces a company statement on whether there is undisclosed information.
- **Exchange inquiry letters are public.** Comment and concern letters (问询函, 关注函) and the company's replies are posted immediately, often around deals and annual reports. Like SEC comment letters, but faster and more pointed.
- **Top-10 shareholders every quarter.** Including the top-10 holders of free-float shares, so fund names are visible four times a year.
- **Distress in the ticker.** Companies that fail financial tests get an ST or *ST prefix on the symbol and a 5% daily price limit. The disclosure is embedded in the ticker.

### 🇹🇼 Taiwan

- **Monthly revenue by the 10th of the following month.** Mandatory, for every listed company, through an official API.
- **Some companies also self-report monthly earnings.** Financial holding companies in particular publish voluntary monthly self-assessed profit (自結損益).
- **The earnings call is a filing.** For investor conferences (法說會), the slides *and the audio recording* must be posted on MOPS.
- **Mandatory press conferences.** For certain major events the company must hold a press conference at the exchange and file the explanation.
- **Two holder regimes, 5% and 10%.** Since May 2024 crossing 5% triggers a substantial-holder declaration within 10 days (lowered from 10%). Separately, directors, supervisors, officers and >10% holders report holdings and pledges monthly, and must pre-declare planned transfers three days before selling.
- **Daily per-stock flows and positioning.** Foreign, investment-trust and dealer net buying; margin and securities-lending balances; foreign ownership percentage, for every stock, every day.
- **Regulator-run governance scores.** An annual corporate-governance evaluation ranks every listed company into tiers, published.

### 🇺🇸 US

- **Manager-side portfolios.** Form 13F lists every US stock a large institution holds, quarterly. Asia discloses top holders from the company side; nobody discloses from the manager side.
- **Insider trades in two days, in XML.** Form 4.
- **A clean restatement flag.** 8-K Item 4.02, filed when prior financials can no longer be relied upon.
- **Regulator correspondence is public.** SEC comment letters and company responses.
- **Nothing is filed on earnings day.** The press release is "furnished," the call is not filed at all, and guidance is voluntary.

The pattern across all five: **Korea and Taiwan expose positioning and flows; Japan exposes guidance and cross-holdings; China exposes who management is talking to; the US exposes who owns the company.** Everything below is the detail behind that sentence.

---

## 1. Five Architectures for the Same Question

Every market has to answer the same investor questions: What did the company earn? Did guidance change? Did it buy back stock? Did a large holder add? Did it sign a major contract, build capacity, buy or sell an asset? Is there litigation, regulatory action or distress?

The information exists everywhere. The architecture does not.

| Market | Architecture | Primary sources | One-line summary |
|---|---|---|---|
| 🇰🇷 Korea | **Integrated hub** | DART / OpenDART (+ KRX exchange disclosure, FTC disclosure) | One ecosystem, one API, one taxonomy |
| 🇯🇵 Japan | **Deliberately split** | EDINET (statutory) + TDnet (exchange timely disclosure) | Two regimes; you need both |
| 🇨🇳 China | **Distributed** | CSRC (rules) → SSE / SZSE / BSE (exchange rules and publication) + CNINFO (cross-market portal) | No single "Chinese DART" |
| 🇹🇼 Taiwan | **Central platform + open APIs** | MOPS (central) + TWSE / TPEx OpenAPI | Easiest to turn into a database |
| 🇺🇸 US | **Single statutory system** | SEC EDGAR (+ NYSE / Nasdaq press-release rules) | One regulator, one archive, no separate exchange filing taxonomy |

### What those labels actually mean

The table uses a few terms that are worth spelling out, because the whole framework depends on them.

**Statutory disclosure vs. exchange (timely) disclosure.** Every market has two kinds of rules. *Statutory* disclosure is required by securities law and filed with the government regulator: the annual report, the securities registration statement, large-shareholder reports. It is legally prescribed and form-driven, and the annual report is audited. *Exchange* or *timely* disclosure is required by the stock exchange's listing rules and published through the exchange's own system: earnings releases, buyback announcements, a big contract, a CEO change. It is fast, event-driven, and designed to reach the market the same day. Most markets blend the two into one portal. Japan keeps them physically separate: **EDINET** is the regulator's (FSA's) statutory system, **TDnet** is the Tokyo Stock Exchange's timely-disclosure system. A Japanese company's audited annual report lives in EDINET; the buyback it announced yesterday lives in TDnet. Korea has the same legal split (statutory "major matter reports" go to the FSS, event disclosures go to KRX), but both are served through DART, which is why it feels like one system.

**"CSRC (rules) → exchanges → CNINFO (portal)."** In China the roles are split three ways. The **CSRC**, the China Securities Regulatory Commission and China's SEC, writes the regulations but is not where you go to read a filing. The **exchanges** (Shanghai, Shenzhen, Beijing) write the detailed listing rules that say *which* events must be disclosed and *when*, and they are the ones who actually enforce them. The exchanges also publish the announcements on their own sites. **CNINFO** (巨潮资讯) is the official cross-market portal, closely tied to the Shenzhen infrastructure, where announcements from all three exchanges can be searched in one place. So "who sets the rule," "who enforces and publishes it" and "where you search" are different institutions, the exchanges remain first-class sources rather than mirrors of the portal, and reading only the CSRC regulation gives you an incomplete picture of what companies actually file.

**"FTC disclosure" in Korea.** This is not a securities-law filing at all. Korea's **Fair Trade Commission** (공정거래위원회) requires companies that belong to designated large business groups, the chaebol, to disclose transactions *inside* the group: a subsidiary lending money to an affiliate, an affiliate buying shares or assets from another, large internal supply contracts, and the group's overall ownership structure. These filings exist because Korean regulators worry about controlling families moving value between affiliates. They are published through the same DART ecosystem, which is why they look like ordinary disclosures, but no other market in this piece requires anything comparable. For anyone analyzing a Korean holding company, a succession event or a related-party trade, they are the primary source.

**"No separate exchange filing taxonomy" in the US.** NYSE and Nasdaq do require companies to disclose material news promptly, but they enforce that through press releases and a phone call to the exchange, not through a structured filing system with its own event categories the way TSE does. In practice almost everything investable still flows into **EDGAR**, the SEC's archive, mostly through one form: the **8-K**, the US "current report" for events. The US is therefore the mirror image of Japan: Japan moved its event disclosure into a separate exchange system with a mandatory item list; the US kept it inside the regulator's system.

**First rule:** do not look for the "DART equivalent" or the "8-K equivalent" in each country. Understand the layers first.

---

## 2. The Disclosure Universe, Organized by Economic Event

Korea's OpenDART (DART's public API) is the best starting taxonomy because it already separates disclosure into clean top-level buckets: periodic reports (annual, semi-annual, quarterly), major-event reports, securities issuance, equity ownership, external audit, funds, asset-backed securities, exchange disclosure and Fair Trade Commission disclosure.

For investing, though, the useful unit is not the filing name. It is the **economic event**. Below is the cross-market map I ended up with, with EDGAR as the fifth column. Local names are illustrative pointers into each source taxonomy, not exhaustive lists. "None" means there is no standard mandatory category: the information may still appear inside a periodic report or a voluntary release, but nothing forces the company to file it as a discrete event.

### 2.1 Periodic and Earnings Disclosure

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Annual report | 사업보고서 (DART) | 有価証券報告書 (EDINET) | 年度报告 | 年報 (MOPS) | 10-K |
| Semi-annual / interim | 반기보고서 | 半期報告書 (EDINET) | 半年度报告 | 半年度財報 | 10-Q (Q2); *optional Form 10-S proposed in 2026* |
| Q1 / Q3 | 분기보고서 | 決算短信 (TDnet); *statutory quarterly report abolished April 2024* | 季度报告 (exchange rules) | 季報 | 10-Q |
| Preliminary / flash earnings | 영업(잠정)실적 공정공시 (voluntary) | 決算短信 | 业绩快报 (optional) | 自結損益 (voluntary, monthly) | 8-K Item 2.02 (earnings release, *furnished*, see below) |
| Earnings preannouncement / warning | 매출액·손익구조 30% 변동 (annual, ex post) | 業績予想の修正 (TDnet) | 业绩预告 (mandatory on loss, turnaround or large change; details vary by board) | none | none (voluntary via 8-K 2.02 / 7.01) |
| **Monthly revenue** | none | none | none | **每月營收 (TWSE / TPEx API)** | none |
| Guidance / forecast revision | 공정공시 (voluntary) | 業績予想の修正 (TDnet, XBRL, mandatory above threshold) | 业绩预告 | none | none (voluntary, Reg FD → 8-K 7.01) |

Japan is the only market where guidance is structured and its revision is mandatory. Publishing a full-year forecast is not itself a legal requirement, but the exchange's earnings-report format includes one and nearly every company provides it. Once published the forecast is binding: when it moves beyond the threshold, the company must file a tagged, machine-readable revision that same day. Taiwan is the only market with *mandatory monthly revenue*. China is the only market with a *mandatory early warning* before results, triggered by an expected loss, a turnaround, or a large swing (commonly ~50%), with the exact rule depending on exchange and board. And the US, despite its reputation for transparency, treats guidance as entirely voluntary and typically does not even "file" the earnings release; it is *furnished* under 8-K Item 2.02, a legal category with a lower liability standard than a filed document. (Reg FD, "Regulation Fair Disclosure," just says that if a US company tells anyone material information it must tell everyone; it does not oblige the company to say anything in the first place.)

### 2.2 Shareholder Return and Financing

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Buyback authorization | 자기주식취득 | 自己株式取得 (TDnet) | 股份回购 | 庫藏股 | none (press release / 8-K 8.01, voluntary) |
| Buyback execution | 자기주식취득결과보고서 | 自己株券買付状況報告書 (monthly, statutory, EDINET) + TDnet progress notices | 回购进展 | 庫藏股執行情形 | 10-Q / 10-K Item 703 table (quarterly, monthly detail) |
| Treasury share disposal / cancellation | 자기주식처분·소각 | 自己株式消却 | 回购股份注销 | 庫藏股註銷 | none |
| Dividend | 현금·현물배당결정 | 配当予想の修正 (TDnet, XBRL) | 利润分配 | 股利分派 | none (press release; exchange notice) |
| Equity issuance | 유상증자 | 有価証券届出書 (EDINET) / 新株発行 (TDnet) | 增发 / 配股 | 現金增資 | S-1 / S-3, 424B prospectus; 8-K 3.02 (unregistered) |
| Convertible / debt | 전환사채·신주인수권부사채 | 転換社債型新株予約権付社債 | 可转债 | 可轉換公司債 | 8-K 2.03 (direct financial obligation) |
| Capital reduction | 감자 | 減資 | 减资 | 減資 | none |
| Tender offer | 공개매수 | 公開買付届出書 / 意見表明報告書 (EDINET) | 要约收购 | 公開收購 | Schedule TO / SC 14D-9 |

The buyback row is the most instructive. In all four Asian markets the *authorization* is an event filing and the *execution* is reported on a fixed cadence; in Japan's case a monthly statutory status report on EDINET, plus progress notices on TDnet. In the US, the authorization is a press release and the execution shows up as a table inside the next quarterly report, weeks after the fact. The SEC's 2023 rule requiring daily repurchase data was struck down in court before it took effect. On buybacks, Asia's data is simply better.

### 2.3 Ownership, Positioning and Control

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Large holder report (threshold) | 주식등의 대량보유상황보고서 (5%) | 大量保有報告書 (5%, EDINET; institutions on batched schedule) | 权益变动报告书 (5%) | 大量持股申報 (>5%, Art. 43-1, since May 2024; within 10 days) | Schedule 13D / 13G (5%; 13D within 5 business days) |
| Top holders, company-side | 사업보고서 5%+ 주주 | 有報 大株主 top 10 (semi-annual) | **前十大股东 + 前十大流通股东 (quarterly)** | Directors, officers and >10% holders (Art. 25, monthly) | Proxy (DEF 14A), annual |
| **Manager-side portfolios** | none | none | none | none | **Form 13F (quarterly, 45-day lag)** |
| Insider / major holder trades | 임원·주요주주 소유상황보고서 (5 days after) + **거래계획보고 (30 days before, ≥1% or ₩5bn)** | none (via 大量保有 amendments) | 股东增减持 + **减持预披露 (15 days before)** | 內部人持股轉讓 + **事前申報 (3 days before)** | Forms 3 / 4 / 5 (Form 4 within 2 business days, XML) |
| **Short positions** | **공매도 잔고 ≥0.5%, holder named** | **空売り残高 ≥0.5%, holder named** | none | Aggregate securities lending, daily | Aggregate only |
| **Daily flows by investor type, per stock** | **Yes (KRX)** | Weekly aggregate only | Northbound flow (Stock Connect) | **Yes (TWSE/TPEx)** | none |
| **Share pledge** | 담보제공 (in large holder report) | none | **股权质押** | 內部人設質 (monthly table) | none (proxy footnotes only) |
| Control change | 최대주주변경 | 親会社・主要株主の異動 (TDnet) | 控制权变更 | 董事長／總經理變動 | 8-K 5.01 |
| Management change | 대표이사변경 | 代表取締役の異動 (TDnet) | 董监高变动 | 經理人異動 | 8-K 5.02 |
| Related-party / group | **FTC 대규모내부거래·기업집단 공시 (ex ante)** | none | 关联交易 | 關係人交易 | 10-K Item 13 / DEF 14A proxy |
| **Cross-shareholdings** | none | **政策保有株式 (by name, with reason, in 有報)** | none | none | none |

Ownership is where the two philosophies diverge most clearly. The US discloses from the *manager's* side: **Form 13F**, a quarterly list of every US stock a large institution holds, has no comparable manager-by-manager regime in any of the four Asian markets. Asia discloses from the *company's* side: China publishes the top-10 holders (including top-10 float holders) every quarter, Japan every half-year, Korea the 5% holders, Taiwan the >5% substantial holders (lowered from 10% in May 2024) plus a separate monthly table of directors, officers and >10% holders. You can see which funds own a Chinese stock; you cannot see a Chinese fund's whole book.

Asia also discloses things the US does not touch. **Short positions of 0.5% or more are published with the holder's name** in Korea and Japan. **Daily net buying by foreigners, institutions and retail, per stock**, is published every evening in Korea and Taiwan. **Share pledges** (a controlling shareholder using stock as loan collateral) are discrete events in China and a monthly table in Taiwan, which lets you link ownership to the controller's financing stress. And in Korea, China and Taiwan, **insiders must announce planned trades in advance**: about 30 days in Korea for trades of 1% or more or KRW 5 billion or more, 15 trading days in China, 3 days in Taiwan. That is the opposite of the US Form 4, which reports two days *after*.

**Form 4** remains the best-structured insider filing in the world: two business days, machine-readable XML, a code for each transaction type. But it is the only thing in this table where the US is clearly ahead.

### 2.4 Investment, Operations and Restructuring

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| CAPEX / new capacity | 신규시설투자 | 固定資産の取得 (TDnet) | 重大投资 | 重大訊息 (取得資產) | none (MD&A narrative only) |
| Asset acquisition / disposal | 유형자산·타법인주식 취득·처분 | 固定資産の譲渡 | 重大资产重组 / 出售 | 取得或處分資產 | 8-K 2.01 (on completion, above a size test); 2.06 impairment |
| **Major contract** | **단일판매·공급계약체결 (threshold; counterparty may be redacted)** | none (no standard category; via 業務提携) | 重大合同 | 重大訊息 | 8-K 1.01 (material definitive agreement) + Exhibit 10 |
| M&A / spin-off | 합병·분할 | 合併・会社分割 (TDnet) | 重大资产重组 | 合併・分割 | 8-K 1.01; S-4; DEFM14A |
| Business / capital alliance | none | 業務提携・資本提携 (TDnet) | 战略合作 | 策略聯盟 | none (8-K 1.01 only if a material agreement) |
| Production halt | 생산중단 | 操業停止 | 停产 | 停工 | none (8-K 8.01, voluntary) |
| Technology transfer / licensing | 기술도입·이전 | none | 技术转让 | 技術授權 | none |
| **Rumor / price-move response** | **조회공시 (exchange-demanded, ~1 day)** | 報道に関するお知らせ (voluntary) | **股价异动公告 (mandatory at ~20% / 3 days)** | **澄清媒體報導 (exchange-demanded)** | none |

This table answers the first question I started with, and it is the core of the Asia-versus-US argument.

Korea's supply-contract filing (단일판매·공급계약체결) is mandatory once a contract exceeds a fixed share of the prior year's revenue (5% on KOSPI, 2.5% for large corporations, 10% on KOSDAQ), and it names the counterparty, the value and the contract period. The Taiwanese foundry on the other side would file a material-information notice (重大訊息) on MOPS if the contract triggers TWSE's material-information procedures, which enumerate event types (important contracts among them) with quantitative tests and a residual materiality clause. For a large foundry one supplier contract usually falls below those tests, so no filing appears. The Japanese equipment maker most likely files nothing either: Japan has no dedicated "major contract" category like Korea's, only other TDnet categories (business alliance, fixed-asset acquisition) and a residual timely-disclosure obligation that a routine supply contract rarely meets. So the same contract can appear as a mandatory filing in Seoul, a rule-triggered but usually untriggered filing in Taipei, and no filing at all in Tokyo. That asymmetry is itself information, and it is the reason a missing filing must be classified as "no filing expected" rather than "not found."

The last row is a category that does not exist in the US at all. In Korea, China and Taiwan the exchange can *make* a company respond publicly to a rumor or an unexplained price move, on a deadline. A Korean 조회공시 answer of "미확정" ("under review") to a merger rumor is a tradeable event. A US company under the same circumstances issues nothing.

The US is closer to Japan than to Korea on contracts. 8-K Item 1.01 covers "material definitive agreements," but *material* is the company's own judgment, ordinary-course contracts are excluded, and there is no numeric threshold. CAPEX commitments and production halts have no US event filing at all; they appear, if at all, in the narrative management-discussion section of the next quarterly report.

### 2.5 Risk, Distress and Regulator Interaction

| Event | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Litigation | 소송등의 제기 | 訴訟の提起 (TDnet) | 重大诉讼 | 重大訴訟 | 10-K Item 3 / 10-Q Part II Item 1; 8-K 8.01 voluntary |
| Regulatory action / penalty | 행정처분 (기타 주요경영사항) | 行政処分 | 行政处罚 | 主管機關處分 | 8-K 8.01 / 10-K (voluntary as event) |
| Audit opinion / going concern | 감사보고서 (외부감사) | 監査報告書 | 审计意见 | 會計師查核意見 | 10-K; 8-K 4.01 auditor change |
| **Restatement / non-reliance** | 정정공시 | 訂正報告書 | 更正公告 | 重編 | **8-K 4.02 (non-reliance on prior financials)** |
| Insolvency / restructuring | 회생절차·부도 | 民事再生・会社更生 | 破产重整 / **ST·*ST ticker flag** | 重整・破產 | 8-K 1.03 (bankruptcy); 3.01 (delisting notice) |
| **Regulator ↔ company correspondence** | none | none | **问询函 / 关注函 + replies, public** | none | **SEC comment letters, public (delayed)** |
| **Disclosure-quality penalty** | **불성실공시법인 지정 (public, points)** | none | 监管函 / 公开谴责 | Fines | none |

The US is stronger on *financial-control* events (8-K 4.02, which a company must file when it concludes its previously published financial statements can no longer be relied upon, is a clean, machine-detectable restatement signal) and weaker on *operational* ones, where litigation and penalties are usually buried in periodic reports unless the company chooses to file an 8-K. China's exchange inquiry letters are the closest Asian analogue to SEC comment letters, and they arrive faster: a 关注函 about a suspicious deal is often posted within days, with the reply due within a week.

---

## 3. Earnings: Five Different Clocks, Five Different Deliverables

The earnings event is where the five systems look most alike on the surface and differ most underneath. "Earnings" in each market is not one document but a sequence, and what counts as a *filing* versus an *IR courtesy* changes from market to market.

### 3.1 The earnings sequence

| Step | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| **Early warning** | 30%/15% change filing at annual close (mandatory, ex post) | Forecast revision when threshold breached (mandatory) | 业绩预告 by Jan 31 for annual, on expected loss, turnaround or large swing (mandatory; details vary by board) | Monthly revenue by 10th (mandatory) | none |
| **Preliminary number** | 잠정실적 공정공시: voluntary; large caps ~1–2 weeks after quarter-end, often just sales and operating profit | none (決算短信 is already the full release) | 业绩快报: optional; common on STAR / ChiNext | 自結損益: voluntary monthly, mainly financials | none |
| **Formal release** | 분기보고서 / 사업보고서 (reviewed / audited) | 決算短信 within 45 days (TSE asks for 30), full statements + new forecast, XBRL | 定期报告 by Apr 30 / Aug 31 / Oct 31 | 財報 within 45 days (annual 3 months) | Press release + 8-K 2.02 (furnished) |
| **Statutory report** | 사업보고서 within 90 days; 분기·반기 within 45 days | 有価証券報告書 within 3 months; Q1/Q3 no longer statutory | 年报 by Apr 30 (Q1 also by Apr 30, the "April 30 wall") | 年報 by Mar 31 | 10-K 60–90 days; 10-Q 40–45 days |
| **Investor briefing** | Conference call for large caps; 기업설명회(IR) 개최 notice filed on KIND, deck usually on company site | 決算説明会; deck posted to TDnet as 補足資料; call mostly in Japanese | 业绩说明会: annual results briefing open to all investors, online, since 2022 expected for most companies; record posted | 法說會: slides and audio must be posted on MOPS | Earnings call; transcript not filed; slides sometimes furnished under 8-K 7.01 |
| **Who management met** | none | none | **投资者关系活动记录表: attendee funds + Q&A, within 2 days (Shenzhen mandatory)** | none | none |

### 3.2 What this means in practice

**Korea's preliminary number is a large-cap phenomenon.** 잠정실적 is a *fair-disclosure* filing, which means it is voluntary, but once filed the company is bound by it. The biggest names (Samsung, SK Hynix, LG, Hyundai) publish a two-line preliminary (consolidated sales and operating profit, no breakdown) roughly a week after quarter-end, and the detailed release follows weeks later with the call. For the majority of listed companies there is no preliminary at all: the first number the market sees is the quarterly report itself, up to 45 days after the period ends. So "Korean earnings season" is really two seasons: a handful of two-line prints in the first two weeks, then a long tail. A pipeline needs to know which companies are in which group; the split is stable and predictable.

**Japan puts everything in one document, on one day.** The 決算短信 is simultaneously the earnings release, the financial statements, and the new full-year forecast, all XBRL-tagged, all released through TDnet at a fixed time (usually 15:00 or 15:30 JST, after the close). The IR deck follows on TDnet as a supplementary document. The call itself is the least formal part, often Japanese-only, with English transcripts produced by vendors rather than the company.

**China staggers the information across three documents with different legal weight.** The preannouncement is mandatory and thresholded; the flash report is optional but increasingly used; the formal report is the only one with full statements. Because annual and Q1 reports share the same April 30 deadline, thousands of companies file both in the last week of April, a scheduling fact that matters for anyone running a real-time pipeline. The post-earnings briefing (业绩说明会) is open to retail investors and conducted online through exchange-affiliated platforms, and the record is posted. And separately, every institutional meeting a Shenzhen company holds generates a public record with the visiting funds' names.

**Taiwan replaces the "preliminary" with a monthly series.** By the time a Taiwanese company reports quarterly earnings, the market has already seen three monthly revenue prints. The quarterly report mostly resolves margins. The investor conference is a regulated event: slides and the audio file are uploaded to MOPS, which makes Taiwan the only market where the earnings call is literally in the disclosure archive.

**The US has the most calls and the fewest filings.** Nearly every US company holds a call and publishes a deck, but none of it is a filing in the strict sense. The press release is furnished under 8-K Item 2.02 (with a Reg G reconciliation of any non-GAAP numbers), the deck may be furnished under 7.01, the transcript exists only through vendors, and the actual filed financial statements arrive weeks later in the 10-Q. For a data pipeline this means the US earnings event is *earlier* than Asia's formal reports but *less official*.

### 3.3 Where the IR materials actually live

| Material | 🇰🇷 Korea | 🇯🇵 Japan | 🇨🇳 China | 🇹🇼 Taiwan | 🇺🇸 US |
|---|---|---|---|---|---|
| Earnings press release | DART (잠정실적, if any) + company site | TDnet (決算短信) | CNINFO (业绩快报 / 定期报告) | MOPS | EDGAR (8-K 2.02 exhibit) + newswire |
| Earnings deck | Company IR site (occasionally attached to DART) | **TDnet** | Company site; 路演 platform | **MOPS (mandatory)** | Company site; sometimes 8-K 7.01 |
| Call audio / transcript | Company site (large caps) | Company site; vendor transcripts | 业绩说明会 record on exchange platform | **MOPS (audio mandatory)** | Company site; vendor transcripts |
| Guidance | 공정공시 on DART if given | **決算短信 forecast + revision filings (TDnet)** | 业绩预告 only | none | Press release / call (voluntary) |
| Meeting records | none | none | **投资者关系活动记录表 (CNINFO)** | none | none |

The practical rule: in Japan and Taiwan the IR deck is a regulatory document and can be collected from the disclosure system; in Korea, China and the US it lives on the company's own site and has to be scraped. China compensates with the meeting records and the retail Q&A stream; Korea compensates with the preliminary prints and the daily flow data.

---

## 4. What Each Market Does Better Than the Others

### 🇰🇷 Korea: the API-native hub

OpenDART is the cleanest single entry point in Asia. Periodic reports, major events, issuance, ownership, audit filings, exchange disclosures and FTC disclosures sit in one searchable ecosystem with a structured API and machine-readable financial statements.

The unique asset is the **Fair Trade Commission disclosure universe** described above: group structure, related-party funding, intra-group equity and asset transfers. For chaebol analysis this has no equivalent anywhere else; the US proxy statement's related-party section is a paragraph, not a dataset. I would give it its own concept, `RELATED_PARTY_AND_GROUP_DISCLOSURE`, and let Korea have deeper coverage.

**Edge:** supply-contract filings for the semiconductor, battery and shipbuilding chains; group-structure disclosures for holding-company and succession trades; named short positions and daily flows for positioning.

### 🇯🇵 Japan: structurally clean, but two systems

The mental model is simple: **EDINET = statutory, TDnet = timely.**

EDINET (run by the Financial Services Agency) covers securities reports, extraordinary reports, registration statements, large-holding reports, tender-offer filings, target-opinion reports and internal-control reports. It is the source for financial statements, ownership, M&A and capital raising, and for the cross-shareholding tables.

TDnet (run by the Tokyo Stock Exchange) carries what moves the stock on the day: earnings, forecast revisions, dividend changes, buybacks, issuance, fixed-asset transactions, executive changes, alliances and litigation. JPX distributes machine-readable data for earnings and forecast/dividend revisions, and offers a database service, real-time feed, API and a Snowflake data share.

**The 2024 regime break:** from April 1, 2024 the statutory quarterly securities report was abolished. Q1 and Q3 now live only in the exchange earnings-report framework. A pipeline that says "I have EDINET, therefore I have Japanese filings" is missing half the year, and any long backtest needs to model the break.

**Edge:** structured forecast revisions are a direct earnings-momentum signal; cross-shareholding tables drive the unwind trade; the TSE capital-cost list and monthly EDINET buyback status reports make capital policy a live catalyst class.

### 🇨🇳 China: information-rich, source-complex

Stop looking for a Chinese DART. The hierarchy is the one described in Section 1: CSRC sets the regulatory framework (the current Information Disclosure Measures, Order No. 226, took effect 1 July 2025) → the exchanges define, enforce and publish the detailed disclosure rules (Shanghai's listing rules were last revised in April 2026) → CNINFO is the cross-market search portal → data vendors add structure on top. Keep SSE, SZSE, BSE and CNINFO as separate source IDs; the portal is a convenience layer, not the authoritative node.

The layers matter. CSRC regulation treats annual and interim reports as the core statutory periodic filings; Shanghai's listing rules additionally require Q1 and Q3 reports. The real filing universe is the union of both layers.

Several categories are natural event factors: earnings preannouncements, flash earnings, buybacks, holder purchases and sales (with advance notice), share pledges, major asset restructuring, major investment, major contracts, profit distribution, major litigation and regulatory penalties. Layered on top are the things no other market has: institutional meeting records with attendee names, the retail Q&A platforms, and public exchange inquiry letters.

China's problem is not finding interesting data. It is normalizing the sources and handling revisions correctly.

**Edge:** preannouncement-versus-actual accuracy; pledge ratios as a controller-stress indicator; meeting records as a map of institutional attention; inquiry letters and ST flags for short books.

### 🇹🇼 Taiwan: the hidden data gem

MOPS (公開資訊觀測站, the "Market Observation Post System") is the central platform for financials, material events, ownership, governance, capital actions, prospectuses, shareholder meetings, and investor-conference audio. Taiwan adopted XBRL, the standard for tagging financial statements so machines can read them, in 2010, and has required the inline version (iXBRL, where the tags are embedded in the human-readable document) since Q1 2019.

What makes Taiwan unusual is the **official OpenAPI layer**. TWSE exposes structured endpoints for daily material information, monthly revenue, financial statements, insider and >10% shareholdings, governance and ESG; TPEx (the OTC exchange) mirrors this for its listed names. Add the daily per-stock flow, margin, lending and foreign-ownership data, and it is the easiest of the four Asian markets to turn from a website into a database.

The standout dataset is **monthly revenue (每月營收)**. Listed companies disclose monthly operating revenue by the 10th of the following month, and TWSE serves it through an official API. That gives you a high-frequency fundamental series that behaves like alternative data but is official disclosure:

Monthly revenue → 3M trend / YoY / seasonality → quarterly nowcast → compare with consensus → compare with suppliers and customers → compare with alternative data.

For Taiwan technology research this is the first dataset I would load.

**Edge:** monthly-revenue nowcasts for the entire TSMC supply chain, cross-checked against Japanese equipment-maker guidance and Korean memory supply contracts; daily foreign flows and insider pre-declarations for positioning.

### 🇺🇸 US: the benchmark, structured and principles-based but thin on events

EDGAR is one archive, one regulator, one language. Every filing has a unique accession number, amendments carry a `/A` suffix, and the acceptance timestamp is recorded to the second. The SEC publishes free JSON APIs (a company's filing history, its tagged financial facts, and cross-sectional "frames" of one line item across all companies), full-text search, and its own comment-letter correspondence with issuers. From a pure data-engineering standpoint EDGAR is at least as good as OpenDART and probably better documented.

But the *event menu* is different in kind. The 8-K is a fixed list of roughly thirty items, and outside that list disclosure is governed by *materiality*, a legal standard that leaves the judgment to the company. Every market mixes enumerated events, numeric tests and a residual materiality clause; the difference is that the Asian regimes enumerate far more operational events and attach numeric triggers to them. So the US has excellent coverage of governance and financial-control events (executive changes, auditor changes, restatements, bankruptcy, delisting) and almost no mandatory coverage of operational events (CAPEX, supply contracts, production halts, monthly revenue, guidance, rumor responses). Quarterly reporting itself is now in play: the SEC proposed in May 2026 to let companies replace quarterly 10-Qs with a semiannual Form 10-S. If adopted, that is a US regime break to model alongside Japan's 2024 one.

**Edge:** 13F-based crowding and ownership-flow signals; Form 4 clusters; 8-K 4.02 restatements; comment-letter mining: all things Asia cannot offer.

---

## 5. Asia vs. EDGAR: Where the Edge Actually Sits

Putting the five columns side by side, the pattern is consistent. The US discloses *who owns the company and who runs it* in more structured detail than anyone. Asia discloses *what the company is actually doing, who is trading it, and who management is talking to* in more structured detail than the US.

| Dimension | US EDGAR | Asia (best-in-class market) |
|---|---|---|
| Ownership, manager-side | 13F, quarterly | None |
| Ownership, company-side | Proxy, annual | **China: top-10 holders quarterly** |
| Insider trades | Form 4, 2 days after | **Korea / China / Taiwan: announced 30 / 15 / 3 days before** |
| Short positions | Aggregate | **Korea / Japan: ≥0.5% named** |
| Daily flows by investor type | None | **Korea / Taiwan: per stock, daily** |
| Guidance | Voluntary | **Japan: mandatory, tagged revisions** |
| High-frequency revenue | None | **Taiwan: mandatory monthly revenue** |
| Earnings early warning | None | **China: mandatory preannouncement; Korea: 30% change filing** |
| Buyback execution | Quarterly table, lagged | **Japan: monthly statutory report; Korea: result reports** |
| Supply contracts | Materiality-based, no threshold | **Korea: mandatory above revenue threshold, with counterparty** |
| CAPEX commitments | Narrative only | Korea / China / Taiwan: event filings |
| Rumor / price-move response | None | **Korea / China / Taiwan: exchange-demanded** |
| Share pledges | Proxy footnotes | **China / Taiwan: discrete events** |
| Cross-shareholdings | None | **Japan: by name, with reason** |
| Group / related-party structure | Proxy section | **Korea: FTC disclosure universe, ex ante** |
| Who management met | None | **China (Shenzhen): fund names + Q&A within 2 days** |
| Earnings call materials | Company site | **Japan: deck on TDnet; Taiwan: deck + audio on MOPS** |
| Restatements | 8-K 4.02, clean signal | Correction filings, less standardized |
| Regulator correspondence | Comment letters, delayed | **China: inquiry letters, immediate** |
| Data access | JSON APIs, full-text search | Korea / Taiwan APIs comparable; Japan split; China fragmented |
| Language | One | Four scripts + partial English |

For a US-centric desk, the practical implication is that porting a US event-driven playbook to Asia loses the 13F and Form 4 signals but gains an entire layer of operational, positioning and management-attention events that has no US analogue. The models that work best in Asia are not the ones that work best in the US.

---

## 6. Structured Financial Data: Everywhere, but Not Equally Usable

This is the second question I started with, comparing semiconductor financial statements across markets. All five markets require companies to tag their financial statements with XBRL, so in principle "revenue," "operating income" and "capex" are machine-readable fields everywhere. In practice the developer experience differs a lot.

| Market | Structured-data reality |
|---|---|
| 🇰🇷 Korea | OpenDART gives a clean API route into tagged financials; one call per company per period |
| 🇯🇵 Japan | Mature EDINET taxonomy; the 2026 taxonomy covers tender offers and large-holding reports, and the FSA has published a draft 2027 taxonomy including sustainability. But Q1/Q3 numbers now sit in TDnet's earnings-report tags, not EDINET's |
| 🇨🇳 China | XBRL exists in the exchange ecosystem, but there is no single official API; most people go through a vendor |
| 🇹🇼 Taiwan | iXBRL since 2019, taxonomy downloads from MOPS, plus TWSE / TPEx APIs that serve the statements directly |
| 🇺🇸 US | XBRL since 2009, iXBRL phased in 2019–2021; the SEC's company-facts and frames APIs make a cross-sectional pull of one line item across every filer a single request |

Two practical warnings. First, the *taxonomies* differ: Korea and Taiwan tag against IFRS-based local taxonomies, Japan against its own, the US against US GAAP, so "operating income" is not guaranteed to be the same concept in each. Second, fiscal years differ (Japanese companies mostly end in March), so "FY2025" is not the same twelve months. A cross-market comparison needs a mapping layer for concepts and a calendar layer for periods before any of the numbers are comparable.

Ranked purely on public-data engineering, the largest Asian market does not have the easiest infrastructure, and the US is a peer of Korea and Taiwan, not a class above them.

---

## 7. Engineering Rules That Determine Whether the Data Is Tradeable

### The local filing name is never the data model

A buyback query should not require five searches (자기주식취득, 自己株式取得, 股份回购, 庫藏股, "8-K Item 8.01 + press release"). All five map to `BUYBACK`. The same applies to `MAJOR_CONTRACT`, `CAPEX`, `ASSET_ACQUISITION`, `DIVIDEND`, `LARGE_HOLDER`, `INSIDER_TRANSACTION`, `INSIDER_SALE_NOTICE`, `SHORT_POSITION`, `CONTROL_CHANGE`, `RUMOR_RESPONSE`, `LITIGATION`, `REGULATORY_ACTION`, `PRODUCTION_HALT`, `DISTRESS`.

Local taxonomy belongs in the source layer. Investors interact with the economic-event layer.

### Corrections are part of the event

A disclosure is rarely one immutable document: original → correction → second correction → shareholder approval → completion notice. Overwriting the old record with the latest filing creates *point-in-time* contamination: your backtest ends up "knowing" the corrected number on a date when the market only had the original. Every document needs an original ID, a revision chain, publication timestamp, event date, reporting period, first-seen timestamp, source URL and raw file hash.

EDGAR's accession-number-plus-`/A` convention is a useful reference design here; the Asian sources need the equivalent built on top.

For backtesting, what was known at that moment matters more than what the final corrected filing says today.

### Store four clocks

| Clock | Meaning | Who cares |
|---|---|---|
| Event time | When the economic event happened | Fundamental analysts |
| Reporting period | Which financial period it describes | Fundamental database |
| Published time | When the market received it | Event-driven strategies |
| First-seen time | When your pipeline received it | Latency and leakage audits |

A contract signed Monday, announced Tuesday evening, ingested seconds later has three different timestamps, and the wrong one silently corrupts a backtest. EDGAR is a reminder of how subtle this is: a filing accepted after 5:30 p.m. Eastern generally carries the *next* business day's filing date (with exceptions by submission type), so "filing date" and "acceptance time" are already two different clocks in the cleanest system of the five. Store both rather than coding a blanket rule.

### Preserve the original, normalize the event

Korean, Japanese, Simplified Chinese, Traditional Chinese, English: all should survive in the raw layer. Normalization is a separate layer:

Original filing → local-language rules → multilingual classifier / LLM → common event taxonomy → English normalized description.

The goal is not to translate everything into English first. It is to keep the evidence intact while making events comparable.

---

## 8. Build Order

If I were building this from scratch, I would not start with China.

1. **Korea**: build the common schema from DART.
2. **Taiwan**: stress-test the taxonomy against the OpenAPIs, monthly revenue and material-event data.
3. **US**: map EDGAR onto the same schema to confirm the taxonomy is not Asia-specific; it is also the cheapest source to wire up.
4. **Japan EDINET**: add statutory filings, tagged financials, large holders, tender offers, cross-shareholdings.
5. **Japan TDnet**: add earnings, guidance, dividends, buybacks and event-driven disclosure.
6. **China**: only then add SSE, SZSE, BSE and CNINFO one source at a time, and treat the meeting records and Q&A platforms as a separate text pipeline.

China is rich enough to dictate the entire architecture before the basic model is stable.

---

## 9. From Filing Archive to Research Graph

Once five markets share one event layer, the interface can hide the countries entirely. A disclosure service should route KR → OpenDART, JP → EDINET + TDnet, CN → SSE / SZSE / BSE / CNINFO, TW → MOPS / TWSE / TPEx, US → EDGAR behind semantic tools: `resolve_entity`, `search_disclosures`, `get_financials`, `get_guidance_changes`, `get_monthly_operating_data`, `get_buybacks`, `get_large_holders`, `get_short_positions`, `get_flows`, `get_major_contracts`, `get_capex`, `get_mna`, `get_litigation`, `get_meeting_records`, `get_disclosure_timeline`.

Go back to the two questions at the top. The first, *the Korean supplier filed a contract with a Japanese and a Taiwanese counterparty; where do I find the other side?*, becomes `resolve_entity` on the counterparty names, then `get_major_contracts` and `search_disclosures` on the resolved Japanese and Taiwanese IDs, with the system already knowing which rule applies on each side, so that it can label the Japanese result "no filing expected" and the Taiwanese result "filing expected only if TWSE's material-information tests were met" rather than simply "not found." The second, *compare the financial statements of twelve semiconductor names across four markets*, becomes one `get_financials` call that hides four taxonomies and two fiscal-year conventions.

And once that layer exists, the questions get better:

- Which APAC semiconductor companies raised CAPEX, signed new supply contracts and saw insider accumulation within the same 60-day window?
- Which buyback announcements were followed by actual share retirement rather than just authorization?
- How accurate were Chinese earnings preannouncements compared with Taiwan monthly-revenue nowcasts and Japanese management guidance?
- Which Korean groups shifted funding to a subsidiary in the quarter before a control event?
- Which Shenzhen companies saw a jump in institutional visits in the month before a guidance-beating flash report?
- Which Japanese companies' cross-shareholding tables shrank fastest after the TSE capital-cost list was published, and who was on the other side?
- When a US hyperscaler files an 8-K 1.01 supply agreement, which Korean and Taiwanese suppliers file the matching 공급계약 or 重大訊息, and how many days later?

That last question is the real prize. The same economic event is disclosed on both ends of the supply chain, under two different regimes, with two different lags. Once the event layer is shared, the lag itself becomes the signal.

---

## Takeaway

| Market | Strength | The catch |
|---|---|---|
| 🇰🇷 Korea | API-native, broadest universe, unique group and contract disclosure, named shorts, daily flows | Preliminary earnings only for large caps |
| 🇯🇵 Japan | Cleanest structure, mandatory structured guidance revisions, cross-shareholdings by name, monthly statutory buyback reports | Two systems; 2024 regime break |
| 🇨🇳 China | Richest event menu, preannouncements, pledges, meeting records with fund names | Source hierarchy and revisions |
| 🇹🇼 Taiwan | Monthly revenue, open APIs, iXBRL, earnings-call audio on file, daily flows | Underused by non-local investors |
| 🇺🇸 US | Best ownership data (13F, Form 4), best APIs, restatement signal | Almost no mandatory operational events; guidance voluntary; 10-Q now in question |

The filings, languages, APIs and rules are all different. The economic events are the same. And the market everyone treats as the gold standard turns out to be the one that asks companies to say the least about what they are actually doing.

**Normalize the event. Preserve the source.**

---

## Glossary

| Term | Plain-language meaning |
|---|---|
| **Statutory disclosure** | Filings required by securities law and submitted to the government regulator (FSA, CSRC, SEC, FSS). Annual reports, registration statements, large-holder reports. Formal, audited, slow. |
| **Exchange / timely disclosure** | Filings required by the stock exchange's listing rules and published through the exchange's own system. Earnings, buybacks, contracts, executive changes. Fast and event-driven. |
| **DART / OpenDART** | Korea's electronic disclosure system, run by the Financial Supervisory Service, and its public API. |
| **KIND** | Korea Exchange's own disclosure portal; the exchange-side view of the same filings. |
| **FTC disclosure** | Korean Fair Trade Commission filings by large business groups about transactions between affiliates and the group's ownership structure. Published through DART; no equivalent elsewhere. |
| **공정공시 (fair disclosure)** | Korea's Reg FD: information given selectively to analysts must be filed publicly. Preliminary earnings and guidance travel through this channel, which is why they are voluntary. |
| **조회공시 (inquiry disclosure)** | An exchange-demanded public answer to a rumor or unexplained price move. |
| **EDINET** | Japan's statutory filing system, run by the Financial Services Agency. |
| **TDnet** | Japan's timely-disclosure system, run by the Tokyo Stock Exchange. |
| **決算短信** | Japan's earnings report: release, financials and forecast in one tagged document. |
| **政策保有株式** | Japanese "strategic" or cross-shareholdings, listed by name in the annual report. |
| **CSRC** | China Securities Regulatory Commission, China's SEC. Writes the rules; not where filings are read. |
| **SSE / SZSE / BSE** | Shanghai, Shenzhen and Beijing stock exchanges. Write the detailed listing rules and enforce disclosure. |
| **CNINFO** | 巨潮资讯, the official cross-market portal where announcements from all Mainland exchanges can be searched. The exchanges' own sites remain the authoritative publication points. |
| **业绩预告 / 业绩快报** | Chinese earnings preannouncement (mandatory, thresholded) and flash report (optional). |
| **投资者关系活动记录表** | Chinese investor-relations activity record: who visited, when, what was asked. |
| **ST / \*ST** | Chinese ticker prefixes for companies under financial risk warning; carry a 5% daily limit. |
| **MOPS** | Taiwan's Market Observation Post System (公開資訊觀測站), the central disclosure platform. |
| **TWSE / TPEx** | Taiwan Stock Exchange and the Taipei Exchange (OTC market). Both expose official data APIs. |
| **法說會** | Taiwanese investor conference; slides and audio filed on MOPS. |
| **EDGAR** | The SEC's filing archive. |
| **8-K** | The US "current report", the form for disclosing events between periodic reports. Organized into numbered items (1.01 material agreement, 2.02 earnings, 4.02 restatement, 5.02 executive change, and so on). |
| **10-K / 10-Q / 10-S** | US annual report, quarterly report, and the proposed semiannual report. |
| **Furnished vs. filed** | US legal distinction. A *filed* document carries full liability under securities law; a *furnished* one (such as an earnings release attached to an 8-K) carries less. |
| **Reg FD** | Regulation Fair Disclosure. If a US company tells anyone material information, it must tell everyone. It does not require the company to say anything in the first place. |
| **Materiality** | Information a reasonable investor would consider important. Every market uses it as a residual test alongside enumerated events and numeric thresholds; the US relies on it most heavily for operational events, the Asian regimes least. |
| **13D / 13G** | US filings when a holder crosses 5% of a company (13D if they may seek influence, 13G if passive). |
| **13F** | Quarterly list of holdings filed by large US institutional managers. |
| **Form 4** | US insider-transaction report, due within two business days. |
| **Share pledge** | A shareholder using their stock as collateral for a loan. A stress signal for controlling families. |
| **XBRL / iXBRL** | The standard for tagging financial statements so machines can read them; the inline version embeds the tags in the human-readable document. |
| **Point-in-time** | A dataset that records what was known on each date, rather than the latest corrected value. Essential for honest backtests. |

---

*Primary sources reviewed: OpenDART, KRX KIND, Japan FSA / EDINET, JPX / TDnet, CSRC, Shanghai and Shenzhen Stock Exchanges, CNINFO, MOPS, TWSE, TPEx, and SEC / EDGAR. Personal research, unrelated to my day job. Not investment advice. All classifications, comparisons and errors are my own.*
