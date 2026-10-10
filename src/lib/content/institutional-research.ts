export interface ResearchSource {
	id: string;
	name: string;
	url: string;
	description: string;
	cadence: string;
	access?: string;
}

export interface ResearchSourceGroup {
	title: string;
	description: string;
	sourceIds: string[];
}

export const researchSources: ResearchSource[] = [
	{ id: 'citadel', name: 'Citadel Securities · Global Market Intelligence', url: 'https://www.citadelsecurities.com/news-and-insights/global-market-intelligence/', description: 'Market structure, liquidity, dealer positioning, options and ETF activity from a market-maker perspective.', cadence: 'Occasional' },
	{ id: 'aqr', name: 'AQR · Alternative Thinking', url: 'https://www.aqr.com/insights/research/alternative-thinking', description: 'Research on factors, style premia, trend following and multi-asset portfolio construction.', cadence: 'Occasional' },
	{ id: 'man', name: 'Man Group · Insights', url: 'https://www.man.com/insights', description: 'Macro regimes, hedge-fund strategies, relative value and credit, including Views From the Floor.', cadence: 'Weekly series and occasional' },
	{ id: 'apollo', name: 'Apollo Academy', url: 'https://www.apolloacademy.com/', description: 'Torsten Slok’s macro charts and commentary, including The Daily Spark and The Weekly Brief.', cadence: 'Daily and weekly' },
	{ id: 'blackrock', name: 'BlackRock Investment Institute', url: 'https://www.blackrock.com/corporate/insights/blackrock-investment-institute', description: 'Global macro, asset allocation, market themes and portfolio implications.', cadence: 'Weekly and occasional' },
	{ id: 'jpm', name: 'J.P. Morgan Asset Management · Market Insights', url: 'https://am.jpmorgan.com/hk/en/asset-management/per/insights/market-insights/', description: 'Market commentary and multi-asset context; the Guide to the Markets is a useful chart library.', cadence: 'Weekly and quarterly' },
	{ id: 'jpm-weekly', name: 'J.P. Morgan · Weekly Market Recaps', url: 'https://am.jpmorgan.com/wr/en/asset-management/institutional/insights/market-insights/market-updates/', description: 'Concise summaries of recent market and macro developments.', cadence: 'Weekly' },
	{ id: 'kkr', name: 'KKR · Insights', url: 'https://www.kkr.com/wealth/insights', description: 'Private equity, private credit, real assets, global macro and asset allocation.', cadence: 'Occasional' },
	{ id: 'alphasense', name: 'AlphaSense · Resources', url: 'https://www.alpha-sense.com/resources/', description: 'Public thematic research connecting earnings calls, company disclosures and sector trends.', cadence: 'Occasional', access: 'The platform is paid; some public research is available.' },
	{ id: 'bridgewater', name: 'Bridgewater · Research & Insights', url: 'https://www.bridgewater.com/research-and-insights', description: 'Global macro, economic regimes, policy and cross-asset relationships.', cadence: 'Occasional' },
	{ id: 'twosigma', name: 'Two Sigma · Insights', url: 'https://www.twosigma.com/insights/', description: 'Quantitative investing, machine learning, statistics and data-driven research.', cadence: 'Occasional' },
	{ id: 'point72', name: 'Point72 · Insights', url: 'https://www.point72.com/insights/', description: 'Investment process, data science and market perspectives.', cadence: 'Occasional' },
	{ id: 'goldman-top', name: 'Goldman Sachs · Top of Mind', url: 'https://www.goldmansachs.com/insights/top-of-mind', description: 'In-depth coverage of important investment debates, often with expert interviews.', cadence: 'Occasional' },
	{ id: 'goldman', name: 'Goldman Sachs · Insights', url: 'https://www.goldmansachs.com/insights/', description: 'Research on the economy, companies, capital markets and global investing.', cadence: 'Several times per week' },
	{ id: 'goldman-markets', name: 'Goldman Sachs · The Markets', url: 'https://www.goldmansachs.com/insights/the-markets', description: 'Short market-focused conversations with Goldman Sachs analysts and investors, including views on positioning, rates, equities and hedge-fund sentiment.', cadence: 'Weekly' },
	{ id: 'morgan-stanley-totm', name: 'Morgan Stanley · Thoughts on the Market', url: 'https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market', description: 'Short weekday market takes from different Morgan Stanley research perspectives; recent episodes include Korea, Japan, breadth, rates and credit.', cadence: 'Weekdays' },
	{ id: 'oaktree-memos', name: 'Oaktree · Howard Marks Memos', url: 'https://www.oaktreecapital.com/insights/memos', description: 'Howard Marks on market cycles, risk, investor psychology and credit. A distinctive long-form counterpoint to daily sell-side commentary.', cadence: 'Irregular; read deeply when published' },
	{ id: 'gmo-library', name: 'GMO · Research Library', url: 'https://www.gmo.com/americas/research-library/', description: 'Long-horizon valuation, asset-class forecasts and GMO’s often contrarian views on bubbles, expected returns and portfolio construction.', cadence: 'Occasional; forecasts and letters on a slower cycle' },
	{ id: 'hussman-commentary', name: 'Hussman Funds · Market Commentary', url: 'https://www.hussmanfunds.com/category/comment/', description: 'John Hussman’s valuation- and market-internals-driven, risk-conscious interpretation; useful as a deliberately different view, not as a consensus signal.', cadence: 'Irregular; recent posts have been several weeks apart' },
	{ id: 'ubs', name: 'UBS · Wealth Management Insights', url: 'https://www.ubs.com/global/en/wealth-management/insights.html', description: 'CIO market views, asset allocation and investment ideas.', cadence: 'Occasional' },
	{ id: 'pimco', name: 'PIMCO · Insights', url: 'https://www.pimco.com/us/en/insights', description: 'Rates, bonds, credit and global macro research.', cadence: 'Occasional' },
	{ id: 'vanguard', name: 'Vanguard · Investment Insights', url: 'https://www.vanguard.com.au/personal/learn/smart-investing', description: 'Long-term asset allocation, ETFs and investor behavior.', cadence: 'Occasional' },
	{ id: 'msci-charts', name: 'MSCI · Charting Private Assets', url: 'https://www.msci.com/data-and-analytics/private-asset-solutions/visualizations', description: 'Visualizations of private equity, venture capital and private-credit performance and flows.', cadence: 'Weekly series' },
	{ id: 'msci-benchmarks', name: 'MSCI · Private Capital Benchmarks', url: 'https://www.msci.com/research-and-insights/paper/msci-private-capital-benchmarks-summary', description: 'Private-fund performance, dry powder, capital calls and distributions.', cadence: 'Quarterly', access: 'Registration may be required.' },
	{ id: 'blackstone', name: 'Blackstone · Insights', url: 'https://www.blackstone.com/insights/', description: 'Private equity, real estate and credit markets.', cadence: 'Occasional' },
	{ id: 'bain', name: 'Bain · Global Private Equity Report', url: 'https://www.bain.com/insights/topics/global-private-equity-report/', description: 'Buyouts, fundraising, exits and private-equity performance.', cadence: 'Annual' },
	{ id: 'preqin', name: 'Preqin · Insights', url: 'https://www.preqin.com/insights', description: 'Private equity, venture capital, hedge funds and private-capital data.', cadence: 'Occasional' },
	{ id: 'cambridge', name: 'Cambridge Associates · Insights', url: 'https://www.cambridgeassociates.com/insight/', description: 'Institutional portfolios, manager selection and private markets.', cadence: 'Occasional' },
	{ id: 'caia', name: 'CAIA · Alternative Investments', url: 'https://caia.org/blog', description: 'Educational material on alternative investments, hedge funds and portfolio construction.', cadence: 'Occasional' },
	{ id: 'spglobal', name: 'S&P Global Market Intelligence', url: 'https://www.spglobal.com/marketintelligence/en/news-insights', description: 'Company data, credit markets and industry developments.', cadence: 'Occasional' },
	{ id: 'cboe', name: 'Cboe · Insights', url: 'https://www.cboe.com/insights/', description: 'Options, volatility and market structure.', cadence: 'Occasional' },
	{ id: 'cme', name: 'CME Group · Featured Reports', url: 'https://www.cmegroup.com/education/featured-reports.html', description: 'Futures, positioning, interest rates and commodities.', cadence: 'Occasional' },
	{ id: 'lseg', name: 'LSEG · Insights', url: 'https://www.lseg.com/en/insights', description: 'Capital markets, financial data and investment analysis.', cadence: 'Occasional' },
	{ id: 'nasdaq', name: 'Nasdaq · Market Articles', url: 'https://www.nasdaq.com/articles', description: 'ETFs, capital markets, companies and trading.', cadence: 'Occasional' },
	{ id: 'nomura', name: 'Nomura · Nomura Connects', url: 'https://www.nomuraconnects.com/', description: 'Asian macro, Japan and investment strategy.', cadence: 'Occasional' },
	{ id: 'nikko', name: 'Nikko Asset Management · Insights', url: 'https://www.nikkoam.com/institutional/insights', description: 'Japanese equities, Asia-Pacific markets and macro.', cadence: 'Occasional' },
	{ id: 'eastspring', name: 'Eastspring Investments · Insights', url: 'https://www.eastspring.com/insights', description: 'Asian equities, bonds and asset allocation.', cadence: 'Occasional' },
	{ id: 'gavekal', name: 'Gavekal Research', url: 'https://research.gavekal.com/', description: 'China, global macro and liquidity research.', cadence: 'Occasional', access: 'Public articles and full research may have different access terms.' },
	{ id: 'adb', name: 'Asian Development Bank · Publications', url: 'https://www.adb.org/publications', description: 'Asian economies, financial markets and structural change.', cadence: 'Occasional' }
];

