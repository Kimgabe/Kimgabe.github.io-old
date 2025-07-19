---
title: "[예측] 상점별 미래 3개월 카드매출 예측하기(2) - Preprocessing"
cover: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1920&h=1080&fit=crop"
date: 2021-07-08
categories:
  - [personal-study, preprocessing]
tags:
  - feature engineering
  - prediction
  - regression. DACON
  - 시계열
  - 카드매출
  - 예측
  - KNN
  - RandomForestRegressor
  - LightGBM
  - 머신러닝
  - 딥러닝
toc: true
---

# 1. 주제 : 상점 신용카드 매출 예측

- 2019.07 ~ 2019.10 에 DACON에서 주최한 상점 신용카드 매출 예측 경진대회의 데이터

- 데이터 제공자 : 핀테크 기업 FUNDA 

- 문제 : 2019년 2월 28일까지의 카드 거래 데이터를 이용해 2019년 3월 1일 ~ 5월 31일 까지의 상점별 3개월 총 매출 예측하기

# 2. 데이터 소개 및 문제 정의

## 데이터 소개

[데이터 출처](https://dacon.io/competitions/official/140472/data) : DACON 

funda_train.csv : 모델 학습용 데이터

- store_id : 상점의 고유id

- card_id : 사용한 카드의 고유 id

- card_company : 비식별화된 카드 회사

- transcated_date : 거래 날짜

- transacted_time : 거래 시간

- installment_term : 할부 개월 수 

- region : 상점이 위치한 지역

- type_of_business : 상점 업종

- amount : 거래액 (단위: 미상) 

## 문제 정의

- 주어진 데이터는 거래액 (amount) 인데, 예측해야 할 값은 '상점 별 매출액' 이다.

- 또한, store_id별 3월 1일 ~ 5월 31일 매출(3개월)의 총 합을 예측해야 한다.

- 각 상점별 특정 기간 기준 매출 데이터의 특징을 기반으로 + 3개월 뒤의 매출액을 예측하는 식으로 모델이 구축되야 할 것 같다.

- 그 특정 기간은 정답 format과 같은 3개월을 기준으로 상점별 특징을 잡는 것이 좋을 것 같다.

---


EDA로 살펴본 데이터들을 모델링하기 위해 전처리를 통해 별도의 feature를 만들고 불필요한 자료들을 다듬는 과정
---


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 캔버스 사이즈 적용
plt.rcParams["figure.figsize"] = (12, 9)

# 컬럼 전체 확인 가능하도록 출력 범위 설정
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)

# 불필요한 경고 표시 생략
import warnings
warnings.filterwarnings(action = 'ignore')

# pandas 결과값의 표현 범위 소수점 2자리수로 변경
pd.options.display.float_format = "{:.2f}".format

# 파일 로드위한 directory 확인 및 현재 경로로 설정
a = os.getcwd()
os.chdir(a)
```

```python
df = pd.read_csv("funda_train.csv")
submission_df = pd.read_csv("submission.csv")
```

# Data Processing - Train data

## 년/월 추출

```python
# .str.split으로 년/월 추출

# year
df['transacted_year'] = df['transacted_date'].str.split('-', expand = True).iloc[:, 0].astype(int)

# month
df['transacted_month'] = df['transacted_date'].str.split('-', expand = True).iloc[:, 1].astype(int)
df.head()
```





- transacted_date의 시작점이 2016년 6월 1일 이므로 transacted_year에서 2016을 빼고 'month'를 기준으로 데이터를 분류하는 index번호처럼 생성

계산 방식은 다음과 같다.

```python

standard_t = (연도-2016)*12 + '월'

