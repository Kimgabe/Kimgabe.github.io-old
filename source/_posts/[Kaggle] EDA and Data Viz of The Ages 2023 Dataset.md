---
title: "[Shadowing] EDA and Data Viz of The Ages 2023 Dataset"
cover: "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=1920&h=1080&fit=crop"
date: 2025-07-18
categories:
  - [personal-study, shadowing]
tags: []
toc: true
---
The Ages 2023 Dataset을 활용해 EDA를 수행한 Kaggle의 코드를 쉐도잉하며 정리했습니다.



# EDA and Data Visualization 📈 of The Ages 2023 Dataset



    





    📌 Dataset Link: https://www.kaggle.com/datasets/lasaljaywardena/age-dataset-2023



## Intro

Kaggle의 EDA and Data Viz 📈 of The Ages 2023 Dataset 을 쉐도잉한 내용입니다.

- 페이지 링크 : https://www.kaggle.com/code/lasaljaywardena/eda-and-data-viz-of-the-ages-2023-dataset

- 코드 자체를 쉐도잉 하면서 4가지 작업을 추가로 진행했습니다.

1) 코드 주석 재작성 및 추가

2) 분석한 내용에 대한 해석

3) 분석 결과에 대한 생각

4) 일부 코드 수정 및 변경(더 나은 분석 및 가독성 위해)

## Dataset 설명

- 여러 국가의 인구 통계에 대한 데이터

- 개인정보, 출생 및 사망 이벤트, 성별, 직업, 관련국가 등의 다양한 지표를 포함하고 있음

- 인구동태, 인간생활의 다양한 측면 분석 등에 이용 가능

### column 설명

- Id : 각 개인에 대한 고유 식별자 

- Name : 사람의 이름

- Short description : 개인에 대한 간단한 설명 또는 요약

- Gender : 개인의 성별

- Country : 거주 및 출생국가

- Occupation : 개인의 직업

- Birth year : 출생년도

- Death year : 사망년도

- Manner of death : 사망원인

- Age of death : 사망당시 나이

- Associated countried : 관련된 국가

# EDA 시작

## Download Additional Libraries

```python
# `missingno` 라이브러리를 설치
# missingno는 누락된 데이터를 시각화하는 데 도움을 주는 라이브러리
# `--quiet` 옵션은 설치 과정 중 불필요한 출력을 줄이는 명령어
# 주피터 노트북에서 라이브러리를 설치할때는 명령어 앞에 '!'를 반드시 붙여야 한다.
!pip install missingno --quiet
```



[notice] A new release of pip is available: 23.0.1 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip

## Import Libraries

```python
# 필요한 라이브러리들을 임포트
# tqdm: 진행률 표시바를 제공하는 라이브러리
from tqdm import tqdm
# pandas: 데이터 분석 및 조작을 위한 라이브러리
import pandas as pd
# numpy: 배열 및 행렬 연산을 위한 라이브러리
import numpy as np
# missingno: 누락된 데이터를 시각화하는 라이브러리
import missingno as msno
# matplotlib 및 seaborn: 데이터 시각화 라이브러리
import matplotlib.pyplot as plt
import seaborn as sns
# wordcloud: 단어 구름 시각화를 생성하는 라이브러리
from wordcloud import WordCloud
# folium 및 FastMarkerCluster: 지도 시각화 라이브러리
import folium
from folium.plugins import FastMarkerCluster

# 주피터 노트북에서 그래프를 인라인으로 표시하기 위한 설정
%matplotlib inline
```

```python
# 경고 메시지를 숨기기 위한 설정

# warnings: 파이썬에서 경고 메시지를 제어하는 라이브러리
import warnings

# 실행 중인 코드의 경고 메시지를 숨김
warnings.filterwarnings('ignore')

# 문자열의 최대 출력 길이를 설정
pd.set_option('display.max_colwidth', None) # 추가한 부분
```

## Load Dataset

```python
# os 모듈을 사용하여 현재 경로를 확인
import os

# 현재 작업 디렉터리의 경로를 가져오기
current_path = os.getcwd()

# CSV 파일의 상대 경로를 지정
csv_file_path = os.path.join(current_path, 'ages_dataset.csv')

# pandas를 사용하여 CSV 파일을 읽기
import pandas as pd
df = pd.read_csv(csv_file_path)
```

## Initial EDA 🔍 (Explolatory Data Analysis)

```python
# 데이터셋의 처음 5행을 확인하는 코드
# 이를 통해 데이터의 구조 및 내용을 빠르게 확인 가능
df.head()
```





```python
# 데이터셋의 기본적인 정보를 확인하는 코드
# 컬럼명, 데이터 타입, 누락된 값 등 확인 가능

df.info()
```



RangeIndex: 1223009 entries, 0 to 1223008
Data columns (total 13 columns):
 #   Column                                    Non-Null Count    Dtype  
---  ------                                    --------------    -----  


0   Id                                        1223009 non-null  object 
 1   Name                                      1223009 non-null  object 
 2   Short description                         1155109 non-null  object 
 3   Gender                                    1089363 non-null  object 
 4   Country                                   887500 non-null   object 
 5   Occupation                                1016095 non-null  object 
 6   Birth year                                1223009 non-null  int64  
 7   Death year                                1223008 non-null  float64
 8   Manner of death                           53603 non-null    object 
 9   Age of death                              1223008 non-null  float64
 10  Associated Countries                      854316 non-null   object 
 11  Associated Country Coordinates (Lat/Lon)  854316 non-null   object 
 12  Associated Country Life Expectancy        854079 non-null   object 
dtypes: float64(2), int64(1), object(10)
memory usage: 121.3+ MB


```python
# 데이터셋의 수치형 컬럼들에 대한 기본 통계 정보를 확인하는 코드
# (평균, 표준편차, 최소값, 25%, 50%, 75% 백분위수, 최대값)

df.describe()
```





### 지수로 표현되는 값 정수로 바꾸기(pandas)

```python
# df의 표시값이 너무 길면 위와 같이 지수로 표현됨
# 이를 일반 정수로 바꾸려면 pandas의 출력 옵션을 바꿔야 함

import pandas as pd

pd.set_option('display.float_format', '{:.2f}'.format)

df.describe()
```





