---
layout: single
title:  "[예측] 상점별 미래 3개월 카드매출 예측하기(2) - Preprocessing"
categories: portfolio
tag: [feature engineering, prediction, regression. DACON, 시계열, 카드매출, 예측, KNN, RandomForestRegressor, LightGBM, 머신러닝, 딥러닝]
toc: true
highlight: false
header:
  teaser: /assets/images/unsplash/credit_card.jpg
  overlay_image: /assets/images/unsplash/credit_card.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/52jRtc2S_VE)"
---

<head>
  <style>
    table.dataframe {
      white-space: normal;
      width: 100%;
      height: 240px;
      display: block;
      overflow: auto;
      font-family: Arial, sans-serif;
      font-size: 0.9rem;
      line-height: 20px;
      text-align: center;
      border: 0px !important;
    }

    table.dataframe th {
      text-align: center;
      font-weight: bold;
      padding: 8px;
    }

    table.dataframe td {
      text-align: center;
      padding: 8px;
    }

    table.dataframe tr:hover {
      background: #b8d1f3; 
    }

    .output_prompt {
      overflow: auto;
      font-size: 0.9rem;
      line-height: 1.45;
      border-radius: 0.3rem;
      -webkit-overflow-scrolling: touch;
      padding: 0.8rem;
      margin-top: 0;
      margin-bottom: 15px;
      font: 1rem Consolas, "Liberation Mono", Menlo, Courier, monospace;
      color: $code-text-color;
      border: solid 1px $border-color;
      border-radius: 0.3rem;
      word-break: normal;
      white-space: pre;
    }

  .dataframe tbody tr th:only-of-type {
      vertical-align: middle;
  }

  .dataframe tbody tr th {
      vertical-align: top;
  }

  .dataframe thead th {
      text-align: center !important;
      padding: 8px;
  }

  .page__content p {
      margin: 0 0 0px !important;
  }

  .page__content p > strong {
    font-size: 0.8rem !important;
  }

  </style>
</head>



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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>card_id</th>
      <th>card_company</th>
      <th>transacted_date</th>
      <th>transacted_time</th>
      <th>installment_term</th>
      <th>region</th>
      <th>type_of_business</th>
      <th>amount</th>
      <th>transacted_year</th>
      <th>transacted_month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>b</td>
      <td>2016-06-01</td>
      <td>13:13</td>
      <td>0</td>
      <td>NaN</td>
      <td>기타 미용업</td>
      <td>1857.14</td>
      <td>2016</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>h</td>
      <td>2016-06-01</td>
      <td>18:12</td>
      <td>0</td>
      <td>NaN</td>
      <td>기타 미용업</td>
      <td>857.14</td>
      <td>2016</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>2</td>
      <td>c</td>
      <td>2016-06-01</td>
      <td>18:52</td>
      <td>0</td>
      <td>NaN</td>
      <td>기타 미용업</td>
      <td>2000.00</td>
      <td>2016</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>3</td>
      <td>a</td>
      <td>2016-06-01</td>
      <td>20:22</td>
      <td>0</td>
      <td>NaN</td>
      <td>기타 미용업</td>
      <td>7857.14</td>
      <td>2016</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>4</td>
      <td>c</td>
      <td>2016-06-02</td>
      <td>11:06</td>
      <td>0</td>
      <td>NaN</td>
      <td>기타 미용업</td>
      <td>2000.00</td>
      <td>2016</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>


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

<pre>
array([ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
       23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38])
</pre>
## 업종 특성, 지역, 할부 평균 - 파생변수 생성


### installment_term - 매장별 평균 할부 비율



- EDA에서 본 바와 같이 대부분이 일시불이므로 일시불 / 할부로 범주를 이원화 하여 사용 (전체 할부 개월 수 로 하기엔 너무 범위가 큼)

- 다만, 단순 할부 여부는 동일 매장에서 결제 건수가 여러건 발생 하므로 T/F로 입력할 수가 없다. -> 매장별 평균 할부개월 비율로 전처리



```python
df['installment_term'] = (df['installment_term'] > 0).astype(int) # bool to int (True=1, False=0)
df['installment_term'].value_counts()
```

<pre>
0    6327632
1     228981
Name: installment_term, dtype: int64
</pre>

```python
# 각 매장 기준으로 할부 기간의 평균 계산
installment_term_per_store = df.groupby(['store_id'])['installment_term'].mean()
installment_term_per_store.head()
```

<pre>
store_id
0   0.04
1   0.00
2   0.08
4   0.00
5   0.08
Name: installment_term, dtype: float64
</pre>

```python
# 결측치 확인
pd.DataFrame(installment_term_per_store).isnull().sum()
```

<pre>
installment_term    0
dtype: int64
</pre>
### region - group by로 데이터 셋팅


