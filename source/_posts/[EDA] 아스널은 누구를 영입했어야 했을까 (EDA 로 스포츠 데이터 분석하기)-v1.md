---
title: "[EDA] 아스널은 누구를 영입했어야 했을까 (EDA 로 스포츠 데이터 분석하기)"
cover: "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=1920&h=1080&fit=crop"
date: 2020-08-07
categories:
  - [portfolio]
tags:
  - EDA
toc: true
---
스포츠데이터를 EDA하며 간단한 분석을 해보았습니다. 우리팀엔 어떤 선수들이 필요할까?!

# 스포츠 데이터 분석 : 유럽 축구 분석
## 부제 - Arsenal의 부활을 위해 필요한 선수는 누구?!

# Introduction

![season_result](/images/portfolio/season_result.png)

지난 2018년 4월 20일 Arsenal F.C를 20여년간 지도했던 위대한 명장 Arsène Wenger이 성적 부진을 이유로 감독직에서 해임되었다. 

이후 성적 반등을 위해 UEFA 유로파리그 3연패라는 대업을 이룬 Unai Emery 감독을 선임후 1년간의 적응기를 거친뒤 2019-2020시즌 구단의 지원하에 베테랑

및 고가의 몸값을 가진 선수를 성공적으로 영입하며 기대에 부응해줄 것을 고대했다. 

하지만 그의 성적은 한때 리그 10위권 밖으로 내려가는등

EPL이라는 영국 프로축구리그의 Top4로 불리던 옛 영광을 재현하지 못하였고 결국 리그8위라는 처참한 성적을 내고 말았다.
asdfadf

이후 팀의 리빌딩을 위해 Arsenal F.C출신의 레전드 선수 Mikel Arteta를 감독으로 임명하였으나

그 또한 이번 시즌 (2020-2021)을 8위로 마감하며 구단과 팬들의 기대에 부응하지 못하였다.

이러한 구단의 부진에는 두 감독의 부족한 전술운영 능력등에 대한 영향도 있겠지만, Unai Emery 감독이 2019-2020시즌에 1000억이라는 거금으로 영입한 Nicolas Pépé나 베테랑 David Luiz의 부진, 그리고 유망주로서 영입한 선수들이 성장세를 보이지 못한 점 등이 팬들에게 많은 비판을 받고 있다. 

당시에 영입한 선수들로 인한 팀의 부진 등은 현재도 지속되고 있기에 "당시에 어떤 선수를 방출하고 영입했어야 좋았을까?" 라는 팬심을 담아

FIFA 에서 제공하는 2018-2019의 선수데이터를 통해 Arsenal F.C를 분석한 뒤 대체로 영입했으면 좋았을 선수들을 선정해 보겠다.

---------------------------------------------------------------------------------------------------------------------------------


# 데이터 수집

## a. 데이터 불러오기

```python
# 분석에 필요한 모듈 불러오기

import pandas as pd
import os

# 컬럼 전체 확인 가능하도록 출력 범위 설정
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# 불필요한 경고 표시 생략
import warnings
warnings.filterwarnings(action = 'ignore')
```

```python
os.listdir()
```


['.ipynb_checkpoints',
 'FIFA_data(origin).csv',
 'FIFA_data.csv',
 '[EDA] 아스널은 누구를 영입했어야 했을까 (EDA 로 스포츠 데이터 분석하기).ipynb']


```python
# 분석할 데이터 로드
data = pd.read_csv('FIFA_data.csv')
```

```python
# 데이터 확인
data.head()
```





## b. 데이터 확인 및 분석 계획 설립

| 번호 | 컬럼 명           | 컬럼 의미             | 번호 | 컬럼 명           | 컬럼 의미           |
|------|------------------|---------------------|------|------------------|---------------------|
| 1    | ID               | 고유의 번호          | 11   | Skill Moves      | 개인기               |
| 2    | Name             | 이름                | 12   | Position         | 포지션               |
| 3    | Age              | 나이                | 13   | Jersey Number    | 등번호               |
| 4    | Overall          | 현재 능력치         | 14   | Joined           | 소속 팀 입단 날짜    |
| 5    | Potential        | 잠재 능력치         | 15   | Contract Valid Until | 계약 기간         |
| 6    | Club             | 소속 팀             | 16   | Height           | 키 (피트)            |
| 7    | Value            | 예상 이적료 (유로)   | 17   | Weight           | 몸무게 (파운드)      |
| 8    | Wage             | 주급 (유로)         | 18~26| LS ~ RB          | 포지션 별 능력치     |
| 9    | Preferred Foot   | 잘 사용하는 발      | 27~79| Crossing ~ GKReflexes | 세부 능력치     |
| 10   | Weak Foot        | 잘 사용하지 않는 발  | 80   | Release Clause   | 바이아웃            |

### 해당 컬럼들을 이용해서 어떻게 주제에 맞게 분석을 할지 고민

분석 순서

- Arsenal F.C.의 선수들을 분석

- Arsenal F.C.의 지역 라이벌  Chelsea F.C. 선수와 능력치 비교

- 라이벌팀 대비 부족한 포지션 2개 선정

- 다른팀의 선수 중  Arsenal F.C.의 재정, 현실가능성, 영입방침을 고려하여 2명의 선수를 영입

