export interface DisclosureDocument {
	slug: string;
	title: string;
	format: string;
	description: string;
	descriptionKo: string;
	href: string;
	markdownPath: string;
	pageDescription: string;
	pageDescriptionKo: string;
	note: string;
	noteKo: string;
}

export const disclosureDocuments: DisclosureDocument[] = [
	{
		slug: 'taxonomy',
		title: 'A Taxonomy of Asian Disclosure Systems',
		format: 'Asia Stock Review · Overview',
		description: 'A comparative overview of disclosure architecture and the event-level research edge across Korea, Japan, China, Taiwan and the US.',
		descriptionKo: '한국·일본·중국·대만·미국의 공시 체계와 이벤트 기반 리서치 기회를 비교하는 개요입니다.',
		href: 'disclosures/taxonomy/',
		markdownPath: 'asia_stock_review_disclosure_systems.md',
		pageDescription: 'How Korea, Japan, China and Taiwan disclose, and how the US compares.',
		pageDescriptionKo: '한국·일본·중국·대만의 공시 방식과 미국 비교.',
		note: 'Overview edition · English original · Personal research, not investment advice.',
		noteKo: '개요판 · 영어 원문 · 개인 리서치이며 투자 조언이 아닙니다.'
	},
	{
		slug: 'taxonomy-detail',
		title: 'A Taxonomy of Asian Disclosure Systems: Detailed Edition',
		format: 'Detailed edition · Rules and data architecture',
		description: 'Rule-level detail, cross-market event matrices, a canonical data architecture, research signals and official source references.',
		descriptionKo: '규칙별 상세 설명, 시장 간 이벤트 비교, 데이터 구조, 리서치 시그널과 공식 출처를 담은 상세판입니다.',
		href: 'disclosures/taxonomy-detail/',
		markdownPath: 'asia_disclosure_systems_DETAIL_EN.md',
		pageDescription: 'Korea, Japan, China and Taiwan, benchmarked against US EDGAR, with rule-level detail and a data architecture.',
		pageDescriptionKo: '한국·일본·중국·대만을 EDGAR와 비교하고 규칙과 데이터 아키텍처까지 정리한 상세판입니다.',
		note: 'As of 12 September 2026 · English original · Rules and thresholds require primary-source verification before production use.',
		noteKo: '2026년 9월 12일 기준 · 영어 원문 · 실제 운영 전에는 규칙과 기준값을 1차 출처로 확인해야 합니다.'
	},
	{
		slug: 'nine-company-examples',
		title: 'A Taxonomy of Asian Disclosure Systems: Nine Worked Examples',
		format: 'Worked examples · Nine semiconductor companies',
		description: 'Apply the framework end to end to Samsung Electronics, SK hynix, Samsung Electro-Mechanics, Kioxia, Tokyo Electron, Advantest, TSMC, MediaTek and ASE.',
		descriptionKo: '삼성전자, SK hynix, 삼성전기, Kioxia, Tokyo Electron, Advantest, TSMC, MediaTek, ASE에 프레임워크를 적용한 사례입니다.',
		href: 'disclosures/nine-company-examples/',
		markdownPath: 'asia_disclosure_nine_company_examples_EN.md',
		pageDescription: 'Apply the framework to nine semiconductor companies across Korea, Japan and Taiwan.',
		pageDescriptionKo: '한국·일본·대만 반도체 기업 9곳에 공시 프레임워크를 적용합니다.',
		note: 'As of 13 September 2026 · English original · Bracketed values are author-marked estimates and should be verified against primary filings.',
		noteKo: '2026년 9월 13일 기준 · 영어 원문 · 대괄호로 표시된 추정치는 원문 공시에서 확인해야 합니다.'
	},
	{
		slug: 'linkedin-tables',
		title: 'A Taxonomy of Asian Disclosure Systems: 5 Tables',
		format: 'LinkedIn carousel · Five comparison tables',
		description: 'A concise, slide-friendly summary of the five-market taxonomy, distinctive disclosures, earnings clocks and positioning data.',
		descriptionKo: '5개 시장의 공시 분류, 시장별 특징, 실적 발표 시계, 포지셔닝 데이터를 표로 요약한 캐러셀 원고입니다.',
		href: 'disclosures/linkedin-tables/',
		markdownPath: 'asia_disclosure_linkedin_tables.md',
		pageDescription: 'Five tables comparing the disclosure systems of Korea, Japan, China, Taiwan and the US.',
		pageDescriptionKo: '한국·일본·중국·대만·미국의 공시 체계를 비교하는 다섯 개 표입니다.',
		note: 'Carousel edition · English original · Personal research, not investment advice.',
		noteKo: '캐러셀 원고 · 영어 원문 · 개인 리서치이며 투자 조언이 아닙니다.'
	}
];

export function getDisclosureDocument(slug: string): DisclosureDocument {
	const document = disclosureDocuments.find((item) => item.slug === slug);
	if (!document) throw new Error(`Unknown disclosure document: ${slug}`);
	return document;
}
