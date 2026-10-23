<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import { researchGroupsKo, researchSourceCopyKo, weeklyRoutineKo } from '#lib/content/institutional-research-ko.js';
	import {
		researchSources,
		researchSourceGroups,
		weeklyReadingRoutine
	} from '#lib/content/institutional-research.js';
	import type { ResearchSource } from '#lib/content/institutional-research.js';
	import rawRadar from '#lib/content/research-radar.json';

	type InstitutionalItem = { id: string; title: string; url: string; sourceId: string; publishedAt: string | null; detectedAt: string | null; excerpt: string };
	type Paper = { id: string; title: string; url: string; topics: string[]; indexedAt: string; abstract: string };
	type Repo = { id: string; name: string; url: string; stars: number; stars7d: number | null; description: string };
	const radar: {
		lastCheckedAt: string | null;
		sourceErrors: string[];
		institutional: InstitutionalItem[];
		ssrn: Paper[];
		github: Repo[];
		weekly: { start: string | null; institutionalIds: string[]; ssrnIds: string[]; githubIds: string[] };
	} = rawRadar;
	const institutions = $derived(radar.weekly.institutionalIds.map((id) => radar.institutional.find((x: InstitutionalItem) => x.id === id)).filter((x): x is InstitutionalItem => !!x));
	const papers = $derived(radar.weekly.ssrnIds.map((id) => radar.ssrn.find((x: Paper) => x.id === id)).filter((x): x is Paper => !!x));
	const repos = $derived(radar.weekly.githubIds.map((id) => radar.github.find((x: Repo) => x.id === id)).filter((x): x is Repo => !!x));

	const sourcesById = new Map(researchSources.map((source) => [source.id, source]));
	const findSource = (id: string): ResearchSource => {
		const source = sourcesById.get(id);
		if (!source) throw new Error(`Unknown research source: ${id}`);
		return source;
	};
	const copy = $derived(siteCopy[$locale].library);
	const weekdays: Record<string, string> = $derived(siteCopy[$locale].weekdays);
</script>

<svelte:head>
	<title>{copy.title} | Asia Stock Market Research (ASMR)</title>
	<meta
		name="description"
		content={copy.description}
	/>
</svelte:head>

