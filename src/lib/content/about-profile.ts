export const aboutProfiles = {
	en: {
		eyebrow: 'About Me',
		name: 'Hyunwoo Roh',
		role: 'Data @Bloomberg · Senior Data Professional',
		location: 'Hong Kong',
		linkedin: 'LinkedIn profile',
		medium: 'Medium blog',
		mediumUrl: 'https://medium.com/@corr-roh',
		googleScholar: 'Google Scholar',
		googleScholarUrl: 'https://scholar.google.com/citations?user=kXl69rUAAAAJ&hl=en&oi=sra',
		ssrn: 'SSRN papers',
		ssrnUrl: 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3744765',
		interestsTitle: 'Research Interests',
		interests: [
			{ id: 'data-quality', label: 'Financial Data & XBRL', href: 'disclosures/', color: 'data' },
			{ id: 'apac-disclosures', label: 'APAC Company Disclosures', href: 'disclosures/', color: 'data' },
			{ id: 'alternative-data', label: 'Alternative Data', href: 'institutional-research/', anchor: 'alternative-data', color: 'data' },
			{ id: 'financial-institutions', label: 'Financial Institutions', href: 'core-concepts/', color: 'institutions' },
			{ id: 'quant-research', label: 'Quantitative Investing', href: 'quant/', color: 'quant' },
			{ id: 'portfolio-strategy', label: 'Portfolio Strategy', href: 'quant/', color: 'quant' },
			{ id: 'market-structure', label: 'Market Structure', href: 'market-overlay/', color: 'markets' },
			{ id: 'market-volatility', label: 'Market Volatility', href: 'market-overlay/', color: 'risk' },
			{ id: 'geopolitical-risk', label: 'Geopolitical Risk', href: 'market-overlay/', color: 'risk' }
		],
		intro:
			'I build financial-data products and investment workflows where accounting knowledge meets data engineering, workflow automation and applied NLP. At Bloomberg, I work with company financials in the Finance Sector and use AI to improve data review and delivery. Earlier roles span market sensing, robo-advisory, portfolio management, alpha research and alternative-data credit modeling.',
			independence:
			'ASMR is a personal research project. Views here are my own and are not affiliated with or endorsed by Bloomberg or any current or former employer. The site does not use confidential, licensed or employer-owned data.',
		sections: {
			navigation: 'On this page',
			experience: 'Experience',
			education: 'Education',
			research: 'Selected Research & Publications',
			interests: 'Research Interests'
		},
		experience: [
			{
				company: 'Bloomberg',
				role: 'Senior Data Professional · Finance Sector',
				location: 'Hong Kong',
				dates: 'Aug 2025 – Present',
				team: 'Company Financials Industry Team',
				points: [
					'Build finance-sector workflows across data engineering, workflow automation and applied NLP, grounded in accounting and market nuances.',
					'Leverage AI to accelerate and optimize financial-data review and delivery processes.',
					'Develop APAC golden templates for banks, insurers and securities firms, standardizing core fields, mappings and market-specific exceptions.'
				]
			},
			{
				company: 'Samsung Securities',
				role: 'Assistant Manager · Senior Associate',
				location: 'Seoul, South Korea',
				dates: 'Feb 2023 – Aug 2025',
				points: [
					'Channel Solution Strategy Team: developed a market-sensing pipeline from data collection through investment-strategy delivery.',
					'Received the Samsung Securities Employee of the Year award in 2024.',
					'Wrap Management Team: developed robo-advisor algorithms and researched alpha; managed discretionary model portfolios and quantitative portfolio strategies.'
				]
			},
			{
				company: 'Wavebridge',
				role: 'Quantitative Researcher',
				location: 'Seoul, South Korea',
				dates: 'Nov 2022 – Jan 2023',
				points: [
					'Researched statistical-arbitrage alpha in crypto markets using internal C# and Python research templates.',
					'Developed execution rules and engines to reduce latency, market impact, trading risk and transaction costs.'
				]
			},
			{
				company: 'PFCT · PFC Technologies (Peoplefund)',
				role: 'Data Scientist',
				location: 'Seoul, South Korea',
				dates: 'May 2021 – Oct 2022',
				points: [
					'Presented genetic-algorithm research on optimal credit approval at the INFORMS 2022 Workshop on Data Science.',
					'Modeled and optimized loan-pricing and loan-amount strategies to improve profitability and efficiency.',
					'Enhanced credit scoring with machine-learning methods and features derived from alternative data.'
				]
			},
			{
				company: 'Yuro Instruments · JURO Instruments',
				role: 'Quantitative Researcher',
				location: 'Seoul, South Korea',
				dates: 'May 2020 – Sep 2020',
				points: [
					'Researched an early-warning system for financial risks across stocks, derivatives and digital assets using fat-tailed distributions and machine learning, advised by Professor Aaron Youngshin Kim of Stony Brook University.'
				]
			},
			{
				company: 'University of Chicago',
				role: 'Research and Teaching Assistant',
				location: 'Chicago, Illinois, USA',
				dates: 'Oct 2019 – Mar 2020',
				points: [
					'Led weekly office hours and review sessions for Econometrics and Statistical Methods in Economics.',
				'Assisted with stochastic-analysis and portfolio-theory course materials, grading, and a behavioral-economics meta-analysis project on energy.'
				]
			}
		],
		education: [
			{
				school: 'University of Chicago',
				degree: 'M.A. in Economics',
				location: 'Chicago, USA',
				dates: 'Aug 2018 – Aug 2020',
				details: [
					'Advisor: Per Mykland.',
					'Thesis: Predicting High-frequency Stock Price Using Machine Learning Technique. SSRN 3744765.',
					'Coursework: applied statistics, multivariate time series, machine learning in finance, high-frequency financial statistics, econometrics and computational modeling.',
					'Teaching assistant for Statistical Methods in Economics and Econometrics, including weekly office hours and review sessions.'
				],
				link: 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3744765',
				linkLabel: 'Thesis on SSRN'
			},
			{
				school: 'Kyung Hee University',
				degree: 'B.A. (Honors) in Economics and International Studies',
				location: 'Seoul, South Korea',
				dates: 'Mar 2013 – Aug 2018',
				details: [
					'Dean’s List, Fall 2014 and Fall 2016.',
					'Mathematics coursework included real analysis, general topology, differential equations, numerical analysis, statistics and finance.'
				]
			},
			{
				school: 'University of California, Berkeley',
				degree: 'Exchange Student · Political Economy',
				location: 'Berkeley, USA',
				dates: '2014 – 2015',
				details: []
			},
			{
				school: 'Taegu Foreign Language High School',
				degree: 'High School Diploma',
				location: 'Daegu, South Korea',
				dates: 'Mar 2009 – Feb 2012',
				details: []
			}
		],
		publications: [
			{
				title: 'Finding an Optimal Approval Strategy in Credit Scoring System Using Genetic Algorithm',
				venue: 'Company research project · Oct 2022',
				url: 'https://dx.doi.org/10.2139/ssrn.4461370',
				methodIds: ['genetic-algorithm'],
				interestIds: ['quant-research', 'financial-institutions']
			},
			{
				title: 'What Moves Analyst Forecasts? Topic-Level Under- and Overreaction in Korean Financial Holding Companies',
				venue: 'Working paper',
				interestIds: ['financial-institutions', 'market-structure']
			},
			{
				title: 'Predicting High-frequency Stock Price Using Machine Learning Technique',
				venue: 'Graduate research project · Dec 2020',
				url: 'https://dx.doi.org/10.2139/ssrn.3744765',
				methodIds: ['machine-learning'],
				interestIds: ['quant-research', 'market-structure']
			},
			{
				title: 'Risk Budgeting Approach using Black-Litterman Model: Combining Investor Views With Market Equilibrium',
				venue: 'With Hongjae Lee and Taesuk Kim · Global Business Administration Review, 17(5), 88–114 · Oct 2020',
				methodIds: ['black-litterman', 'risk-budgeting'],
				interestIds: ['portfolio-strategy', 'quant-research']
			},
			{
				title: 'Measuring North Korean Geopolitical Risks: Implications for Asia’s Financial Volatilities',
				venue: 'With Jiyoun An · East Asian Policy, 10(3), 41–50 · Jul/Sep 2018',
				methodIds: ['alternative-data'],
				interestIds: ['geopolitical-risk', 'market-volatility']
			},
			{
				title: 'A Study on Information Spillover Effect at Industry Level between Korean and US Stock Market',
				venue: 'With Sunmi Lee · KyungHee Journal of Natural Science · Dec 2016',
				methodIds: ['garch-family'],
				interestIds: ['market-structure', 'market-volatility']
			}
		]
	},
	ko: {
		eyebrow: '소개',
		name: '노현우',
		role: 'Data @Bloomberg · Senior Data Professional',
		location: '홍콩',
		linkedin: 'LinkedIn 프로필',
		medium: 'Medium 블로그',
		mediumUrl: 'https://medium.com/@corr-roh',
		googleScholar: 'Google Scholar 검색',
		googleScholarUrl: 'https://scholar.google.com/citations?user=kXl69rUAAAAJ&hl=en&oi=sra',
		ssrn: 'SSRN 논문',
		ssrnUrl: 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3744765',
		interestsTitle: '연구 관심 분야',
		interests: [
			{ id: 'data-quality', label: '금융 데이터·XBRL', href: 'disclosures/', color: 'data' },
			{ id: 'apac-disclosures', label: '아시아·태평양 기업 공시', href: 'disclosures/', color: 'data' },
			{ id: 'alternative-data', label: '대체데이터', href: 'institutional-research/', anchor: 'alternative-data', color: 'data' },
			{ id: 'financial-institutions', label: '금융기관 분석', href: 'core-concepts/', color: 'institutions' },
			{ id: 'quant-research', label: '퀀트 투자', href: 'quant/', color: 'quant' },
			{ id: 'portfolio-strategy', label: '포트폴리오 전략', href: 'quant/', color: 'quant' },
			{ id: 'market-structure', label: '시장 구조', href: 'market-overlay/', color: 'markets' },
			{ id: 'market-volatility', label: '시장 변동성', href: 'market-overlay/', color: 'risk' },
			{ id: 'geopolitical-risk', label: '지정학적 리스크', href: 'market-overlay/', color: 'risk' }
		],
		intro:
			'회계 지식과 시장 이해를 바탕으로 금융 데이터 제품과 투자 워크플로를 만듭니다. Bloomberg Finance Sector에서 데이터 엔지니어링, 워크플로 자동화, 응용 NLP와 AI를 활용하고 있습니다. 이전에는 시장 센싱 파이프라인, 로보어드바이저, 포트폴리오 전략, 알파 리서치, 대체데이터 기반 신용평가를 수행했습니다.',
		independence:
			'ASMR은 개인 리서치 프로젝트입니다. 이곳의 견해는 개인의 의견이며 Bloomberg 또는 현재·과거 고용주의 견해나 지지를 대변하지 않습니다. 기밀·라이선스·고용주 소유 데이터는 사용하지 않습니다.',
		sections: {
			navigation: '페이지 바로가기',
			experience: '경력',
			education: '학력',
			research: '주요 연구 및 논문',
			interests: '연구 관심 분야'
		},
		experience: [
			{
				company: 'Bloomberg',
				role: 'Senior Data Professional · Finance Sector',
				location: '홍콩',
				dates: '2025년 8월 – 현재',
				team: 'Company Financials Industry Team',
				points: [
					'회계·시장 맥락을 바탕으로 금융 데이터 엔지니어링, 워크플로 자동화, 응용 NLP 업무를 수행합니다.',
					'AI를 활용해 금융 데이터 검토와 전달 프로세스를 가속하고 최적화합니다.',
					'아시아·태평양 은행, 보험사, 증권사의 골든 템플릿을 개발해 핵심 필드, 매핑, 시장별 예외를 표준화합니다.'
				]
			},
			{
				company: '삼성증권',
				role: '과장 · Senior Associate',
				location: '대한민국 서울',
				dates: '2023년 2월 – 2025년 8월',
				points: [
					'Channel Solution Strategy Team에서 데이터 수집부터 투자전략 제공까지 이어지는 Market Sensing 파이프라인을 개발했습니다.',
					'2024년 삼성증권인상을 수상했습니다.',
					'Wrap Management Team에서 로보어드바이저 시스템과 알파를 연구하고 일임형 모델 포트폴리오 및 퀀트 전략을 개발·관리했습니다.'
				]
			},
			{
				company: '웨이브릿지',
				role: '퀀트 리서처',
				location: '대한민국 서울',
				dates: '2022년 11월 – 2023년 1월',
				points: [
					'C# 및 Python 기반 사내 연구 템플릿으로 가상자산 시장의 통계적 차익거래 알파를 연구했습니다.',
					'지연시간, 시장 충격, 거래 위험과 거래 비용을 줄이는 주문 집행 규칙과 엔진을 개발했습니다.'
				]
			},
			{
				company: 'PFCT · PFC Technologies (피플펀드)',
				role: '데이터 사이언티스트',
				location: '대한민국 서울',
				dates: '2021년 5월 – 2022년 10월',
				points: [
					'유전 알고리즘 기반 최적 신용 승인 전략 연구를 INFORMS 2022 데이터 사이언스 워크숍에서 발표했습니다.',
					'수익성과 효율성 개선을 위해 대출 금리 및 한도 전략을 모델링하고 최적화했습니다.',
					'머신러닝과 대체데이터 피처를 적용해 신용평가모형을 개선했습니다.'
				],
			},
			{
				company: '유로인스트루먼츠 · JURO Instruments',
				role: '퀀트 리서처',
				location: '대한민국 서울',
				dates: '2020년 5월 – 2020년 9월',
				points: [
					'Aaron Youngshin Kim 교수(Stony Brook University)의 지도 아래 팻테일 분포와 머신러닝을 활용해 주식, 파생상품, 디지털 자산의 금융 위험 조기경보 시스템을 연구·개발했습니다.'
				]
			},
			{
				company: 'University of Chicago',
				role: 'Research and Teaching Assistant',
				location: '미국 일리노이주 시카고',
				dates: '2019년 10월 – 2020년 3월',
				points: [
					'계량경제학과 경제통계방법론의 주간 오피스아워와 리뷰 세션을 진행했습니다.',
					'확률미적분 및 포트폴리오 이론 과목의 해설 자료와 과제 채점을 지원했습니다.',
					'에너지 분야 실험·행동경제학 메타분석 프로젝트에 참여했습니다.'
				]
			}
		],
		education: [
			{
				school: 'University of Chicago',
				degree: '경제학 석사',
				location: '미국 시카고',
				dates: '2018년 8월 – 2020년 8월',
				details: [
					'지도교수: Per Mykland.',
					'논문: 머신러닝 기법을 이용한 고빈도 주가 예측. SSRN 3744765.',
					'주요 수강 과목: 응용통계, 다변량 시계열, 금융 머신러닝, 고빈도 금융통계, 계량경제학, 계산경제학.',
					'경제통계방법론 및 계량경제학 과목 조교로 매주 오피스아워와 리뷰 세션을 진행했습니다.'
				],
				link: 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3744765',
				linkLabel: 'SSRN 논문 보기'
			},
			{
				school: '경희대학교',
				degree: '경제학·국제학 학사 (우등 졸업)',
				location: '대한민국 서울',
				dates: '2013년 3월 – 2018년 8월',
				details: [
					'성적우수자 명단(Dean’s List) 2회: 2014년 가을, 2016년 가을.',
					'수학 과목: 실해석학, 일반위상수학, 미분방정식, 수치해석, 통계수학, 금융수학.'
				]
			},
			{
				school: 'University of California, Berkeley',
				degree: '교환학생 · 정치경제학',
				location: '미국 버클리',
				dates: '2014년 – 2015년',
				details: []
			},
			{
				school: '대구외국어고등학교',
				degree: '고등학교 졸업',
				location: '대한민국 대구',
				dates: '2009년 3월 – 2012년 2월',
				details: []
			}
		],
		publications: [
			{
				title: '유전 알고리즘을 이용한 신용평가 시스템의 최적 승인 전략 탐색',
				venue: '기업 연구 프로젝트 · 2022년 10월',
				url: 'https://dx.doi.org/10.2139/ssrn.4461370',
				methodIds: ['genetic-algorithm'],
				interestIds: ['quant-research', 'financial-institutions']
			},
			{
				title: '애널리스트 전망을 움직이는 요인: 한국 금융지주사의 주제별 과소·과잉 반응',
				venue: '워킹 페이퍼',
				interestIds: ['financial-institutions', 'market-structure']
			},
			{
				title: '머신러닝 기법을 이용한 고빈도 주가 예측',
				venue: '대학원 연구 프로젝트 · 2020년 12월',
				url: 'https://dx.doi.org/10.2139/ssrn.3744765',
				methodIds: ['machine-learning'],
				interestIds: ['quant-research', 'market-structure']
			},
			{
				title: '블랙-리터만 모형을 이용한 리스크 버짓팅: 투자자 전망과 시장 균형의 결합',
				venue: '이홍재·김태석 공저 · Global Business Administration Review, 17(5), 88–114 · 2020년 10월',
				methodIds: ['black-litterman', 'risk-budgeting'],
				interestIds: ['portfolio-strategy', 'quant-research']
			},
			{
				title: '북한 지정학적 위험 측정: 아시아 금융 변동성에 대한 시사점',
				venue: '안지연 공저 · East Asian Policy, 10(3), 41–50 · 2018년 7/9월',
				methodIds: ['alternative-data'],
				interestIds: ['geopolitical-risk', 'market-volatility']
			},
			{
				title: '한국과 미국 주식시장 간 산업 수준 정보 파급효과 연구',
				venue: '선미 공저 · KyungHee Journal of Natural Science · 2016년 12월',
				methodIds: ['garch-family'],
				interestIds: ['market-structure', 'market-volatility']
			}
		]
	}
} as const;