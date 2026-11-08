<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
	import rawRadar from '#lib/content/research-radar.json';
	import researchFeeds from '#lib/content/research-feeds.json';
	import { researchSources } from '#lib/content/institutional-research.js';

	type Verification = {
		status: 'VERIFIED_NEW' | 'VERIFIED_EXISTING' | 'POSSIBLE_NEW' | 'UNVERIFIED' | 'UPDATED_EXISTING' | 'REMOVED';
		confidence?: 'HIGH' | 'MEDIUM' | 'LOW';
		verifiedAt?: string;
		officialDomain?: boolean;
		listingPageMatch?: boolean;
		articlePageMatch?: boolean;
		titleMatch?: boolean;
		dateFound?: boolean;
		publishedAt?: string;
		reason?: string;
	};
	type InstitutionalItem = {
		id: string;
		title: string;
		url: string;
		sourceId: string;
		publishedAt: string | null;
		detectedAt: string | null;
		firstSeenAt?: string | null;
		excerpt: string;
		verification?: Verification;
		topics?: string[];
		regions?: string[];
		asiaRelevance?: number | null;
		researchPriority?: number | null;
		contentType?: string;
		summaryBasis?: string;
		asmrCandidate?: boolean;
		asmrReason?: string;
	};
	type Paper = { id: string; title: string; url: string; topics: string[]; indexedAt: string; abstract: string };
	type Repo = { id: string; name: string; url: string; stars: number; stars7d: number | null; description: string };
	type SourceCheck = { sourceId: string; method?: string; ok: boolean; error?: string | null };
	type VerificationRun = {
		completedAt: string;
		candidateCount: number;
		verifiedNewCount: number;
		verifiedExistingCount: number;
		needsReviewCount: number;
		unverifiedCount: number;
	};
	const radar: {
		lastCheckedAt: string | null;
		lastVerificationAt?: string | null;
		verificationRun?: VerificationRun | null;
		sourceErrors: string[];
		sourceChecks?: SourceCheck[];
		institutional: InstitutionalItem[];
		ssrn: Paper[];
		github: Repo[];
		weekly: { start: string | null; institutionalIds: string[]; ssrnIds: string[]; githubIds: string[] };
	} = rawRadar;
	const sourceNames = new Map(researchSources.map((source) => [source.id, source.name]));
	let search = $state('');
	let sourceFilter = $state('all');
	let typeFilter = $state('all');
	let regionFilter = $state('all');
	let topicFilter = $state('all');
	let statusFilter = $state('all');
	let timeFilter = $state('7');
	let minimumAsia = $state('0');
	let minimumPriority = $state('0');
	let showOtherFeeds = $state(false);

	const sourceOptions = researchSources.map((source) => source.id).sort();
	const typeOptions = [...new Set([
		'Research Article', 'Research Report', 'Market Commentary', 'Memo', 'White Paper',
		'Podcast', 'Video', 'Weekly Outlook', 'Monthly Outlook', 'Quarterly Outlook',
		'Investment Outlook', 'Research PDF', 'Interview'
	])].sort();
	const regionOptions = [...new Set([
		'Asia', 'China', 'Japan', 'Korea', 'Taiwan', 'Hong Kong', 'India',
		'Singapore', 'Australia', 'Global', ...radar.institutional.flatMap((item) => item.regions ?? [])
	])].sort();
	const topicOptions = [...new Set([
		'Macro', 'Equities', 'Rates', 'Credit', 'FX', 'Commodities', 'Volatility',
		'Options', 'Market Structure', 'Quant', 'Factors', 'Systematic Investing',
		'Asset Allocation', 'Private Markets', 'Private Credit', 'Real Estate',
		'Earnings', 'Valuation', 'Positioning', 'Flows', 'Liquidity', 'ETF',
		'AI', 'Technology', 'Semiconductors', 'Banks', 'Insurance', 'Asia',
		...radar.institutional.flatMap((item) => item.topics ?? [])
	])].sort();
	const configuredSourceIds = new Set([
		...researchFeeds.feeds.map((item) => item.sourceId),
		...researchFeeds.pages.map((item) => item.sourceId)
	]);
	const unresolvedCount = radar.institutional.filter(
		(item) => !['VERIFIED_NEW', 'VERIFIED_EXISTING'].includes(item.verification?.status ?? 'UNVERIFIED')
	).length;
	const hasVerificationRun = Boolean(radar.verificationRun || radar.lastVerificationAt);
	const filteredInstitutions = $derived(
		radar.institutional
			.filter((item) => {
				const status = item.verification?.status ?? 'UNVERIFIED';
				const dateValue = item.publishedAt ?? item.firstSeenAt ?? item.detectedAt;
				const ageDays = dateValue ? (Date.now() - new Date(dateValue).getTime()) / 86_400_000 : Number.POSITIVE_INFINITY;
				return (
					(!search || `${item.title} ${item.sourceId} ${item.excerpt}`.toLowerCase().includes(search.toLowerCase())) &&
					(sourceFilter === 'all' || item.sourceId === sourceFilter) &&
					(typeFilter === 'all' || item.contentType === typeFilter) &&
					(regionFilter === 'all' || item.regions?.includes(regionFilter)) &&
					(topicFilter === 'all' || item.topics?.includes(topicFilter)) &&
					(statusFilter === 'all' || status === statusFilter) &&
					(timeFilter === 'all' || ageDays <= Number(timeFilter)) &&
					(item.asiaRelevance ?? 0) >= Number(minimumAsia) &&
					(item.researchPriority ?? 0) >= Number(minimumPriority)
				);
			})
			.sort((a, b) => {
				const priority = (b.researchPriority ?? -1) - (a.researchPriority ?? -1);
				if (priority !== 0) return priority;
				return (b.publishedAt ?? b.firstSeenAt ?? b.detectedAt ?? '').localeCompare(
					a.publishedAt ?? a.firstSeenAt ?? a.detectedAt ?? ''
				);
			})
	);
	const sourceErrors = radar.sourceChecks?.filter((check) => !check.ok) ?? [];
	const confidenceLabel = (confidence?: string) => {
		if ($locale !== 'ko') return confidence ?? 'LOW';
		return confidence === 'HIGH' ? '높음' : confidence === 'MEDIUM' ? '보통' : '낮음';
	};
	const dateLabel = (value?: string | null) => {
		const unknownDate = $locale === 'ko' ? '날짜 미확인' : 'Date unknown';
		if (!value) return unknownDate;
		const date = new Date(value);
		return Number.isNaN(date.valueOf())
			? unknownDate
			: date.toLocaleDateString($locale === 'ko' ? 'ko-KR' : 'en-US', { year: 'numeric', month: 'short', day: 'numeric' });
	};
	const verificationDateLabel = (value?: string | null) =>
		value ? dateLabel(value) : $locale === 'ko' ? '실행 전' : 'Not run';
	const evidenceValue = (value?: boolean) =>
		value ? ($locale === 'ko' ? '예' : 'Yes') : ($locale === 'ko' ? '미확인' : 'Not confirmed');
	const statusLabel = (status?: string) => {
		if ($locale === 'ko') {
			return ({
				VERIFIED_NEW: '신규 검증',
				VERIFIED_EXISTING: '기존 자료 확인',
				POSSIBLE_NEW: '확인 필요',
				UPDATED_EXISTING: '기존 자료 업데이트',
				REMOVED: '삭제됨',
				UNVERIFIED: '미검증'
			} as Record<string, string>)[status ?? ''] ?? '미검증';
		}
		return (status ?? 'UNVERIFIED').replaceAll('_', ' ');
	};