Birth year (출생 연도)

- count: 1,223,009

    - count는 해당 컬럼에 있는 데이터의 총 개수

    - 즉 전체 데이터에 1,223,009 명에 대한 출생연도 데이터가 있음

- mean: 약 1845년

    - mean은 평균값으로 여기서는 전체 데이터의 출생 연도의 평균이 1845년임을 의미

- std: 약 147.9년

    - std는 표준편차를 나타내며, 데이터의 분산 정도를 의미

    - 출생 연도의 표준편차가 147.9년으로 출생 연도 데이터가 평균 1845년 주변에서 약 148년 정도의 범위로 흩어져 있음을 의미

- min: -2700

    - min은 해당 컬럼의 최소값. 가장 오래된 출생 연도는 기원전 2700년으로 해석 될 수 있음

- 25%: 1828년

    - 25%는 1사분위수를 나타내며, 전체 데이터의 25%가 이 값 이하임을 의미. 즉, 25%의 사람들은 1828년 이전에 태어났음을 알 수 있음.

- 50%: 1887년

    - 50%는 중앙값(전체 데이터의 중간에 위치하는 값). 즉, 중앙값이 1887년이라는 것은 전체 데이터의 중간에 위치하는 사람의 출생 연도가 1887년임을 의미

- 75%: 1918년

    - 75%는 3사분위수(전체 데이터의 75%가 이 값 이하임을 의미). 즉, 75%의 사람들은 1918년 이전에 태어났음을 알 수 있음.

- max: 2016년

    - max는 해당 컬럼의 최대값을 의미. 여기서는 '연도' 데이터이므로 가장 최근의 출생 연도가 2016년임을 의미.

Death year (사망 연도)

- count: 1,223,008

    - 해당 컬럼에 있는 데이터의 총 개수가 1,223,008로 전체 데이터에 1,223,008 명에 대한 사망연도 데이터가 있다는 의미

- mean: 약 1914년

    - mean은 평균값으로 여기서는 전체 데이터의 사망 연도의 평균이 1914년임을 의미

- std: 약 151.7년

    - 사망 연도의 표준편차가 151.7년으로 사망 연도 데이터가 평균 1914년 주변에서 약 152년 정도의 범위로 흩어져 있음을 의미

- min: -2659

    - min은 해당 컬럼의 최소값. 가장 오래된 사망 연도는 기원전 2659년으로 해석 될 수 있음

    - 하지만 데이터셋이 사람의 '나이'임을 감안했을때 해당 데이터는 이상치(outlier)라고 판단하는 것이 적합

- 25%: 1895년

    - 25%는 1사분위수를 나타내며, 전체 데이터의 25%가 이 값 이하임을 의미. 즉, 25%의 사람들은 1895년 이전에 사망했음을 알 수 있음.

- 50%: 1955년

    - 50%는 중앙값. 즉, 중앙값이 1955년이라는 것은 전체 데이터의 중간에 위치하는 사람의 사망 연도가 1955년임을 의미

- 75%: 1994년

    - 75%는 3사분위수. 즉, 75%의 사람들은 1994년 이전에 사망했음을 알 수 있음.

- max: 2021년

    - max는 해당 컬럼의 최대값. 여기서는 '연도' 데이터이므로 가장 최근의 사망 연도가 2021년임을 의미.

Age of death (사망 나이)

- count: 1,223,008

- 해당 컬럼에 있는 데이터의 총 개수가 1,223,008이며 이는 전체 데이터에 1,223,008 명에 대한 사망 나이 데이터가 있음을 의미

- mean: 약 69.3세

    - mean은 평균값으로 여기서는 전체 데이터의 사망 나이의 평균이 69.3세임을 의미

- std: 약 16.6세

    - std는 표준편차를 나타내며, 데이터의 분산 정도를 의미

    - 사망 나이의 표준편차가 16.6세로 사망 나이 데이터가 평균 69.3세 주변에서 약 17세 정도의 범위로 흩어져 있음을 의미

- min: 0세

    - min은 해당 컬럼의 최소값. 즉, 0세에 사망한 경우도 있음을 의미

- 25%: 60세

    - 25%는 1사분위수. 즉, 25%의 사람들은 60세 이전에 사망했음을 알 수 있음.

- 50%: 72세

    - 50%는 중앙값. 즉, 중앙값이 72세라는 것은 전체 데이터의 중간에 위치하는 사람의 사망 나이가 72세임을 의미

- 75%: 81세

    - 75%는 3사분위수. 즉, 75%의 사람들은 81세 이전에 사망했음을 알 수 있음

- max: 169세

    - max는 해당 컬럼의 최대값. 여기서는 '나이' 데이터이므로 가장 오래 살았던 사람의 나이가 169세임을 의미

### describe 요약

#### 1. Birth year (출생 연도)

- 총 1,223,009명의 데이터가 있음

- 평균 출생 연도는 약 1845년

- 출생 연도의 표준편차는 약 147.9년

- 가장 오래된 출생 연도는 약 기원전 2700년이며, 가장 최근의 출생 연도는 2016년

- 25%의 사람들은 1828년 이전에 태어났으며, 중앙값(50%)은 1887년, 75%의 사람들은 1918년 이전에 태어났음

#### 2. Death year (사망 연도)

- 총 1,223,008명의 사망 연도 데이터가 있음 (1명의 사망 연도 정보가 누락되었음).

- 평균 사망 연도는 약 1914년

- 사망 연도의 표준편차는 약 151.7년

- 가장 오래된 사망 연도는 약 기원전 2659년이며, 가장 최근의 사망 연도는 2021년

- 25%의 사람들은 1895년 이전에 사망하였으며, 중앙값(50%)은 1955년, 그리고 75%의 사람들은 1994년 이전에 사망하였음

#### 3. Age of death (사망 시 나이)

- 총 1,223,008명의 사망 시 나이 데이터가 있음

- 평균 사망 시 나이는 약 69.3세

- 사망 시 나이의 표준편차는 약 16.6세

- 가장 어린 사망 나이는 0세 (출생 직후 사망한 경우)이며, 가장 높은 사망 나이는 169세

