---
title: "[Cheat Sheet] '코드 한줄로 EDA를 하는 도구가 있다면?!"
cover: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1920&h=1080&fit=crop"
date: 2023-11-21
categories:
  - [personal-study, cheat_sheet]
tags: []
toc: true
---
## 🚦 Summary
- 이번 포스팅에서는 데이터 분석 및 AI모델링의 가장 기본적 단계인 EDA를 손쉽게 하기 위한 도구를 소개합니다.
- 샘플 데이터로는 seaborn의 대표적 예제데이터인 planets.csv 파일을 사용합니다.
- 이 라이브러리를 사용하면 수십줄에 달하는 EDA 코드를 딱 1줄의 코드로 구현할 수 있습니다.
- 전통적인 EDA 방법과의 비교를 위해 실제 데이터를 불러와서 EDA 하는 코드를 직접 작성했습니다.
- 대용량의 파일에 대해서는 리포트 생성에 다소 많은 시간이 필요하지만, 간단하게 데이터를 살펴보고 분석 방향 및 데이터 전처리 방향을 설정하기에 유용한 도구라 생각합니다.

---


## 📌Intro

- 일반적으로 EDA를 함에 있어 가장 많이 활용되는 것은 Pandas입니다. 
- 보통 이 pandas를 통해 데이터의 `info()`를 살펴보거나, `describe()`를 통해 각종 통계량을 살펴보기도 하며, 데이터의 결측치나 correlation 등을 살펴보며 데이터의 특성과 패턴을 파악하고 분석 방향을 잡는데 활용합니다.
- 포트폴리오 등을 만들때는 데이터에 대한 EDA를 점진적으로 하면서 통계량을 확인해서 의미를 유추해보고, 데이터의 성질을 파악한 뒤, 전처리를 거쳐 각 데이터를 시각화 하는 과정을 실습해 보는 것은 매우 좋은 일입니다. 다만 이는 많은 시간을 소모하는 일이기도 합니다.
- 이러한 EDA과정을 (기존의 방식보다는 덜 세세할 수 있지만) 간단한 코드 몇줄로 빠른 시간안에 할 수 있도록 도와주는 module이 ydata profiling입니다. 이미 공개된지는 좀 오래된 툴이지만 손쉽게 사용할 수 있다는 점에서 강점이 있고, 빠르게 데이터를 살펴볼때 유용하다 생각합니다.
- ydata profiling은 Interactive한 결과를 통해 데이터의 전체적인 overview, correlation이 높은 feature, feature별 결측치 정도 등을 즉각적으로 확인할 수 있습니다. 

---


### 작업에 필요한 기본 라이브러리 불러오기

```python
# 기초 전처리
import pandas as pd

# 컬럼 전체 확인 가능하도록 출력 범위 설정
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)

# 불필요한 경고 표시 생략
import warnings
warnings.filterwarnings(action = 'ignore')

# pandas 결과값의 표현 범위 소수점 2자리수로 변경
pd.options.display.float_format = '{:.2f}'.format

# 파일 로드위한 directory 확인 및 현재 경로로 설정
import os
a = os.getcwd()
os.chdir(a)
```

## Normal Pandas with EDA

- Intro에서 말한 가장 기본적인 EDA 기법들 몇가지를 사용해 EDA를 진행해보겠습니다. 

- 실질적인 비교를 위해서는 시각화 코드도 몇개 넣어 보는게 좋을 것 같습니다.

- 데이터는 seaborn을 학습하기 위한 샘플 코드로 유명한 planets.csv 파일을 사용해 보겠습니다.

- planets 데이터는 외계행성에 대한 관측데이터를 포함하는 데이터로, 행성이름, 발견방법, 연도, 질량, 거리, 궤도주기 등에 대한 정보를 담고 있는 데이터셋 입니다.

    - 일반적으로 시각화를 위한 다양한 형태의 데이터를 가지고 있고, seaborn의 대표적인 예제 데이터중 하나입니다.

```python
import pandas as pd
planets_data= pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv')
```

### 기본정보 및 통계요약 확인

```python
display(planets_data.info())
display(planets_data.describe())
planets_data.head()
```



