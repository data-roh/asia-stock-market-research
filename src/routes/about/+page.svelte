<script lang="ts">
	import { resolve } from '$app/paths';
	import { locale } from '#lib/locale.js';
	import { siteCopy } from '#lib/content/site-copy.js';
	import { aboutProfiles } from '#lib/content/about-profile.js';
	import { researchMethods } from '#lib/content/research-methods.js';

	const profile = $derived(aboutProfiles[$locale]);
	const copy = $derived(siteCopy[$locale].track);
	const interestById = $derived(new Map(profile.interests.map((interest) => [interest.id, interest])));

	function navigateToInterest(event: MouseEvent, anchor?: string): void {
		if (!anchor) return;
		event.preventDefault();
		window.location.assign(`${resolve('institutional-research/')}#${anchor}`);
	}
</script>

<svelte:head>
	<title>{profile.name} | About Me · ASMR</title>
	<meta name="description" content={profile.intro} />
</svelte:head>

<main class="research-page">
	<section class="page-intro">
		<div class="shell about-intro">
			<div>
				<p class="eyebrow">{profile.eyebrow} · {profile.location}</p>
				<h1>{profile.name}</h1>
				<p class="about-role">{profile.role}</p>
				<p class="intro-copy">{profile.intro}</p>
				<div class="profile-links" aria-label="Professional profiles and papers">
					<a class="text-link" href="https://www.linkedin.com/in/rohdata" target="_blank" rel="external noreferrer">
						{profile.linkedin} <span aria-hidden="true">↗</span>
					</a>
					<a class="text-link" href={profile.mediumUrl} target="_blank" rel="external noreferrer">
						{profile.medium} <span aria-hidden="true">↗</span>
					</a>
					<a class="text-link" href={profile.googleScholarUrl} target="_blank" rel="external noreferrer">
						{profile.googleScholar} <span aria-hidden="true">↗</span>
					</a>
					<a class="text-link" href={profile.ssrnUrl} target="_blank" rel="external noreferrer">
						{profile.ssrn} <span aria-hidden="true">↗</span>
					</a>
				</div>
			</div>
		</div>
	</section>

	<div class="page-body shell about-body">
		<nav class="profile-toc" aria-label={profile.sections.navigation}>
			<a href="#experience">{profile.sections.experience}</a>
			<a href="#education">{profile.sections.education}</a>
			<a href="#research">{profile.sections.research}</a>
		</nav>

		<section id="experience" class="about-section" aria-labelledby="experience-title">
			<div class="about-section-heading">
				<p class="eyebrow">01</p>
				<h2 id="experience-title">{profile.sections.experience}</h2>
			</div>
			<div class="experience-list">
				{#each profile.experience as job (job.company)}
					<article class="experience-row">
						<div class="experience-meta">
							<p class="eyebrow">{job.dates}</p>
							<h3>{job.company}</h3>
							<p>{job.role} · {job.location}</p>
							{#if 'team' in job}<p class="experience-team">{job.team}</p>{/if}
						</div>
						<ul>
							{#each job.points as point (point)}<li>{point}</li>{/each}
						</ul>
					</article>
				{/each}
			</div>
		</section>

		<section id="education" class="about-section" aria-labelledby="education-title">
			<div class="about-section-heading">
				<p class="eyebrow">02</p>
				<h2 id="education-title">{profile.sections.education}</h2>
			</div>
			<div class="education-list">
				{#each profile.education as school (school.school)}
					<article class="education-row">
						<div>
							<p class="eyebrow">{school.dates}</p>
							<h3>{school.school}</h3>
							<p>{school.degree} · {school.location}</p>
						</div>
						<div>
							<ul>{#each school.details as detail (detail)}<li>{detail}</li>{/each}</ul>
							{#if 'link' in school}<a class="text-link" href={school.link} target="_blank" rel="external noreferrer">{school.linkLabel} <span aria-hidden="true">↗</span></a>{/if}
						</div>
					</article>
				{/each}
			</div>
		</section>

		<section id="research" class="about-section" aria-labelledby="research-title">
			<div class="about-section-heading">
				<p class="eyebrow">03</p>
				<h2 id="research-title">{profile.sections.research}</h2>
			</div>
			<ol class="publication-list">
				{#each profile.publications as publication (publication.title)}
					<li>
						<div>
							<h3>{publication.title}</h3>
							<p>{publication.venue}</p>
							{#if 'methodIds' in publication && publication.methodIds.length > 0}
								<div class="publication-methods">
									{#each publication.methodIds ?? [] as methodId (methodId)}
										{@const method = researchMethods[methodId as keyof typeof researchMethods]}
										<span class={`method-tag method-${method.family}`}>{method[$locale]}</span>
									{/each}
								</div>
							{/if}
							{#if publication.interestIds?.length}
								<div class="interest-tags publication-tags" aria-label={profile.sections.interests}>
									{#each publication.interestIds as interestId (interestId)}
										{@const interest = interestById.get(interestId)}
										{#if interest}
											<a class={`interest-tag interest-${interest.color}`} href={resolve(interest.href)} onclick={(event) => navigateToInterest(event, 'anchor' in interest ? interest.anchor : undefined)}>{interest.label}</a>
										{/if}
									{/each}
								</div>
							{/if}
						</div>
						{#if 'url' in publication}<a href={publication.url} target="_blank" rel="external noreferrer" aria-label={`${publication.title} ↗`}>↗</a>{/if}
					</li>
				{/each}
			</ol>
		</section>

		<aside class="about-disclosure">{profile.independence}</aside>

		<section class="about-section interest-section" aria-labelledby="interests-title">
			<div class="about-section-heading">
				<h2 id="interests-title">{profile.sections.interests}</h2>
			</div>
			<div class="interest-tags">
				{#each profile.interests as interest (interest.id)}
					<a class={`interest-tag interest-${interest.color}`} href={resolve(interest.href)} onclick={(event) => navigateToInterest(event, 'anchor' in interest ? interest.anchor : undefined)}>{interest.label}<span aria-hidden="true">↗</span></a>
				{/each}
			</div>
		</section>

		<div class="page-back"><a class="text-link" href={resolve('/')}>← {copy.backHome}</a></div>
	</div>
</main>