- 범주형이지만, 종류가 너무 많아 dummy 하여 사용하기는 어려움 -> 활용을 위해 파생변수 생성 필요 (group by)

- 결측치가 2042766 개 존재함

- 결측치를 drop하기에는 너무 많은 데이터 -> 전처리를 통해 group by에 포함되도록 해야 함



```python
# 결측치 전처리
df['region'].fillna('미분류', inplace = True)
df['region'].value_counts().head()
```

<pre>
미분류       2042766
경기 수원시     122029
충북 청주시     116766
경남 창원시     107147
경남 김해시     100673
Name: region, dtype: int64
</pre>

```python
# 결측치 재확인
df['region'].value_counts().isnull().sum()
```

<pre>
0
</pre>
### type_of_business - 데이터 셋팅

- 범주형이지만, 종류가 너무 많아(145개) dummy 하여 사용하기는 어려움 -> 활용을 위해 파생변수 생성 필요 (group by)

- 결측치가 3952609 개 존재함

- 결측치를 drop하기에는 너무 많은 데이터 -> 전처리를 통해 group by에 포함되도록 해야 함



```python
# groupby에 결측을 포함시키기 위해, 결측을 문자로 대체
df['type_of_business'].fillna('미분류', inplace = True)
df['type_of_business'].value_counts().head()
```

<pre>
미분류        3952609
한식 음식점업     745905
두발 미용업      178475
의복 소매업      158234
기타 주점업      102413
Name: type_of_business, dtype: int64
</pre>

```python
# 결과 재확인
df['type_of_business'].value_counts().isnull().sum()
```

<pre>
0
</pre>
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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>region</th>
      <th>type_of_business</th>
      <th>std_mth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>6</td>
    </tr>
    <tr>
      <th>145</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>7</td>
    </tr>
    <tr>
      <th>323</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>8</td>
    </tr>
    <tr>
      <th>494</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>9</td>
    </tr>
    <tr>
      <th>654</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>


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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>std_mth</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>6</td>
      <td>747000.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>7</td>
      <td>1005000.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>8</td>
      <td>871571.43</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>9</td>
      <td>897857.14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>10</td>
      <td>835428.57</td>
    </tr>
  </tbody>
</table>
</div>


- group by의 경우 지정한 조건에 해당하는 값이 없으면 건너뛴다.

- 각 지점별로 '모든 월' 에 대한 amount가 들어가야 하므로, 매장별 매출에서 값이 생략된 월들은 0으로 값을 넣어줘야 한다.

- 그렇지 않을 경우 다른 데이터와 merge 할 경우 에러 발생, 혹은 잘못된 값이 입력될 수 있다.


매장별로 결측된 월이 있는지 확인



```python
total_amt_per_mth_and_store.groupby(['store_id'])['std_mth'].count()
```

