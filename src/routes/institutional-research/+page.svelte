<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import researchFeedConfig from '#lib/content/research-feeds.json';
	import researchUpdateReport from '#lib/content/research-updates.json';
	import { researchGroupsKo, researchSourceCopyKo, weeklyRoutineKo } from '#lib/content/institutional-research-ko.js';
	import {
		researchSources,
		researchSourceGroups,
		weeklyReadingRoutine
	} from '#lib/content/institutional-research.js';
	import type { ResearchSource } from '#lib/content/institutional-research.js';

	interface ResearchUpdate {
		key: string;
		sourceId: string;
		title: string;
		url: string;
		publishedAt: string | null;
		summary: string;
	}

	interface ResearchUpdateReport {
		lastCheckedAt: string | null;
		sourceChecks: { sourceId: string; ok: boolean; error: string | null }[];
		items: ResearchUpdate[];
	}

	const updateReport = researchUpdateReport as ResearchUpdateReport;
	const sourcesById = new Map(researchSources.map((source) => [source.id, source]));
	const trackedSourceIds = new Set(researchFeedConfig.feeds.map((feed) => feed.sourceId));
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
		<section class="resource-group updates-group" aria-labelledby="updates-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">{copy.updatesEyebrow}</p>
					<h2 id="updates-title">{copy.updatesTitle}</h2>
				</div>
				<p>{copy.updatesNote}</p>
			</div>
			<div class="updates-status">
				<span>{copy.lastCheckedLabel}: {updateReport.lastCheckedAt?.slice(0, 16).replace('T', ' ') ?? copy.notCheckedYet} UTC</span>
				<span>{copy.monitoredSources}: {researchFeedConfig.feeds.length}</span>
				{#if updateReport.sourceChecks.some((check) => !check.ok)}
					<span class="updates-warning">{copy.feedWarning}</span>
				{/if}
			</div>
			{#if updateReport.items.length > 0}
				<div class="updates-list">
					{#each updateReport.items as item (item.key)}
						{@const source = findSource(item.sourceId)}
						<article class="update-entry">
							<div class="update-entry-meta">
								<span>{source.name}</span>
								<time datetime={item.publishedAt ?? undefined}>{item.publishedAt?.slice(0, 10) ?? copy.unknownDate}</time>
							</div>
							<h3><a href={item.url} target="_blank" rel="external noreferrer">{item.title} <span aria-hidden="true">↗</span></a></h3>
							{#if item.summary}<p>{item.summary}</p>{/if}
						</article>
					{/each}
				</div>
			{:else}
				<p class="updates-empty">{copy.noNewUpdates}</p>
			{/if}
		</section>

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
								<span class:tracking-enabled={trackedSourceIds.has(sourceId)} class="tracking-status">{trackedSourceIds.has(sourceId) ? copy.trackedLabel : copy.untrackedLabel}</span>
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