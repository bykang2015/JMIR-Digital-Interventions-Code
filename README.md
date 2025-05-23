# JMIR Digital Interventions Analysis Code

## 📄 논문 정보
**제목:** Digital Interventions for Reducing Loneliness and Depression in Korean College Students: Mixed Methods Evaluation

**저자:** Boyoung Kang, MBA, ME; Munpyo Hong, PhD

**저널:** JMIR Formative Research 2024;8:e58791

**DOI:** [10.2196/58791](https://doi.org/10.2196/58791)

## 📊 연구 개요
COVID-19 팬데믹 이후 대학생들의 외로움과 우울증 감소를 위한 디지털 중재(Woebot, Happify)의 효과성을 평가한 혼합 연구방법론 연구

- **참여자:** 63명 모집 → 27명 최종 분석
- **기간:** 4개월
- **대상:** 성균관대학교 대학생 (18-27세)

## 💻 분석 코드 파일

### 1. 주요 지표 변화 분석
- **`PHQ9&UCLA_Loneliness_Trend code.ipynb`**
  - PHQ-9 (우울증) 점수 변화 분석
  - UCLA 외로움 척도 변화 분석
  - 그룹간 비교 분석

### 2. 신뢰도 분석 (Cronbach's Alpha)
- **`baseline_cronbach.ipynb`** - 기준선 신뢰도 분석
- **`1month_cronbach.ipynb`** - 1개월 후 신뢰도 분석  
- **`2month_cronbach.ipynb`** - 2개월 후 신뢰도 분석
- **`post_cronbach.ipynb`** - 사후 신뢰도 분석

### 3. 행동 및 태도 분석
- **`(sum)behavior belief.ipynb`** - 행동 믿음 및 태도 가설 검증

### 4. 정신건강 리터러시 분석
- **`Self-report_literacy.ipynb`** - 자가보고 정신건강 리터러시 수준 분석

## 📈 주요 결과
- 중재군과 대조군 모두에서 외로움과 우울 점수 감소 관찰
- 그룹간 차이는 통계적으로 유의하지 않음 (UCLA 외로움: p=.67, PHQ-9: p=.35)
- 질적 데이터에서 사용자 만족도와 개인화 개선 요구 확인

## 🔒 데이터 요청
연구 데이터가 필요하시면 연구 목적을 명시하여 연락주세요.
- **연락처:** bykang2015@gmail.com
- 데이터 사용 동의서 작성 필요

## 🛠 분석 환경
- **플랫폼:** Google Colab
- **언어:** Python
- **주요 라이브러리:** pandas, numpy, matplotlib, seaborn, scipy

## 📞 연락처
**교신저자:** 강보영 (Boyoung Kang)  
**이메일:** bykang2015@gmail.com  
**소속:** 성균관대학교