```

- 2016년의 경우 6월 =6, 7월 =7

- 2017년의 경우 1월 = 12, 2월 = 24

- 위와 같이 각 연도별 월을 구분지을 수 있게 가공된다.

## 기준 시점이 될 std_mth (= standard_month) 생성

```python
# 데이터 병합을 위해 시간 데이터를 standard_t 로 변경하고, 불필요한 컬럼은 drop
df['std_mth'] = (df['transacted_year'] - 2016) * 12 + df['transacted_month']
df.drop(['transacted_year', 'transacted_month', 'transacted_date', 'transacted_time'], axis = 1, inplace = True)
```

```python
df['std_mth'].unique()
```


array([ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
       23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38])

## 업종 특성, 지역, 할부 평균 - 파생변수 생성

### installment_term - 매장별 평균 할부 비율

- EDA에서 본 바와 같이 대부분이 일시불이므로 일시불 / 할부로 범주를 이원화 하여 사용 (전체 할부 개월 수 로 하기엔 너무 범위가 큼)

- 다만, 단순 할부 여부는 동일 매장에서 결제 건수가 여러건 발생 하므로 T/F로 입력할 수가 없다. -> 매장별 평균 할부개월 비율로 전처리

```python
df['installment_term'] = (df['installment_term'] > 0).astype(int) # bool to int (True=1, False=0)
df['installment_term'].value_counts()
```


0    6327632
1     228981
Name: installment_term, dtype: int64


```python
# 각 매장 기준으로 할부 기간의 평균 계산
installment_term_per_store = df.groupby(['store_id'])['installment_term'].mean()
installment_term_per_store.head()
```


store_id
0   0.04
1   0.00
2   0.08
4   0.00
5   0.08
Name: installment_term, dtype: float64


```python
# 결측치 확인
pd.DataFrame(installment_term_per_store).isnull().sum()
```


installment_term    0
dtype: int64

### region - group by로 데이터 셋팅

- 범주형이지만, 종류가 너무 많아 dummy 하여 사용하기는 어려움 -> 활용을 위해 파생변수 생성 필요 (group by)

- 결측치가 2042766 개 존재함

- 결측치를 drop하기에는 너무 많은 데이터 -> 전처리를 통해 group by에 포함되도록 해야 함

```python
# 결측치 전처리
df['region'].fillna('미분류', inplace = True)
df['region'].value_counts().head()
```


미분류       2042766
경기 수원시     122029
충북 청주시     116766
경남 창원시     107147
경남 김해시     100673
Name: region, dtype: int64


```python
# 결측치 재확인
df['region'].value_counts().isnull().sum()
```


0

### type_of_business - 데이터 셋팅

- 범주형이지만, 종류가 너무 많아(145개) dummy 하여 사용하기는 어려움 -> 활용을 위해 파생변수 생성 필요 (group by)

- 결측치가 3952609 개 존재함

- 결측치를 drop하기에는 너무 많은 데이터 -> 전처리를 통해 group by에 포함되도록 해야 함

```python
# groupby에 결측을 포함시키기 위해, 결측을 문자로 대체
df['type_of_business'].fillna('미분류', inplace = True)
df['type_of_business'].value_counts().head()
```


미분류        3952609
한식 음식점업     745905
두발 미용업      178475
의복 소매업      158234
기타 주점업      102413
Name: type_of_business, dtype: int64


```python
# 결과 재확인
df['type_of_business'].value_counts().isnull().sum()
```


0

## 불필요한 변수 제거

- card_id, card_company는 특징으로 사용하기에는 범주가 너무 세밀하고, 특징으로서 유의하지 않을 것이라 판단되므로 drop

```python
df.drop(['card_id', 'card_company'], axis = 1, inplace = True)
```

## 중복 데이터 처리

```python
# 'store_id', 'region', 'type_of_business', 'std_mth'를 기준으로 중복 제거
train_df = df.drop_duplicates(subset = ['store_id', 'region', 'type_of_business', 'std_mth'])[['store_id', 'region', 'type_of_business', 'std_mth']]
train_df.head()
```





## 평균 할부율 입력 to train_df

```python
train_df['평균할부율'] = train_df['store_id'].replace(installment_term_per_store.to_dict())
```

## std_mth(기준월)의 -1, -2, -3 시점에 대한 매장별/지역별/ 업종별 매출 파생변수 생성

- df1에서는 시점 t를, 다른 데이터에서는 시점 t+1 or t-1 을 붙여야 되는 상황

- t가 유니크 하다면, df2를 shift()해서 공백을 만든 뒤 concat을 하면 된다. (시계열 데이터에서 많이 사용)

- t가 유니크 하지 않은 경우는 새로운 변수( e.g: t_1)을 만들어서 merge한다.

![preprocessing.png](assets/images/portfolio/credit_card_preprocessing.png)

---


- 단, std_mth는 각 매장별로 값이 존재하고, 필요한 값은 기준 월(std_mth)을 중심으로 -1, -2, -3 개월의 매출 값이다.

- 이를 위해 for문을 사용하여 i = 1, 2, 3 일때 각각 t_{i} 값이 들어가는 변수를 만들어서 병합할 것이다.

- 중복 방지를 위해 병합한 변수명 변경 및 drop 작업도 함께 수행한다.

### 각 시점별 매장의 월 매출 (파생변수)

##### 각 store당 월별 amount 계산

- standard_t (월): 6(2016년 6월) ~ 38 (2019년 2월)

- 즉, store_id가 0이라는 매장의 standard_t가 6일때의 매출 , 7일때의 매출... 38일때의 매출을 각각 입력

```python
# store_id와 standard_t에 따른 amount 합계 계산: total_amt_per_mth_and_store
total_amt_per_mth_and_store = df.groupby(['store_id', 'std_mth'], as_index = False)['amount'].sum()
total_amt_per_mth_and_store.head()
```





- group by의 경우 지정한 조건에 해당하는 값이 없으면 건너뛴다.

- 각 지점별로 '모든 월' 에 대한 amount가 들어가야 하므로, 매장별 매출에서 값이 생략된 월들은 0으로 값을 넣어줘야 한다.

- 그렇지 않을 경우 다른 데이터와 merge 할 경우 에러 발생, 혹은 잘못된 값이 입력될 수 있다.

매장별로 결측된 월이 있는지 확인

```python
total_amt_per_mth_and_store.groupby(['store_id'])['std_mth'].count()
```


store_id
0       33
1       33
2       33
4       33
5       33
        ..
2132    31
2133    32
2134    26
2135    31
2136    22
Name: std_mth, Length: 1967, dtype: int64

- 몇몇 store_id에서 누락된 값이 보인다.

- group by에서 생략된 값이 실제 매출이 발생했는데 단순 누락된 값인지, 매장 운영이 되지 않은 기간이어서 0인건지 확인이 어렵다.

- 이를 위해 pivot_table 활용

---


- 누락된 값이 연속적인 경우만 있다면 매출이 발생하지 않은 것으로 가정 하여 0으로 채운다.

    - e.g) 시작점은 2016년 6월이지만, 누락된 매장들은 시작점 보다 늦게 개점하여 누락된 경우

- 누락된 값이 불연속적이라면, 매출값이 누락된 것이라 가정하고 누락된 값의 '전/후' 값으로 채워넣는다.

```python
# pivot_table로 nan값의 분포 형태 확인
check_nan_amount = pd.pivot_table(df, values = 'amount', index = 'store_id', columns = 'std_mth', aggfunc = 'sum')
check_nan_amount
```



1967 rows × 33 columns


- pivot table을 통해 보았을때, '월' 의 중간 중간 nan값이 발생하는 것으로 보아, 실제 매출은 발생하였으나 누락된 데이터 일 것이라 가정

- nan값을 바로 앞, 뒤 standard_t의 매출로 채워 넣는다.

```python
# 발생한 nan값을 바로 앞/뒤의 값으로 채워넣는다.
# method = 'ffill', axis = 1 #전
# method = 'bfill', axis = 1 #후

