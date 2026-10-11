<script lang="ts">
	import { onMount } from 'svelte';
	import { BarController, BarElement, CategoryScale, Chart, LinearScale, Tooltip } from 'chart.js';
	import { locale } from '#lib/locale.js';
	import type { MarketPoint } from '#lib/types/market.js';

	let { markets }: { markets: MarketPoint[] } = $props();
	let canvas: HTMLCanvasElement;

	Chart.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip);

	const marketNamesKo: Record<string, string> = {
		Korea: '한국',
		Japan: '일본',
		Taiwan: '대만',
		China: '중국',
		'Hong Kong': '홍콩'
	};
	const marketLabel = (country: string, language: 'en' | 'ko') =>
		language === 'ko' ? marketNamesKo[country] ?? country : country;
	const chartLabel = $derived($locale === 'ko'
		? '주요 아시아 시장의 1주일 지수 수익률. 청록색은 0 이상, 빨간색은 음수입니다.'
		: 'One-week index returns by market. Teal bars are non-negative, red bars are negative.');

	onMount(() => {
		const chart = new Chart(canvas, {
			type: 'bar',
			data: {
				labels: markets.map((market) => marketLabel(market.country, 'en')),
				datasets: [
					{
						data: markets.map((market) => market.return_1w),
						backgroundColor: markets.map((market) => (market.return_1w >= 0 ? '#087f78' : '#c84f4b')),
						borderRadius: 2,
						borderSkipped: false,
						barPercentage: 0.58,
						categoryPercentage: 0.72
					}
				]
			},
			options: {
				responsive: true,
				maintainAspectRatio: false,
				plugins: {
					legend: { display: false },
					tooltip: {
						callbacks: {
							label: (context) => {
								const value = Number(context.parsed.y);
								return ` ${value >= 0 ? '+' : ''}${value.toFixed(1)}%`;
							}
						}
					}
				},
				scales: {
					x: {
						grid: { display: false },
						border: { display: false },
						ticks: { color: '#526974', font: { size: 11 } }
					},
					y: {
						beginAtZero: true,
						grid: { color: '#e8eeec' },
						border: { display: false },
						ticks: {
							color: '#74858b',
							callback: (value) => `${Number(value).toFixed(1)}%`
						}
					}
				}
			}
		});

		const unsubscribe = locale.subscribe((language) => {
			chart.data.labels = markets.map((market) => marketLabel(market.country, language));
			chart.canvas.setAttribute('aria-label', language === 'ko'
				? '주요 아시아 시장의 1주일 지수 수익률 차트'
				: 'One-week index returns by market');
			chart.update();
		});

		return () => {
			unsubscribe();
			chart.destroy();
		};
	});
</script>

<div class="chart-wrap">
	<canvas bind:this={canvas} aria-label={chartLabel}></canvas>
	<p class="sr-only">{markets.map((market) => `${marketLabel(market.country, $locale)}: ${market.return_1w >= 0 ? '+' : ''}${market.return_1w.toFixed(1)}%`).join('; ')}</p>
</div>