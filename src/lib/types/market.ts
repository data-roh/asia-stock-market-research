export interface MarketPoint {
	country: string;
	index: string;
	return_1w: number;
	breadth: number;
}

export interface MarketSummary {
	title: string;
	as_of: string;
	is_demo: true;
	source: string;
	markets: MarketPoint[];
}