# JMIR Digital Interventions Analysis Code

## 📄 출간 논문 정보
**제목:** Digital Interventions for Reducing Loneliness and Depression in Korean College Students: Mixed Methods Evaluation  
**저자:** Boyoung Kang, MBA, ME; Munpyo Hong, PhD  
**저널:** JMIR Formative Research 2024;8:e58791  
**DOI:** [10.2196/58791](https://doi.org/10.2196/58791)

## 📊 연구 개요
COVID-19 팬데믹 이후 대학생들의 외로움과 우울증 감소를 위한 디지털 중재(Woebot, Happify)의 효과성을 평가한 혼합 연구방법론 연구

* **참여자:** 63명 모집 → 27명 최종 분석
* **기간:** 4개월  
* **대상:** 성균관대학교 대학생 (18-27세)

## 💻 분석 코드 파일

### 📈 출간 논문 분석 (JMIR Formative Research)

**1. 주요 지표 변화 분석**
* `PHQ9&UCLA_Loneliness_Trend code.ipynb`
   * PHQ-9 (우울증) 점수 변화 분석
   * UCLA 외로움 척도 변화 분석
   * 그룹간 비교 분석

**2. 신뢰도 분석 (Cronbach's Alpha)**
* `baseline_cronbach.ipynb` - 기준선 신뢰도 분석
* `1month_cronbach.ipynb` - 1개월 후 신뢰도 분석  
* `2month_cronbach.ipynb` - 2개월 후 신뢰도 분석
* `post_cronbach.ipynb` - 사후 신뢰도 분석

**3. 행동 및 태도 분석**
* `(sum)behavior belief.ipynb` - 행동 믿음 및 태도 가설 검증

**4. 정신건강 리터러시 분석**
* `Self-report_literacy.ipynb` - 자가보고 정신건강 리터러시 수준 분석

### 🔍 박사논문 추가 분석 (심화 연구)

**5. 개별 참가자 궤적 분석**
* `individual_trajectory_analysis.py` - **NEW!** 
   * 개별 참가자 변화 궤적 시각화
   * 반응자/비반응자 분류 (Löwe et al., 2004 기준)
   * 치료 반응 패턴 분석 (포물선, 지연반응, 조기반응, 악화)
   * 소표본 연구의 개인차 탐색

**주요 특징:**
- **반응자 정의**: PHQ-9 ≥5점 감소, UCLA ≥10점 감소
- **패턴 감지**: 자동 궤적 패턴 분류
- **시각화**: 그룹별/반응자별 차별화된 표시
- **종합 리포트**: 반응률, 패턴 분석, 주목 사례

## 📈 주요 결과

### 출간 논문 결과
* 중재군과 대조군 모두에서 외로움과 우울 점수 감소 관찰
* 그룹간 차이는 통계적으로 유의하지 않음 (UCLA 외로움: p=.67, PHQ-9: p=.35)  
* 질적 데이터에서 사용자 만족도와 개인화 개선 요구 확인

### 박사논문 추가 발견
* **개인별 치료 반응의 이질성**: 동일 중재에도 매우 상이한 반응 양상
* **지연 반응 패턴**: 일부 참가자는 중간 시점 악화 후 호전
* **반응자 비율**: 그룹별로 상이한 임상적 개선 비율 확인
* **포물선 궤적**: 특정 참가자들의 독특한 변화 패턴 (예: P24의 14→19→13→6)

## 🔒 데이터 요청
연구 데이터가 필요하시면 연구 목적을 명시하여 연락주세요.
* **연락처:** bykang2015@gmail.com
* 데이터 사용 동의서 작성 필요

## 🛠 분석 환경
* **플랫폼:** Google Colab, Local Python Environment
* **언어:** Python
* **주요 라이브러리:** pandas, numpy, matplotlib, seaborn, scipy

## 📚 인용 정보

### 출간 논문 인용
```bibtex
@article{kang2024digital,
  title={Digital Interventions for Reducing Loneliness and Depression in Korean College Students: Mixed Methods Evaluation},
  author={Kang, Boyoung and Hong, Munpyo},
  journal={JMIR Formative Research},
  volume={8},
  pages={e58791},
  year={2024},
  publisher={JMIR Publications},
  doi={10.2196/58791}
}
```

### 개별 궤적 분석 인용
박사논문에서의 개별 궤적 분석을 사용하시는 경우:
```
Kang, B. (2024). Individual trajectory analysis for digital mental health interventions. 
Doctoral dissertation, Sungkyunkwan University. 
Code available: https://github.com/bykang2015/JMIR-Digital-Interventions-Code
```

## 📞 연락처
**교신저자:** 강보영 (Boyoung Kang)  
**이메일:** bykang2015@gmail.com  
**소속:** 성균관대학교

---

## 🆕 업데이트 로그
- **2024.06**: 개별 참가자 궤적 분석 코드 추가 (`individual_trajectory_analysis.py`)
- **2024.03**: JMIR Formative Research 논문 출간
- **2024.01**: 초기 분석 코드 업로드
