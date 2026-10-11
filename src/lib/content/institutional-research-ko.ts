export const researchSourceCopyKo: Record<string, { description: string; cadence: string; access?: string }> = {
	citadel: { description: '마켓 메이커 관점에서 시장 구조, 유동성, 딜러 포지셔닝, 옵션, ETF 활동을 해석합니다.', cadence: '비정기' },
	aqr: { description: '팩터, 스타일 프리미엄, 추세 추종, 멀티에셋 포트폴리오 구성 연구입니다.', cadence: '비정기' },
	man: { description: '매크로 국면, 헤지펀드 전략, 상대가치, 크레딧을 다루며 Views From the Floor 시리즈를 포함합니다.', cadence: '주간 시리즈 및 비정기' },
	apollo: { description: 'Torsten Slok의 매크로 차트와 해설, The Daily Spark와 The Weekly Brief를 제공합니다.', cadence: '매일·매주' },
	blackrock: { description: '글로벌 매크로, 자산배분, 시장 테마와 포트폴리오 시사점을 다룹니다.', cadence: '주간 및 비정기' },
	jpm: { description: '시장 코멘터리와 멀티에셋 관점을 제공하며 Guide to the Markets는 차트 자료로 유용합니다.', cadence: '주간·분기' },
	'jpm-weekly': { description: '최근 시장 및 매크로 변화를 간결하게 요약합니다.', cadence: '주간' },
	kkr: { description: '사모주식, 사모신용, 실물자산, 글로벌 매크로와 자산배분을 분석합니다.', cadence: '비정기' },
	alphasense: { description: '실적 발표, 기업 공시, 산업 흐름을 연결하는 공개 테마 리서치입니다.', cadence: '비정기', access: '플랫폼은 유료이며 일부 공개 리서치를 이용할 수 있습니다.' },
	bridgewater: { description: '글로벌 매크로, 경제 국면, 정책, 자산 간 관계를 다룹니다.', cadence: '비정기' },
	twosigma: { description: '퀀트 투자, 머신러닝, 통계와 데이터 기반 연구입니다.', cadence: '비정기' },
	point72: { description: '투자 프로세스, 데이터 사이언스, 시장 관점을 다룹니다.', cadence: '비정기' },
	'goldman-top': { description: '주요 투자 논쟁을 전문가 인터뷰와 함께 심층 분석합니다.', cadence: '비정기' },
	goldman: { description: '경제, 기업, 자본시장, 글로벌 투자 관련 리서치입니다.', cadence: '주 여러 차례' },
	'goldman-markets': { description: 'Goldman Sachs 애널리스트와 투자자가 포지셔닝, 금리, 주식, 헤지펀드 심리를 짧게 해설합니다.', cadence: '주간' },
	'morgan-stanley-totm': { description: 'Morgan Stanley 리서치 담당자들이 평일마다 시장을 짧게 해설합니다. 한국·일본, 시장 폭, 금리, 크레딧을 다룬 에피소드도 있습니다.', cadence: '평일' },
	'bloomberg-odd-lots': { description: 'Joe Weisenthal과 Tracy Alloway가 금융, 시장 구조, 경제의 흥미로운 질문을 깊게 다룹니다. 주요 팟캐스트 앱에서도 들을 수 있습니다.', cadence: '월·목·금, 뉴스레터는 자주 업데이트', access: '오디오는 폭넓게 공개되며 Bloomberg 기사와 뉴스레터는 가입 또는 구독이 필요할 수 있습니다.' },
	'bloomberg-money-stuff': { description: 'Matt Levine이 월가와 금융을 독특하고 분석적으로 해설하는 뉴스레터입니다. 공식 Bloomberg 하우스 뷰가 아니라 개인 전문가 코멘터리로 보는 것이 적절합니다.', cadence: '매일 뉴스레터', access: '뉴스레터 신청이 가능하며 연결된 일부 Bloomberg 기사는 구독이 필요할 수 있습니다.' },
	'oaktree-memos': { description: 'Howard Marks의 시장 사이클, 위험, 투자자 심리, 크레딧에 관한 장문 메모입니다.', cadence: '비정기 · 발행 시 정독 추천' },
	'gmo-library': { description: '장기 밸류에이션, 자산군 전망, 버블과 기대수익률에 대한 GMO의 독자적 관점을 제공합니다.', cadence: '비정기 · 전망과 레터는 장기 주기' },
	'hussman-commentary': { description: '밸류에이션과 시장 내부 지표를 중심으로 한 John Hussman의 위험 관리 관점입니다. 시장 컨센서스와 다른 시각을 비교할 때 유용합니다.', cadence: '비정기 · 최근 수 주 간격' },
	ubs: { description: 'CIO의 시장 전망, 자산배분과 투자 아이디어를 다룹니다.', cadence: '비정기' },
	pimco: { description: '금리, 채권, 크레딧, 글로벌 매크로 리서치입니다.', cadence: '비정기' },
	vanguard: { description: '장기 자산배분, ETF, 투자자 행동을 다룹니다.', cadence: '비정기' },
	'msci-charts': { description: '사모주식, 벤처캐피털, 사모신용 성과와 자금 흐름을 시각화합니다.', cadence: '주간 시리즈' },
	'msci-benchmarks': { description: '비상장 펀드 성과, 드라이파우더, 자본 납입과 분배를 다룹니다.', cadence: '분기', access: '등록이 필요할 수 있습니다.' },
	blackstone: { description: '사모주식, 부동산, 크레딧 시장을 다룹니다.', cadence: '비정기' },
	bain: { description: '바이아웃, 펀드레이징, 회수, 사모주식 성과를 정리합니다.', cadence: '연간' },
	preqin: { description: '사모주식, 벤처캐피털, 헤지펀드와 사모자본 데이터입니다.', cadence: '비정기' },
	cambridge: { description: '기관 포트폴리오, 운용사 선정, 사모시장을 다룹니다.', cadence: '비정기' },
	caia: { description: '대체투자, 헤지펀드, 포트폴리오 구성 교육 자료입니다.', cadence: '비정기' },
	spglobal: { description: '기업 데이터, 크레딧 시장과 산업 동향을 다룹니다.', cadence: '비정기' },
	cboe: { description: '옵션, 변동성, 시장 구조 자료를 제공합니다.', cadence: '비정기' },
	cme: { description: '선물, 포지셔닝, 금리와 원자재 리포트입니다.', cadence: '비정기' },
	lseg: { description: '자본시장, 금융 데이터와 투자 분석을 다룹니다.', cadence: '비정기' },
	nasdaq: { description: 'ETF, 자본시장, 기업, 트레이딩 관련 글입니다.', cadence: '비정기' },
	nomura: { description: '아시아 매크로, 일본 시장과 투자 전략을 다룹니다.', cadence: '비정기' },
	nikko: { description: '일본 주식, 아시아·태평양 시장과 매크로를 다룹니다.', cadence: '비정기' },
	eastspring: { description: '아시아 주식, 채권과 자산배분을 다룹니다.', cadence: '비정기' },
	gavekal: { description: '중국, 글로벌 매크로와 유동성 리서치입니다.', cadence: '비정기', access: '공개 글과 전체 리서치의 접근 조건이 다를 수 있습니다.' },
	adb: { description: '아시아 경제, 금융시장과 구조 변화를 다룹니다.', cadence: '비정기' }
};