total_amt_per_mth_and_store = check_nan_amount.fillna(method = 'ffill', axis = 1).fillna(method = 'bfill', axis = 1)
total_amt_per_mth_and_store.head(10)
```





- train_df와 병합을 위해 pivot_table 형태인 total_amt_per_mth_and_store 테이블을 stack() 함수를 사용해 동일한 형태의 DataFrame으로 변경

- stack() : column 과 row를 바꾸는 함수

- 위의 pivot_table 기준으로보면 store_id, std_mth, amount가 column이 되고, 기존 columns 별로 입력되있던 값이 row가 된다.

```python
total_amt_per_mth_and_store = total_amt_per_mth_and_store.stack().reset_index() # index 번호 새로 부여
```

```python
total_amt_per_mth_and_store
```



64911 rows × 3 columns


```python
# amount로 컬럼명 변경
total_amt_per_mth_and_store.rename({0:"amount"}, axis = 1, inplace = True)
total_amt_per_mth_and_store.head(3)
```





##### 매장별 월 매출 + train_df

```python
# std_mth + i (i = 1, 2, 3) 시점의 부착
# train_df의 std_mth는 total_amt_per_mth_and_store의 std_mth-i와 부착되어야 하므로, total_amt_per_mth_and_store의 std_mth에 i를 더함

