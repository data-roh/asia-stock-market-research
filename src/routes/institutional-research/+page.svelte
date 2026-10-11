<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import { researchGroupsKo, researchSourceCopyKo, weeklyRoutineKo } from '#lib/content/institutional-research-ko.js';
	import {
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
	const copy = $derived(siteCopy[$locale].library);
	const weekdays: Record<string, string> = $derived(siteCopy[$locale].weekdays);
</script>

<svelte:head>
	<title>{copy.title} | Asia Stock Market Research (ASMR)</title>
	<meta
		name="description"
		content={copy.description}
	/>
</svelte:head>

<main class="research-page">
	<section class="page-intro">
		<div class="shell">
			<p class="eyebrow">{copy.eyebrow}</p>
			<h1>{copy.title}</h1>
			<p class="intro-copy">{copy.description}</p>
		</div>
	</section>

	<div class="page-body shell">
		{#each researchSourceGroups as group, groupIndex (group.title)}
			{@const groupCopy = $locale === 'ko' ? researchGroupsKo[groupIndex] : group}
			<section id={group.anchor} class="resource-group" aria-label={groupCopy.title}>
				<div class="resource-group-heading">
					<div>
						<p class="eyebrow">{String(groupIndex + 1).padStart(2, '0')} · {copy.groupsEyebrow}</p>
						<h2>{groupCopy.title}</h2>
					</div>
					<p>{groupCopy.description}</p>
				</div>
				<div class="resource-grid">
					{#each group.sourceIds as sourceId (sourceId)}
						{@const source = findSource(sourceId)}
						{@const sourceCopy = $locale === 'ko' ? researchSourceCopyKo[sourceId] : undefined}
						<article class="resource-card">
							<h3><a href={source.url} target="_blank" rel="external noreferrer">{source.name} <span aria-hidden="true">↗</span></a></h3>
							<p>{sourceCopy?.description ?? source.description}</p>
							<div class="resource-meta">
								<span>{sourceCopy?.cadence ?? source.cadence}</span>
								{#if source.access}<span>{sourceCopy?.access ?? source.access}</span>{/if}
							</div>
						</article>
					{/each}
				</div>
			</section>
		{/each}

		<section class="resource-group" aria-labelledby="routine-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">{copy.routineEyebrow}</p>
					<h2 id="routine-title">{copy.routineTitle}</h2>
				</div>
				<p>{copy.routineNote}</p>
			</div>
			<div class="reading-routine">
				{#each weeklyReadingRoutine as day, dayIndex (day.day)}
					<article class="reading-day">
						<p class="eyebrow">{weekdays[day.day]}</p>
						<h3>{$locale === 'ko' ? weeklyRoutineKo[dayIndex] : day.theme}</h3>
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
					<p class="eyebrow">{copy.frameworkEyebrow}</p>
					<h2 id="framework-title">{copy.frameworkTitle}</h2>
				</div>
			</div>
			<ul class="framework-list">
				{#each copy.framework as item (item.title)}
					<li><strong>{item.title}</strong><span>{item.description}</span></li>
				{/each}
			</ul>
			<aside class="method-panel" aria-label="Applying institutional research to Asia">
				<div>
					<p class="eyebrow">{copy.asiaEyebrow}</p>
					<h2>{copy.asiaTitle}</h2>
				</div>
				<p>{copy.asiaBody}</p>
			</aside>
		</section>

		<div class="page-back"><a class="text-link" href={resolve('/')}>← {copy.backHome}</a></div>
	</div>
</main>