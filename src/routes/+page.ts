import { error } from '@sveltejs/kit';
import { asset } from '$app/paths';
import type { PageLoad } from './$types';
import type { MarketSummary } from '#lib/types/market.js';

export const load: PageLoad = async ({ fetch }) => {
	const response = await fetch(asset('data/market_summary.json'));

	if (!response.ok) {
		throw error(response.status, 'Unable to load the illustrative market summary.');
	}

	const marketSummary = (await response.json()) as MarketSummary;

	if (!marketSummary.is_demo || marketSummary.markets.length !== 5) {
		throw error(500, 'The market summary does not match the expected publication-safe demo contract.');
	}

	return { marketSummary };
};