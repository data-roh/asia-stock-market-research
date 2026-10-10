<script lang="ts">
	import type { MarketPoint } from '#lib/types/market.js';

	let { point }: { point: MarketPoint } = $props();
	const marketCodes: Record<string, string> = {
		Korea: 'KR',
		Japan: 'JP',
		Taiwan: 'TW',
		China: 'CN',
		'Hong Kong': 'HK'
	};
	const formattedReturn = $derived(`${point.return_1w >= 0 ? '+' : ''}${point.return_1w.toFixed(1)}%`);
</script>

<article class="market-card">
	<div class="market-topline">
		<div>
			<span class="market-country">{point.country}</span>
			<span class="market-index">{point.index}</span>
		</div>
		<span class="market-code">{marketCodes[point.country] ?? 'AS'}</span>
	</div>
	<div class="market-metrics">
		<strong class:positive={point.return_1w >= 0} class:negative={point.return_1w < 0} class="market-return">
			{formattedReturn}
		</strong>
		<div class="market-breadth">
			<strong>{point.breadth.toFixed(0)}%</strong>
			<span>breadth</span>
		</div>
	</div>
</article>

<style>
	.positive { color: #087f78; }
	.negative { color: #c84f4b; }
</style>