export const researchGroupsKo = [
	{ title: '핵심 기관 리서치', description: '시장 구조, 퀀트, 매크로, 증권사 코멘터리와 사모시장 자료를 폭넓게 살펴봅니다.' },
	{ title: '증권사·셀사이드 시장 전망', description: '대형 리서치 조직의 공개 시황을 통해 애널리스트의 해석을 살펴봅니다. 기관 고객용 리서치 전체를 대체하지는 않습니다.' },
	{ title: 'Bloomberg의 독특한 목소리', description: 'Bloomberg의 시장 팟캐스트와 월가·금융을 다루는 개성 있는 일간 뉴스레터를 함께 읽습니다. 공식 기관 리서치가 아닌 편집 콘텐츠입니다.' },
	{ title: '운용자의 독자적 관점', description: '매일 업데이트되지는 않지만, 명확한 투자 철학을 주간 시장 컨센서스와 비교하기 좋습니다.' },
	{ title: '헤지펀드·퀀트 리서치', description: '팩터의 경제적 근거, 전략 구현, 데이터 기반 증거를 비교합니다.' },
	{ title: '자산배분·글로벌 매크로', description: '포트폴리오 구성, 자산배분, 매크로 국면 관점에서 시장 변화를 읽습니다.' },
	{ title: '사모시장', description: '자주 업데이트되는 시장 차트와 성과·펀드레이징·회수·유동성 장기 자료를 함께 봅니다.' },
	{ title: '대체데이터·시장 인텔리전스', description: '기업 공시와 실적 발표를 산업 테마, 포지셔닝, 시장 데이터에 연결합니다.' },
	{ title: '아시아 시장', description: '미국 중심 리서치에 한국·일본·중국·대만 및 아시아 지역 관점을 더합니다.' }
];

export const weeklyRoutineKo = [
	'글로벌 시장 요약',
	'셀사이드·시장 구조',
	'퀀트·팩터 리서치',
	'사모시장·운용자 관점',
	'아시아·실적 정보'
];

export const researchFrameworkKo = [
	{ title: '시장 관찰', description: '이번 주에 무슨 일이 있었나요? 수익률, 시장 폭, 자금 흐름, 변동성을 살펴봅니다.' },
	{ title: '기관의 해석', description: '서로 다른 기관은 같은 시장 현상을 어떻게 다르게 해석하나요?' },
	{ title: '데이터와 방법론', description: '결론의 근거가 된 데이터, 정의, 계산 방법을 확인합니다.' },
	{ title: '리서치 재현', description: '같은 아이디어를 아시아 시장에서 검증하려면 어떤 데이터와 모델이 필요할까요?' }
];