<main class="research-page">
	<section class="page-intro">
		<div class="shell">
			<p class="eyebrow">{copy.eyebrow}</p>
			<h1>{copy.title}</h1>
			<p class="intro-copy">{copy.description}</p>
		</div>
	</section>

	<div class="page-body shell">
		<section class="resource-group research-radar" aria-labelledby="radar-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">RESEARCH RADAR · {radar.weekly.start ?? 'AWAITING FIRST SCAN'}</p>
					<h2 id="radar-title">{$locale === 'ko' ? '지난주 리서치 레이더' : 'Weekly research radar'}</h2>
				</div>
				<p>{$locale === 'ko' ? '지난 홍콩 주간(월~일)에 발견한 공개 자료와 최근 별 수가 늘어난 퀀트 저장소입니다.' : 'Public research found in the last completed Hong Kong week, plus quant repositories gaining stars.'}</p>
			</div>
			{#if !radar.lastCheckedAt}
				<p class="radar-empty">{$locale === 'ko' ? '첫 번째 자동 수집이 완료되면 이곳에 목록이 나타납니다.' : 'The first scheduled scan will populate this section.'}</p>
			{:else}
				<div class="radar-columns">
					<div class="radar-column">
						<h3>{$locale === 'ko' ? '기관 리서치' : 'Institutional research'}</h3>
						{#each institutions as item (item.id)}
							<article><a href={item.url} target="_blank" rel="external noreferrer">{item.title} ↗</a><small>{item.sourceId} · {(item.publishedAt ?? item.detectedAt ?? '').slice(0, 10)}</small>{#if item.excerpt}<p>{item.excerpt}</p>{/if}</article>
						{:else}<p class="radar-empty">{$locale === 'ko' ? '이번 기간 새로 확인된 자료가 없습니다.' : 'No new items in this period.'}</p>{/each}
					</div>
					<div class="radar-column">
						<h3>SSRN · {$locale === 'ko' ? '퀀트 논문' : 'Quant papers'}</h3>
						{#each papers as paper (paper.id)}
							<article><a href={paper.url} target="_blank" rel="external noreferrer">{paper.title} ↗</a><small>{paper.topics.join(', ')} · {paper.indexedAt.slice(0, 10)}</small>{#if paper.abstract}<p>{paper.abstract}</p>{/if}</article>
						{:else}<p class="radar-empty">{$locale === 'ko' ? '이번 기간 확인된 논문이 없습니다.' : 'No indexed papers in this period.'}</p>{/each}
					</div>
					<div class="radar-column">
						<h3>GitHub · {$locale === 'ko' ? '별 상승' : 'Star growth'}</h3>
						{#each repos as repo (repo.id)}
							<article><a href={repo.url} target="_blank" rel="external noreferrer">{repo.name} ↗</a><small>★ {repo.stars.toLocaleString()} · +{repo.stars7d} {$locale === 'ko' ? '최근 7일' : 'last 7 days'}</small>{#if repo.description}<p>{repo.description}</p>{/if}</article>
						{:else}<p class="radar-empty">{$locale === 'ko' ? '7일 별 수 비교가 쌓이는 중입니다. 첫 주에는 증가량을 표시하지 않습니다.' : 'Collecting a seven-day star baseline. Growth appears after the first week.'}</p>{/each}
					</div>
				</div>
				<p class="radar-method">{$locale === 'ko' ? '제목·발췌는 제공된 공개 메타데이터에 한정됩니다. SSRN 날짜는 DOI 등록일이며 게시일과 다를 수 있습니다. GitHub 증가량은 추적 중인 저장소의 관측값입니다. 원문을 열어 주장과 방법론을 확인하세요.' : 'Titles and excerpts come from public metadata only. SSRN dates are DOI registration dates and can differ from posting dates. GitHub growth uses observed snapshots of tracked repos. Open the original to verify claims and methods.'}</p>
				{#if radar.sourceErrors.length}<p class="radar-method">{$locale === 'ko' ? `${radar.sourceErrors.length}개 출처를 마지막 실행에서 확인하지 못해 기존 자료를 유지했습니다.` : `${radar.sourceErrors.length} source checks failed on the last run; previous records were retained.`}</p>{/if}
			{/if}
		</section>

		{#each researchSourceGroups as group, groupIndex (group.title)}
			{@const groupCopy = $locale === 'ko' ? researchGroupsKo[groupIndex] : group}
			<section id={group.anchor} class="resource-group" aria-label={groupCopy.title}>
				<div class="resource-group-heading">
					<div>
						<p class="eyebrow">{String(groupIndex + 1).padStart(2, '0')} · {copy.groupsEyebrow}</p>
						<h2>{groupCopy.title}</h2>
					</div>
					<p>{groupCopy.description}</p>
				</div>
				<div class="resource-grid">
					{#each group.sourceIds as sourceId (sourceId)}
						{@const source = findSource(sourceId)}
						{@const sourceCopy = $locale === 'ko' ? researchSourceCopyKo[sourceId] : undefined}
						<article class="resource-card">
							<h3><a href={source.url} target="_blank" rel="external noreferrer">{source.name} <span aria-hidden="true">↗</span></a></h3>
							<p>{sourceCopy?.description ?? source.description}</p>
							<div class="resource-meta">
								<span>{sourceCopy?.cadence ?? source.cadence}</span>
								{#if source.access}<span>{sourceCopy?.access ?? source.access}</span>{/if}
							</div>
						</article>
					{/each}
				</div>
			</section>
		{/each}

		<section class="resource-group" aria-labelledby="routine-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">{copy.routineEyebrow}</p>
					<h2 id="routine-title">{copy.routineTitle}</h2>
				</div>
				<p>{copy.routineNote}</p>
			</div>
			<div class="reading-routine">
				{#each weeklyReadingRoutine as day, dayIndex (day.day)}
					<article class="reading-day">
						<p class="eyebrow">{weekdays[day.day]}</p>
						<h3>{$locale === 'ko' ? weeklyRoutineKo[dayIndex] : day.theme}</h3>
						<ul>
							{#each day.sourceIds as sourceId (sourceId)}
								<li><a href={findSource(sourceId).url} target="_blank" rel="external noreferrer">{findSource(sourceId).name}</a></li>
							{/each}
						</ul>
					</article>
				{/each}
			</div>
		</section>

		<section class="resource-group" aria-labelledby="framework-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">{copy.frameworkEyebrow}</p>
					<h2 id="framework-title">{copy.frameworkTitle}</h2>
				</div>
			</div>
			<ul class="framework-list">
				{#each copy.framework as item (item.title)}
					<li><strong>{item.title}</strong><span>{item.description}</span></li>
				{/each}
			</ul>
			<aside class="method-panel" aria-label="Applying institutional research to Asia">
				<div>
					<p class="eyebrow">{copy.asiaEyebrow}</p>
					<h2>{copy.asiaTitle}</h2>
				</div>
				<p>{copy.asiaBody}</p>
			</aside>
		</section>

		<div class="page-back"><a class="text-link" href={resolve('/')}>← {copy.backHome}</a></div>
	</div>
</main>
