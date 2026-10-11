<script lang="ts">
	import DisclosureResearchArticle from '#lib/components/DisclosureResearchArticle.svelte';
	import { getDisclosureDocument } from '#lib/content/disclosure-documents.js';
	import articleMarkdown from '#lib/content/asia_disclosure_linkedin_tables.md?raw';

	const article = getDisclosureDocument('linkedin-tables');
</script>

<DisclosureResearchArticle {article} markdown={articleMarkdown} />