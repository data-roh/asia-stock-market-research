<script lang="ts">
	import { resolve } from '$app/paths';
	import ResearchTopicCard from '#lib/components/ResearchTopicCard.svelte';
	import type { ResearchTrack } from '#lib/content/research-tracks.js';

	let { track }: { track: ResearchTrack } = $props();
</script>

<svelte:head>
	<title>{track.title} | Asia Stock Market Research (ASMR)</title>
	<meta name="description" content={track.metaDescription} />
</svelte:head>

<main class="research-page">
	<section class="page-intro">
		<div class="shell">
			<p class="eyebrow">{track.eyebrow}</p>
			<h1>{track.title}</h1>
			<p class="intro-copy">{track.description}</p>
		</div>
	</section>
	<section class="page-body shell" aria-label={`${track.title} research topics`}>
		<div class="topic-grid">
			{#each track.topics as topic (topic.title)}
				<ResearchTopicCard {topic} />
			{/each}
		</div>
		<aside class="method-panel" aria-labelledby="method-title">
			<div>
				<p class="eyebrow">Methodology</p>
				<h2 id="method-title">A careful comparison, not a shortcut.</h2>
			</div>
			<p>{track.method}</p>
		</aside>
		<div class="page-back"><a class="text-link" href={resolve('/')}>← Back to ASMR home</a></div>
	</section>
</main>