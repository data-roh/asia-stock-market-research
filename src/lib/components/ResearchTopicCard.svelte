<script lang="ts">
	import type { ResearchTopic } from '#lib/content/research-tracks.js';

	let { topic, statusLabel }: { topic: ResearchTopic; statusLabel: string } = $props();
</script>

<article class="topic-card">
	<span class="topic-status">{statusLabel}</span>
	<h2>{topic.title}</h2>
	<p>{topic.description}</p>
</article>