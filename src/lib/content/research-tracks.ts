export interface ResearchTopic {
	title: string;
	description: string;
	status: 'Planned' | 'Framework' | 'Building' | 'Research area';
}

export interface ResearchTrack {
	slug: string;
	path: 'disclosures/' | 'core-concepts/' | 'market-overlay/' | 'quant/';
	eyebrow: string;
	title: string;
	shortDescription: string;
	description: string;
	metaDescription: string;
	method: string;
	topics: ResearchTopic[];
}

export const researchTracks: Record<string, ResearchTrack> = {
	disclosures: {
		slug: 'disclosures',
		path: 'disclosures/',
		eyebrow: 'Research track 01',
		title: 'Disclosures',
		shortDescription: 'Map how Asian companies publish financial, operating and risk information.',
		description: 'Understand how Asian markets disclose financial, operating, ownership, customer, supplier, contract and risk information.',
		metaDescription: 'A working map of Asian disclosure systems, source provenance, document lineage and point-in-time publication.',
		method: 'Compare what each market publishes, where it appears and how it changes over time. Every future field should retain its source, publication date and revision history.',
		topics: [
			{ title: 'Korea, Japan, China and Taiwan disclosure systems', description: 'Compare filing channels, publication timing and market-specific document types.', status: 'Planned' },
			{ title: 'IR material and factbook source maps', description: 'Organize investor-relations material around stable, attributable source locations.', status: 'Planned' },
			{ title: 'Supply-chain and major-contract disclosures', description: 'Track disclosed supplier, customer, contract and operating relationships.', status: 'Research area' },
			{ title: 'Source provenance and document lineage', description: 'Keep each normalized field traceable to the original public document.', status: 'Framework' },
			{ title: 'Point-in-time publication and revision tracking', description: 'Distinguish what was known at a date from revisions published later.', status: 'Planned' }
		]
	},
	'core-concepts': {
		slug: 'core-concepts',
		path: 'core-concepts/',
		eyebrow: 'Research track 02',
		title: 'Financial Core Concepts',
		shortDescription: 'Build a practical comparison framework for Asian financial institutions.',
		description: 'Build a practical comparison framework for banks, insurers, securities firms, digital banks and financial holding companies.',
		metaDescription: 'Financial concepts and market-specific accounting differences for banks, insurers, securities firms and holding companies.',
		method: 'Define each concept before comparing companies. Separate accounting definitions, regulatory definitions and analyst calculations, then map local fields to a documented golden template.',
		topics: [
			{ title: 'Bank concepts: NIM, CET1, Tier 1, CAR, LCR, leverage and RWA', description: 'Separate profitability, capital adequacy, liquidity and risk-weighted asset measures.', status: 'Framework' },
			{ title: 'Insurance concepts: solvency, CSM, combined ratio and investment yield', description: 'Compare underwriting performance, contract service margins and capital strength.', status: 'Planned' },
			{ title: 'Securities concepts: brokerage, investment banking, trading and capital', description: 'Build segment-aware comparisons for diversified securities businesses.', status: 'Planned' },
			{ title: 'Market-specific accounting and regulatory differences', description: 'Document where similar labels conceal different accounting or supervisory rules.', status: 'Research area' },
			{ title: 'Golden-template concepts and source-field mapping', description: 'Map market-specific source fields into a consistent, auditable data model.', status: 'Building' }
		]
	},
	'market-overlay': {
		slug: 'market-overlay',
		path: 'market-overlay/',
		eyebrow: 'Research track 03',
		title: 'Market Overlay',
		shortDescription: 'Connect company fundamentals and disclosures to market behavior.',
		description: 'Connect company fundamentals and disclosures to price action, positioning, revisions, flows, breadth and market regimes.',
		metaDescription: 'Market overlays connecting Asian company fundamentals with price action, breadth, revisions, flows and market regimes.',
		method: 'Keep market observations distinct from causal claims. Align timestamps, define the comparison universe and show the denominator behind every breadth, flow or contribution measure.',
		topics: [
			{ title: 'Index returns and market breadth', description: 'Track index performance alongside the share of constituents participating.', status: 'Building' },
			{ title: 'Contribution and concentration', description: 'Measure how much index movement comes from a small number of names.', status: 'Planned' },
			{ title: 'EPS revisions', description: 'Observe the direction and dispersion of earnings estimate changes.', status: 'Planned' },
			{ title: 'ETF and active-ETF flows', description: 'Compare fund flows with holdings, concentration and underlying market moves.', status: 'Research area' },
			{ title: 'Buybacks and capital returns', description: 'Connect announced capital-return programs with realized execution.', status: 'Planned' },
			{ title: 'Fear, greed and market regimes', description: 'Test transparent indicators for shifts in participation and risk appetite.', status: 'Research area' }
		]
	},
	quant: {
		slug: 'quant',
		path: 'quant/',
		eyebrow: 'Research track 04',
		title: 'Quant Research',
		shortDescription: 'Turn market intuition into transparent, reproducible research.',
		description: 'Convert market intuition into transparent, testable and reproducible empirical research.',
		metaDescription: 'Reproducible quantitative research on Asian markets, with explicit assumptions and backtest validation.',
		method: 'Every study should state its hypothesis, point-in-time data assumptions, transaction costs and failure modes. A chart is an observation, not proof of an edge.',
		topics: [
			{ title: 'Intraday market relay', description: 'Explore how information and returns propagate across regional trading sessions.', status: 'Research area' },
			{ title: 'Korea-Taiwan memory lead-lag', description: 'Test whether memory-sector signals travel across the two markets.', status: 'Planned' },
			{ title: 'Close auction behavior', description: 'Study closing-auction volume, imbalance and next-session behavior.', status: 'Planned' },
			{ title: 'Cash-futures basis', description: 'Measure basis behavior with contract, roll and timestamp controls.', status: 'Research area' },
			{ title: 'Factor research', description: 'Evaluate factor definitions, exposures and stability across markets.', status: 'Planned' },
			{ title: 'Backtest validation and common research mistakes', description: 'Check look-ahead bias, survivorship, costs and parameter selection.', status: 'Framework' }
		]
	}
};