<pre>
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
</pre>
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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>std_mth</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
      <th>20</th>
      <th>21</th>
      <th>22</th>
      <th>23</th>
      <th>24</th>
      <th>25</th>
      <th>26</th>
      <th>27</th>
      <th>28</th>
      <th>29</th>
      <th>30</th>
      <th>31</th>
      <th>32</th>
      <th>33</th>
      <th>34</th>
      <th>35</th>
      <th>36</th>
      <th>37</th>
      <th>38</th>
    </tr>
    <tr>
      <th>store_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>747000.00</td>
      <td>1005000.00</td>
      <td>871571.43</td>
      <td>897857.14</td>
      <td>835428.57</td>
      <td>697000.00</td>
      <td>761857.14</td>
      <td>585642.86</td>
      <td>794000.00</td>
      <td>720257.14</td>
      <td>685285.71</td>
      <td>744428.57</td>
      <td>682000.00</td>
      <td>728285.71</td>
      <td>749000.00</td>
      <td>840857.14</td>
      <td>600571.43</td>
      <td>630857.14</td>
      <td>812714.29</td>
      <td>643142.86</td>
      <td>685285.71</td>
      <td>848428.57</td>
      <td>636142.86</td>
      <td>686428.57</td>
      <td>707285.71</td>
      <td>758714.29</td>
      <td>679857.14</td>
      <td>651857.14</td>
      <td>739000.00</td>
      <td>676000.00</td>
      <td>874571.43</td>
      <td>682857.14</td>
      <td>515285.71</td>
    </tr>
    <tr>
      <th>1</th>
      <td>137214.29</td>
      <td>163000.00</td>
      <td>118142.86</td>
      <td>90428.57</td>
      <td>118071.43</td>
      <td>111857.14</td>
      <td>115571.43</td>
      <td>129642.86</td>
      <td>160214.29</td>
      <td>168428.57</td>
      <td>152571.43</td>
      <td>107500.00</td>
      <td>110357.14</td>
      <td>132571.43</td>
      <td>107642.86</td>
      <td>131357.14</td>
      <td>80142.86</td>
      <td>110142.86</td>
      <td>100714.29</td>
      <td>109571.43</td>
      <td>94214.29</td>
      <td>108357.14</td>
      <td>108857.14</td>
      <td>80500.00</td>
      <td>78285.71</td>
      <td>100785.71</td>
      <td>92142.86</td>
      <td>63571.43</td>
      <td>95000.00</td>
      <td>80785.71</td>
      <td>85285.71</td>
      <td>148285.71</td>
      <td>77428.57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>260714.29</td>
      <td>82857.14</td>
      <td>131428.57</td>
      <td>142857.14</td>
      <td>109714.29</td>
      <td>198571.43</td>
      <td>160000.00</td>
      <td>180714.29</td>
      <td>154285.71</td>
      <td>43571.43</td>
      <td>201428.57</td>
      <td>186428.57</td>
      <td>120571.43</td>
      <td>207142.86</td>
      <td>190000.00</td>
      <td>232857.14</td>
      <td>266714.29</td>
      <td>252857.14</td>
      <td>238571.43</td>
      <td>299714.29</td>
      <td>312857.14</td>
      <td>189714.29</td>
      <td>283571.43</td>
      <td>472857.14</td>
      <td>354285.71</td>
      <td>689285.71</td>
      <td>457857.14</td>
      <td>480714.29</td>
      <td>510000.00</td>
      <td>185428.57</td>
      <td>340714.29</td>
      <td>407857.14</td>
      <td>496857.14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>733428.57</td>
      <td>768928.57</td>
      <td>698428.57</td>
      <td>936428.57</td>
      <td>762714.29</td>
      <td>859571.43</td>
      <td>1069857.14</td>
      <td>689142.86</td>
      <td>1050142.86</td>
      <td>970285.71</td>
      <td>1085171.43</td>
      <td>1035857.14</td>
      <td>894142.86</td>
      <td>1027285.71</td>
      <td>1186857.14</td>
      <td>972571.43</td>
      <td>1060571.43</td>
      <td>1189142.86</td>
      <td>1010142.86</td>
      <td>831571.43</td>
      <td>651000.00</td>
      <td>908000.00</td>
      <td>792214.29</td>
      <td>775428.57</td>
      <td>881285.71</td>
      <td>1050928.57</td>
      <td>849285.71</td>
      <td>698142.86</td>
      <td>828428.57</td>
      <td>883000.00</td>
      <td>923857.14</td>
      <td>944857.14</td>
      <td>882285.71</td>
    </tr>
    <tr>
      <th>5</th>
      <td>342500.00</td>
      <td>432714.29</td>
      <td>263500.00</td>
      <td>232142.86</td>
      <td>211571.43</td>
      <td>182085.71</td>
      <td>147571.43</td>
      <td>120957.14</td>
      <td>186428.57</td>
      <td>169000.00</td>
      <td>312857.14</td>
      <td>235342.86</td>
      <td>475857.14</td>
      <td>410914.29</td>
      <td>297714.29</td>
      <td>291428.57</td>
      <td>396157.14</td>
      <td>399285.71</td>
      <td>441557.14</td>
      <td>388428.57</td>
      <td>316785.71</td>
      <td>370142.86</td>
      <td>297857.14</td>
      <td>443857.14</td>
      <td>563714.29</td>
      <td>607071.43</td>
      <td>482885.71</td>
      <td>195000.00</td>
      <td>324928.57</td>
      <td>383300.00</td>
      <td>399571.43</td>
      <td>323000.00</td>
      <td>215514.29</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2132</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>281142.86</td>
      <td>783428.57</td>
      <td>822000.00</td>
      <td>941142.86</td>
      <td>731142.86</td>
      <td>684571.43</td>
      <td>701000.00</td>
      <td>742428.57</td>
      <td>624614.29</td>
      <td>566857.14</td>
      <td>742857.14</td>
      <td>865285.71</td>
      <td>898428.57</td>
      <td>787857.14</td>
      <td>531857.14</td>
      <td>1095000.00</td>
      <td>1014071.43</td>
      <td>580785.71</td>
      <td>703857.14</td>
      <td>909142.86</td>
      <td>938428.57</td>
      <td>670571.43</td>
      <td>757857.14</td>
      <td>753428.57</td>
      <td>524142.86</td>
      <td>637714.29</td>
      <td>938571.43</td>
      <td>729857.14</td>
      <td>474285.71</td>
      <td>571142.86</td>
      <td>630428.57</td>
    </tr>
    <tr>
      <th>2133</th>
      <td>85000.00</td>
      <td>367857.14</td>
      <td>743571.43</td>
      <td>494714.29</td>
      <td>178571.43</td>
      <td>124285.71</td>
      <td>36285.71</td>
      <td>31857.14</td>
      <td>145114.29</td>
      <td>313128.57</td>
      <td>300685.71</td>
      <td>384057.14</td>
      <td>524342.86</td>
      <td>425342.86</td>
      <td>438257.14</td>
      <td>493757.14</td>
      <td>421214.29</td>
      <td>646628.57</td>
      <td>601171.43</td>
      <td>433414.29</td>
      <td>277342.86</td>
      <td>308485.71</td>
      <td>484071.43</td>
      <td>626071.43</td>
      <td>395700.00</td>
      <td>421614.29</td>
      <td>548942.86</td>
      <td>310971.43</td>
      <td>192700.00</td>
      <td>84714.29</td>
      <td>NaN</td>
      <td>84000.00</td>
      <td>116285.71</td>
    </tr>
    <tr>
      <th>2134</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>393000.00</td>
      <td>678214.29</td>
      <td>459071.43</td>
      <td>463428.57</td>
      <td>446285.71</td>
      <td>363571.43</td>
      <td>580285.71</td>
      <td>486857.14</td>
      <td>503642.86</td>
      <td>467785.71</td>
      <td>431642.86</td>
      <td>248714.29</td>
      <td>355714.29</td>
      <td>374142.86</td>
      <td>313785.71</td>
      <td>171857.14</td>
      <td>245571.43</td>
      <td>72357.14</td>
      <td>216142.86</td>
      <td>209785.71</td>
      <td>140714.29</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84428.57</td>
      <td>60785.71</td>
      <td>4285.71</td>
      <td>209428.57</td>
      <td>166000.00</td>
    </tr>
    <tr>
      <th>2135</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>357428.57</td>
      <td>786000.00</td>
      <td>760285.71</td>
      <td>751428.57</td>
      <td>682857.14</td>
      <td>544000.00</td>
      <td>656000.00</td>
      <td>631000.00</td>
      <td>698571.43</td>
      <td>611714.29</td>
      <td>763857.14</td>
      <td>675857.14</td>
      <td>575714.29</td>
      <td>575857.14</td>
      <td>473714.29</td>
      <td>505285.71</td>
      <td>521857.14</td>
      <td>563714.29</td>
      <td>443928.57</td>
      <td>468285.71</td>
      <td>445142.86</td>
      <td>577571.43</td>
      <td>714428.57</td>
      <td>438428.57</td>
      <td>566142.86</td>
      <td>509857.14</td>
      <td>850428.57</td>
      <td>589428.57</td>
      <td>541857.14</td>
      <td>462285.71</td>
      <td>404285.71</td>
    </tr>
    <tr>
      <th>2136</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>469214.29</td>
      <td>2713814.29</td>
      <td>2967357.14</td>
      <td>3364357.14</td>
      <td>3190642.86</td>
      <td>3364285.71</td>
      <td>2706714.29</td>
      <td>2869571.43</td>
      <td>1877857.14</td>
      <td>2023642.86</td>
      <td>2352071.43</td>
      <td>2197428.57</td>
      <td>2194428.57</td>
      <td>2333000.00</td>
      <td>1601785.71</td>
      <td>1222300.00</td>
      <td>2775714.29</td>
      <td>2012214.29</td>
      <td>2135428.57</td>
      <td>2427428.57</td>
      <td>1873642.86</td>
      <td>2227428.57</td>
    </tr>
  </tbody>
