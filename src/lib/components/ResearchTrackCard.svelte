<script lang="ts">
	import { resolve } from '$app/paths';
	import type { ResearchTrack } from '#lib/content/research-tracks.js';

	let { track, number }: { track: ResearchTrack; number: string } = $props();
	const topicPreview = $derived(track.topics.slice(0, 3).map((topic) => topic.title).join(' · '));
</script>

<a class="track-card" href={resolve(track.path)}>
	<div class="track-number"><span>TRACK {number}</span><span>{track.topics.length} TOPICS</span></div>
	<h3>{track.title}</h3>
	<p>{track.shortDescription}</p>
	<div class="track-topics">{topicPreview}</div>
	<span class="track-arrow" aria-hidden="true">Explore track →</span>
</a>