### 본격적 데이터 분석에 앞선 기초 전처리

Value, Wage 등 수치값이지만 화폐단위등과 같이 입력되어 str 형태인 데이터들을 숫자로 변환

분석 데이터가 2020년 데이터 이므로 유로환율을 2020년 평균으로 환산

2020년 유로 평균 환율 = 1,368.16

1M = 1,000,000

1K = 1,000




```python
# 화폐관련 데이터의 각 단위에 맞게 숫자로 변경

# M = 000,000 으로 대체
# K = 000  으로 대체

data['Value'] = data['Value'].str.replace('M','000000')
data['Value'] = data['Value'].str.replace('K','000')
data['Wage'] = data['Wage'].str.replace('M','000000')
data['Wage'] = data['Wage'].str.replace('K','000')
data['Release Clause'] = data['Release Clause'].str.replace('M','000000')
data['Release Clause'] = data['Release Clause'].str.replace('K','000')
```

```python
print(data[['Value', 'Wage','Release Clause']].info())
data[['Value', 'Wage','Release Clause']]
```



RangeIndex: 18207 entries, 0 to 18206
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 


0   Value           18207 non-null  object
 1   Wage            18207 non-null  object
 2   Release Clause  16643 non-null  object
dtypes: object(3)
memory usage: 426.9+ KB
None



18207 rows × 3 columns




숫자 앞의 € 를 제외 하는 작업

인덱싱을 활용하여 1번째 자리에 있는 값부터 그 뒤의 값을 전부 slicing

여러번 반복하면 slicing한 상태에서 또 slincing을 하기 때문에 여러번 반복하지 않도록 주의

```python
data['Value'] = data['Value'].str.slice(1,)

data['Wage'] = data['Wage'].str.slice(1,)

data['Release Clause'] = data['Release Clause'].str.slice(1,)

# 결과 확인
data[['Value', 'Wage','Release Clause']]
```



18207 rows × 3 columns




- M, K 등으로 소수점 이 들어가있던 자료의 소수점을 제거

```python
data['Value'] = data['Value'].str.replace('.','')

data['Wage'] = data['Wage'].str.replace('.','')

data['Release Clause'] = data['Release Clause'].str.replace('.','')

# 결과 확인
print(data[['Value', 'Wage','Release Clause']].info())
data[['Value', 'Wage','Release Clause']]
```



RangeIndex: 18207 entries, 0 to 18206
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 


0   Value           18207 non-null  object
 1   Wage            18207 non-null  object
 2   Release Clause  16643 non-null  object
dtypes: object(3)
memory usage: 426.9+ KB
None



18207 rows × 3 columns




- 문자형으로된 숫자값을 숫자형으로 변환

```python
data['Value'] = data['Value'].astype(float)

data['Wage'] = data['Wage'].astype(float)

data['Release Clause'] = data['Release Clause'].astype(float)

# 결과 확인
print(data[['Value', 'Wage','Release Clause']].info())
```



