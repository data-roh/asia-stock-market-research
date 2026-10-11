<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import { researchStatusKo, researchTracksKo } from '#lib/content/research-tracks-ko.js';
	import { disclosureDocuments } from '#lib/content/disclosure-documents.js';
	import ResearchTopicCard from '#lib/components/ResearchTopicCard.svelte';
	import type { ResearchTrack } from '#lib/content/research-tracks.js';

	let { track }: { track: ResearchTrack } = $props();
	const koreanTrack = $derived($locale === 'ko' ? researchTracksKo[track.slug as keyof typeof researchTracksKo] : undefined);
	const title = $derived(koreanTrack?.title ?? track.title);
	const eyebrow = $derived(koreanTrack?.eyebrow ?? track.eyebrow);
	const description = $derived(koreanTrack?.description ?? track.description);
	const method = $derived(koreanTrack?.method ?? track.method);
	const topics = $derived(track.topics.map((topic, index) => ({
		...topic,
		...(koreanTrack?.topics[index] ?? {})
	})));
	const copy = $derived(siteCopy[$locale].track);
</script>

<svelte:head>
	<title>{title} | Asia Stock Market Research (ASMR)</title>
	<meta name="description" content={koreanTrack?.metaDescription ?? track.metaDescription} />
</svelte:head>

<main class="research-page">
	<section class="page-intro">
		<div class="shell">
			<p class="eyebrow">{eyebrow}</p>
			<h1>{title}</h1>
			<p class="intro-copy">{description}</p>
		</div>
	</section>
	{#if track.slug === 'disclosures'}
		<section class="disclosure-collection shell" aria-labelledby="disclosure-collection-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">{copy.disclosureCollectionEyebrow}</p>
					<h2 id="disclosure-collection-title">{copy.disclosureCollectionTitle}</h2>
				</div>
				<p>{copy.disclosureCollectionDescription}</p>
			</div>
			<div class="disclosure-document-grid">
				{#each disclosureDocuments as document (document.slug)}
					<a class="disclosure-document-card" href={resolve(document.href)}>
						<p class="eyebrow">{document.format}</p>
						<h3>{document.title}</h3>
						<p>{$locale === 'ko' ? document.descriptionKo : document.description}</p>
						<span class="text-link">{copy.disclosureArticleAction} <span aria-hidden="true">→</span></span>
					</a>
				{/each}
			</div>
		</section>
	{/if}
	<section class="page-body shell" aria-label={`${title} research topics`}>
		<div class="topic-grid">
			{#each topics as topic (topic.title)}
				<ResearchTopicCard {topic} statusLabel={$locale === 'ko' ? researchStatusKo[topic.status] : topic.status} />
			{/each}
		</div>
		<aside class="method-panel" aria-labelledby="method-title">
			<div>
				<p class="eyebrow">{copy.methodology}</p>
				<h2 id="method-title">{copy.methodTitle}</h2>
			</div>
			<p>{method}</p>
		</aside>
		<div class="page-back"><a class="text-link" href={resolve('/')}>← {copy.backHome}</a></div>
	</section>
</main>