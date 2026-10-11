<script lang="ts">
	import DisclosureResearchArticle from '#lib/components/DisclosureResearchArticle.svelte';
	import { getDisclosureDocument } from '#lib/content/disclosure-documents.js';
	import articleMarkdown from '#lib/content/asia_disclosure_systems_DETAIL_EN.md?raw';

	const article = getDisclosureDocument('taxonomy-detail');
</script>

<DisclosureResearchArticle {article} markdown={articleMarkdown} />