RangeIndex: 18207 entries, 0 to 18206
Data columns (total 3 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  


0   Value           18207 non-null  float64
 1   Wage            18207 non-null  float64
 2   Release Clause  16643 non-null  float64
dtypes: float64(3)
memory usage: 426.9 KB
None


```python
data[['Value', 'Wage','Release Clause']]
```



18207 rows × 3 columns


--------------------------------------------------------------------------------------------------------------------------




# Arsenal F.C 분석 - Arsenal F.C는 어떤 선수들이 존재하는가?

## a. EDA

```python
# data 의 데이터는 모든 축구선수 데이터를 포함하고 있기 때문에 Arsernal F.C. 선수 데이터 분석을 위해 별도 테이블 생성

gunners = data[data['Club']== 'Arsenal']
```

```python
# 추출된 결과 확인 (Arsenal 선수들만 추출된 것인지) - 2개 모두 가능

#gunners.Club.unique()
gunners['Club'].unique()
```


array(['Arsenal'], dtype=object)


```python
# 추출된 gunners 테이블의 세부 데이터를 print 하여 확인

# print() 함수에 'f'를 입력하면 "" 내에서 변수를 사용 할 수 있다.
# 실행할 함수는 {} 사이에 입력한다.

print(f"아스널 선수들의 총 인원 : {gunners.shape[0]}")  #print(f"총 인원 : {len(gunners)} ") 도 가능
print("\n")

print(f"아스널 선수들의 평균 연령 : {gunners['Age'].mean():.2f}") # "출력할 내용 : .숫자f" 로 소수점 조절 가능 
print("\n")

print(f"아스널 선수들의 포지션 종류 : {gunners['Position'].unique()}")
print("\n")

print(f"아스널 선수들의 평균 능력치 : {gunners['Overall'].mean():.2f}") # "출력할 내용 : .숫자f" 로 소수점 조절 가능 
print("\n")

print(f"아스널 선수들의 평균 잠재 능력치 : {gunners['Potential'].mean():.2f}") # "출력할 내용 : .숫자f" 로 소수점 조절 가능 
```


아스널 선수들의 총 인원 : 33

아스널 선수들의 평균 연령 : 24.61

아스널 선수들의 포지션 종류 : ['LS' 'CAM' 'ST' 'GK' 'RCB' 'RM' 'LCM' 'CB' 'LDM' 'RB' 'LB' 'LM' 'LW'
 'RDM' 'CDM' 'CM']

아스널 선수들의 평균 능력치 : 75.18

아스널 선수들의 평균 잠재 능력치 : 81.39


```python
gunners
```





```python
# 데이터 시각화를 위해 seabron 로드 

import seaborn as sns 
```

```python
# Arsenal F.C의 나이대분포 확인

sns.countplot(gunners['Age'])
```






```python
# Arsenal F.C의 포지션 분포 확인

sns.countplot(gunners['Position'])
```






```python
# 포지션별 능력치 분포에 이상치가 있는지 확인 - boxplot 사용

sns.boxplot(data = gunners, x = 'Position', y = 'Overall')
```






```python
# 포지션별 잠재력 분포에 이상치가 있는지 확인 - boxplot 사용

sns.boxplot(data = gunners, x = 'Position', y = 'Potential')
```






### 결측치 찾기

```python
gunners.info()
```



Int64Index: 33 entries, 33 to 16216
Data columns (total 81 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  


0   Unnamed: 0                33 non-null     int64  
 1   ID                        33 non-null     int64  
 2   Name                      33 non-null     object 
 3   Age                       33 non-null     int64  
 4   Nationality               33 non-null     object 
 5   Overall                   33 non-null     float64
 6   Potential                 33 non-null     float64
 7   Club                      33 non-null     object 
 8   Value                     33 non-null     float64
 9   Wage                      33 non-null     float64
 10  Preferred Foot            33 non-null     object 
 11  International Reputation  33 non-null     float64
 12  Weak Foot                 33 non-null     float64
 13  Skill Moves               33 non-null     float64
 14  Position                  33 non-null     object 
 15  Jersey Number             33 non-null     float64
 16  Joined                    33 non-null     object 
 17  Contract Valid Until      33 non-null     object 
 18  Height                    33 non-null     object 
 19  Weight                    33 non-null     object 
 20  LS                        30 non-null     object 
 21  ST                        30 non-null     object 
 22  RS                        30 non-null     object 
 23  LW                        30 non-null     object 
 24  LF                        30 non-null     object 
 25  CF                        30 non-null     object 
 26  RF                        30 non-null     object 
 27  RW                        30 non-null     object 
 28  LAM                       30 non-null     object 
 29  CAM                       30 non-null     object 
 30  RAM                       30 non-null     object 
 31  LM                        30 non-null     object 
 32  LCM                       30 non-null     object 
 33  CM                        30 non-null     object 
 34  RCM                       30 non-null     object 
 35  RM                        30 non-null     object 
 36  LWB                       30 non-null     object 
 37  LDM                       30 non-null     object 
 38  CDM                       30 non-null     object 
 39  RDM                       30 non-null     object 
 40  RWB                       30 non-null     object 
 41  LB                        30 non-null     object 
 42  LCB                       30 non-null     object 
 43  CB                        30 non-null     object 
 44  RCB                       30 non-null     object 
 45  RB                        30 non-null     object 
 46  Crossing                  33 non-null     float64
 47  Finishing                 33 non-null     float64
 48  HeadingAccuracy           33 non-null     float64
 49  ShortPassing              33 non-null     float64
 50  Volleys                   33 non-null     float64
 51  Dribbling                 33 non-null     float64
 52  Curve                     33 non-null     float64
 53  FKAccuracy                33 non-null     float64
 54  LongPassing               33 non-null     float64
 55  BallControl               33 non-null     float64
 56  Acceleration              33 non-null     float64
 57  SprintSpeed               33 non-null     float64
 58  Agility                   33 non-null     float64
 59  Reactions                 33 non-null     float64
 60  Balance                   33 non-null     float64
 61  ShotPower                 33 non-null     float64
 62  Jumping                   33 non-null     float64
 63  Stamina                   33 non-null     float64
 64  Strength                  33 non-null     float64
 65  LongShots                 33 non-null     float64
 66  Aggression                33 non-null     float64
 67  Interceptions             33 non-null     float64
 68  Positioning               33 non-null     float64
 69  Vision                    33 non-null     float64
 70  Penalties                 33 non-null     float64
 71  Composure                 33 non-null     float64
 72  Marking                   33 non-null     float64
 73  StandingTackle            33 non-null     float64
 74  SlidingTackle             33 non-null     float64
 75  GKDiving                  33 non-null     float64
 76  GKHandling                33 non-null     float64
 77  GKKicking                 33 non-null     float64
 78  GKPositioning             33 non-null     float64
 79  GKReflexes                33 non-null     float64
 80  Release Clause            33 non-null     float64
dtypes: float64(43), int64(3), object(35)
memory usage: 22.4+ KB


```python
# LS ~ RB 컬럼에 3개씩 결측치가 있음
# 어떤 데이터에서 누락이 발생하는지 확인

gunners[gunners.isnull()['LS']]

# 포지션이 GK인 선수는 다른 포지션들의 값이 비어있는 것이 원인
```





```python
# 포지션이 GK인 선수는 다른 포지션에 대한 능력치를 부여할 필요가 없기에 NaN으로 채워져 있는 것으로 가정
# NaN값을 측정할 수 없다는 의미의 -1로 교체
# 다른 데이터 분석시 -값이 존재한다면 -1로 쓰는 것은 의미가 없다. (현재 데이터는 모두 양수값이 기에 사용)

gunners = gunners.fillna(-1)
```

```python
# 결칙치가 잘 대체되었는지 확인

#gunners[gunners['Position']=='GK'] 로 결측치 있던 부분만 재확인 
gunners.info()
```



Int64Index: 33 entries, 33 to 16216
Data columns (total 81 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  


0   Unnamed: 0                33 non-null     int64  
 1   ID                        33 non-null     int64  
 2   Name                      33 non-null     object 
 3   Age                       33 non-null     int64  
 4   Nationality               33 non-null     object 
 5   Overall                   33 non-null     float64
 6   Potential                 33 non-null     float64
 7   Club                      33 non-null     object 
 8   Value                     33 non-null     float64
 9   Wage                      33 non-null     float64
 10  Preferred Foot            33 non-null     object 
 11  International Reputation  33 non-null     float64
 12  Weak Foot                 33 non-null     float64
 13  Skill Moves               33 non-null     float64
 14  Position                  33 non-null     object 
 15  Jersey Number             33 non-null     float64
 16  Joined                    33 non-null     object 
 17  Contract Valid Until      33 non-null     object 
 18  Height                    33 non-null     object 
 19  Weight                    33 non-null     object 
 20  LS                        33 non-null     object 
 21  ST                        33 non-null     object 
 22  RS                        33 non-null     object 
 23  LW                        33 non-null     object 
 24  LF                        33 non-null     object 
 25  CF                        33 non-null     object 
 26  RF                        33 non-null     object 
 27  RW                        33 non-null     object 
 28  LAM                       33 non-null     object 
 29  CAM                       33 non-null     object 
 30  RAM                       33 non-null     object 
 31  LM                        33 non-null     object 
 32  LCM                       33 non-null     object 
 33  CM                        33 non-null     object 
 34  RCM                       33 non-null     object 
 35  RM                        33 non-null     object 
 36  LWB                       33 non-null     object 
 37  LDM                       33 non-null     object 
 38  CDM                       33 non-null     object 
 39  RDM                       33 non-null     object 
 40  RWB                       33 non-null     object 
 41  LB                        33 non-null     object 
 42  LCB                       33 non-null     object 
 43  CB                        33 non-null     object 
 44  RCB                       33 non-null     object 
 45  RB                        33 non-null     object 
 46  Crossing                  33 non-null     float64
 47  Finishing                 33 non-null     float64
 48  HeadingAccuracy           33 non-null     float64
 49  ShortPassing              33 non-null     float64
 50  Volleys                   33 non-null     float64
 51  Dribbling                 33 non-null     float64
 52  Curve                     33 non-null     float64
 53  FKAccuracy                33 non-null     float64
 54  LongPassing               33 non-null     float64
 55  BallControl               33 non-null     float64
 56  Acceleration              33 non-null     float64
 57  SprintSpeed               33 non-null     float64
 58  Agility                   33 non-null     float64
 59  Reactions                 33 non-null     float64
 60  Balance                   33 non-null     float64
 61  ShotPower                 33 non-null     float64
 62  Jumping                   33 non-null     float64
 63  Stamina                   33 non-null     float64
 64  Strength                  33 non-null     float64
 65  LongShots                 33 non-null     float64
 66  Aggression                33 non-null     float64
 67  Interceptions             33 non-null     float64
 68  Positioning               33 non-null     float64
 69  Vision                    33 non-null     float64
 70  Penalties                 33 non-null     float64
 71  Composure                 33 non-null     float64
 72  Marking                   33 non-null     float64
 73  StandingTackle            33 non-null     float64
 74  SlidingTackle             33 non-null     float64
 75  GKDiving                  33 non-null     float64
 76  GKHandling                33 non-null     float64
 77  GKKicking                 33 non-null     float64
 78  GKPositioning             33 non-null     float64
 79  GKReflexes                33 non-null     float64
 80  Release Clause            33 non-null     float64
dtypes: float64(43), int64(3), object(35)
memory usage: 22.4+ KB



# Arsenal F.C는 어떤 포지션을 보강해야 할까?

## a. 전처리

```python
# Chelsea F.C.선수와 능력치 비교를 하기 위해 추가로 Chelsea 선수들의 데이터가 담긴 테이블 생성

blues = data[data['Club']== 'Chelsea']
blues.info()
```



Int64Index: 33 entries, 5 to 16806
Data columns (total 81 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  


0   Unnamed: 0                33 non-null     int64  
 1   ID                        33 non-null     int64  
 2   Name                      33 non-null     object 
 3   Age                       33 non-null     int64  
 4   Nationality               33 non-null     object 
 5   Overall                   33 non-null     float64
 6   Potential                 33 non-null     float64
 7   Club                      33 non-null     object 
 8   Value                     33 non-null     float64
 9   Wage                      33 non-null     float64
 10  Preferred Foot            33 non-null     object 
 11  International Reputation  33 non-null     float64
 12  Weak Foot                 33 non-null     float64
 13  Skill Moves               33 non-null     float64
 14  Position                  33 non-null     object 
 15  Jersey Number             33 non-null     float64
 16  Joined                    32 non-null     object 
 17  Contract Valid Until      33 non-null     object 
 18  Height                    33 non-null     object 
 19  Weight                    33 non-null     object 
 20  LS                        29 non-null     object 
 21  ST                        29 non-null     object 
 22  RS                        29 non-null     object 
 23  LW                        29 non-null     object 
 24  LF                        29 non-null     object 
 25  CF                        29 non-null     object 
 26  RF                        29 non-null     object 
 27  RW                        29 non-null     object 
 28  LAM                       29 non-null     object 
 29  CAM                       29 non-null     object 
 30  RAM                       29 non-null     object 
 31  LM                        29 non-null     object 
 32  LCM                       29 non-null     object 
 33  CM                        29 non-null     object 
 34  RCM                       29 non-null     object 
 35  RM                        29 non-null     object 
 36  LWB                       29 non-null     object 
 37  LDM                       29 non-null     object 
 38  CDM                       29 non-null     object 
 39  RDM                       29 non-null     object 
 40  RWB                       29 non-null     object 
 41  LB                        29 non-null     object 
 42  LCB                       29 non-null     object 
 43  CB                        29 non-null     object 
 44  RCB                       29 non-null     object 
 45  RB                        29 non-null     object 
 46  Crossing                  33 non-null     float64
 47  Finishing                 33 non-null     float64
 48  HeadingAccuracy           33 non-null     float64
 49  ShortPassing              33 non-null     float64
 50  Volleys                   33 non-null     float64
 51  Dribbling                 33 non-null     float64
 52  Curve                     33 non-null     float64
 53  FKAccuracy                33 non-null     float64
 54  LongPassing               33 non-null     float64
 55  BallControl               33 non-null     float64
 56  Acceleration              33 non-null     float64
 57  SprintSpeed               33 non-null     float64
 58  Agility                   33 non-null     float64
 59  Reactions                 33 non-null     float64
 60  Balance                   33 non-null     float64
 61  ShotPower                 33 non-null     float64
 62  Jumping                   33 non-null     float64
 63  Stamina                   33 non-null     float64
 64  Strength                  33 non-null     float64
 65  LongShots                 33 non-null     float64
 66  Aggression                33 non-null     float64
 67  Interceptions             33 non-null     float64
 68  Positioning               33 non-null     float64
 69  Vision                    33 non-null     float64
 70  Penalties                 33 non-null     float64
 71  Composure                 33 non-null     float64
 72  Marking                   33 non-null     float64
 73  StandingTackle            33 non-null     float64
 74  SlidingTackle             33 non-null     float64
 75  GKDiving                  33 non-null     float64
 76  GKHandling                33 non-null     float64
 77  GKKicking                 33 non-null     float64
 78  GKPositioning             33 non-null     float64
 79  GKReflexes                33 non-null     float64
 80  Release Clause            32 non-null     float64
dtypes: float64(43), int64(3), object(35)
memory usage: 21.1+ KB


```python
# 결측치 확인

blues[blues.isnull()['LS']]
```





```python
# Arsenal과 마찬가지로 GK 포지션의 선수들에서 결측치가 발생 동일한 방식으로 -1을 입력하여 해결

blues = blues.fillna(-1)
blues.info()
```



Int64Index: 33 entries, 5 to 16806
Data columns (total 81 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  


0   Unnamed: 0                33 non-null     int64  
 1   ID                        33 non-null     int64  
 2   Name                      33 non-null     object 
 3   Age                       33 non-null     int64  
 4   Nationality               33 non-null     object 
 5   Overall                   33 non-null     float64
 6   Potential                 33 non-null     float64
 7   Club                      33 non-null     object 
 8   Value                     33 non-null     float64
 9   Wage                      33 non-null     float64
 10  Preferred Foot            33 non-null     object 
 11  International Reputation  33 non-null     float64
 12  Weak Foot                 33 non-null     float64
 13  Skill Moves               33 non-null     float64
 14  Position                  33 non-null     object 
 15  Jersey Number             33 non-null     float64
 16  Joined                    33 non-null     object 
 17  Contract Valid Until      33 non-null     object 
 18  Height                    33 non-null     object 
 19  Weight                    33 non-null     object 
 20  LS                        33 non-null     object 
 21  ST                        33 non-null     object 
 22  RS                        33 non-null     object 
 23  LW                        33 non-null     object 
 24  LF                        33 non-null     object 
 25  CF                        33 non-null     object 
 26  RF                        33 non-null     object 
 27  RW                        33 non-null     object 
 28  LAM                       33 non-null     object 
 29  CAM                       33 non-null     object 
 30  RAM                       33 non-null     object 
 31  LM                        33 non-null     object 
 32  LCM                       33 non-null     object 
 33  CM                        33 non-null     object 
 34  RCM                       33 non-null     object 
 35  RM                        33 non-null     object 
 36  LWB                       33 non-null     object 
 37  LDM                       33 non-null     object 
 38  CDM                       33 non-null     object 
 39  RDM                       33 non-null     object 
 40  RWB                       33 non-null     object 
 41  LB                        33 non-null     object 
 42  LCB                       33 non-null     object 
 43  CB                        33 non-null     object 
 44  RCB                       33 non-null     object 
 45  RB                        33 non-null     object 
 46  Crossing                  33 non-null     float64
 47  Finishing                 33 non-null     float64
 48  HeadingAccuracy           33 non-null     float64
 49  ShortPassing              33 non-null     float64
 50  Volleys                   33 non-null     float64
 51  Dribbling                 33 non-null     float64
 52  Curve                     33 non-null     float64
 53  FKAccuracy                33 non-null     float64
 54  LongPassing               33 non-null     float64
 55  BallControl               33 non-null     float64
 56  Acceleration              33 non-null     float64
 57  SprintSpeed               33 non-null     float64
 58  Agility                   33 non-null     float64
 59  Reactions                 33 non-null     float64
 60  Balance                   33 non-null     float64
 61  ShotPower                 33 non-null     float64
 62  Jumping                   33 non-null     float64
 63  Stamina                   33 non-null     float64
 64  Strength                  33 non-null     float64
 65  LongShots                 33 non-null     float64
 66  Aggression                33 non-null     float64
 67  Interceptions             33 non-null     float64
 68  Positioning               33 non-null     float64
 69  Vision                    33 non-null     float64
 70  Penalties                 33 non-null     float64
 71  Composure                 33 non-null     float64
 72  Marking                   33 non-null     float64
 73  StandingTackle            33 non-null     float64
 74  SlidingTackle             33 non-null     float64
 75  GKDiving                  33 non-null     float64
 76  GKHandling                33 non-null     float64
 77  GKKicking                 33 non-null     float64
 78  GKPositioning             33 non-null     float64
 79  GKReflexes                33 non-null     float64
 80  Release Clause            33 non-null     float64
dtypes: float64(43), int64(3), object(35)
memory usage: 21.1+ KB


```python
data.Position.unique()
```


array(['RF', 'ST', 'LW', 'GK', 'RCM', 'LF', 'RS', 'RCB', 'LCM', 'CB',
       'LDM', 'CAM', 'CDM', 'LS', 'LCB', 'RM', 'LAM', 'LB', 'RDM', 'RW',
       'LM', 'CM', 'RB', 'RAM', 'CF', 'RWB', 'LWB', nan], dtype=object)

### 주전선수 비교를 위하여 Arsenal 과 Chelsea의 주전을 선정

- 기본 전술포메이션은 4-4-2 (공격수 - 미드필더 - 수비수) 로 통일 (GK는 포메이션명에서 제외 - 굳이 쓰자면 4-4-2-1)

- 즉, GK : 1명, CB : 4명 MF : 4명 ST : 2명을 선발

- 선발의 기준은 현재능력치

- GK 리스트 = GK

- CB 리스트 = CB, LCB, RCB, RB, LB

- MF 리스트 = RCM, LCM, RDM, LDM, CDM, CM, LM, RM, CAM

- ST 리스트 = ST, LW, RW, LS, RS

```python
# 각 포지션 별 리스트 작성
st_list = ['ST', 'LW', 'RW', 'LS','RS','LF','RF','CF']
mf_list = ['RCM', 'LCM', 'RDM','LDM', 'CDM', 'CM','LM', 'RM', 'CAM', 'LAM','RAM']
cb_list = ['CB', 'LCB', 'RCB', 'RB', 'LB', 'LWB','RWB']
gk_list = ['GK']
```

아스널 라인업 선발

```python
# 각 포지션별 남은 자리 숫자를 입력
st_num = 2
mf_num = 4
cb_num = 4
gk_num = 1

lineup=[]
for index in gunners.index:
    # gk 포지션 선발
    if gunners['Position'][index] in gk_list:  # 포지션이 gk인 선수들 중에서
        if gk_num != 0:  # gk 포지션에 남은 자리가 0이 아니라면 (= 있다면)
            lineup.append(gunners['ID'][index])  # 해당 선수의 ID를 lineup에 입력하고
            gk_num -= 1  # gk_num (선수자리)의 값을 -1 해라

            # st 포지션 선발
    elif gunners['Position'][index] in st_list:  # 포지션이 st인 선수들 중에서
        if st_num != 0:  # st 포지션에 남은 자리가 0이 아니라면( = 있다면)
            lineup.append(gunners['ID'][index])  # 해당 선수의 ID를 lineup에 입력하고
            st_num -= 1  # st_num(선수 자리)의 값을 -1 해라
            gunners['Position'][index] = 'ST' #포지션은 ST 로 통일
    # mf포지션 선발
    elif gunners['Position'][index] in mf_list:  # 포지션이 mf인 선수들 중에서
        if mf_num != 0:  # mf 포지션에 남은 자리가 0이 아니라면( = 있다면)
            lineup.append(gunners['ID'][index])  # 해당 선수의 ID를 lineup에 입력하고
            mf_num -= 1  # mf_num(선수 자리)의 값을 -1 해라
            gunners['Position'][index] = 'MF' #포지션은 MF 로 통일

    # cb 포지션 선발
    else:
        if cb_num != 0:  # cb 포지션에 남은 자리가 0이 아니라면( = 있다면)
            lineup.append(gunners['ID'][index])  # 해당 선수의 ID를 lineup에 입력하고
            cb_num -= 1  # cb_num(선수 자리)의 값을 -1 해라
            gunners['Position'][index] = 'CB' #포지션은 CB 로 통일
```

```python
gunners_lineup = gunners[gunners['ID'].isin(lineup)]
gunners_lineup
```





선발된 선수들의 포지션을 4가지 유형으로 분류 한다.

첼시 라인업 선발

```python
# 각 포지션별 남은 자리 숫자를 입력
st_num = 2
mf_num = 4
cb_num = 4
gk_num = 1

lineup=[]
for index in blues.index:
    # gk 포지션 선발
    if blues['Position'][index] in gk_list:  # 포지션이 gk인 선수들 중에서
        if gk_num != 0:  # gk 포지션에 남은 자리가 0이 아니라면 (= 있다면)
            lineup.append(blues['ID'][index])  # 해당 선수의 ID를 lineup에 입력하고
            gk_num -= 1  # gk_num (선수자리)의 값을 -1 해라

            # st 포지션 선발
    elif blues['Position'][index] in st_list:  # 포지션이 st인 선수들 중에서
        if st_num != 0:  # st 포지션에 남은 자리가 0이 아니라면( = 있다면)
            lineup.append(blues['ID'][index])  # 해당 선수의 ID를 lineup에 입력하고
            st_num -= 1  # st_num(선수 자리)의 값을 -1 해라
            blues['Position'][index] = 'ST' #포지션은 ST 로 통일
    # mf포지션 선발
    elif blues['Position'][index] in mf_list:  # 포지션이 mf인 선수들 중에서
        if mf_num != 0:  # mf 포지션에 남은 자리가 0이 아니라면( = 있다면)
            lineup.append(blues['ID'][index])  # 해당 선수의 ID를 lineup에 입력하고
            mf_num -= 1  # mf_num(선수 자리)의 값을 -1 해라
            blues['Position'][index] = 'MF' #포지션은 MF 로 통일

    # cb 포지션 선발
    else:
        if cb_num != 0:  # cb 포지션에 남은 자리가 0이 아니라면( = 있다면)
            lineup.append(blues['ID'][index])  # 해당 선수의 ID를 lineup에 입력하고
            cb_num -= 1  # cb_num(선수 자리)의 값을 -1 해라
            blues['Position'][index] = 'CB' #포지션은 CB 로 통일
```

```python
blues_lineup = blues[blues['ID'].isin(lineup)]
blues_lineup
```





```python
 # 두팀의 주전선수가 모인 데이터를 생성

london = pd.concat([gunners_lineup, blues_lineup])
print(len(london))
london
```


22





## b. EDA

- 주전선수 비교

포지션별 선수 능력치 비교

```python
# 박스클폿으로 이상치 확인 및 두 팀의 선수 데이터 비교

sns.boxplot(data=london, x='Position', y='Overall', hue= 'Club')
```






```python
# MF 부분 이상치 확인
london[london['Position'] == 'MF'][['Name','Age','Value','Overall','Position','Club']]

# 전체적인 데이터가 80대에 분포해있고 N. Kanté 선수가 다른 선수들에 비해 능력치가 높아서 인것으로 확인
# 특이사항은 아니므로 그대로 분석 진행
```





```python
london[london['Position'] == 'CB'][['Name','Age','Value','Overall','Position','Club']]

# 전체적인 데이터가 80대에 분포해있고 Azpilicueta 선수가 다른 선수들에 비해 능력치가 높아서 인것으로 확인
# 특이사항은 아니므로 그대로 분석 진행
```





두 팀을 비교해봤을때 아스널이 첼시에 비해 중원(미드필드)라인과 수비라인에서 다소 부족한 상태임을 알 수 있음

선수의 몸값 대비 능력치로 비교

```python
sns.boxplot(data=london, x='Position', y='Value', hue= 'Club')
```






```python
london[london['Position'] == 'ST'][['Name','Age','Value','Overall','Position','Club']]
```





```python
london[london['Position'] == 'CB'][['Name','Age','Value','Overall','Position','Club']]
```





아스날선수와 첼시선수의 선발 선수명단을 비교해보면 

- 포지션 대비 능력로 보았을때 

아스널의 선수들이 첼시 선수들에 비해 미드필더 부분과 수비부분에서 능력치가 열세임이 확인된다.

- 선수가치 대비 능력치를 보았을때 

아스널의 선수들이 첼시 선수들에 비해 공격수 부분은 낮은 몸값대비 비슷한 능력치를 보이고 있는 반면

미드 필더 부분은 아스널 선수들이 더 높은 몸값을 가진 것에 비해 첼시 선수들보다 더 낮은 능력치를 보이고 있다.

즉 포지션별로 선수들의 몸값과 역략을 고려하였을때 아스날 선수단이 첼시 선수단에 비해서 미드필더 부분과 수비부분에서 부족함을 보이고 있음을 알 수 있다.
---






# 4. Arsenal F.C는 어떤 선수를 영입해야 할까?

## a. EDA

- 필요 포지션의 어떤 선수를 대체해야할지 확인

- 기준은 영입일, 능력치, 잠재력, 나이

### 방출 기준을 위한 나만의 공식 만들기

- 선수의 미래가치 = (Overall + Potential*2) / Age 

(가중치 2, 나이가 낮을 수록 가치가 높아지도록)

- 현재 기량도 고려해야 하지만 추후에도 성장하며 지속적으로 활약해줘야 하기 때문에 Potential을 고려함

```python
gunners_lineup['Point'] = (gunners_lineup['Overall'] + gunners_lineup['Potential']*2 / gunners_lineup['Age'])
```

문제가 되는 미드필더 & 수비 포지션의 선수들을 대상으로 계산한 미래가치를 확인

```python
release_list_mf = gunners_lineup[gunners_lineup['Position']=='MF'][ ['Name','Overall','Potential','Age','Joined', 'Point']]
release_list_mf = release_list_mf.sort_values(by=["Point","Joined","Age"], ascending=[True, False, False])
release_list_mf
```





```python
release_list_cb = gunners_lineup[gunners_lineup['Position']=='CB'][ ['Name','Overall','Potential','Age','Joined', 'Point']]
release_list_cb = release_list_cb.sort_values(by=["Point","Joined","Age"], ascending=[True, False, False])
release_list_cb
```





잔류포인트, 합류일자, 나이로 보았을때 가장 위에 위치한 A. Ramsey, L. Koscielny 방출 후 MF, CB한명씩 영입해야 한다.

- Arsenal F.C의 영입방칙은 최근 새로 부임한 아르테타 감독의 영입방침을 따른다.

[영입 방침]

- 선수의 나이는 어릴수록 좋음

- 잠재력 보다 현재 바로 주전으로 사용할 수 있는 선수

- 포지션은  A. Ramsey와 Héctor Bellerín의 상세포지션인 CAM, CB를 따른다.

- 라이벌팀이거나 빅클럽(리그 상위권에 속한 팀)의 선수는 영입하지 않는다.

```python
# 위에서 사용한 Point 데이터를 market에서도 사용하기 위해 전체 선수데이터에도 동일 기준 적용

data['Point'] = (data['Overall'] + data['Potential']*2 / data['Age'])
```

```python
# 전체 데이터에서 원하는 포지션이 있는 데이터만 추출하여 이적시장 데이터 형성 CAM, CB 포지션을 제외한 선수들을 제거
market = data[ (data['Position']=='CAM') | (data['Position']=='CB')]
market.drop(['Unnamed: 0'], axis = 1, inplace = True)
market.head()
```





# 시각화 하여 비교 후 영입 명단 작성

```python
import matplotlib.pyplot as plt
```

`plt.subplots(행, 열, figsize=(가로, 세로))` 심화

여러개의 그래프를 한번에 그리기 위하여 설정해 줍니다.

이것을 변수 ax에 담는다면 ax[1, 1]은 1열 1행에 그래프가 그려집니다.

```python
f, ax = plt.subplots(2,4, figsize = (35,10))

compare_list_mf = ['Age', 'Overall', 'Point', 'BallControl']
compare_list_cb = ['Age', 'Overall', 'Point', 'Interceptions']

for i in range(8):
    # CAM 선수데이터를 비교할 그래프 
    if i 

`plt.barplot(x, y, data, palette, ax)` 심화

평균치 이상이면 음영에 차이를 주기 & 평균선 그어주기

```python
f, ax = plt.subplots(2, 4, figsize=(35, 10))

compare_list_mf = ['Age', 'Overall', 'Point', 'BallControl']
compare_list_cb = ['Age', 'Overall', 'Point', 'Interceptions']

for i in range(8):
    if i  market[market['Position'] == 'CAM'][:15][compare_list_mf[i]].mean()
                  else 'gray' for x in market[market['Position'] == 'CAM'][:15][compare_list_mf[i]]]

        sns.barplot(x=compare_list_mf[i], y='Name', data=market[market['Position']
                                                             == 'CAM'][:15], palette=colors, ax=ax[i//4, i % 4])

        ax[i//4, i % 4].axvline(market[market['Position'] == 'CAM']
                                [:15][compare_list_mf[i]].mean(), ls='--')

    else:
        sns.barplot(x=compare_list_cb[i % 4], y='Name',
                    data=market[market['Position'] == 'CB'][:15], ax=ax[i//4, i % 4])

        ax[i//4, i % 4].axvline(market[market['Position'] == 'CB']
                                [:15][compare_list_cb[i % 4]].mean(), ls='--')
```



# 결론

- 포지션 별로 4개의 주요 지표를 비교해 보았을때 영입 list 는 다음과 같다.

[미드필더]

- N.Fekir :Ramsey 선수보다 어리면서도, Overall이 높아 바로 기용이 가능하고 미래 가치인 Point도 평균치 이상으로 가장 적합하다.

[수비수]

- S.de Vrij : L. Koscielny 선수보다 매우 어리고, Overall도 높아 바로 기용이 가능하고, 미래 가치인 Point도 평균치로 나이대비 준수한 편이며, 수비수의 주요 지표인 Interceptions 수치가 상위권으로 가장 적합하다.

