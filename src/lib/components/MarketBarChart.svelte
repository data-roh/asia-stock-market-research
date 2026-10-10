<script lang="ts">
	import { onMount } from 'svelte';
	import { BarController, BarElement, CategoryScale, Chart, LinearScale, Tooltip } from 'chart.js';
	import type { MarketPoint } from '#lib/types/market.js';

	let { markets }: { markets: MarketPoint[] } = $props();
	let canvas: HTMLCanvasElement;

	Chart.register(BarController, BarElement, CategoryScale, LinearScale, Tooltip);

	onMount(() => {
		const chart = new Chart(canvas, {
			type: 'bar',
			data: {
				labels: markets.map((market) => market.country),
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

		return () => chart.destroy();
	});
</script>

<div class="chart-wrap">
	<canvas bind:this={canvas} aria-label="One-week index returns by market. Teal bars are non-negative, red bars are negative."></canvas>
	<p class="sr-only">{#each markets as market, index}{index > 0 ? '; ' : ''}{market.country}: {market.return_1w >= 0 ? '+' : ''}{market.return_1w.toFixed(1)} percent{/each}</p>
</div>