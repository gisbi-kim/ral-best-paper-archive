# RA-L Best Paper Archive

IEEE Robotics and Automation Letters Best Paper Award 수상 논문 검색 사이트.

## 실행

압축을 풀고 `index.html`을 브라우저에서 열면 됩니다. 설치나 빌드, API 키는 필요 없습니다. 인터넷 연결은 논문 링크를 열 때만 필요합니다.

## 수록 범위

- 시상 연도 2017–2026의 본상 수상 논문 39편
- 제목, 저자 목록, 확인된 소속, 한국어 내용 요약, 저널 발행 정보, 일부 arXiv 최초 공개일
- 확인된 공개 PDF 링크 24편. 나머지는 논문 자료 또는 검색 링크 제공
- 본상 수상자만 수록하며 후보·최종 후보·RAM 논문상은 포함하지 않음
- 소속은 일부 기관만 확인되었으며, 저자별 전체 소속 대응표가 아님
- 일부 논문은 발행월 및 최초 공개일 정보가 없음. 확인되지 않은 날짜는 추정하지 않음
- 요약은 검색용 간략 설명. 원문 초록 번역이나 상세 리뷰가 아님
- 자료 확인 기준: 2026-11-02

## GitHub Pages에 게시

기존 `gisbi-kim.github.io` 저장소가 아닌 **새 저장소**를 사용합니다.

1. GitHub에서 새 공개 저장소 `ral-best-paper-archive`를 만듭니다.
2. 이 폴더 안의 파일을 저장소 최상위에 업로드하고 `main` 브랜치에 저장합니다. 폴더 자체를 한 단계 더 중첩하지 않습니다.
3. 저장소 Settings → Pages에서 브랜치 배포를 선택하고 `main` / 최상위 폴더를 지정합니다.
4. GitHub가 표시하는 배포 완료 주소를 엽니다. 계정이 `gisbi-kim`이면 예상 주소는 `https://gisbi-kim.github.io/ral-best-paper-archive/`입니다.
5. 제목 검색, 연도 필터, PDF 링크가 정상 동작하는지 확인합니다.

이 패키지 자체는 아직 배포된 사이트가 아닙니다. 기존 홈페이지 파일이나 설정을 수정할 필요가 없습니다.

## 파일

- `index.html`: 화면과 검색·필터 기능
- `data.js`: 브라우저에서 바로 읽는 데이터
- `data.json`: 편집 및 재사용용 원본 데이터
- `update-data.py`: JSON 수정 후 JS 데이터를 다시 만드는 도구
- `.nojekyll`: GitHub Pages 정적 파일 게시용
- `HOSTING_PROMPT.txt`: 다른 컴퓨터의 작업 도구에 전달할 배포 요청문

데이터 변경 시 `data.json`을 수정하고 이 폴더에서 `python3 update-data.py`를 실행한 뒤, `data.json`과 `data.js`를 함께 업로드합니다.

## 출처

- IEEE RAS 공식 수상자: https://www.ieee-ras.org/awards-recognition/publications-awards/ieee-robotics-and-automation-letters-best-paper-award/
- RA-L 논문상 안내: https://www.ieee-ras.org/publications/ra-l/ra-l-paper-awards/
- 개별 논문의 출판사·공개본·자료 링크는 데이터에 포함

PDF 파일 자체는 재배포하지 않습니다. 공개본 링크만 제공합니다. IEEE 공식 사이트가 아닙니다.