</table>
<p>1967 rows × 33 columns</p>
</div>


- pivot table을 통해 보았을때, '월' 의 중간 중간 nan값이 발생하는 것으로 보아, 실제 매출은 발생하였으나 누락된 데이터 일 것이라 가정

- nan값을 바로 앞, 뒤 standard_t의 매출로 채워 넣는다.



```python
# 발생한 nan값을 바로 앞/뒤의 값으로 채워넣는다.
# method = 'ffill', axis = 1 #전
# method = 'bfill', axis = 1 #후

total_amt_per_mth_and_store = check_nan_amount.fillna(method = 'ffill', axis = 1).fillna(method = 'bfill', axis = 1)
total_amt_per_mth_and_store.head(10)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>std_mth</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
      <th>20</th>
      <th>21</th>
      <th>22</th>
      <th>23</th>
      <th>24</th>
      <th>25</th>
      <th>26</th>
      <th>27</th>
      <th>28</th>
      <th>29</th>
      <th>30</th>
      <th>31</th>
      <th>32</th>
      <th>33</th>
      <th>34</th>
      <th>35</th>
      <th>36</th>
      <th>37</th>
      <th>38</th>
    </tr>
    <tr>
      <th>store_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>747000.00</td>
      <td>1005000.00</td>
      <td>871571.43</td>
      <td>897857.14</td>
      <td>835428.57</td>
      <td>697000.00</td>
      <td>761857.14</td>
      <td>585642.86</td>
      <td>794000.00</td>
      <td>720257.14</td>
      <td>685285.71</td>
      <td>744428.57</td>
      <td>682000.00</td>
      <td>728285.71</td>
      <td>749000.00</td>
      <td>840857.14</td>
      <td>600571.43</td>
      <td>630857.14</td>
      <td>812714.29</td>
      <td>643142.86</td>
      <td>685285.71</td>
      <td>848428.57</td>
      <td>636142.86</td>
      <td>686428.57</td>
      <td>707285.71</td>
      <td>758714.29</td>
      <td>679857.14</td>
      <td>651857.14</td>
      <td>739000.00</td>
      <td>676000.00</td>
      <td>874571.43</td>
      <td>682857.14</td>
      <td>515285.71</td>
    </tr>
    <tr>
      <th>1</th>
      <td>137214.29</td>
      <td>163000.00</td>
      <td>118142.86</td>
      <td>90428.57</td>
      <td>118071.43</td>
      <td>111857.14</td>
      <td>115571.43</td>
      <td>129642.86</td>
      <td>160214.29</td>
      <td>168428.57</td>
      <td>152571.43</td>
      <td>107500.00</td>
      <td>110357.14</td>
      <td>132571.43</td>
      <td>107642.86</td>
      <td>131357.14</td>
      <td>80142.86</td>
      <td>110142.86</td>
      <td>100714.29</td>
      <td>109571.43</td>
      <td>94214.29</td>
      <td>108357.14</td>
      <td>108857.14</td>
      <td>80500.00</td>
      <td>78285.71</td>
      <td>100785.71</td>
      <td>92142.86</td>
      <td>63571.43</td>
      <td>95000.00</td>
      <td>80785.71</td>
      <td>85285.71</td>
      <td>148285.71</td>
      <td>77428.57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>260714.29</td>
      <td>82857.14</td>
      <td>131428.57</td>
      <td>142857.14</td>
      <td>109714.29</td>
      <td>198571.43</td>
      <td>160000.00</td>
      <td>180714.29</td>
      <td>154285.71</td>
      <td>43571.43</td>
      <td>201428.57</td>
      <td>186428.57</td>
      <td>120571.43</td>
      <td>207142.86</td>
      <td>190000.00</td>
      <td>232857.14</td>
      <td>266714.29</td>
      <td>252857.14</td>
      <td>238571.43</td>
      <td>299714.29</td>
      <td>312857.14</td>
      <td>189714.29</td>
      <td>283571.43</td>
      <td>472857.14</td>
      <td>354285.71</td>
      <td>689285.71</td>
      <td>457857.14</td>
      <td>480714.29</td>
      <td>510000.00</td>
      <td>185428.57</td>
      <td>340714.29</td>
      <td>407857.14</td>
      <td>496857.14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>733428.57</td>
      <td>768928.57</td>
      <td>698428.57</td>
      <td>936428.57</td>
      <td>762714.29</td>
      <td>859571.43</td>
      <td>1069857.14</td>
      <td>689142.86</td>
      <td>1050142.86</td>
      <td>970285.71</td>
      <td>1085171.43</td>
      <td>1035857.14</td>
      <td>894142.86</td>
      <td>1027285.71</td>
      <td>1186857.14</td>
      <td>972571.43</td>
      <td>1060571.43</td>
      <td>1189142.86</td>
      <td>1010142.86</td>
      <td>831571.43</td>
      <td>651000.00</td>
      <td>908000.00</td>
      <td>792214.29</td>
      <td>775428.57</td>
      <td>881285.71</td>
      <td>1050928.57</td>
      <td>849285.71</td>
      <td>698142.86</td>
      <td>828428.57</td>
      <td>883000.00</td>
      <td>923857.14</td>
      <td>944857.14</td>
      <td>882285.71</td>
    </tr>
    <tr>
      <th>5</th>
      <td>342500.00</td>
      <td>432714.29</td>
      <td>263500.00</td>
      <td>232142.86</td>
      <td>211571.43</td>
      <td>182085.71</td>
      <td>147571.43</td>
      <td>120957.14</td>
      <td>186428.57</td>
      <td>169000.00</td>
      <td>312857.14</td>
      <td>235342.86</td>
      <td>475857.14</td>
      <td>410914.29</td>
      <td>297714.29</td>
      <td>291428.57</td>
      <td>396157.14</td>
      <td>399285.71</td>
      <td>441557.14</td>
      <td>388428.57</td>
      <td>316785.71</td>
      <td>370142.86</td>
      <td>297857.14</td>
      <td>443857.14</td>
      <td>563714.29</td>
      <td>607071.43</td>
      <td>482885.71</td>
      <td>195000.00</td>
      <td>324928.57</td>
      <td>383300.00</td>
      <td>399571.43</td>
      <td>323000.00</td>
      <td>215514.29</td>
    </tr>
    <tr>
      <th>6</th>
      <td>568857.14</td>
      <td>568857.14</td>
      <td>568857.14</td>
      <td>1440142.86</td>
      <td>1238857.14</td>
      <td>1055428.57</td>
      <td>926857.14</td>
      <td>885642.86</td>
      <td>800357.14</td>
      <td>930714.29</td>
      <td>855071.43</td>
      <td>1029785.71</td>
      <td>1071571.43</td>
      <td>1037214.29</td>
      <td>1054857.14</td>
      <td>937857.14</td>
      <td>1216285.71</td>
      <td>1833571.43</td>
      <td>2429500.00</td>
      <td>2147714.29</td>
      <td>2113357.14</td>
      <td>2348714.29</td>
      <td>1876857.14</td>
      <td>1808357.14</td>
      <td>1752285.71</td>
      <td>1583785.71</td>
      <td>1628785.71</td>
      <td>2074071.43</td>
      <td>1907642.86</td>
      <td>2389142.86</td>
      <td>2230285.71</td>
      <td>2015500.00</td>
      <td>2463857.14</td>
    </tr>
    <tr>
      <th>7</th>
      <td>107857.14</td>
      <td>107857.14</td>
      <td>107857.14</td>
      <td>375642.86</td>
      <td>323642.86</td>
      <td>345000.00</td>
      <td>291428.57</td>
      <td>231614.29</td>
      <td>271357.14</td>
      <td>249857.14</td>
      <td>131500.00</td>
      <td>118642.86</td>
      <td>53285.71</td>
      <td>372285.71</td>
      <td>183000.00</td>
      <td>527857.14</td>
      <td>218214.29</td>
      <td>817714.29</td>
      <td>750645.71</td>
      <td>761571.43</td>
      <td>636571.43</td>
      <td>339857.14</td>
      <td>1039357.14</td>
      <td>265714.29</td>
      <td>419542.86</td>
      <td>462842.86</td>
      <td>423128.57</td>
      <td>320328.57</td>
      <td>420028.57</td>
      <td>314385.71</td>
      <td>302414.29</td>
      <td>136471.43</td>
      <td>57971.43</td>
    </tr>
    <tr>
      <th>8</th>
      <td>192571.43</td>
      <td>192571.43</td>
      <td>192571.43</td>
      <td>192571.43</td>
      <td>192571.43</td>
      <td>192571.43</td>
      <td>735500.00</td>
      <td>467857.14</td>
      <td>475642.86</td>
      <td>603500.00</td>
      <td>1074642.86</td>
      <td>1144571.43</td>
      <td>1030928.57</td>
      <td>1375571.43</td>
      <td>1078928.57</td>
      <td>984500.00</td>
      <td>896785.71</td>
      <td>514500.00</td>
      <td>552214.29</td>
      <td>618785.71</td>
      <td>461714.29</td>
      <td>744500.00</td>
      <td>867071.43</td>
      <td>1837428.57</td>
      <td>1359857.14</td>
      <td>1213542.86</td>
      <td>1086000.00</td>
      <td>1369557.14</td>
      <td>1272071.43</td>
      <td>1260557.14</td>
      <td>1157257.14</td>
      <td>1134671.43</td>
      <td>1298328.57</td>
    </tr>
    <tr>
      <th>9</th>
      <td>107142.86</td>
      <td>107142.86</td>
      <td>107142.86</td>
      <td>107142.86</td>
      <td>107142.86</td>
      <td>637142.86</td>
      <td>603571.43</td>
      <td>225428.57</td>
      <td>287142.86</td>
      <td>344428.57</td>
      <td>352857.14</td>
      <td>208571.43</td>
      <td>178571.43</td>
      <td>761714.29</td>
      <td>535000.00</td>
      <td>715714.29</td>
      <td>672142.86</td>
      <td>634285.71</td>
      <td>333714.29</td>
      <td>295428.57</td>
      <td>628285.71</td>
      <td>318571.43</td>
      <td>1016857.14</td>
      <td>638571.43</td>
      <td>276571.43</td>
      <td>340000.00</td>
      <td>254285.71</td>
      <td>926571.43</td>
      <td>871428.57</td>
      <td>692857.14</td>
      <td>662857.14</td>
      <td>370000.00</td>
      <td>405714.29</td>
    </tr>
    <tr>
      <th>10</th>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>496714.29</td>
      <td>492571.43</td>
      <td>341857.14</td>
      <td>442428.57</td>
      <td>438714.29</td>
      <td>438571.43</td>
      <td>470428.57</td>
      <td>144428.57</td>
      <td>444714.29</td>
      <td>466714.29</td>
      <td>722857.14</td>
      <td>338571.43</td>
      <td>475000.00</td>
      <td>290285.71</td>
      <td>607857.14</td>
      <td>444571.43</td>
      <td>641428.57</td>
      <td>795571.43</td>
      <td>499285.71</td>
      <td>590142.86</td>
      <td>518428.57</td>
      <td>525142.86</td>
      <td>654857.14</td>
    </tr>
  </tbody>
</table>
</div>


- train_df와 병합을 위해 pivot_table 형태인 total_amt_per_mth_and_store 테이블을 stack() 함수를 사용해 동일한 형태의 DataFrame으로 변경



- stack() : column 과 row를 바꾸는 함수

- 위의 pivot_table 기준으로보면 store_id, std_mth, amount가 column이 되고, 기존 columns 별로 입력되있던 값이 row가 된다.



```python
total_amt_per_mth_and_store = total_amt_per_mth_and_store.stack().reset_index() # index 번호 새로 부여
```


```python
total_amt_per_mth_and_store
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>std_mth</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>6</td>
      <td>747000.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>7</td>
      <td>1005000.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>8</td>
      <td>871571.43</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>9</td>
      <td>897857.14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>10</td>
      <td>835428.57</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>64906</th>
      <td>2136</td>
      <td>34</td>
      <td>2012214.29</td>
    </tr>
    <tr>
      <th>64907</th>
      <td>2136</td>
      <td>35</td>
      <td>2135428.57</td>
    </tr>
    <tr>
      <th>64908</th>
      <td>2136</td>
      <td>36</td>
      <td>2427428.57</td>
    </tr>
    <tr>
      <th>64909</th>
      <td>2136</td>
      <td>37</td>
      <td>1873642.86</td>
    </tr>
    <tr>
      <th>64910</th>
      <td>2136</td>
      <td>38</td>
      <td>2227428.57</td>
    </tr>
  </tbody>