- 25%의 사람들은 60세 이전에 사망하였으며, 중앙값(50%)은 72세, 그리고 - 75%의 사람들은 81세 이전에 사망하였음

#### 이 결과를 통해 알 수 있는 것:

- 이 데이터셋에는 고대부터 최근까지의 사람들에 대한 정보가 포함되어 있음

- 대부분의 사람들은 60세에서 81세 사이에 사망하였음

- 몇몇 사람들은 매우 오래 전 (기원전)에 태어났고 사망하였음

- 사망연도에는 이상치 데이터가 분포해 있을 수 있음

## Data Cleaning 🧹 - Drop Unwanted Columns

```python
# Drop the "id" column
# 분석에 불필요한 컬럼(메모리 세이브)
df = df.drop('Id', axis=1)
```

```python
# drop 결과 확인
df.head()
```





## Data Cleaning 🧹 - Null Values

```python
# 각 컬럼별로 누락된 데이터의 개수를 확인
df.isnull().sum()
```


Name                                              0
Short description                             67900
Gender                                       133646
Country                                      335509
Occupation                                   206914
Birth year                                        0
Death year                                        1
Manner of death                             1169406
Age of death                                      1
Associated Countries                         368693
Associated Country Coordinates (Lat/Lon)     368693
Associated Country Life Expectancy           368930
dtype: int64

### column별 null데이터 시각화

```python
# 누락된 값의 시각화를 위한 설정
sns.set(style='whitegrid', font_scale=1.2)

# 데이터셋의 각 컬럼별 누락된 값의 비율을 바 차트로 시각화
# 'Blues' 색상 팔레트를 사용하며, 컬럼의 개수에 따라 색상의 변화를 표현
# 파라미터 설명 msno.bar(시각화할 데이터, bar pot의 색상, 그래프크기, fontsize, df의 값 표기 여부)
# 색상 지정: seaborn의 color_palette함수를 이용해 Blues 색상 팔레트에서 현재 df의 컬럼수 만큼 색상을 생성(n_colors)
msno.bar(df, color=sns.color_palette('Blues', n_colors=len(df.columns)), figsize=(10, 6), fontsize=12, labels=True)

# 그래프의 제목, x축, y축 라벨을 설정
plt.title('Non-Null Value Visualization Before Cleaning', fontsize=16)
plt.xlabel('Columns', fontsize=14)
plt.ylabel('Percentage of Missing Values', fontsize=14)

# x축의 라벨을 45도 기울여서 표시하며, 라벨의 오른쪽을 기준으로 정렬
plt.xticks(rotation=45, ha='right')

# 그래프의 레이아웃을 조정
plt.tight_layout()

# 그래프를 표시
plt.show()
```



- 컬럼별 결측치 분포를 시각화 하여 확인

### 결측치(null values) 제거

```python
# For Visualization Purposes:
# Lets Drop rows with null values in 'occupation', 'associated_countries', and 'death_year'
df = df.dropna(subset=['Occupation', 'Associated Countries', 'Death year'], how='any')

# dropna 옵션
# subset : 누락된 값을 체크할 컬럼 입력
# how : 누락된 값을 어떻게 제거할지 정의
# any 선택시 : subset에 지정된 컬럼중 하나라도 누락된 값을 포함하는 행 제거
# all 선택시 : subset에 지정된 모든 컬럼이 누락된 값을 가질경우 해당 행만 제거
```

- null값이 있는 데이터를 그대로 시각화 하면 데이터에 대한 왜곡된 정보를 제공할 수 있음

- 여기서는 분석에 중요한 영향이 있으리라 생각되는 주요 3개 컬럼(occupation, associated_countries, Death year)에 대한 결측치를 drop

- 물론 이 3개의 데이터가 중요한지 아닌지는 분석가의 가설에 의한 것

```python
# drop한 결과 확인
df.info()
```



Int64Index: 782779 entries, 0 to 1223008
Data columns (total 12 columns):
 #   Column                                    Non-Null Count   Dtype  
---  ------                                    --------------   -----  


0   Name                                      782779 non-null  object 
 1   Short description                         778748 non-null  object 
 2   Gender                                    713089 non-null  object 
 3   Country                                   782779 non-null  object 
 4   Occupation                                782779 non-null  object 
 5   Birth year                                782779 non-null  int64  
 6   Death year                                782779 non-null  float64
 7   Manner of death                           44874 non-null   object 
 8   Age of death                              782779 non-null  float64
 9   Associated Countries                      782779 non-null  object 
 10  Associated Country Coordinates (Lat/Lon)  782779 non-null  object 
 11  Associated Country Life Expectancy        782555 non-null  object 
dtypes: float64(2), int64(1), object(9)
memory usage: 77.6+ MB

### null drop 결과 시각화

```python
# 시각화 설정
sns.set(style='whitegrid', font_scale=1.2)

# 결측치가 아닌 값의 비율을 바 차트로 시각화
msno.bar(df, color=sns.color_palette('Blues', n_colors=len(df.columns)), figsize=(10, 6), fontsize=12, labels=True)

# 그래프 제목 설정
plt.title('Non-Null Value Visualization After Cleaning', fontsize=16)

# x축, y축 라벨 설정
plt.xlabel('Columns', fontsize=14)
plt.ylabel('Percentage of Missing Values', fontsize=14)

# x축 라벨 각도 조정
# 컬럼명이 길어서 겹칠 수 있기 때문
plt.xticks(rotation=45, ha='right')

# 그래프 레이아웃 최적화
plt.tight_layout()

# 그래프 표시
plt.show()
```



## Drilling Deeper Into EDA 🔍 - Correlations

```python
# 원본 데이터(df)를 보존하기 위해 복사본을 만들고 EDA수행
# EDA에서 발생하는 전처리나 데이터 조정이 원본데이터에 영향을 미치지 않게 하기 위함
eda_df = df.copy()
```

### Correlation Heatmap

