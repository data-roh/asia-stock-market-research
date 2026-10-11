export const researchMethods = {
	'genetic-algorithm': { en: 'Genetic Algorithm', ko: '유전 알고리즘', family: 'optimization' },
	'machine-learning': { en: 'Machine Learning', ko: '머신러닝', family: 'ml' },
	'black-litterman': { en: 'Black–Litterman Model', ko: 'Black–Litterman 모형', family: 'portfolio' },
	'risk-budgeting': { en: 'Risk Budgeting', ko: '리스크 버짓팅', family: 'portfolio' },
	'univariate-garch': { en: 'Univariate GARCH', ko: '단변량 GARCH', family: 'time-series' },
	'dcc-garch': { en: 'Bivariate DCC-GARCH', ko: '이변량 DCC-GARCH', family: 'time-series' }
} as const;

export const researchMethodCopy = {
	en: {
		heading: 'Methods',
		notSpecified: 'Specific method not listed in the supplied résumé.'
	},
	ko: {
		heading: '방법론',
		notSpecified: '공유해주신 이력서에는 구체적인 방법론이 기재되어 있지 않습니다.'
	}
} as const;