</script>

<svelte:head>
	<title>Research Radar | Asia Stock Market Research (ASMR)</title>
	<meta name="description" content="Verified institutional research, source evidence, and Asia-market relevance in one research desk." />
</svelte:head>

<main class="research-page">
	<section class="page-intro radar-intro">
		<div class="shell">
			<p class="eyebrow">ASMR · RESEARCH INTELLIGENCE</p>
			<h1>{$locale === 'ko' ? '리서치 레이더' : 'Research Radar'}</h1>
			<p class="intro-copy">
				{$locale === 'ko'
					? '새 자료의 발견과 공식 출처 검증을 구분합니다. 검증 상태와 근거를 확인하고, 아시아 시장에 의미 있는 자료를 우선 살펴보세요.'
					: 'Discovery is separated from official-source verification. Review the evidence, then prioritize research relevant to Asian markets.'}
			</p>
			<div class="radar-meta">
				<span>{$locale === 'ko' ? '마지막 수집' : 'Last scan'} · {dateLabel(radar.lastCheckedAt)}</span>
				<span>{$locale === 'ko' ? '마지막 검증' : 'Last verification'} · {verificationDateLabel(radar.lastVerificationAt)}</span>
				<a href={resolve('institutional-research/')}>{$locale === 'ko' ? '출처 라이브러리 보기 →' : 'Browse source library →'}</a>
			</div>
		</div>
	</section>

	<div class="page-body shell">
		<section class="radar-overview" aria-label={$locale === 'ko' ? '레이더 요약' : 'Radar overview'}>
			<article>
				<span>{$locale === 'ko' ? '이번 실행에서 신규 확인' : 'Verified new this run'}</span>
				<strong>
					{radar.verificationRun
						? radar.verificationRun.verifiedNewCount
						: hasVerificationRun ? '—' : ($locale === 'ko' ? '미실행' : 'Not run')}
				</strong>
				{#if radar.verificationRun}
					<small>
						{$locale === 'ko'
							? `검증 대상 ${radar.verificationRun.candidateCount}건 · 확인 필요 ${radar.verificationRun.needsReviewCount}건`
							: `${radar.verificationRun.candidateCount} candidates · ${radar.verificationRun.needsReviewCount} need review`}
					</small>
				{:else if hasVerificationRun}
					<small>{$locale === 'ko' ? '실행 기록은 있으나 상세 집계 데이터가 없습니다' : 'Run recorded; detailed counts unavailable'}</small>
				{/if}
			</article>
			<article><span>{$locale === 'ko' ? '확인 필요·미검증' : 'Needs review / unverified'}</span><strong>{unresolvedCount}</strong></article>
			<article><span>{$locale === 'ko' ? '설정된 추적 출처' : 'Configured sources'}</span><strong>{configuredSourceIds.size}</strong></article>
			<article><span>{$locale === 'ko' ? '확인 실패 출처' : 'Source check failures'}</span><strong>{radar.sourceChecks ? sourceErrors.length : '—'}</strong></article>
		</section>
		<p class="radar-run-note">
			{$locale === 'ko'
				? '매일 자동으로 출처를 수집한 뒤 AQR·Citadel·Man Group·Apollo·Oaktree의 신규 후보를 공식 목록과 원문에서 확인합니다. 접근 실패나 제목 불일치는 “확인 필요”로 남고, 나머지 출처는 자동 검증 범위가 아닙니다.'
				: 'The daily job scans configured sources, then checks new candidates from AQR, Citadel, Man Group, Apollo, and Oaktree against official listings and article pages. Access failures or title mismatches stay in “Needs review”; other sources are outside automated verification for now.'}
		</p>

		<section class="resource-group radar-workspace" aria-labelledby="institutional-title">
			<div class="resource-group-heading">
				<div>
					<p class="eyebrow">{$locale === 'ko' ? '공식 페이지 근거 포함' : 'WITH OFFICIAL-PAGE EVIDENCE'}</p>
					<h2 id="institutional-title">{$locale === 'ko' ? '기관 리서치' : 'Institutional research'}</h2>
				</div>
				<p>
					{$locale === 'ko'
						? '“신규 검증”은 공식 목록과 원문 페이지에서 일치한 자료입니다. 나머지는 신규 사실로 단정하지 않습니다.'
						: '“Verified new” items matched both the official listing and article page. Other statuses are not presented as confirmed new research.'}
				</p>
			</div>

			<div class="radar-filters">
				<label>
					<span>{$locale === 'ko' ? '검색' : 'Search'}</span>
					<input bind:value={search} type="search" placeholder={$locale === 'ko' ? '제목, 출처, 요약' : 'Title, source, excerpt'} />
				</label>
				<label>
					<span>{$locale === 'ko' ? '기간' : 'Time range'}</span>
					<select bind:value={timeFilter}>
						<option value="1">{$locale === 'ko' ? '오늘' : 'Today'}</option>
						<option value="3">{$locale === 'ko' ? '최근 3일' : 'Last 3 days'}</option>
						<option value="7">{$locale === 'ko' ? '최근 7일' : 'Last 7 days'}</option>
						<option value="30">{$locale === 'ko' ? '최근 30일' : 'Last 30 days'}</option>
						<option value="all">{$locale === 'ko' ? '전체 보관 자료' : 'All archived items'}</option>
					</select>
				</label>
				<label>
					<span>{$locale === 'ko' ? '출처' : 'Institution'}</span>
					<select bind:value={sourceFilter}>
						<option value="all">{$locale === 'ko' ? '모든 출처' : 'All institutions'}</option>
						{#each sourceOptions as sourceId (sourceId)}
							<option value={sourceId}>{sourceNames.get(sourceId) ?? sourceId}</option>
						{/each}
					</select>
				</label>
				<label>
					<span>{$locale === 'ko' ? '주제' : 'Topic'}</span>
					<select bind:value={topicFilter}>
						<option value="all">{$locale === 'ko' ? '모든 주제' : 'All topics'}</option>
						{#each topicOptions as topic (topic)}
							<option value={topic}>{topic}</option>
						{/each}
					</select>
				</label>
				<label>
					<span>{$locale === 'ko' ? '검증 상태' : 'Verification'}</span>
					<select bind:value={statusFilter}>
						<option value="all">{$locale === 'ko' ? '모든 상태' : 'All statuses'}</option>
						<option value="VERIFIED_NEW">{$locale === 'ko' ? '신규 검증' : 'Verified new'}</option>
						<option value="VERIFIED_EXISTING">{$locale === 'ko' ? '기존 자료 확인' : 'Verified existing'}</option>
						<option value="POSSIBLE_NEW">{$locale === 'ko' ? '확인 필요' : 'Needs review'}</option>
						<option value="UNVERIFIED">{$locale === 'ko' ? '미검증' : 'Unverified'}</option>
					</select>
				</label>
				<label>
					<span>{$locale === 'ko' ? '콘텐츠 유형' : 'Content type'}</span>
					<select bind:value={typeFilter}>
						<option value="all">{$locale === 'ko' ? '모든 유형' : 'All types'}</option>
						{#each typeOptions as contentType (contentType)}<option value={contentType}>{contentType}</option>{/each}
					</select>
				</label>
				<label>
					<span>{$locale === 'ko' ? '지역' : 'Region'}</span>
					<select bind:value={regionFilter}>
						<option value="all">{$locale === 'ko' ? '모든 지역' : 'All regions'}</option>
						{#each regionOptions as region (region)}<option value={region}>{region}</option>{/each}
					</select>
				</label>
				<label>
					<span>{$locale === 'ko' ? '최소 아시아 관련성' : 'Minimum Asia relevance'}</span>
					<select bind:value={minimumAsia}>
						<option value="0">0+</option><option value="50">50+</option><option value="70">70+</option><option value="90">90+</option>
					</select>
				</label>
				<label>
					<span>{$locale === 'ko' ? '최소 연구 우선순위' : 'Minimum research priority'}</span>
					<select bind:value={minimumPriority}>
						<option value="0">0+</option><option value="60">60+</option><option value="80">80+</option><option value="90">90+</option>
					</select>
				</label>
			</div>

			<div class="radar-results-header">
				<p>{filteredInstitutions.length} {$locale === 'ko' ? '개 자료' : 'items'}</p>
				<p>{$locale === 'ko' ? '아시아 관련성과 연구 우선순위 순' : 'Sorted by Asia relevance and research priority'}</p>
			</div>

			<div class="radar-article-list">
				{#each filteredInstitutions as item (item.id)}
					{@const verification = item.verification}
					<article class="radar-article">
						<div class="radar-article-topline">
							<span class="radar-status" class:verified={verification?.status === 'VERIFIED_NEW'} class:review={verification?.status === 'POSSIBLE_NEW'}>
								{statusLabel(verification?.status)}
							</span>
							<span>{sourceNames.get(item.sourceId) ?? item.sourceId}</span>
							<span>{item.contentType ?? 'Research Article'}</span>
						</div>
						<h3><a href={item.url} target="_blank" rel="external noreferrer">{item.title} <span aria-hidden="true">↗</span></a></h3>
						<div class="radar-article-meta">
							<span>{$locale === 'ko' ? '발행일' : 'Published'} · {dateLabel(item.publishedAt)}</span>
							<span>{$locale === 'ko' ? '최초 발견' : 'First seen'} · {dateLabel(item.firstSeenAt ?? item.detectedAt)}</span>
							{#if verification?.confidence}<span>{$locale === 'ko' ? '신뢰도' : 'Confidence'} · {confidenceLabel(verification.confidence)}</span>{/if}
						</div>
						{#if item.excerpt}
							<p class="radar-excerpt">{item.excerpt}</p>
							{#if item.summaryBasis === 'official_metadata'}<small class="radar-summary-label">{$locale === 'ko' ? '발행사 공개 설명 기반 · AI 요약 아님' : 'Publisher description · not an AI-generated summary'}</small>{/if}
						{:else}
							<p class="radar-excerpt radar-unavailable">{$locale === 'ko' ? '공개 설명을 가져오지 못했습니다. 원문에서 내용을 확인하세요.' : 'No reliable public description was available. Read the original for details.'}</p>
						{/if}
						<div class="radar-tags">
							{#each item.topics ?? [] as topic (topic)}<span>{topic}</span>{/each}
							{#each item.regions ?? [] as region (region)}<span class="region-tag">{region}</span>{/each}
							{#if item.asiaRelevance !== null && item.asiaRelevance !== undefined}
								<span class="score-tag">{$locale === 'ko' ? '아시아 관련성' : 'Asia relevance'} {item.asiaRelevance}/100</span>
							{/if}
						</div>
						{#if item.asmrCandidate && item.asmrReason}
							<p class="radar-asmr"><strong>ASMR</strong> · {item.asmrReason}</p>
						{/if}
						<details class="radar-evidence">
							<summary>{$locale === 'ko' ? '신규 판정 근거' : 'Why is this marked as new?'}</summary>
							<dl>
								<div><dt>{$locale === 'ko' ? '공식 도메인' : 'Official domain'}</dt><dd>{evidenceValue(verification?.officialDomain)}</dd></div>
								<div><dt>{$locale === 'ko' ? '공식 목록에서 발견' : 'Found on official listing'}</dt><dd>{evidenceValue(verification?.listingPageMatch)}</dd></div>
								<div><dt>{$locale === 'ko' ? '원문 페이지 확인' : 'Article page checked'}</dt><dd>{evidenceValue(verification?.articlePageMatch)}</dd></div>
								<div><dt>{$locale === 'ko' ? '제목 일치' : 'Title match'}</dt><dd>{evidenceValue(verification?.titleMatch)}</dd></div>
								<div><dt>{$locale === 'ko' ? '발행일 확인' : 'Publication date found'}</dt><dd>{verification?.dateFound ? dateLabel(verification.publishedAt) : ($locale === 'ko' ? '미확인' : 'Unknown')}</dd></div>
								<div><dt>{$locale === 'ko' ? '검증 시각' : 'Verified at'}</dt><dd>{dateLabel(verification?.verifiedAt)}</dd></div>
							</dl>
							{#if verification?.reason}<p>{verification.reason}</p>{/if}
						</details>
					</article>
				{:else}
					<p class="radar-empty">
						{$locale === 'ko'
							? '선택한 조건에 맞는 자료가 없습니다. 기간이나 검증 필터를 바꿔보세요.'
							: 'No research matches these filters. Try a wider time range or another verification status.'}
					</p>
				{/each}
			</div>
			<p class="radar-caveat">
				{$locale === 'ko'
					? '요약 대신 발행사의 공개 설명을 표시합니다. 자동 분류 점수는 연구 보조 지표이며 투자 조언이 아닙니다. 검증을 통과하지 못한 출처는 신규 자료로 단정하지 않습니다.'
					: 'Publisher descriptions are shown instead of generated summaries. Automated classifications are research aids, not investment advice. Items that fail verification are not asserted to be new.'}
			</p>
		</section>

		<details class="radar-health">
			<summary>{$locale === 'ko' ? '출처 상태' : 'Source health'} · {radar.sourceChecks?.length ?? ($locale === 'ko' ? '아직 없음' : 'not yet reported')}</summary>
			<div class="radar-health-grid">
				{#each radar.sourceChecks ?? [] as check (check.sourceId)}
					<div class:health-failed={!check.ok}>
						<strong>{sourceNames.get(check.sourceId) ?? check.sourceId}</strong>
						<span>{check.ok ? (check.method ?? 'checked') : (check.error ?? 'check failed')}</span>
					</div>
				{:else}
					<p>{$locale === 'ko' ? '수집기에서 출처별 상태 정보를 제공하지 않았습니다.' : 'No per-source health data was provided by the collector.'}</p>
				{/each}
			</div>
			{#if sourceErrors.length}
				<p class="radar-caveat">{$locale === 'ko' ? '수집 실패는 새 글이 없다는 뜻이 아닙니다.' : 'A failed check does not mean that no new research was published.'}</p>
			{/if}
		</details>

		<details class="radar-other-feeds" bind:open={showOtherFeeds}>
			<summary>{$locale === 'ko' ? '보조 레이더 데이터' : 'Other radar feeds'}</summary>
			<div class="radar-columns">
				<div class="radar-column">
					<h3>SSRN · {$locale === 'ko' ? '퀀트 논문' : 'Quant papers'}</h3>
					{#each radar.weekly.ssrnIds as id (id)}
						{@const paper = radar.ssrn.find((entry) => entry.id === id)}
						{#if paper}<article><a href={paper.url} target="_blank" rel="external noreferrer">{paper.title} ↗</a><small>{paper.topics.join(', ')} · {dateLabel(paper.indexedAt)}</small>{#if paper.abstract}<p>{paper.abstract}</p>{/if}</article>{/if}
					{:else}<p class="radar-empty">{$locale === 'ko' ? '이번 주 확인된 논문이 없습니다.' : 'No papers in this period.'}</p>{/each}
				</div>
				<div class="radar-column">
					<h3>GitHub · {$locale === 'ko' ? '별 상승' : 'Star growth'}</h3>
					{#each radar.weekly.githubIds as id (id)}
						{@const repo = radar.github.find((entry) => entry.id === id)}
						{#if repo}<article><a href={repo.url} target="_blank" rel="external noreferrer">{repo.name} ↗</a><small>★ {repo.stars.toLocaleString()} · {repo.stars7d === null ? ($locale === 'ko' ? '기준치 수집 중' : 'building baseline') : `+${repo.stars7d} ${$locale === 'ko' ? '최근 7일' : 'last 7 days'}`}</small>{#if repo.description}<p>{repo.description}</p>{/if}</article>{/if}
					{:else}<p class="radar-empty">{$locale === 'ko' ? '7일 별 수 비교가 쌓이는 중입니다.' : 'Collecting seven-day star history.'}</p>{/each}
				</div>
			</div>
			<p class="radar-caveat">{$locale === 'ko' ? 'SSRN 날짜는 DOI 등록일일 수 있으며, GitHub 별 증가는 정확한 7일치 스냅샷이 있는 경우에만 표시합니다.' : 'SSRN dates may be DOI registration dates. GitHub growth is shown only when exact seven-day snapshots are available.'}</p>
		</details>

		<div class="page-back"><a class="text-link" href={resolve('institutional-research/')}>← {$locale === 'ko' ? '리서치 라이브러리' : 'Institutional Research Library'}</a></div>
	</div>
</main>
