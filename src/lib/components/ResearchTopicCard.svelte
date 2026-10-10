<script lang="ts">
	import type { ResearchTopic } from '#lib/content/research-tracks.js';

	let { topic }: { topic: ResearchTopic } = $props();
</script>

<article class="topic-card">
	<span class="topic-status">{topic.status}</span>
	<h2>{topic.title}</h2>
	<p>{topic.description}</p>
</article>