```python
# 수치형 특성들 간의 상관 관계를 계산
correlation_matrix = eda_df.corr()

# 상관 관계를 표시할 히트맵의 크기 설정
plt.figure(figsize=(6, 4))

# 상관 관계 히트맵 생성
# annot=True는 각 셀에 상관 계수 값을 표시하게 하며, cmap='Blues'는 파란색 계열의 색상 팔레트를 사용
# linewidths=0.5는 셀 간 경계선의 두께를 설정
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', linewidths=0.5)

# 그래프의 제목 설정
plt.title('Correlation Heatmap', fontsize=12)

# 그래프 레이아웃 최적화
plt.tight_layout()

# 그래프 표시
plt.show()
```



- 상관관계는 1~-1 사이의 값을 가지며 1에 가까울수록 양의 상관관계, -1에 가까울 수록 음의 상관관계를 가짐

    - 즉 1에 가까우면 특정 값이 증가하는데 다른 컬럼의 영향이 큰 것이고

    - 반대로 -1에 가까우면 특정값이 감소하는데 다른 컬럼의 영향이 큰 것

- Birth year와 가장 상관관계가 큰 것은 Death year로(0.99) 사람이 태어난 연도와 사망한 연도가 매우 밀접하게 연관되어 있음을 의미

    - 태어난 연도가 최근일수록 사망한연도도 최근일 가능성이 높음

- Birth year와 Age  of death의 상관관계는 0.13으로 사실상 거의 연관성이 없는 지표임을 의미

    - 즉, 특정 연도에 태어난 사람이 반드시 더 길게 혹은 짧게 살지는 않는 다는 것을 의미

- Death year와 Age of death의 상관계수는 0.28로 어느정도는 양의 상관성이 있음을 의미

    - 최근에 사망한 사람들이 과거에 사망한 사람들보다 약간 더 오래 살 확률이 있을 '수도' 있음

    - Death year의 값이 클수록 Age of Death의 값도 큰 경향을 보이기 때문

    - 이러한 상관관계의 원인을 더 명확하게 조사하거나 추가적인 데이터를 살펴볼 필요가 있음

### Dendrogram

- 결측데이터의 유사도를 기반으로 변수들을 클러스터링 한 결과

- 어떤 변수들이 서로 유사한 패턴의 결측치를 가지고 있는지를 확인할 수 있음

- 변수들을 비교하며 비슷한 누락 패턴을 가질수록 서로 인접하여 그래프가 그려짐

- 분기(branch)가 높을 수록(아래로 내려갈 수록) 두 변수의 패턴이 더 다르다는 것을 의미

```python
# 상관 관계를 시각화하기 위한 덴드로그램의 크기 설정
plt.figure(figsize=(12, 12))

# 데이터프레임의 결측치에 대한 덴드로그램 생성
# 이 덴드로그램은 변수들 사이의 결측치의 유사도를 기반으로 클러스터링을 수행
msno.dendrogram(df, fontsize=12)

# 그래프의 제목 설정
plt.title('Dendrogram', fontsize=16)

# 그래프 표시
plt.show();
```






- 첫번째 분기 : Associated countrie와 Associated country life expectancy는 dendrogram상에서 가장 먼저 연결된 변수들임

    - 이는 두 변수의 데이터 패턴이 매우 유사함을 의미

- 두번째 분기 : Associated countrie와 Associated country life expectancy의 군집이 Short description과 연결되어 있음

    - 이는 Short description이 Associated countrie와 Associated country life expectancy변수와 어느정도 유사도가 있음을 의미

- 세번째 분기 : Short description과 Gender가 연결되어 있음

    - 즉, 두 변수간에 어느정도 유사한 패턴이 있음을 의미

    - 단 첫번째 분기에서 나온 변수간의 유사도 보다는 낮음

- 네번째 분기 : Gender와 Manner of death가 연결되어 있음

    - 이전 모든 변수들과 비교했을때 manner of death는 가장 유사도가 낮음을 의미

## Data Preprocesing ⚒️

```python
# 원본 데이터(df)를 보존하기 위해 복사본을 만들고 전처리수행
processed_df = df.copy()
```

### 신규컬럼(Number of Citizenships) 생성

```python
# 기존 데이터를 바탕으로 신규 데이터 생성
# 특정 객체(사람)이 얼마나 많은 국가와 연관되어 있는지 파악하기 위한 컬럼
# 다중국적 또는 여러 국가와 연관성을 갖는 객체(사람)을 파악할 수 있음
tqdm.pandas()
processed_df['Number of Citizenships'] = processed_df['Country'].progress_apply(lambda x: len(x.split(';')))
```