RangeIndex: 1035 entries, 0 to 1034
Data columns (total 6 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  


0   method          1035 non-null   object 
 1   number          1035 non-null   int64  
 2   orbital_period  992 non-null    float64
 3   mass            513 non-null    float64
 4   distance        808 non-null    float64
 5   year            1035 non-null   int64  
dtypes: float64(3), int64(2), object(1)
memory usage: 48.6+ KB


None









### 'method' 컬럼의 빈도수 그래프(countplot)

- 각 행성발견 방법별 빈도수를 시각화 합니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.countplot(y='method', data=planets_data)
plt.title('Frequency of Discovery Methods')
plt.show()
```

![](https://i.imgur.com/z9rYlwd.png)

### 'year' 컬럼별 발견된 행성의 수(bar plot)

- 연도별로 발견된 행성의 수를 막대 그래프로 시각화 합니다.

```python
discovery_years = planets_data['year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
discovery_years.plot(kind='bar')
plt.title('Number of Planets Discovered Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Planets Discovered')
plt.show()
```

![](https://i.imgur.com/Gezxovb.png)

- 위와 같이 데이터의 개요를 살펴보고, 원하는 컬럼에 대해 시각화를 하기위해 수십줄의 코드를 작성해야만 합니다. 

- 물론 이를 위해 소요되는 시간도 만만치 않습니다. 

- 반면에 ydata profiling은 어떨까요?

## Fancy Pandas with EDA

```python
# install ydata profiling 
# !pip install ydata-profiling
```

### 데이터 불러오기

```python
# 라이브러리 불러오기
import ydata_profiling
from ydata_profiling import ProfileReport
```

### 주요 기능 설명

- 리포트 생성하기

    - 분석할 데이터프레임명에 `profile_report()` 를 사용해 프로파일링한 리포트를 생성할 수 있습니다.

        - 이 경우 즉각적으로 리포트 결과가 출력됩니다.

    - 또는 ProfileReport(df, title = '타이틀 입력') 의 방식으로 리포트를 생성할 수 있습니다.

        - 생성된 리포트는 `profile.to_widgets()` 를 통해 확인할 수 있습니다.

- **그 외 출력되는 리포트에 대한 각각의 기능은 아래와 같습니다.**

    - **개요(Overview)**: 데이터셋의 기본 정보, 변수의 개수, 누락된 값의 수, 메모리 사용량 등을 제공합니다.

    - **변수(Variables)**: 각 변수에 대한 상세 분석을 제공합니다. 이에는 통계적 요약, 분포, 고유한 값들의 리스트, 누락된 값의 수 등이 포함됩니다.

    - **상호작용(Interactions)**: 변수 간의 상호작용을 시각적으로 보여줍니다. 예를 들어, 산점도를 통해 두 변수 간의 관계를 확인할 수 있습니다.

    - **상관 관계(Correlations)**: 변수 간의 상관 관계를 다양한 방법(피어슨, 스피어만 등)으로 계산하고 시각화합니다.

    - **누락된 데이터(Missing values)**: 데이터의 누락된 부분과 그 패턴을 분석하고 시각화합니다.

    - **샘플(Sample)**: 데이터셋의 헤드와 테일, 즉 처음과 끝 부분의 샘플을 제공합니다.

```python
# 즉시 생성 예시
planets_data.profile_report()
```


Summarize dataset:   0%|          | 0/5 [00:00

Generate report structure:   0%|          | 0/1 [00:00

Render HTML:   0%|          | 0/1 [00:00




- 생성파일을 html로 저장할 수 도 있습니다.

- 코드창에 출력된 결과가 보기 다소 불편하다거나, 외부에 공유가 필요하다면 html파일을 만들어서 사용하는 것이 유용합니다.

- 생성된 html파일은 작업중인 노트북의 경로아래 저장됩니다.

```python
planets_data.profile_report().to_file("your_report.html")
```


Summarize dataset:   0%|          | 0/5 [00:00

Generate report structure:   0%|          | 0/1 [00:00

Render HTML:   0%|          | 0/1 [00:00

Export report to file:   0%|          | 0/1 [00:00
- 정석에 따라 다양한 EDA를 하기위한 코드를 작성하는 것보다 훨씬 빠르게 데이터에 대한 다양한 EDA를 할 수 있음을 확인했습니다.

## ✔️ Outro

- ydata-profiling은 데이터를 분석하기에 앞서 필수과정인 EDA를 빠르게 진행하기 위한 강력한 도구입니다.

- 다만 대용량의 데이터에서 대해서는 처리 시간이 길어 질 수 있으니 이 점을 고려해야 합니다.

- 하지만 이 라이브러리를 잘 이용한다면 데이터에 대한 포괄적인 이해를 할 수 있고, 보고서의 각 탭을 통해 데이터의 전반적인 특징, 잠재적인 문제점을 파악해 데이터 분석 또는 모델 설계를 위한 방향성을 빠르게 잡을 수 있습니다.

Resource : [Exploring your data with just 1 line of Python](https://towardsdatascience.com/exploring-your-data-with-just-1-line-of-python-4b35ce21a82d)

