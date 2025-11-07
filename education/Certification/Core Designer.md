### **Dataiku Academy**

- **아카데미 주소: https://academy.dataiku.com/**
- **Certifications > Core Designer Certificate**


---

### **프로젝트 Flow**

#### **1. 프로젝트 생성 및 데이터 불러오기**
1. Dataiku 홈 화면에서 **+ New Project** 클릭
2. **Blank project** 선택
3. **Dataset Import** (Tip. Import 시 Schema 체크하기)
    - `CO2_and_Oil`
    - `Meat_and_Egg_Production`
    - `Urbanization_GDP_and_Population`

---
<br>


#### **2. 데이터 결합 (Join Recipe)**
- **세 개의 Dataset을 하나의 Dataset으로 Join**
  - 기준파일: `CO2_and_Oil`
  - Key값: `Entity`, `Code`, `Year`

---
<br>

#### **3. 데이터 필터링 (Sample/Filter Recipe)**
- **`Year` 컬럼이 2008년부터 2012년까지의 데이터만 포함되도록 필터링**

---
<br>

#### **4. 데이터 준비 (Prepare Recipe)**
1. **파생변수 생성**</br>
아래 세 개의 컬럼(국가 총계)을 **1인당(per-capita)** 기준으로 변환 
  - **방법**: 각 컬럼을 **Formula**기능을 활용해 `해당 컬럼 값 / Population`으로 계산
  - Tip. 컬럼명은 자유롭게 설정 
  - **대상 컬럼**
      - `Oil production (Etemad & Luciana) (terawatt-hours)`
      - `meat_prod_tonnes`
      - `Food Balance Sheets: Eggs - Production (FAO (2017)) (tonnes)`
      
2. **컬럼 삭제(4개)**
  - `Population`
  - `Oil production (Etemad & Luciana) (terawatt-hours)`
  - `meat_prod_tonnes`
  - `Food Balance Sheets: Eggs - Production (FAO (2017)) (tonnes)`
  
3. **행 삭제(filtering)**
  - `Entity` 컬럼 값이 **world**인 **행 제거**

4. **결측치 대체**
  -  4-1에서 계산한**per-capita 컬럼(3개)**에 대한 **결측치 대체 (대체값 = 0)**

---
<br>

#### **5. 데이터 그룹별 집계 (Group Recipe)**
1. **[4. 데이터 준비] 단계에서 생성된 Dataset 사용**
2. `Group By`값 `Entity`
3. `Code`, `Year`를 **제외한 나머지 컬럼들**에 대해서 `Avg`값 집계

---
<br>

#### **6. 데이터 랭크 (Window Recipe)**
1. 다시 **[4. 데이터 준비] 단계에서 생성된 Dataset 사용**
2. (좌측 옵션) **Windows definions** 설정
    - `PARTITONING COLUMNS`값 `YEAR`
    -  `ORDER COLUMNS`값 `Per capita CO₂ emissions (tonnes per capita)` 컬럼
3. (좌측 옵션) **Aggregations** 설정
    - `Compute`값 `Rank`만 설정
4. (좌측 옵션) **Post-filter** 설정
    - ```rank <= 25```
