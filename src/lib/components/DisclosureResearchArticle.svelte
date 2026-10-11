<script lang="ts">
	import { resolve } from '$app/paths';
	import { marked } from 'marked';
	import sanitizeHtml from 'sanitize-html';
	import { locale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import type { DisclosureDocument } from '#lib/content/disclosure-documents.js';

	let { article, markdown }: { article: DisclosureDocument; markdown: string } = $props();
	const copy = $derived(siteCopy[$locale].track);
	const articleCopy = $derived($locale === 'ko'
		? { description: article.pageDescriptionKo, note: article.noteKo }
		: { description: article.pageDescription, note: article.note });
	const articleBody = $derived(markdown.replace(/^#[^\r\n]*\r?\n(?:\r?\n##[^\r\n]*\r?\n)?/, ''));
	const articleHtml = $derived(sanitizeHtml(marked.parse(articleBody, { async: false }) as string, {
		allowedTags: [...sanitizeHtml.defaults.allowedTags, 'table', 'thead', 'tbody', 'tr', 'th', 'td'],
		allowedAttributes: {
			...sanitizeHtml.defaults.allowedAttributes,
			a: ['href', 'name', 'target', 'rel'],
			th: ['align'],
			td: ['align']
		},
		allowedSchemes: ['http', 'https', 'mailto']
	}));
</script>

<svelte:head>
	<title>{article.title} | ASMR</title>
	<meta name="description" content={articleCopy.description} />
</svelte:head>

<main class="research-page">
	<section class="page-intro">
		<div class="shell">
			<p class="eyebrow">{article.format} · English original</p>
			<h1>{article.title}</h1>
			<p class="intro-copy">{articleCopy.description}</p>
			<p class="article-caveat">{articleCopy.note}</p>
		</div>
	</section>

	<article class="page-body shell article-body">
		<!-- eslint-disable-next-line svelte/no-at-html-tags -->
		<div class="article-content">{@html articleHtml}</div>
		<div class="page-back"><a class="text-link" href={resolve('disclosures/')}>← {copy.backHome}</a></div>
	</article>
</main>
