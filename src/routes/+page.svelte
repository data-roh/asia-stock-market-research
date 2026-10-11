<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import MarketBarChart from '#lib/components/MarketBarChart.svelte';
	import MarketCard from '#lib/components/MarketCard.svelte';
	import ResearchTrackCard from '#lib/components/ResearchTrackCard.svelte';
	import { researchTracks } from '#lib/content/research-tracks.js';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
	const tracks = Object.values(researchTracks);
	const copy = $derived(siteCopy[$locale].home);
</script>

<svelte:head>
	<title>{copy.heroTitle} (ASMR) | Data × Markets × Research</title>
	<meta
		name="description"
		content={copy.heroDescription}
	/>
</svelte:head>

<main>
	<section class="hero-band">
		<div class="shell hero-layout">
			<div class="hero-copy">
				<p class="eyebrow">{copy.heroEyebrow}</p>
				<h1>{copy.heroTitle}</h1>
				<p class="hero-lede">{copy.heroDescription}</p>
				<div class="hero-actions">
					<a class="button button-primary" href="#weekly-briefing">{copy.weeklyLink}</a>
					<a class="button button-secondary" href="#market-knowledge">{copy.knowledgeLink}</a>
				</div>
			</div>
			<div class="hero-index" aria-label={copy.coverage}>
				<div class="hero-index-top"><span>ASIA COVERAGE</span><span>01 / 05</span></div>
				<div class="hero-index-line"></div>
				<p>{copy.coverage}</p>
				<div class="hero-index-bottom"><span>INDEPENDENT RESEARCH</span><span>EST. 2026</span></div>
			</div>
		</div>
	</section>

	<section class="section pulse-section" id="weekly-briefing" aria-labelledby="pulse-title">
		<div class="shell">
			<div class="section-heading pulse-heading">
				<div>
					<p class="eyebrow">{copy.weeklyEyebrow} · {data.marketSummary.as_of}</p>
					<h2 id="pulse-title">{copy.weeklyTitle}</h2>
				</div>
				<p class="demo-note"><span class="demo-dot"></span>{copy.sampleData}</p>
			</div>
			<div class="market-grid">
				{#each data.marketSummary.markets as market (market.country)}
					<MarketCard point={market} />
				{/each}
			</div>
			<div class="chart-panel">
				<div class="chart-heading">
					<div>
						<p class="eyebrow">{copy.performance}</p>
						<h3>{copy.oneWeekReturns}</h3>
					</div>
					<p>{copy.fiveMarkets}</p>
				</div>
				<MarketBarChart markets={data.marketSummary.markets} />
			</div>
		</div>
	</section>

	<section class="section tracks-section" id="market-knowledge" aria-labelledby="tracks-title">
		<div class="shell">
			<div class="section-heading">
				<div>
					<p class="eyebrow">{copy.knowledgeEyebrow}</p>
					<h2 id="tracks-title">{copy.knowledgeTitle}</h2>
				</div>
				<p class="section-aside">{copy.knowledgeAside}</p>
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
				<p class="eyebrow">{copy.aboutEyebrow}</p>
				<h2 id="about-title">{copy.aboutTitle}</h2>
			</div>
			<div class="about-copy">
				<p>{copy.aboutBody}</p>
				<a class="text-link" href={resolve('about/')}>{copy.aboutLink} <span aria-hidden="true">→</span></a>
				<a class="text-link" href={resolve('institutional-research/')}>{copy.libraryLink} <span aria-hidden="true">→</span></a>
			</div>
		</div>
	</section>

	<section class="disclaimer-band" aria-label="Research disclaimer">
		<div class="shell disclaimer-content">
			<p class="eyebrow">{copy.disclaimerLabel}</p>
			<p>{copy.disclaimer}</p>
		</div>
	</section>
</main>
