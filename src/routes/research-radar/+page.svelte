<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
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
	const institutions = radar.weekly.institutionalIds.map((id) => radar.institutional.find((item) => item.id === id)).filter((item): item is InstitutionalItem => !!item);
	const papers = radar.weekly.ssrnIds.map((id) => radar.ssrn.find((item) => item.id === id)).filter((item): item is Paper => !!item);
	const repos = radar.weekly.githubIds.map((id) => radar.github.find((item) => item.id === id)).filter((item): item is Repo => !!item);
</script>

<svelte:head>
	<title>Research Radar | Asia Stock Market Research (ASMR)</title>
	<meta name="description" content="A weekly reading desk for institutional research, SSRN quant papers, and GitHub repositories gaining stars." />
</svelte:head>

<main class="research-page">
	<section class="page-intro">
		<div class="shell">
			<p class="eyebrow">ASMR · RESEARCH RADAR</p>
			<h1>{$locale === 'ko' ? '주간 리서치 레이더' : 'Weekly Research Radar'}</h1>
			<p class="intro-copy">{$locale === 'ko' ? '기관 리서치, SSRN 퀀트 논문, GitHub 프로젝트의 변화를 매주 한눈에 살펴봅니다.' : 'A weekly reading desk for institutional research, SSRN quant papers, and GitHub projects.'}</p>
		</div>
	</section>

	<div class="page-body shell">
		<section class="resource-group research-radar" aria-labelledby="radar-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">{$locale === 'ko' ? '홍콩 시간 기준 월요일–일요일' : 'Monday–Sunday · Hong Kong time'}</p>
					<h2 id="radar-title">{radar.weekly.start ?? ($locale === 'ko' ? '첫 수집 대기 중' : 'Awaiting first scan')}</h2>
				</div>
				<p>{$locale === 'ko' ? '지난주 발견한 공개 자료와 최근 7일 별 수가 늘어난 저장소입니다.' : 'Public material from the last completed week and tracked repositories gaining stars in the last seven days.'}</p>
			</div>
			{#if !radar.lastCheckedAt}
				<p class="radar-empty">{$locale === 'ko' ? '첫 번째 자동 수집이 완료되면 이곳에 목록이 나타납니다.' : 'The first scheduled scan will populate this page.'}</p>
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
							<article><a href={repo.url} target="_blank" rel="external noreferrer">{repo.name} ↗</a><small>★ {repo.stars.toLocaleString()} · {repo.stars7d === null ? ($locale === 'ko' ? '기준 별 수 수집 중' : 'building baseline') : `+${repo.stars7d} ${$locale === 'ko' ? '최근 7일' : 'last 7 days'}`}</small>{#if repo.description}<p>{repo.description}</p>{/if}</article>
						{:else}<p class="radar-empty">{$locale === 'ko' ? '7일 별 수 비교가 쌓이는 중입니다. 첫 주에는 증가량을 표시하지 않습니다.' : 'Collecting a seven-day star baseline. Growth appears after the first week.'}</p>{/each}
					</div>
				</div>
				<p class="radar-method">{$locale === 'ko' ? '제목·발췌는 공개 메타데이터에 한정됩니다. SSRN 날짜는 DOI 등록일이며 게시일과 다를 수 있습니다. GitHub 별 증가량은 오늘과 정확히 7일 전의 홍콩 날짜 스냅샷이 모두 있는 저장소만 표시합니다. 원문에서 주장과 방법론을 확인하세요.' : 'Titles and excerpts come from public metadata only. SSRN dates are DOI registration dates and can differ from posting dates. GitHub star deltas appear only for repositories with both today’s and the exact seven-day-old Hong Kong-date snapshots. Open the original to verify claims and methods.'}</p>
				{#if radar.sourceErrors.length}<p class="radar-method">{$locale === 'ko' ? `${radar.sourceErrors.length}개 출처를 마지막 실행에서 확인하지 못해 기존 자료를 유지했습니다.` : `${radar.sourceErrors.length} source checks failed on the last run; previous records were retained.`}</p>{/if}
			{/if}
		</section>
		<div class="page-back"><a class="text-link" href={resolve('institutional-research/')}>← {$locale === 'ko' ? '리서치 라이브러리' : 'Institutional Research Library'}</a></div>
	</div>
</main>
