## **ML Practitioner**

### **Dataiku Academy**

- **아카데미 주소: https://academy.dataiku.com/**
- **Certifications > ML Pracitioner Certificate**


---

### **프로젝트 Flow**


#### **0.프로젝트 및 데이터 준비**

1. +New Project 클릭
2. Learning projects 클릭
3. `ML Practitioner Assessment` 선택
4. Create

---

#### **1. 통계 worksheet 확인(필수X)**

1. `schools_data`에서 `Automatically suggest analyses` 통계 분석 수행
2. 컬럼 유형(type) 확인
    - `grade` 컬럼이 `슷자형`으로 인식되었는지 확인
    - `repeated` 컬럼이 `문자형`으로 인식되었는지 확인
3.  차트 그리기
     - repeated 컬럼의 범주 간 차이를 보는 차트 그려보기

---

#### **2. 데이터 분할하기(split)**

- `schools_data`의 `data_perimeter` 컬럼 값에 따라 `train_data`와 `validation_data`로 분할

---

#### **3. 모델 생성**

1. **첫 번째 모델링**
     1. `train_data` 데이터를 활용한 AutoML 진행(타겟컬럼: repeated)
     2. 기본 상태로 train 진행(디자인 변경 없음)
     3. Results 창에서 `Diagnostics` 확인

2. **두 번째 모델링**
     1. `디자인탭`으로 이동
     2. `grade` 컬럼 제외
     3. `Debugging 탭`으로 이동
     4. `Assertions` 추가
          - `travel time >= 2` `AND` `absences >= 8`
          - `Expected class = 1`
          - `With valid ratio >= 22%`
     5. 모델 재훈련
     6. `Session2` 에서 `AUC`가 가장 좋은 모델의 결과 그래프 확인
     7. 모델 `AUC`가 가장 좋은 모델 `배포하기`

---

#### **4. 모델 평가 하기**

1. `Score`레시피와 `validation_data'를 사용해 모델 평가하기
   - 단, 출력 컬럼(Input columns to include)에서 `school`과 `repeated`만 선택


2. 위 과정으로 생성된 데이터셋 `validation_scored` 결과 확인하기
     - 학교별 prediction_correct 의 분포를 분석
     - 특히, 학교별로 정답 예측의 비율 확인
