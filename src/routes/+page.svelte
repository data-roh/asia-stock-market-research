<script lang="ts">
	import { resolve } from '$app/paths';
	import MarketBarChart from '#lib/components/MarketBarChart.svelte';
	import MarketCard from '#lib/components/MarketCard.svelte';
	import ResearchTrackCard from '#lib/components/ResearchTrackCard.svelte';
	import { researchTracks } from '#lib/content/research-tracks.js';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
	const tracks = Object.values(researchTracks);
</script>

<svelte:head>
	<title>Asia Stock Market Research (ASMR) | Data × Markets × Research</title>
	<meta
		name="description"
		content="A research workspace for Asian disclosures, financial institutions, market overlays and quantitative signals."
	/>
</svelte:head>

<main>
	<section class="hero-band">
		<div class="shell hero-layout">
			<div class="hero-copy">
				<p class="eyebrow">ASMR · Data × Markets × Research</p>
				<h1>Asia Stock Market Research</h1>
				<p class="hero-lede">
					A research workspace for understanding Asian disclosures, financial institutions,
					market overlays and quantitative signals.
				</p>
				<div class="hero-actions">
					<a class="button button-primary" href="#market-pulse">Explore Market Pulse</a>
					<a class="button button-secondary" href="#research-tracks">Browse Research Tracks</a>
				</div>
			</div>
			<div class="hero-index" aria-label="Research coverage">
				<div class="hero-index-top"><span>REGIONAL COVERAGE</span><span>01 / 05</span></div>
				<div class="hero-index-line"></div>
				<p>Disclosure systems<br />Financial institutions<br />Market signals</p>
				<div class="hero-index-bottom"><span>INDEPENDENT RESEARCH</span><span>EST. 2026</span></div>
			</div>
		</div>
	</section>

	<section class="section pulse-section" id="market-pulse" aria-labelledby="pulse-title">
		<div class="shell">
			<div class="section-heading pulse-heading">
				<div>
					<p class="eyebrow">Regional snapshot · {data.marketSummary.as_of}</p>
					<h2 id="pulse-title">{data.marketSummary.title}</h2>
				</div>
				<p class="demo-note"><span class="demo-dot"></span>Illustrative sample data</p>
			</div>
			<div class="market-grid">
				{#each data.marketSummary.markets as market (market.country)}
					<MarketCard point={market} />
				{/each}
			</div>
			<div class="chart-panel">
				<div class="chart-heading">
					<div>
						<p class="eyebrow">Performance monitor</p>
						<h3>One-week index returns</h3>
					</div>
					<p>Percent change · five markets</p>
				</div>
				<MarketBarChart markets={data.marketSummary.markets} />
			</div>
		</div>
	</section>

	<section class="section tracks-section" id="research-tracks" aria-labelledby="tracks-title">
		<div class="shell">
			<div class="section-heading">
				<div>
					<p class="eyebrow">Research program</p>
					<h2 id="tracks-title">Four connected research tracks</h2>
				</div>
				<p class="section-aside">A common language for data, institutions and markets.</p>
			</div>
			<div class="track-grid">
				{#each tracks as track, index (track.slug)}
					<ResearchTrackCard track={track} number={String(index + 1).padStart(2, '0')} />
				{/each}
			</div>
		</div>
	</section>

	<section class="about-band" aria-labelledby="about-title">
		<div class="shell about-layout">
			<div>
				<p class="eyebrow">Working method</p>
				<h2 id="about-title">Analysis in Python.<br />Research made usable.</h2>
			</div>
			<div class="about-copy">
				<p>
					The analytical work is produced in Python. The website turns selected,
					publication-safe outputs into reusable charts, concept notes and market tools.
				</p>
				<a class="text-link" href={resolve('disclosures/')}>Start with the research tracks <span aria-hidden="true">→</span></a>
				<a class="text-link" href={resolve('institutional-research/')}>Open the institutional research library <span aria-hidden="true">→</span></a>
			</div>
		</div>
	</section>

	<section class="disclaimer-band" aria-label="Research disclaimer">
		<div class="shell disclaimer-content">
			<p class="eyebrow">Important</p>
			<p>Personal research and educational material only. Not investment advice. No confidential, proprietary or employer-owned data.</p>
		</div>
	</section>
</main>