for i in range(1, 4): 
    # i값에 따른 새로운 변수 생성
    total_amt_per_mth_and_store['std_mth_{}'.format(i)] = total_amt_per_mth_and_store['std_mth'] + i
    
    # 두 테이블 데이터 결합
    # 두 table에 모두 std_mth가 존재하므로 drop
    train_df = pd.merge(train_df, total_amt_per_mth_and_store.drop('std_mth', axis = 1), left_on = ['store_id', 'std_mth'], right_on = ['store_id', 'std_mth_{}'.format(i)])
    
    # 변수명 변경: 다음 loop에서 merge할때 중복 column 때문에 _x, _y가 생기는 것 방지
    train_df.rename({"amount":"{}_before_amount".format(i)}, axis = 1, inplace = True)
    
    #필요없어진 변수 drop
    train_df.drop(['std_mth_{}'.format(i)], axis = 1, inplace = True)
    total_amt_per_mth_and_store.drop(['std_mth_{}'.format(i)], axis = 1, inplace = True)
    
train_df.head()
```





- std_mth의 시작점이 6 -> 9로 바뀐다. (for문이 적용되고 merge되면서 사라진 것)

- 6월의 amount는 3_before_amount에 입력되어 있다.

- 일괄적으로 +3이 된 것이기 때문에 ok

- std_mth 9(=16년 9월)를 기준으로 보았을때

    - 1_before_amount는 16년 8월, 2_before_amount는 16년 7월, 3_before_amount는 16년 6월을 의미한다.

- 전체적으로 본다면 2016년 6월에 대한 특징 데이터는 소실된다. 하지만 반대로 다른 시점에 특성을 구분할 수 있는 데이터가 늘어남  

---


- i값을 3으로 한 이유 :

    1) 예측해야 하는 값이 3개월 평균 이기 때문

    2) i가 클수록 유실되는 데이터량이 많아져서 최소화 하기 위해( 1)의 기간도 감안 )

#### 각 시점별 지역의 월 매출 (파생변수)

##### region(지역) 별 평균 매출 계산

```python
#지역별 매장을 분류(dict) & 중복제거
store_to_region = df[['store_id', 'region']].drop_duplicates().set_index(['store_id'])['region'].to_dict() 

# store_id를 region으로 대체 -> 위에서 사용한 코드 동일하게 사용 가능
total_amt_per_mth_and_store['region'] = total_amt_per_mth_and_store['store_id'].replace(store_to_region)

# 지역별 평균 매출 계산
# total_amt_per_mth_and_store에 region이란 컬럼 추가 후 amt_mean_per_std_mth_and_region 테이블로 변경
amt_mean_per_std_mth_and_region = total_amt_per_mth_and_store.groupby(['region', 'std_mth'], as_index = False)['amount'].mean()
```

```python
amt_mean_per_std_mth_and_region.head(3)
```





- 위에서 store_id의 누락치를 처리하는 과정에서 nan값을 모두 처리함

- 즉, store_id를 region으로 대체한 것이기 때문에, pivot_table & stack 등을 통한 결측치 제거는 하지 않아도 됨.

##### train_df + amt_mean_per_std_mth_and_region

```python
# std_mth + i (i = 1, 2, 3)

for i in range(1, 4):
    amt_mean_per_std_mth_and_region['std_mth_{}'.format(i)] = amt_mean_per_std_mth_and_region['std_mth'] + i
    train_df = pd.merge(train_df, amt_mean_per_std_mth_and_region.drop('std_mth', axis = 1), left_on = ['region', 'std_mth'], right_on = ['region', 'std_mth_{}'.format(i)])
    train_df.rename({"amount":"{}_before_amount_of_region".format(i)}, axis = 1, inplace = True)
    
    # 계산에 사용되고 필요없어진 데이터 drop
    train_df.drop(['std_mth_{}'.format(i)], axis = 1, inplace = True)
    amt_mean_per_std_mth_and_region.drop(['std_mth_{}'.format(i)], axis = 1, inplace = True)    
    
