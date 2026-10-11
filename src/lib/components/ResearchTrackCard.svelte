<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import { researchTracksKo } from '#lib/content/research-tracks-ko.js';
	import type { ResearchTrack } from '#lib/content/research-tracks.js';

	let { track, number }: { track: ResearchTrack; number: string } = $props();
	const koreanTrack = $derived($locale === 'ko' ? researchTracksKo[track.slug as keyof typeof researchTracksKo] : undefined);
	const title = $derived(koreanTrack?.title ?? track.title);
	const shortDescription = $derived(koreanTrack?.shortDescription ?? track.shortDescription);
	const topicPreview = $derived((koreanTrack?.topics ?? track.topics).slice(0, 3).map((topic) => topic.title).join(' · '));
	const copy = $derived(siteCopy[$locale].track);
</script>

<a class="track-card" href={resolve(track.path)}>
	<div class="track-number"><span>{copy.track} {number}</span><span>{track.topics.length} {copy.topics}</span></div>
	<h3>{title}</h3>
	<p>{shortDescription}</p>
	<div class="track-topics">{topicPreview}</div>
	<span class="track-arrow" aria-hidden="true">{copy.explore} →</span>
</a>