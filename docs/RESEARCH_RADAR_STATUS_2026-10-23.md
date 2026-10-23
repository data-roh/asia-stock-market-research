# Research Radar 운영 상태 — 2026-10-23

이 문서는 2026-10-23 기준 배포 상태의 스냅샷이다. 숫자와 실행 상태는 이 시점의 기록이며, 이후 자동 갱신 결과는 사이트와 GitHub Actions에서 확인한다.

## 기준과 확인된 결과

| 항목 | 상태 |
| --- | --- |
| 저장소 | [data-roh/asia-stock-market-research](https://github.com/data-roh/asia-stock-market-research) |
| 기능 반영 | [PR #1](https://github.com/data-roh/asia-stock-market-research/pull/1) 병합, squash commit `83cb19fee93beda67120f694b3f1e97472b92d79` |
| 초기 데이터 반영 | `main` commit `b286ef4a20ced1b225e75bc677e64011e6248e5d` |
| 공개 페이지 | [Research Radar](https://data-roh.github.io/asia-stock-market-research/research-radar/)에서 HTTP 200 및 초기 목록 확인 |
| Pages 배포 | [run 39880435488](https://github.com/data-roh/asia-stock-market-research/actions/runs/39880435488) 성공, 초기 데이터 커밋 배포 |
| 데이터 작성 시각 | `2026-10-23T00:47:25Z` (`src/lib/content/research-radar.json`) |
| 데이터 전체 보유 | 기관 자료 33건, SSRN DOI 21건, GitHub 저장소 90건 |
| 화면의 주간 선택 | 홍콩 시간 2026-10-12 ~ 2026-10-18 완료 주간: 기관 12건, SSRN 8건, GitHub 8건 |
| 수집 오류 | 초기 데이터의 `sourceErrors`는 빈 목록 |

홈 화면 내비게이션에는 별도의 **Research Radar** 탭이 있다. 기존 [Institutional Research](https://data-roh.github.io/asia-stock-market-research/institutional-research/) 페이지는 그대로 접근 가능하다.

## 자동 갱신 흐름

1. `.github/workflows/daily-research-newsletter.yml`이 매일 00:17 UTC에 실행된다. 홍콩 시간으로는 08:17이다.
2. 기존 `scan_research_updates.py`가 공개 기관 연구 소스를 수집한다. 그 결과의 비공개 스캔 상태는 Actions cache에서 이어받는다.
3. `build_research_radar.py`가 기관 자료, Crossref의 SSRN DOI(`10.2139/ssrn.*`), GitHub의 quant 관련 저장소를 수집하고 `src/lib/content/research-radar.json`을 갱신한다.
4. JSON에 변경이 있으면 워크플로가 `main`에 커밋하고 Pages 배포 워크플로를 명시적으로 실행한다.
5. 홍콩 시간 월요일에는 `send_weekly_radar.py`가 지난 완료 주간의 목록으로 이메일을 작성한다. 기존 SMTP secrets와 `NEWSLETTER_TO`가 설정된 경우 발송하며, 미설정이면 HTML 미리보기 artifact를 남긴다. 기존 일간 이메일 작업도 별도로 계속 실행된다.

관련 코드: [수집기](../pipeline/build_research_radar.py), [주간 메일](../pipeline/send_weekly_radar.py), [화면](../src/routes/research-radar/+page.svelte), [워크플로](../.github/workflows/daily-research-newsletter.yml).

## 검증 기록

- 초기 데이터 생성 때 축소한 실서비스 API 수집을 수행했고, 기관·SSRN·GitHub 항목이 JSON에 채워지는 것을 확인했다.
- `npm run validate` 통과: Svelte 검사, lint, 정적 빌드.
- `pipeline/test_research_radar.py`의 Python 테스트 4개 통과. 완료 주간 선택과 첫 주 GitHub 기준 별 수 표시를 포함한다.
- 초기 데이터 커밋의 Pages 배포 성공과 공개 페이지 응답을 확인했다.
- 가장 최근에 확인한 **Daily Research Newsletter** 성공 실행은 [run 39702947406](https://github.com/data-roh/asia-stock-market-research/actions/runs/39702947406)이다. 이 실행은 Radar 도입 *이전* 커밋 `fc5fd...`에 대한 것이다. 새 Radar 워크플로의 실제 정기 실행 성공으로 해석하지 않는다.

## 현재의 해석과 확인할 항목

- GitHub의 `stars7d`는 첫 수집일에는 기준 기록이 없어 90개 모두 `null`이다. 현재 화면의 8개는 첫 주에 보여주는 기준 저장소이며 **최근 7일 별 상승 순위가 아니다**. 매일 스냅샷이 누적되고 7일 전 기준값이 생긴 뒤 증가량을 표시한다.
- SSRN 목록은 Crossref에 등록된 SSRN DOI 중 선택한 quant 주제의 제목이 일치하는 일부 논문이다. 날짜는 DOI 등록일이며 SSRN 게시일과 다를 수 있다. SSRN 다운로드 인기 순위나 SSRN 전체 목록은 제공하지 않는다.
- 기관 자료는 출처의 공개 제목·메타데이터·발췌문과 원문 링크를 표시한다. 일부 페이지는 자동 접근을 거절하거나 정확한 발행일을 제공하지 않는다. 원문 전체를 읽거나 자체적으로 요약했다는 뜻은 아니다.
- 새 워크플로의 **첫 정기 실행과 자동 데이터 커밋·Pages 재배포**는 아직 확인되지 않았다. 다음 실행의 스캔, Radar 생성, Git push, 배포 단계를 Actions에서 확인해야 한다.
- 첫 월요일의 주간 메일 **실제 발송 여부**도 아직 확인되지 않았다. 수신을 원하면 저장소의 기존 SMTP 관련 secrets와 `NEWSLETTER_TO` 설정 및 월요일 실행 결과를 확인해야 한다. 비밀값은 이 문서에 기록하지 않는다.
- 첫 주의 7일 별 증가량은 기준 기록이 7일 이상 쌓인 후 확인한다. 데이터는 최신 전체 검색 결과가 아닌 발견한 저장소의 일별 별 수를 비교한다.

## 운영 확인 위치

- [Actions: Daily Research Newsletter](https://github.com/data-roh/asia-stock-market-research/actions/workflows/daily-research-newsletter.yml)
- [Actions: Pages deployment](https://github.com/data-roh/asia-stock-market-research/actions/workflows/deploy.yml)
- [Radar 데이터](../src/lib/content/research-radar.json)
- [README 운영 설명](../README.md)
