<script lang="ts">
	import { resolve } from '$app/paths';
	import {
		researchFramework,
		researchSources,
		researchSourceGroups,
		weeklyReadingRoutine
	} from '#lib/content/institutional-research.js';
	import type { ResearchSource } from '#lib/content/institutional-research.js';

	const sourcesById = new Map(researchSources.map((source) => [source.id, source]));
	const findSource = (id: string): ResearchSource => {
		const source = sourcesById.get(id);
		if (!source) throw new Error(`Unknown research source: ${id}`);
		return source;
	};
</script>

<svelte:head>
	<title>Institutional Research Library | Asia Stock Market Research (ASMR)</title>
	<meta
		name="description"
		content="A curated directory of public institutional research on hedge funds, quant strategies, global macro, private markets and Asia."
	/>
</svelte:head>

<main class="research-page">
	<section class="page-intro">
		<div class="shell">
			<p class="eyebrow">Research directory · Public sources</p>
			<h1>Institutional Research Library</h1>
			<p class="intro-copy">
				A curated reading desk for how investment institutions interpret markets, choose data and connect
				research to portfolio decisions. Some sources may require registration or investor eligibility;
				access and publication schedules can change.
			</p>
		</div>
	</section>

	<div class="page-body shell">
		{#each researchSourceGroups as group (group.title)}
			<section class="resource-group" aria-label={group.title}>
				<div class="resource-group-heading">
					<div>
						<p class="eyebrow">{String(researchSourceGroups.indexOf(group) + 1).padStart(2, '0')} · Research sources</p>
						<h2>{group.title}</h2>
					</div>
					<p>{group.description}</p>
				</div>
				<div class="resource-grid">
					{#each group.sourceIds as sourceId (sourceId)}
						{@const source = findSource(sourceId)}
						<article class="resource-card">
							<h3><a href={source.url} target="_blank" rel="external noreferrer">{source.name} <span aria-hidden="true">↗</span></a></h3>
							<p>{source.description}</p>
							<div class="resource-meta">
								<span>{source.cadence}</span>
								{#if source.access}<span>{source.access}</span>{/if}
							</div>
						</article>
					{/each}
				</div>
			</section>
		{/each}

		<section class="resource-group" aria-labelledby="routine-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">A manageable cadence</p>
					<h2 id="routine-title">Weekly reading routine</h2>
				</div>
				<p>Use these as days to check for new material, not as promised publication dates.</p>
			</div>
			<div class="reading-routine">
				{#each weeklyReadingRoutine as day (day.day)}
					<article class="reading-day">
						<p class="eyebrow">{day.day}</p>
						<h3>{day.theme}</h3>
						<ul>
							{#each day.sourceIds as sourceId (sourceId)}
								<li><a href={findSource(sourceId).url} target="_blank" rel="external noreferrer">{findSource(sourceId).name}</a></li>
							{/each}
						</ul>
					</article>
				{/each}
			</div>
		</section>

		<section class="resource-group" aria-labelledby="framework-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">From reading to research</p>
					<h2 id="framework-title">Four questions to carry into each source</h2>
				</div>
			</div>
			<ul class="framework-list">
				{#each researchFramework as item (item.title)}
					<li><strong>{item.title}</strong><span>{item.description}</span></li>
				{/each}
			</ul>
			<aside class="method-panel" aria-label="Applying institutional research to Asia">
				<div>
					<p class="eyebrow">Asia research application</p>
					<h2>Turn a market view into a testable question.</h2>
				</div>
				<p>
					If a source studies US ETF flows, ask whether the same observation holds for Korea, Taiwan or Japan.
					If it studies global momentum, compare factor definitions and performance across Asian markets.
				</p>
			</aside>
		</section>

		<div class="page-back"><a class="text-link" href={resolve('/')}>← Back to ASMR home</a></div>
	</div>
</main>