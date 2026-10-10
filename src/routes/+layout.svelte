<script lang="ts">
	import { asset, resolve } from '$app/paths';
	import '../app.css';
	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();
	const navigation = [
		{ label: 'Disclosures', href: 'disclosures/' },
		{ label: 'Core Concepts', href: 'core-concepts/' },
		{ label: 'Market Overlay', href: 'market-overlay/' },
		{ label: 'Quant', href: 'quant/' },
		{ label: 'Research Library', href: 'institutional-research/' }
	] as const;
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
		<nav aria-label="Primary navigation">
			<ul class="nav-links">
				{#each navigation as item (item.href)}
					<li><a href={resolve(item.href)}>{item.label}</a></li>
				{/each}
			</ul>
		</nav>
		<a class="header-index" href={resolve('/')}>ASMR <span>01</span></a>
	</div>
</header>

{@render children()}

<footer class="site-footer">
	<div class="shell footer-inner">
		<a class="footer-brand" href={resolve('/')}>Asia Stock Market Research</a>
		<p>Independent research on Asian markets and financial institutions.</p>
		<span>© 2026 · Synthetic demo data only</span>
	</div>
</footer>
