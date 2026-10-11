<script lang="ts">
	import DisclosureResearchArticle from '#lib/components/DisclosureResearchArticle.svelte';
	import { getDisclosureDocument } from '#lib/content/disclosure-documents.js';
	import articleMarkdown from '#lib/content/asia_stock_review_disclosure_systems.md?raw';

	const article = getDisclosureDocument('taxonomy');
</script>

<DisclosureResearchArticle {article} markdown={articleMarkdown} />