</table>
<p>64911 rows × 3 columns</p>
</div>



```python
# amount로 컬럼명 변경
total_amt_per_mth_and_store.rename({0:"amount"}, axis = 1, inplace = True)
total_amt_per_mth_and_store.head(3)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>std_mth</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>6</td>
      <td>747000.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>7</td>
      <td>1005000.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>8</td>
      <td>871571.43</td>
    </tr>
  </tbody>
</table>
</div>


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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>region</th>
      <th>type_of_business</th>
      <th>std_mth</th>
      <th>평균할부율</th>
      <th>1_before_amount</th>
      <th>2_before_amount</th>
      <th>3_before_amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>9</td>
      <td>0.04</td>
      <td>871571.43</td>
      <td>1005000.00</td>
      <td>747000.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>10</td>
      <td>0.04</td>
      <td>897857.14</td>
      <td>871571.43</td>
      <td>1005000.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>11</td>
      <td>0.04</td>
      <td>835428.57</td>
      <td>897857.14</td>
      <td>871571.43</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>12</td>
      <td>0.04</td>
      <td>697000.00</td>
      <td>835428.57</td>
      <td>897857.14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>13</td>
      <td>0.04</td>
      <td>761857.14</td>
      <td>697000.00</td>
      <td>835428.57</td>
    </tr>
  </tbody>
</table>
</div>


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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>region</th>
      <th>std_mth</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강원 강릉시</td>
      <td>6</td>
      <td>623271.75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강원 강릉시</td>
      <td>7</td>
      <td>501311.43</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강원 강릉시</td>
      <td>8</td>
      <td>508130.79</td>
    </tr>
  </tbody>
</table>
</div>


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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>region</th>
      <th>type_of_business</th>
      <th>std_mth</th>
      <th>평균할부율</th>
      <th>1_before_amount</th>
      <th>2_before_amount</th>
      <th>3_before_amount</th>
      <th>1_before_amount_of_region</th>
      <th>2_before_amount_of_region</th>
      <th>3_before_amount_of_region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>9</td>
      <td>0.04</td>
      <td>871571.43</td>
      <td>1005000.00</td>
      <td>747000.00</td>
      <td>761987.42</td>
      <td>756108.67</td>
      <td>739654.07</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>미분류</td>
      <td>미분류</td>
      <td>9</td>
      <td>0.00</td>
      <td>118142.86</td>
      <td>163000.00</td>
      <td>137214.29</td>
      <td>761987.42</td>
      <td>756108.67</td>
      <td>739654.07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>미분류</td>
      <td>미분류</td>
      <td>9</td>
      <td>0.08</td>
      <td>131428.57</td>
      <td>82857.14</td>
      <td>260714.29</td>
      <td>761987.42</td>
      <td>756108.67</td>
      <td>739654.07</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>미분류</td>
      <td>의복 액세서리 및 모조 장신구 도매업</td>
      <td>9</td>
      <td>0.08</td>
      <td>263500.00</td>
      <td>432714.29</td>
      <td>342500.00</td>
      <td>761987.42</td>
      <td>756108.67</td>
      <td>739654.07</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>미분류</td>
      <td>미분류</td>
      <td>9</td>
      <td>0.01</td>
      <td>107857.14</td>
      <td>107857.14</td>
      <td>107857.14</td>
      <td>761987.42</td>
      <td>756108.67</td>
      <td>739654.07</td>
    </tr>
  </tbody>
</table>
</div>


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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>region</th>
      <th>type_of_business</th>
      <th>std_mth</th>
      <th>평균할부율</th>
      <th>1_before_amount</th>
      <th>2_before_amount</th>
      <th>3_before_amount</th>
      <th>1_before_amount_of_region</th>
      <th>2_before_amount_of_region</th>
      <th>3_before_amount_of_region</th>
      <th>1_before_amount_of_type_of_business</th>
      <th>2_before_amount_of_type_of_business</th>
      <th>3_before_amount_of_type_of_business</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>9</td>
      <td>0.04</td>
      <td>871571.43</td>
      <td>1005000.00</td>
      <td>747000.00</td>
      <td>761987.42</td>
      <td>756108.67</td>
      <td>739654.07</td>
      <td>761025.00</td>
      <td>804979.76</td>
      <td>679950.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>792</td>
      <td>미분류</td>
      <td>기타 미용업</td>
      <td>9</td>
      <td>0.22</td>
      <td>681142.86</td>
      <td>880857.14</td>
      <td>733714.29</td>
      <td>761987.42</td>
      <td>756108.67</td>
      <td>739654.07</td>
      <td>761025.00</td>
      <td>804979.76</td>
      <td>679950.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>경기 안양시</td>
      <td>기타 미용업</td>
      <td>9</td>
      <td>0.05</td>
      <td>879242.86</td>
      <td>730857.14</td>
      <td>845285.71</td>
      <td>828831.71</td>
      <td>588733.00</td>
      <td>955973.29</td>
      <td>761025.00</td>
      <td>804979.76</td>
      <td>679950.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>192</td>
      <td>경기 화성시</td>
      <td>기타 미용업</td>
      <td>9</td>
      <td>0.10</td>
      <td>579000.00</td>
      <td>523428.57</td>
      <td>551142.86</td>
      <td>1234460.01</td>
      <td>1227920.91</td>
      <td>1180455.31</td>
      <td>761025.00</td>
      <td>804979.76</td>
      <td>679950.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>536</td>
      <td>서울 광진구</td>
      <td>기타 미용업</td>
      <td>9</td>
      <td>0.01</td>
      <td>96285.71</td>
      <td>79857.14</td>
      <td>99857.14</td>
      <td>3786819.95</td>
      <td>3397972.56</td>
      <td>3524074.62</td>
      <td>761025.00</td>
      <td>804979.76</td>
      <td>679950.00</td>
    </tr>
  </tbody>
</table>
</div>


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

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>std_mth</th>
      <th>Y_1</th>
      <th>Y_2</th>
      <th>Y_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>835428.57</td>
      <td>697000.00</td>
      <td>761857.14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>725142.86</td>
      <td>653428.57</td>
      <td>730071.43</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>741714.29</td>
      <td>608857.14</td>
      <td>844285.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>529000.00</td>
      <td>545142.86</td>
      <td>449714.29</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9</td>
      <td>87142.86</td>
      <td>159928.57</td>
      <td>124142.86</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>50226</th>
      <td>31</td>
      <td>13623585.71</td>
      <td>10826500.00</td>
      <td>12053585.71</td>
    </tr>
    <tr>
      <th>50227</th>
      <td>32</td>
      <td>10826500.00</td>
      <td>12053585.71</td>
      <td>12916214.29</td>
    </tr>
    <tr>
      <th>50228</th>
      <td>33</td>
      <td>12053585.71</td>
      <td>12916214.29</td>
      <td>13290000.00</td>
    </tr>
    <tr>
      <th>50229</th>
      <td>34</td>
      <td>12916214.29</td>
      <td>13290000.00</td>
      <td>15355300.00</td>
    </tr>
    <tr>
      <th>50230</th>
      <td>35</td>
      <td>13290000.00</td>
      <td>15355300.00</td>
      <td>11063685.71</td>
    </tr>
  </tbody>
</table>
<p>50231 rows × 4 columns</p>
</div>


- for loop가 수행되면서 각각 i=1 일때, **total_amt_per_mth_and_store의 std_mth 기준으로** +1 인 시점의 amount 가 Y_1이 된다.

- i=2 일때는 std_mth 기준 +2 인 시점의 amount 가 Y_2이 되고, i=3 일때, std_mth 기준 +3 인 시점의 amount 가 Y_3이 된다.



```python
# Y변수 (미래 3개월의 매출) 생성
train_df['Y'] = train_df['Y_1'] + train_df['Y_2'] + train_df['Y_3']
```


```python
train_df.to_csv('train_df.csv')
```
