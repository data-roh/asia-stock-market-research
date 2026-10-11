<script lang="ts">
	import { locale } from '#lib/locale.js';
	import type { MarketPoint } from '#lib/types/market.js';

	let { point }: { point: MarketPoint } = $props();
	const marketCodes: Record<string, string> = {
		Korea: 'KR',
		Japan: 'JP',
		Taiwan: 'TW',
		China: 'CN',
		'Hong Kong': 'HK'
	};
	const marketNamesKo: Record<string, string> = {
		Korea: '한국',
		Japan: '일본',
		Taiwan: '대만',
		China: '중국',
		'Hong Kong': '홍콩'
	};
	const countryName = $derived($locale === 'ko' ? marketNamesKo[point.country] ?? point.country : point.country);
	const formattedReturn = $derived(`${point.return_1w >= 0 ? '+' : ''}${point.return_1w.toFixed(1)}%`);
</script>

<article class="market-card">
	<div class="market-topline">
		<div>
			<span class="market-country">{countryName}</span>
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
			<span>{$locale === 'ko' ? '상승 종목 비율' : 'breadth'}</span>
		</div>
	</div>
</article>

<style>
	.positive { color: #087f78; }
	.negative { color: #c84f4b; }
</style>