# Extract_package
이 프로젝트는 영화진흥위원회에서 일별 박스 오피스 데이터를 추출하여 Parquet 파일로 저장합니다. 데이터는 날짜별로 정리되며, 추출 날짜의 타임스탬프를 포함합니다.


## 목차

- [필요 조건](#필요-조건)
- [설치](#설치)
- [모듈 기능](#모듈-기능)

## 필요 조건

- Python 3.x
- `requests` 라이브러리
- `pandas` 라이브러리
- `pyarrow` 라이브러리 (Parquet 파일 저장을 위해 필요)

## 설치
- repository 설치 방법
```
git clone https://github.com/5Zigo-Gri-jo/Extract.git
```

- 설치 이후 환경설정
```
pdm init
pdm install
source .venv/bin/activate
```

## 모듈 기능
extract_package.py
- 영화진흥위원회 오픈 API 기능을 통해 지정한 년도의 박스오피스 데이터를 ``` request ```받아 저장하는 모듈입니다.