export const researchSourceGroups: ResearchSourceGroup[] = [
	{
		title: 'Core institutional research',
		description: 'A starting set spanning market structure, quant research, macro, brokerage commentary and private markets.',
		sourceIds: ['citadel', 'aqr', 'man', 'apollo', 'blackrock', 'jpm-weekly', 'goldman-markets', 'morgan-stanley-totm', 'kkr', 'alphasense']
	},
	{
		title: 'Sell-side & brokerage market views',
		description: 'Frequent, public-facing perspectives from large research desks. These are useful windows into analyst framing, not substitutes for institution-client research, which is often gated.',
		sourceIds: ['morgan-stanley-totm', 'goldman-markets', 'goldman', 'jpm-weekly', 'jpm']
	},
	{
		title: 'Distinctive manager voices',
		description: 'Less frequent than daily market commentary, but valuable for contrasting a clear investment philosophy against the weekly consensus.',
		sourceIds: ['oaktree-memos', 'gmo-library', 'hussman-commentary', 'bridgewater', 'man']
	},
	{
		title: 'Hedge funds & quant research',
		description: 'Compare the economic rationale for factors, how strategies are implemented and what data-driven evidence supports them.',
		sourceIds: ['bridgewater', 'twosigma', 'point72', 'aqr', 'man', 'citadel']
	},
	{
		title: 'Wealth management & global macro',
		description: 'Read market developments through the lens of portfolio construction, asset allocation and macro regimes.',
		sourceIds: ['goldman-top', 'goldman', 'jpm', 'jpm-weekly', 'blackrock', 'ubs', 'pimco', 'vanguard']
	},
	{
		title: 'Private markets',
		description: 'Pair frequent market charts with longer-horizon reports on performance, fundraising, exits and liquidity.',
		sourceIds: ['msci-charts', 'msci-benchmarks', 'kkr', 'apollo', 'blackstone', 'bain', 'preqin', 'cambridge', 'caia']
	},
	{
		title: 'Alternative data & market intelligence',
		description: 'Connect company disclosures and earnings commentary to sector themes, positioning and market data.',
		sourceIds: ['alphasense', 'spglobal', 'msci-charts', 'cboe', 'cme', 'lseg', 'nasdaq']
	},
	{
		title: 'Asia markets',
		description: 'Add regional context on Korea, Japan, China, Taiwan and broader Asia to research that often centers on the United States.',
		sourceIds: ['nomura', 'nikko', 'eastspring', 'gavekal', 'adb']
	}
];

export const weeklyReadingRoutine = [
	{ day: 'Monday', theme: 'Global market recap', sourceIds: ['jpm-weekly', 'blackrock', 'apollo'] },
	{ day: 'Tuesday', theme: 'Sell-side & market structure', sourceIds: ['morgan-stanley-totm', 'goldman-markets', 'citadel', 'man', 'cboe'] },
	{ day: 'Wednesday', theme: 'Quant & factor research', sourceIds: ['aqr', 'twosigma'] },
	{ day: 'Thursday', theme: 'Private markets & manager views', sourceIds: ['msci-benchmarks', 'kkr', 'goldman-top', 'oaktree-memos', 'gmo-library'] },
	{ day: 'Friday', theme: 'Asia & earnings intelligence', sourceIds: ['nomura', 'alphasense', 'eastspring'] }
];

export const researchFramework = [
	{ title: 'Market observation', description: 'What happened this week? Track returns, breadth, flows and volatility.' },
	{ title: 'Institutional interpretation', description: 'How do different institutions interpret the same market observation?' },
	{ title: 'Data & methodology', description: 'Identify the source data, definitions and calculations behind each conclusion.' },
	{ title: 'Research replication', description: 'Ask what data and models would be needed to test the same idea in Asian markets.' }
];