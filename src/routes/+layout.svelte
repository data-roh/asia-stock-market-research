<script lang="ts">
	import { onMount } from 'svelte';
	import { asset, resolve } from '$app/paths';
	import { locale, setLocale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import '../app.css';
	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();
	const copy = $derived(siteCopy[$locale]);
	const navigation = [
		{ key: 'about', label: 'about', href: 'about/' },
		{ key: 'weekly', label: 'weekly', anchor: 'weekly-briefing' },
		{ key: 'knowledge', label: 'knowledge', anchor: 'market-knowledge' },
		{ key: 'library', label: 'library', href: 'institutional-research/' }
	] as const;

	function navigateToSection(event: MouseEvent, anchor: string): void {
		event.preventDefault();
		window.location.assign(`${resolve('/')}#${anchor}`);
	}

	onMount(() => {
		const saved = window.localStorage.getItem('asmr-locale');
		if (saved === 'en' || saved === 'ko') locale.set(saved);

		return locale.subscribe((value) => {
			document.documentElement.lang = value;
			window.localStorage.setItem('asmr-locale', value);
		});
	});
</script>

<svelte:head>
	<link rel="icon" href={asset('favicon.svg')} type="image/svg+xml" />
</svelte:head>

<header class="site-header">
	<div class="shell header-inner">
		<a class="brand" href={resolve('/')} aria-label="Asia Stock Market Research home">
			<span class="brand-mark" aria-hidden="true">A<span>SMR</span></span>
			<span class="brand-name">Asia Stock Market Research</span>
		</a>
		<nav aria-label={copy.nav.primary}>
			<ul class="nav-links">
				{#each navigation as item (item.key)}
					<li>
						{#if 'href' in item}
							<a href={resolve(item.href)}>{copy.nav[item.label]}</a>
						{:else}
							<a href={resolve('/')} onclick={(event) => navigateToSection(event, item.anchor)}>{copy.nav[item.label]}</a>
						{/if}
					</li>
				{/each}
			</ul>
		</nav>
		<div class="header-actions">
			<div class="language-switch" role="group" aria-label="Language">
				<button class:active={$locale === 'en'} aria-label={copy.nav.switchToEnglish} aria-pressed={$locale === 'en'} onclick={() => setLocale('en')}>
					<span aria-hidden="true">🇺🇸</span> EN
				</button>
				<button class:active={$locale === 'ko'} aria-label={copy.nav.switchToKorean} aria-pressed={$locale === 'ko'} onclick={() => setLocale('ko')}>
					<span aria-hidden="true">🇰🇷</span> KO
				</button>
			</div>
			<a class="header-index" href={resolve('/')}>ASMR <span>01</span></a>
		</div>
	</div>
</header>

{@render children()}

<footer class="site-footer">
	<div class="shell footer-inner">
		<a class="footer-brand" href={resolve('/')}>Asia Stock Market Research</a>
		<p>{copy.footer.description}</p>
		<span>{copy.footer.data}</span>
	</div>
</footer>