train_df.head()
```





#### 각 시점별 업종의 월 매출 (파생변수)

##### type_of_business별 평균 매출 계산

```python
##업종별 매장을 분류(dict) & 중복제거
store_to_type_of_business = df[['store_id', 'type_of_business']].drop_duplicates().set_index(['store_id'])['type_of_business'].to_dict()

# store_id를 type_of_business으로 대체 -> 위에서 사용한 코드 동일하게 사용 가능
total_amt_per_mth_and_store['type_of_business'] = total_amt_per_mth_and_store['store_id'].replace(store_to_type_of_business)

# 지역별 평균 매출 계산
amount_mean_per_mth_and_type_of_business = total_amt_per_mth_and_store.groupby(['type_of_business', 'std_mth'], as_index = False)['amount'].mean()
```

##### amount_mean_per_mth_and_type_of_business + train_df

```python
# std_mth + i (i = 1, 2, 3)
# train_df의 std_mth는 total_amt_per_mth_and_store의 std_mth-i와 merge 해야하므로, total_amt_per_mth_and_store의 std_mth에 i를 더한다.

for i in range(1, 4):
    amount_mean_per_mth_and_type_of_business['std_mth_{}'.format(i)] = amount_mean_per_mth_and_type_of_business['std_mth'] + i
    train_df = pd.merge(train_df, amount_mean_per_mth_and_type_of_business.drop('std_mth', axis = 1), left_on = ['type_of_business', 'std_mth'], right_on = ['type_of_business', 'std_mth_{}'.format(i)])
    train_df.rename({"amount":"{}_before_amount_of_type_of_business".format(i)}, axis = 1, inplace = True)
    
    # 계산에 사용되고 필요없어진 데이터 drop
    train_df.drop(['std_mth_{}'.format(i)], axis = 1, inplace = True)
    amount_mean_per_mth_and_type_of_business.drop(['std_mth_{}'.format(i)], axis = 1, inplace = True)       
    
train_df.head()
```





## label 부착하기 ( std_mth +1, std_mth+2, std_mth+3)

- label 은 기준월 (std_mth) 에서 각각 +1, +2, +3 인 시점에 대한 amount는 예측 모델을 통해 파악해야 하는 값이다.

- 이후 에는 model 학습을 위한 데이터 전처리가 들어가기 때문에, raw data인 현상황에서 +1, +2, +3 인 시점의 amount를 입력해 두는 것이 추후 작업에서 유용하다.

```python
# 불필요한 컬럼 drop (중복 컬럼 방지)
total_amt_per_mth_and_store.drop(['region', 'type_of_business'], axis = 1, inplace = True)

# std_mth - i (i = 1, 2, 3)
for i in range(1, 4):
    total_amt_per_mth_and_store['std_mth_{}'.format(i)] = total_amt_per_mth_and_store['std_mth'] - i   
    train_df = pd.merge(train_df, total_amt_per_mth_and_store.drop('std_mth', axis = 1), left_on = ['store_id', 'std_mth'], right_on = ['store_id', 'std_mth_{}'.format(i)])
    train_df.rename({"amount": "Y_{}".format(i)}, axis = 1, inplace = True)
    
    # 계산에 사용되고 필요없어진 데이터 drop
    train_df.drop(['std_mth_{}'.format(i)], axis = 1, inplace = True)
    total_amt_per_mth_and_store.drop(['std_mth_{}'.format(i)], axis = 1, inplace = True)      
```

```python
train_df[['std_mth','Y_1','Y_2','Y_3']]
```



50231 rows × 4 columns


- for loop가 수행되면서 각각 i=1 일때, **total_amt_per_mth_and_store의 std_mth 기준으로** +1 인 시점의 amount 가 Y_1이 된다.

- i=2 일때는 std_mth 기준 +2 인 시점의 amount 가 Y_2이 되고, i=3 일때, std_mth 기준 +3 인 시점의 amount 가 Y_3이 된다.

```python
# Y변수 (미래 3개월의 매출) 생성
train_df['Y'] = train_df['Y_1'] + train_df['Y_2'] + train_df['Y_3']
```

```python
train_df.to_csv('train_df.csv')
```
