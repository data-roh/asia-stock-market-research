export const researchTracksKo = {
	disclosures: {
		eyebrow: '리서치 트랙 01',
		title: '기업 공시',
		shortDescription: '아시아 기업이 재무·영업·위험 정보를 공개하는 방식을 정리합니다.',
		description: '아시아 시장의 재무, 영업, 지분, 고객, 공급업체, 계약 및 위험 정보 공시를 살펴봅니다.',
		metaDescription: '아시아 공시 체계, 출처 추적, 문서 계보와 시점별 공시를 정리합니다.',
		method: '각 시장에서 무엇을 어디에 언제 공개하는지 비교합니다. 모든 데이터 필드는 원문 출처, 공시일, 수정 이력을 추적할 수 있어야 합니다.',
		topics: [
			{ title: '한국·일본·중국·대만 공시 체계', description: '공시 경로, 게시 시점, 시장별 문서 유형을 비교합니다.' },
			{ title: 'IR 자료 및 팩트북 출처 지도', description: '안정적이고 출처를 확인할 수 있는 투자자 자료를 구조화합니다.' },
			{ title: '공급망 및 주요 계약 공시', description: '공개된 공급업체, 고객, 계약, 영업 관계를 추적합니다.' },
			{ title: '출처 추적 및 문서 계보', description: '정규화한 각 데이터 필드를 원본 공개 문서까지 추적합니다.' },
			{ title: '시점별 공시와 수정 이력', description: '특정 시점에 알 수 있었던 정보와 이후 수정된 정보를 구분합니다.' }
		]
	},
	'core-concepts': {
		eyebrow: '리서치 트랙 02',
		title: '금융 핵심 개념',
		shortDescription: '아시아 금융기관을 비교하기 위한 실무 프레임워크를 만듭니다.',
		description: '은행, 보험사, 증권사, 디지털 은행, 금융지주를 비교하는 실무 프레임워크를 구축합니다.',
		metaDescription: '은행·보험사·증권사·지주회사 핵심 지표와 시장별 회계·규제 차이를 정리합니다.',
		method: '기업을 비교하기 전에 개념부터 정의합니다. 회계 기준, 규제상 정의, 애널리스트 계산치를 구분하고 현지 필드를 문서화된 기준 템플릿에 매핑합니다.',
		topics: [
			{ title: '은행: NIM, CET1, Tier 1, CAR, LCR, 레버리지, RWA', description: '수익성, 자본 적정성, 유동성, 위험가중자산 지표를 구분합니다.' },
			{ title: '보험: 지급여력, CSM, 합산비율, 투자수익률', description: '보험영업 성과, 계약서비스마진, 자본 건전성을 비교합니다.' },
			{ title: '증권: 브로커리지, IB, 트레이딩, 자본', description: '사업 부문을 고려해 다각화된 증권사를 비교합니다.' },
			{ title: '시장별 회계·규제 차이', description: '비슷한 용어가 서로 다른 회계·감독 기준을 가리키는 경우를 기록합니다.' },
			{ title: '기준 템플릿과 원천 필드 매핑', description: '시장별 원천 필드를 일관되고 감사 가능한 데이터 모델에 연결합니다.' }
		]
	},
	'market-overlay': {
		eyebrow: '리서치 트랙 03',
		title: '시장 오버레이',
		shortDescription: '기업 펀더멘털과 공시를 시장 움직임에 연결합니다.',
		description: '기업 펀더멘털과 공시를 주가, 포지셔닝, 전망치 수정, 자금 흐름, 시장 폭, 국면 변화에 연결합니다.',
		metaDescription: '아시아 기업 펀더멘털을 주가·시장 폭·전망치·자금 흐름·시장 국면과 연결합니다.',
		method: '시장 관찰과 인과 주장을 분리합니다. 시점을 맞추고 비교 대상을 정의하며 시장 폭, 자금 흐름, 기여율의 분모를 함께 표시합니다.',
		topics: [
			{ title: '지수 수익률과 시장 폭', description: '지수 성과와 상승에 참여한 구성 종목 비중을 함께 추적합니다.' },
			{ title: '지수 기여도와 집중도', description: '소수 종목이 지수 움직임에 기여하는 정도를 측정합니다.' },
			{ title: 'EPS 전망치 수정', description: '이익 추정치 변화 방향과 분산을 관찰합니다.' },
			{ title: 'ETF 및 액티브 ETF 자금 흐름', description: '펀드 자금 흐름을 보유 종목, 집중도, 기초시장 움직임과 비교합니다.' },
			{ title: '자사주 매입과 주주환원', description: '발표된 자본 환원 계획과 실제 집행을 연결합니다.' },
			{ title: '공포·탐욕과 시장 국면', description: '시장 참여와 위험 선호 변화 지표를 투명하게 검증합니다.' }
		]
	},
	quant: {
		eyebrow: '리서치 트랙 04',
		title: '퀀트 리서치',
		shortDescription: '시장 직관을 투명하고 재현 가능한 연구로 발전시킵니다.',
		description: '시장에 대한 직관을 투명하고 검증 가능하며 재현 가능한 실증 연구로 바꿉니다.',
		metaDescription: '가정과 백테스트 검증을 명시하는 아시아 시장 퀀트 리서치입니다.',
		method: '모든 연구는 가설, 시점별 데이터 가정, 거래 비용, 실패 가능성을 밝혀야 합니다. 차트는 관찰이지 초과수익의 증거가 아닙니다.',
		topics: [
			{ title: '장중 시장 전이', description: '지역별 거래 세션 간 정보와 수익률 전이를 살펴봅니다.' },
			{ title: '한국·대만 메모리 업종 선후행', description: '메모리 업종 신호가 두 시장 사이에서 전이되는지 검증합니다.' },
			{ title: '종가 단일가 매매', description: '종가 경매 거래량, 불균형과 다음 세션 움직임을 분석합니다.' },
			{ title: '현물·선물 베이시스', description: '계약, 롤오버, 시점 기준을 통제해 베이시스 움직임을 측정합니다.' },
			{ title: '팩터 리서치', description: '시장별 팩터 정의, 노출도, 성과 안정성을 평가합니다.' },
			{ title: '백테스트 검증과 흔한 오류', description: '미래정보 사용, 생존편향, 비용, 파라미터 선택 문제를 점검합니다.' }
		]
	}
} as const;

export const researchStatusKo: Record<string, string> = {
	Planned: '예정',
	Framework: '분석 체계',
	Building: '구축 중',
	'Research area': '연구 주제'
};