100%|█████████████████████████████████████████████████████████████████████| 782779/782779 [00:00

```python
def calculate_average(value):
    # 문자열로 된 값을 실제 값(리스트, 숫자 등)으로 변환
    try:
        val = eval(value)
    except:
        # 변환 중 오류 발생 시 NaN 반환
        return np.nan
    
    # 변환된 값의 평균 반환
    return np.mean(val)
```

```python
# 원본 데이터의 Associated Country Life Expectancy 값에 calculate_average함수 적용한 값
# 각 개체(사람)와 연관된 국가들의 기대 수명값을 평균으로 바꾼뒤, 해당 개체의 예상 수명을 계산
processed_df['Expected Life Expectancy'] = df['Associated Country Life Expectancy'].progress_apply(calculate_average)
```


100%|██████████████████████████████████████████████████████████████████████| 782779/782779 [00:06

```python
processed_df.head()
```





```python
# [1,2,3] 형태와 같은 '배열' 로 저장된 csv 데이터를 불러올때 다시 '배열' 형태로 변환하는 함수

def convert_string_to_array(value):
    try:
        # eval 함수를 사용하여 문자열을 Python 표현식으로 해석하려고 시도
        val = eval(value)
        # 해석된 값을 반환
        return val
    # 위의 시도 중에 오류가 발생하면 except 블록이 실행
    except:
        # 오류가 발생하면 np.nan (NaN 값)을 반환
        return np.nan
```

### csv파일(df)의 string 데이터를 배열(array)값으로 변환

- convert_string_to_array를 적용해 array형태로 변환

```python
processed_df["Associated Countries"] = processed_df["Associated Countries"].progress_apply(convert_string_to_array)
```


100%|██████████████████████████████████████████████████████████████████████| 782779/782779 [00:03

```python
processed_df["Associated Country Coordinates (Lat/Lon)"] = processed_df["Associated Country Coordinates (Lat/Lon)"].progress_apply(convert_string_to_array)
```


100%|██████████████████████████████████████████████████████████████████████| 782779/782779 [00:04

```python
processed_df["Associated Country Life Expectancy"] = processed_df["Associated Country Life Expectancy"].progress_apply(convert_string_to_array)
```


100%|██████████████████████████████████████████████████████████████████████| 782779/782779 [00:03

```python
# 작업 결과 확인
processed_df.iloc[:,-5:-2].head()
```





### 여러개의 값을 가진 컬럼을 배열(array)로 변경

```python
def break_string_to_array(value):
    # 만약 입력값이 float 형태라면, NaN 값을 반환
    # 입력값이 결측치인 경우를 처리하기 위한 조건
    if type(value) == float:
        return np.nan
    
    # 입력값 내에 세미콜론(;)이 있을 경우 해당 문자를 기준으로 문자열을 분리
    if ";" in value:
        arr = value.split(";")
    # 세미콜론이 없는 경우 입력값 자체를 원소로 가진 배열을 생성
    else:
        arr = [value]
    
    # 생성된 배열의 각 원소(문자열) 앞뒤의 공백을 제거
    arr = [x.strip() for x in arr]
    
    # 최종적으로 처리된 배열을 반환
    return arr
```

```python
processed_df['Occupation'] = processed_df['Occupation'].progress_apply(break_string_to_array)
```


100%|█████████████████████████████████████████████████████████████████████| 782779/782779 [00:00

```python
processed_df['Manner of death'] = processed_df['Manner of death'].progress_apply(break_string_to_array)
```


100%|█████████████████████████████████████████████████████████████████████| 782779/782779 [00:00

```python
def get_first_value_only(value):
    # 만약 입력값이 float 형태라면, NaN 값을 반환
    # 입력값이 결측치인 경우를 처리하기 위한 조건
    if type(value) == float:
        return np.nan
    
    # 입력값 내에 세미콜론(;)이 있을 경우 해당 문자를 기준으로 문자열을 분리
    if ";" in value:
        arr = value.split(";")
    # 세미콜론이 없는 경우 입력값 자체를 원소로 가진 배열을 생성
    else:
        arr = [value]
    
    # 생성된 배열의 각 원소(문자열) 앞뒤의 공백을 제거
    arr = [x.strip() for x in arr]
    
    # 배열의 첫 번째 원소만을 반환
    return arr[0]
```

```python
processed_df["Gender"] = processed_df["Gender"].progress_apply(get_first_value_only)
```


100%|█████████████████████████████████████████████████████████████████████| 782779/782779 [00:00

```python
# 작업 결과 확인
processed_df[['Gender','Occupation','Manner of death']].head()
```





## Data Visualization - Visualizing the Gender Distribution

```python
# 'Gender' 컬럼의 각 값별로 발생 횟수를 카운트
gender_counts = processed_df['Gender'].value_counts()

# 'Male'과 'Female'이 아닌 나머지 성별 값들의 총 합을 계산
others_count = gender_counts[~gender_counts.index.isin(['Male', 'Female'])].sum()
# 'Male'과 'Female'만을 포함하는 새로운 카운트 정보를 가져오기
gender_counts = gender_counts[gender_counts.index.isin(['Male', 'Female'])]
# 나머지 성별 값을 'Others'로 합하여 추가
gender_counts['Others'] = others_count

# pyplot을 사용하여 파이 차트를 생성
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.2f%%', colors=sns.color_palette('pastel'))
plt.title('Gender Distribution')
plt.axis('equal')  # 이 설정을 통해 파이 차트를 원형으로 시각화

# 파이 차트를 화면에 출력
plt.show()
```



## Data Visualization - Ages at which People Died

- 데이터상으로 어떤 연령대에서 사람들이 사망했는지 시각화

```python
# 'Age of death' 컬럼을 기반으로 각 연령대별 사람 수를 계산
count = [
    # 100세 초과 사람 수
    processed_df[processed_df['Age of death'] > 100].shape[0],
    # 91세부터 100세 사이의 사람 수
    processed_df[(processed_df['Age of death']  90)].shape[0],
    # 71세부터 90세 사이의 사람 수
    processed_df[(processed_df['Age of death']  70)].shape[0],
    # 51세부터 70세 사이의 사람 수
    processed_df[(processed_df['Age of death']  50)].shape[0],
    # 50세 이하 사람 수 (전체에서 위의 카운트를 제외한 나머지)
    processed_df.shape[0] - (processed_df[processed_df['Age of death'] > 100].shape[0]
                  + processed_df[(processed_df['Age of death']  90)].shape[0]
                  + processed_df[(processed_df['Age of death']  50)].shape[0]
                  + processed_df[(processed_df['Age of death']  70)].shape[0])
]

# 각 연령대를 나타내는 레이블을 정의
age_ranges = ['Age above 100', 'Age between 91 and 100', 'Age between 71 and 90', 'Age between 51 and 70', 'Age below 50']

# 100세 초과 연령대를 강조하기 위해 첫 번째 조각을 돋보이게 설정
explode = [0.1, 0, 0, 0, 0]

# 사용할 색상 팔레트를 Seaborn에서 정의
palette_color = sns.color_palette('pastel')

# pyplot을 사용하여 파이 차트를 생성
plt.figure(figsize=(12, 8))
plt.pie(count, labels=age_ranges, colors=palette_color, explode=explode, autopct='%.2f%%')
plt.title("At What Age Did these People Die?")
plt.axis('equal')  # 파이 차트를 원형으로 시각화

# 파이 차트를 화면에 출력
plt.show()
```



- 대부분의 사람들이 71~90세 사이에 사망

- 이어서 41 ~ 70세 사이에 사망

- 50세 이하의 사망률은 비교적 낮은편으로 100세를 초과하여 사망한 사례는 거의 없음

## Data Visualization - Top 10 Most Represented Countries

```python
# 'Associated Countries' 컬럼에 있는 배열들을 개별 행으로 변환 (explode()를 사용)
# 하나의 행에 [a, b]와 같은 배열로 되어 있다면 두개의 행으로 분리
df_exploded =  processed_df.explode('Associated Countries')

# 'Associated Countries' 컬럼에 있는 각 나라의 발생 횟수를 카운트
top_countries = df_exploded['Associated Countries'].value_counts().reset_index()
# 컬럼명을 'Country'와 'Count'로 변경
top_countries.columns = ['Country', 'Count']

# 상위 10개의 가장 많이 나타난 나라들만을 필터링
top_countries = top_countries.head(10)

# Seaborn을 사용하여 상위 10개 나라에 대한 막대 그래프를 생성
plt.figure(figsize=(10, 6))
sns.barplot(data=top_countries, x='Count', y='Country', palette='viridis')
plt.title('Top 10 Most Represented Countries')
plt.xlabel('Number of People')
plt.ylabel('Country')
plt.show()
```



## Data Visualization - Birth Year Distibution

```python
# 'Birth year' 컬럼의 값이 0보다 큰 데이터를 filtered_df에 저장
# 이렇게 하면 0 이하의 출생 연도(예: 기원전)는 제외됨
filtered_df = processed_df[processed_df['Birth year'] > 0]

# filtered_df에서 'Birth year'별로 데이터를 그룹화하고, 각 연도별 발생 횟수를 카운트
birth_year_counts = filtered_df['Birth year'].value_counts().reset_index()
# 결과 데이터프레임의 컬럼명을 'Birth year'와 'Count'로 변경
birth_year_counts.columns = ['Birth year', 'Count']
# 'Birth year' 기준으로 데이터를 정렬
birth_year_counts = birth_year_counts.sort_values('Birth year')

# 250 단위로 데이터가 없는 연도에 대해 0으로 추가
for year in range(0, 2001, 250):
    if year not in birth_year_counts['Birth year'].values:
        new_row = {'Birth year': year, 'Count': 0}
        birth_year_counts = birth_year_counts.append(new_row, ignore_index=True)
        
birth_year_counts = birth_year_counts.sort_values('Birth year')

plt.figure(figsize=(10, 6))

# Seaborn을 사용하여 'Birth year'별 사람 수를 선 그래프로 시각화
sns.lineplot(data=birth_year_counts, x='Birth year', y='Count', color='b')
plt.title('Birth Year Distribution') 
plt.xlabel('Birth Year')
plt.ylabel('Number of People')
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# x축 250 단위로 데이터 추출해 표로 나타내기
table_data = birth_year_counts[birth_year_counts['Birth year'] % 250 == 0]
# 표의 텍스트 크기와 위치/크기를 조정
plt.table(cellText=table_data.values, colLabels=table_data.columns, cellLoc = 'center', loc='bottom', bbox=[0, -0.5, 1, 0.4], fontsize=8)

# 그래프와 표 간격 조정
plt.subplots_adjust(left=-0.5, bottom=-0.6)

plt.show()
```



- 데이터의 대부분의 사람들이 1500년 이후에 태어났음

    - 원인이되는 역사적 사실을 고려해볼 필요 있음

## Data Visualization - Common Ways People Have Died

```python
# 'Manner of death' 컬럼을 기준으로 각 리스트 항목별로 행을 분리해 exploded_df에 저장
exploded_df = processed_df.explode('Manner of death')

# 상위 10개 사망 원인을 top_10_ways_of_death에 저장
top_10_ways_of_death = exploded_df['Manner of death'].value_counts().nlargest(10)

# Seaborn으로 상위 10개 사망 원인의 막대 그래프 그리기
plt.figure(figsize=(10, 6))
sns.countplot(data=exploded_df, x='Manner of death', order=top_10_ways_of_death.index, palette='muted')
plt.title('Top 10 Causes of Death')
plt.xlabel('Manner of Death')
plt.ylabel('Number of People')
# x축 라벨 회전
plt.xticks(rotation=45, ha='right')
# y축 그리드 표시
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
```



- 대부분은 자연사(natural causes)에 의해 사망함

- 이어서 자살(suicide) 또는 사고사(accident)인 경우가 가장 많았음

- 그 다음으로는 타살(homicide)과 사형(capital punishment)이 많음

## Data Visualization - What Occupation did they do?

```python
# 'Occupation' 컬럼을 기준으로 각 직업 항목별로 행을 분리해 exploded_df에 저장
exploded_df = processed_df.explode('Occupation')

# 각 직업별 사람 수를 occupation_counts에 저장
occupation_counts = exploded_df['Occupation'].value_counts()

# 상위 10개 직업을 top_10_occupations에 저장
top_10_occupations = occupation_counts.head(10)

# Seaborn으로 상위 10개 직업의 수평 막대 그래프 그리기
plt.figure(figsize=(10, 8))
sns.barplot(y=top_10_occupations.index, x=top_10_occupations.values, palette='muted')
plt.title('Top 10 Occupations')
plt.xlabel('Number of People')
plt.ylabel('Occupation')
# x축 라벨 회전 없음
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```



- 전체 데이터에서 Top10 직업에 대한 count를 시각화

- 가장 많은 수를 차지한 직업은 예술가(Artist), 2순위는 정치가(politician)였고, 3순위는 운동선수(Athlet)이며

- 이어서 조사관(Researcher), 군인(Military personnel), 종교 관련종사자(religious figure), 건축가(architect), 사업가(business person), 기자(journalist), 교사(teacher)순으로 나타났음

## In-Depth Visualization - Life Expectancy vs Gender

```python
# 그래프의 크기 설정 (가로 10, 세로 7)
plt.figure(figsize=(10, 7))

# 결측치를 제외한 processed_df 데이터를 사용하여 바이올린 플롯 생성
# x축은 'Gender', y축은 'Age of death'로 설정하며, 색상 팔레트는 'mako' 사용
# 바이올린 내부에는 각 데이터 포인트를 표시하는 스틱 표시 사용
sns.violinplot(data=processed_df.dropna(), x='Gender', y='Age of death', palette='mako', inner='stick')

# 그래프의 제목 설정
plt.title('Age of Death Distribution for Different Genders')

# x축과 y축 라벨 설정
plt.xlabel('Gender')
plt.ylabel('Age of Death')

# x축 라벨의 위치와 회전 각도 조정
plt.xticks(rotation=45, ha='right')

# 그래프를 화면에 표시
plt.show()
```



- violin plot은 데이터의 분포를 보여주는 Plot

    - 폭(width)가 넓을 수록 해당 데이터 범위에 많은 데이터 포인트가 있음을 의미

    - 길이(length)는 데이터의 전체 분포 범위를 의미

    - 바이올린의 중앙선은 데이터의 중앙값(median)을 의미

    - 플롯내의 가로선은 개별 데이터의 값을 의미

- 전반적으로 대부분의 데이터는 Male 또는 Female에 분포되어 있음

- Male의 경우 60~80세 사이에 많이 사망하는 경향이 있음

- Female의 경우 Male에 비해 상대적으로 고르게 사망하고 있으나 그래도 60~80세 사이의 분포가 가장 많음

- Transgender Female의 경우 20대 중반~40대 사이에 주로 사망

- Intersex는는 사망연령의 범위가 '-20에서 110' 사이로 매우 광범위하지만 대체로 40~60세 사이에 사망

- Transgender Male의 경우 약 70세에 주로 사망하고 있음

## In-Depth Visualization - Life Expectancy vs Birth Year

```python
# 1700년 이후의 'Birth year'를 가진 데이터만 필터링하여 filtered_df에 저장
# 이 때, NaN 값을 포함하는 행은 제거
filtered_df = processed_df[(processed_df['Birth year'] > 1700)].dropna()

# 10x7 크기의 그래프 영역을 생성
f, ax = plt.subplots(figsize=(10, 7))

# scatterplot을 사용하여 'Birth year'을 x축, 'Age of death'을 y축으로 하는 산점도를 그린다
# 점의 크기는 10, 색상은 'Birth year' 값에 따라 mako 팔레트를 사용하며 범례는 표시하지 않는다
sns.scatterplot(data=filtered_df, x='Birth year', y='Age of death', s=10, hue='Birth year', palette='mako', legend=False)

# kdeplot을 사용하여 'Birth year'과 'Age of death'의 밀도 분포를 그린다
# 밀도의 레벨은 10으로 설정하고, 밀도 선의 색상은 흰색, 선의 두께는 1로 설정
sns.kdeplot(data=filtered_df, x='Birth year', y='Age of death', levels=10, color="w", linewidths=1)

# 그래프를 출력
plt.show()
```



- 데이터에 있는 대부분의 사람들이 1850이후에 태어났음

- 데이터상 대부분의 사람들은 20~100세 사이에 사망했음

- KDE원의 중심점을 보면 1930~40년대에 태어난 사람들중 대다수가 70세 정도의 나이에서 사망하는 경향이 있음

- 또한 1870년대에서 태어난 사람들은 대략 50대 중후반의 나이에 사망한 경향이 있음

## Advanced Visualization - Is there a link Between Country and Manner of Death?

- 국가별 사망원인이 뚜렷하게 구분되지 않아 TOP3 원인을 별도로 추출하고 색상을 부여해 하이라이트 되도록 수정

```python
# 'Associated Countries'와 'Manner of death' 컬럼을 통해 데이터를 개별의 rows로 분할
exploded_df = processed_df.explode('Associated Countries').explode('Manner of death').reset_index(drop=True)

# 상위 20개 국가 추출
top_20_countries = exploded_df['Associated Countries'].value_counts().nlargest(20)

# 전체 사망 원인 중 상위 10개 추출
top_10_manner_of_death = exploded_df['Manner of death'].value_counts().nlargest(10)

# 상위 3개 사망 원인 추출
top_3_manner_of_death = exploded_df['Manner of death'].value_counts().nlargest(3).index

# 추출된 상위 20개 국가 및 상위 10개 사망 원인으로 데이터 필터링
filtered_df = exploded_df[exploded_df['Associated Countries'].isin(top_20_countries.index) &
                          exploded_df['Manner of death'].isin(top_10_manner_of_death.index)]

# 국가별 사망 원인 횟수를 교차 테이블로 생성
ct = pd.crosstab(filtered_df['Associated Countries'], filtered_df['Manner of death'])

# 교차 테이블의 컬럼 순서를 색상 팔레트 순서에 맞게 재정렬
ordered_columns = list(top_3_manner_of_death) + [col for col in top_10_manner_of_death.index if col not in top_3_manner_of_death]
ct = ct[ordered_columns]

# 상위 3개 사망 원인에 대한 하이라이트 색상 지정
highlight_colors = ['#e74c3c', '#f39c12', '#3498db']
# 나머지 7개 사망 원인에 대한 색상 팔레트 정의
palette_colors = highlight_colors + sns.color_palette('viridis', 7).as_hex()

# 스택 바 차트 생성
plt.figure(figsize=(16, 8))  # 그래프 크기 설정
ax = ct.plot(kind='bar', stacked=True, ax=plt.gca(), color=palette_colors)  # 스택 바 차트를 그립니다.
plt.title('Top 20 Countries with Top 10 Causes of Death', fontdict={'fontsize': 20})  # 그래프 제목 설정
plt.xlabel('Associated Countries')  # x축 레이블 설정
plt.ylabel('Number of Deaths')  # y축 레이블 설정
plt.xticks(rotation=45, ha='right')  # x축 눈금 레이블의 회전 각도와 정렬 설정
plt.legend(title='Manner of death', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 16})  # 범례 설정
plt.tight_layout()  # 그래프의 레이아웃을 최적화
plt.show()  # 그래프를 화면에 출력
```



- 상위 20개 국가별 사망원인 Top10을 시각화한 결과

- 국가별로 보면 공통적으로 자연사(natural causes),사고사(accident), 자살(suicide)이 주요 사망원인으로 나타남

- 일부 차이는 있으나 자연사가 주요 사망요인점은 동일하고, 자살과 사고사는 구간별로 순위에 차이가 있으나 둘다 top3안에 드는 요인임

- 나머지 사망원인도 국가별로 뚜렷한 차이는 보이지 않음

---


- 주어진 데이터만으로는 국가와 특정 사망원인간의 관계를 발견하기는 어려움. 이유는 여러가지가 있음

1) 숫자의 함정 : 사망자수가 많은 국가는 대체로 인구가 많은 국가일 가능성이 높음. 인구수에 비례해 사망자수를 조절하지 않으면 인구가 많은 국가의 사망원인이 타국의 사망원인보다 중요하게 해석될 수 있음.

2) 다양성 손실 : 유사한 관점에서 20개의 국가만을 대상으로 관계를 규명하려 했다는점이 데이터의 다양성을 손실 시킬 수 있음

3) 누적 막대그래프 자체의 한계 : 지금 그래프와 같이 특정 사망원인(자연사)가 dominent한 경우 다른 원인들간의 차이를 표로 구분할 수가 없음. 실제로 지금 그래프를 봐도 Top4를 제외하고는 국가별로 다른 원인에 대한 중요도나 차이를 구별하기 어려움

4) 인과관계 부족 : 위 그래프는 국가와 사망원인간 관계를 표면적으로는 보여주지만, 특정 국가에서 특정원인으로 인한 사망이 왜 높은가에 대한 설명을 하기에는 부족한 자료.

## Geo Visualization with Associated Countries

```python
# processed_df의 복사본을 생성하여 지도 플로팅용 데이터로 사용
map_df = processed_df.copy()

# 'Associated Countries'와 'Associated Country Coordinates (Lat/Lon)' 컬럼을 통해 데이터를 개별 rows로 분할
map_df = map_df.explode('Associated Countries')
map_df = map_df.explode('Associated Country Coordinates (Lat/Lon)')

# 'Associated Country Coordinates (Lat/Lon)' 컬럼이 NaN인 데이터를 제거
map_df = map_df.dropna(subset=["Associated Country Coordinates (Lat/Lon)"])

# 'Associated Country Coordinates (Lat/Lon)' 컬럼에서 위도와 경도를 추출
map_df['Lat'] = map_df['Associated Country Coordinates (Lat/Lon)'].apply(lambda x: pd.Series(x[0]))
map_df['Lon'] = map_df['Associated Country Coordinates (Lat/Lon)'].apply(lambda x: pd.Series(x[1]))

# 위도나 경도 정보가 누락된 행 제거
map_df = map_df.dropna(subset=['Lat', 'Lon'], how="any")

# Folium을 사용하여 지도를 생성. 초기 위치는 위도 20, 경도 0으로 설정하고, 줌 레벨은 2로 설정
folium_map = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB dark_matter')

# FastMarkerCluster를 사용하여 위도와 경도 정보를 바탕으로 클러스터를 지도에 추가
FastMarkerCluster(data=list(zip(map_df['Lat'].values, map_df['Lon'].values))).add_to(folium_map)

# 지도에 레이어 제어 기능 추가
folium.LayerControl().add_to(folium_map)

# 지도 표시
folium_map
```

Make this Notebook Trusted to load map: File -> Trust Notebook

## First Name World Cloud

```python
# 'Name' 컬럼에서 첫 번째 이름(이름의 첫 부분)만 추출하여 'first_names_df'에 저장.
# 'expand=True'는 각 이름 부분을 별도의 컬럼으로 분리하며, [0]은 첫 번째 컬럼(즉, 첫 번째 이름)만 선택.
# 'str.strip()'은 문자열의 앞뒤 공백을 제거하고, 'str.title()'은 첫 글자만 대문자로 바꾸어 이름을 표준화.
first_names_df = processed_df['Name'].str.split(expand=True)[0].str.strip().str.title()

# 중복을 제거한 첫 이름의 집합을 생성
unique_first_names = set(first_names_df)

# 모든 고유한 첫 이름을 하나의 문자열로 결합
all_first_names = ' '.join(unique_first_names)

# WordCloud 객체를 생성하여 첫 이름 데이터로 워드 클라우드를 생성
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_first_names)

# 워드 클라우드 시각화
plt.figure(figsize=(10, 5))  # 그래프의 크기 설정
plt.imshow(wordcloud, interpolation='bilinear')  # 워드 클라우드 이미지 표시, 'bilinear'는 이미지를 부드럽게 표시
plt.axis('off')  # x, y 축 눈금과 레이블을 표시하지 않음
plt.title('Word Cloud of First Names', fontsize=16)  # 그래프의 제목 설정
plt.show()  # 그래프 출력
```



## Last Name World Cloud

```python
# 'Name' 컬럼에서 두 번째 이름(이름의 두 번째 부분, 일반적으로 성)만 추출하여 'last_names_df'에 저장.
# 'expand=True'는 각 이름 부분을 별도의 컬럼으로 분리하며, [1]은 두 번째 컬럼(즉, 성)만 선택.
# 'str.strip()'은 문자열의 앞뒤 공백을 제거하고, 'str.title()'은 첫 글자만 대문자로 바꾸어 이름을 표준화.
last_names_df = processed_df['Name'].str.split(expand=True)[1].str.strip().str.title()

# 중복을 제거한 성의 집합을 생성하고, 결측값(None 값) 제거
unique_last_names = set(last_names_df.dropna())

# 모든 고유한 성을 하나의 문자열로 결합
all_last_names = ' '.join(unique_last_names)

# WordCloud 객체를 생성하여 성 데이터로 워드 클라우드를 생성
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_last_names)

# 워드 클라우드 시각화
plt.figure(figsize=(10, 5))  # 그래프의 크기 설정
plt.imshow(wordcloud, interpolation='bilinear')  # 워드 클라우드 이미지 표시, 'bilinear'는 이미지를 부드럽게 표시
plt.axis('off')  # x, y 축 눈금과 레이블을 표시하지 않음
plt.title('Word Cloud of Last Names', fontsize=16)  # 그래프의 제목 설정
plt.show()  # 그래프 출력
```



### 위 코드는 Kaggle의 EDA and Data Viz 📈 of The Ages 2023 Dataset 을 쉐도잉한 내용입니다.

- 페이지 링크 :https://www.kaggle.com/code/lasaljaywardena/eda-and-data-viz-of-the-ages-2023-dataset

- 코드 자체를 쉐도잉 하면서 분석한 내용에 대한 해석, 저만의 생각을 몇가지 추가로 더 작성해 보았습니다.

