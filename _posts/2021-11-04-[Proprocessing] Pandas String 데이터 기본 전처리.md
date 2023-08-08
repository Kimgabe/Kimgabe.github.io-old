---
layout: single
title:  "[Proprocessing] Pandas String 데이터 기본 전처리"
categories: [Personal Study, Pre-processing, Tips]
tag: [python, 전처리, Pre-processing, pandas, 문자열 데이터 전처리, 문자열 찾기, 문자열 채우기, 공백제거하기, 대소문자 변경]
toc: true
header :
    teaser : "/assets/img/teaser/Blog_Tips-001.png"
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


# Intro.

---



- 데이터 분석에 사용되는 기법은 전통적인 통계적 기법과 크게 다르지 않다. 다만 최근들어 '빅데이터' 분석이 각광 받는 이유는 말그대로 '빅데이터'를 모으고 조합해 분석함으로써 기존에 얻을 수 없는 다양한 인사이트를 얻을 수 있기 때문이다.

- 실제로 많은 기업들이 데이터를 기반으로 전략을 세우고, 의사결정을 내리고자하며 데이터 분석가 포지션이 주목받았다.

- 하지만 '데이터 분석'을 시작함에 있어 가장 중요한 것은 바로 '데이터 전처리(Pre-processing)'이다.

- 대부분의 원시데이터(raw data)는 불완전하거나, 서로 연관이 없거나, 오류가 있을 수 있기 때문이다.

- 본 포스팅에서는 pandas를 이용한 기본적인 전처리를 위한 cheat sheet 코드들을 기록하고자 한다.



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


```python
# 샘플 데이터 load
df = pd.read_csv("서울시공시지가(2020).csv", encoding='cp949', index_col=0)
print(df.info())
df.head()
```

<pre>
<class 'pandas.core.frame.DataFrame'>
Int64Index: 909537 entries, 30 to 30302880
Data columns (total 12 columns):
 #   Column   Non-Null Count   Dtype  
---  ------   --------------   -----  
 0   고유번호     909537 non-null  float64
 1   법정동코드    909537 non-null  int64  
 2   법정동명     909537 non-null  object 
 3   특수지구분코드  909537 non-null  int64  
 4   특수지구분명   909537 non-null  object 
 5   지번       909537 non-null  object 
 6   기준연도     909537 non-null  int64  
 7   기준월      909537 non-null  int64  
 8   공시지가     909537 non-null  int64  
 9   공시일자     909537 non-null  object 
 10  표준지여부    909537 non-null  object 
 11  데이터기준일자  909537 non-null  object 
dtypes: float64(1), int64(5), object(6)
memory usage: 90.2+ MB
None
</pre>
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
      <th>고유번호</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>특수지구분코드</th>
      <th>특수지구분명</th>
      <th>지번</th>
      <th>기준연도</th>
      <th>기준월</th>
      <th>공시지가</th>
      <th>공시일자</th>
      <th>표준지여부</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>1</td>
      <td>2020</td>
      <td>1</td>
      <td>4357000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>01월 01일</td>
      <td>2020</td>
      <td>1</td>
      <td>1392000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
    <tr>
      <th>75</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>01월 02일</td>
      <td>2020</td>
      <td>1</td>
      <td>2520000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
    <tr>
      <th>107</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>01월 03일</td>
      <td>2020</td>
      <td>1</td>
      <td>4337000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
    <tr>
      <th>120</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>01월 04일</td>
      <td>2020</td>
      <td>1</td>
      <td>1554000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
  </tbody>
</table>
</div>


# string 인덱싱 : str[]



- 데이터 형식이 object인 컬럼

- iloc이나 loc 으로 인덱싱 하는 것과 동일한 방식

- **str.find를 접목**해 원하는 문자열만 잘라서 추출할 수 있다.



```python
# 맨처음부터 5글자 추출 
# 
df['법정동명'].str[:5].head()
```

<pre>
30     서울특별시
43     서울특별시
75     서울특별시
107    서울특별시
120    서울특별시
Name: 법정동명, dtype: object
</pre>
## 원하는 문자열 위치 찾아서 slice 하기



```python
# find로 원하는 문자열 위치 찾아서 idx 번호 확인
print(df['법정동명'].str.find('특').head(1))
print(df['법정동명'].str.find('별').head(1))
```

<pre>
30    2
Name: 법정동명, dtype: int64
30    3
Name: 법정동명, dtype: int64
</pre>

```python
df['법정동명'].str[2:4].head()
```

<pre>
30     특별
43     특별
75     특별
107    특별
120    특별
Name: 법정동명, dtype: object
</pre>
# string split : str.split()



## 데이터를 split해서 컬럼으로 나누기



- str.split("") 에서 "" 사이에 split하는 기준이 될 조건을 입력한다.



```python
df[['법정동코드','법정동명']].head(3)
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
      <th>법정동코드</th>
      <th>법정동명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
    </tr>
    <tr>
      <th>75</th>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
    </tr>
  </tbody>
</table>
</div>



```python
df['법정동명'].str.split(" ") # 공백 = 띄어쓰기 기준으로 split
```

<pre>
30          [서울특별시, 종로구, 청운동]
43          [서울특별시, 종로구, 청운동]
75          [서울특별시, 종로구, 청운동]
107         [서울특별시, 종로구, 청운동]
120         [서울특별시, 종로구, 청운동]
                  ...        
30302774    [서울특별시, 강동구, 강일동]
30302784    [서울특별시, 강동구, 강일동]
30302815    [서울특별시, 강동구, 강일동]
30302846    [서울특별시, 강동구, 강일동]
30302880    [서울특별시, 강동구, 강일동]
Name: 법정동명, Length: 909537, dtype: object
</pre>

```python
# df에 바로 컬럼으로 추가하기(1)
# expand=True 이면 split될때마다 하나의 컬럼으로 구분된다.
df['법정동명'].str.split(" ", expand=True).head()
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
    <tr>
      <th>43</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
    <tr>
      <th>75</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
    <tr>
      <th>107</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
    <tr>
      <th>120</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
  </tbody>
</table>
</div>



```python
# df에 바로 컬럼으로 추가하기(2)
# split한 Series 형태의 결과를 DataFrame으로 만들기
split = df['법정동명'].str.split(" ").head()
split = split.apply(lambda x : pd.Series(x))
split
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
    <tr>
      <th>43</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
    <tr>
      <th>75</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
    <tr>
      <th>107</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
    <tr>
      <th>120</th>
      <td>서울특별시</td>
      <td>종로구</td>
      <td>청운동</td>
    </tr>
  </tbody>
</table>
</div>



```python
# tip. df.stack()으로 데이터 프레임의 행 <-> 열 바꾸기 도 가능
split.stack()
```

<pre>
30   0    서울특별시
     1      종로구
     2      청운동
43   0    서울특별시
     1      종로구
     2      청운동
75   0    서울특별시
     1      종로구
     2      청운동
107  0    서울특별시
     1      종로구
     2      청운동
120  0    서울특별시
     1      종로구
     2      청운동
dtype: object
</pre>
## 한 데이터를 split으로 여러 행으로 나누기



```python
# 예제 용 df 생성
df2 = pd.DataFrame({'foo': ['a,b,c,d,e', 'd,e,f', 'h,i']})
df2
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
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a,b,c,d,e</td>
    </tr>
    <tr>
      <th>1</th>
      <td>d,e,f</td>
    </tr>
    <tr>
      <th>2</th>
      <td>h,i</td>
    </tr>
  </tbody>
</table>
</div>



```python
# split을 사용해서 , 기준으로 데이어를 나누기
df2['foo'].str.split(',')
```

<pre>
0    [a, b, c, d, e]
1          [d, e, f]
2             [h, i]
Name: foo, dtype: object
</pre>

```python
# 동일 결과
df2.foo.str.split(',')
```

<pre>
0    [a, b, c, d, e]
1          [d, e, f]
2             [h, i]
Name: foo, dtype: object
</pre>
# 시작하는 글자와 일치하는 문자열 찾기 str.startwith()



- boolean을 반환한다.

- 입력한 글자로 시작하면 True / 아니면 False



```python
# 그냥 조건입력만 하면 T / F로만 나온다.
df['법정동명'].str.startswith("서울")
```

<pre>
30          True
43          True
75          True
107         True
120         True
            ... 
30302774    True
30302784    True
30302815    True
30302846    True
30302880    True
Name: 법정동명, Length: 909537, dtype: bool
</pre>

```python
# 실제 데이터를 보려면 
df[df['법정동명'].str.startswith("서울")].head(2)
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
      <th>고유번호</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>특수지구분코드</th>
      <th>특수지구분명</th>
      <th>지번</th>
      <th>기준연도</th>
      <th>기준월</th>
      <th>공시지가</th>
      <th>공시일자</th>
      <th>표준지여부</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>1</td>
      <td>2020</td>
      <td>1</td>
      <td>4357000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>01월 01일</td>
      <td>2020</td>
      <td>1</td>
      <td>1392000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 시작글자가 일치하지 않으면 아무것도 출력되지 않는다. 
df[df['법정동명'].str.startswith("종로구")].head(2)
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
      <th>고유번호</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>특수지구분코드</th>
      <th>특수지구분명</th>
      <th>지번</th>
      <th>기준연도</th>
      <th>기준월</th>
      <th>공시지가</th>
      <th>공시일자</th>
      <th>표준지여부</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>


# 끝 글자와 일치하는 문자열 찾기 str.endswith()



- str.startswith()와 동일방식



```python
# 그냥 조건입력만 하면 T / F로만 나온다.
df['법정동명'].str.endswith("구")
```

<pre>
30          False
43          False
75          False
107         False
120         False
            ...  
30302774    False
30302784    False
30302815    False
30302846    False
30302880    False
Name: 법정동명, Length: 909537, dtype: bool
</pre>

```python
# 실제 데이터를 보려면 
df[df['법정동명'].str.endswith("쌍문동")].head(2)
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
      <th>고유번호</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>특수지구분코드</th>
      <th>특수지구분명</th>
      <th>지번</th>
      <th>기준연도</th>
      <th>기준월</th>
      <th>공시지가</th>
      <th>공시일자</th>
      <th>표준지여부</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12266863</th>
      <td>1132010000000000000.00</td>
      <td>1132010500</td>
      <td>서울특별시 도봉구 쌍문동</td>
      <td>1</td>
      <td>일반</td>
      <td>07월 02일</td>
      <td>2020</td>
      <td>1</td>
      <td>2610000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
    <tr>
      <th>12266891</th>
      <td>1132010000000000000.00</td>
      <td>1132010500</td>
      <td>서울특별시 도봉구 쌍문동</td>
      <td>1</td>
      <td>일반</td>
      <td>07월 17일</td>
      <td>2020</td>
      <td>1</td>
      <td>854700</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 끝글자가 일치하지 않으면 아무것도 출력되지 않는다.
df[df['법정동명'].str.endswith("쌍문")].head(2)
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
      <th>고유번호</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>특수지구분코드</th>
      <th>특수지구분명</th>
      <th>지번</th>
      <th>기준연도</th>
      <th>기준월</th>
      <th>공시지가</th>
      <th>공시일자</th>
      <th>표준지여부</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>


# 문자열을 포함하는 데이터 찾기 str.contains()



- 시작과 끝글자말고, 중간에 있는 글자값을 찾고 싶을때 사용



```python
# str.endswith()에서는 일치하는 결과가 없었지만 이번에는 출력이 된다.
df[df['법정동명'].str.contains("쌍문")].head(2)
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
      <th>고유번호</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>특수지구분코드</th>
      <th>특수지구분명</th>
      <th>지번</th>
      <th>기준연도</th>
      <th>기준월</th>
      <th>공시지가</th>
      <th>공시일자</th>
      <th>표준지여부</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12266863</th>
      <td>1132010000000000000.00</td>
      <td>1132010500</td>
      <td>서울특별시 도봉구 쌍문동</td>
      <td>1</td>
      <td>일반</td>
      <td>07월 02일</td>
      <td>2020</td>
      <td>1</td>
      <td>2610000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
    <tr>
      <th>12266891</th>
      <td>1132010000000000000.00</td>
      <td>1132010500</td>
      <td>서울특별시 도봉구 쌍문동</td>
      <td>1</td>
      <td>일반</td>
      <td>07월 17일</td>
      <td>2020</td>
      <td>1</td>
      <td>854700</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 한글자도 가능하다.
df[df['법정동명'].str.contains("특")].head(2)
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
      <th>고유번호</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>특수지구분코드</th>
      <th>특수지구분명</th>
      <th>지번</th>
      <th>기준연도</th>
      <th>기준월</th>
      <th>공시지가</th>
      <th>공시일자</th>
      <th>표준지여부</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>1</td>
      <td>2020</td>
      <td>1</td>
      <td>4357000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1111010000000000000.00</td>
      <td>1111010100</td>
      <td>서울특별시 종로구 청운동</td>
      <td>1</td>
      <td>일반</td>
      <td>01월 01일</td>
      <td>2020</td>
      <td>1</td>
      <td>1392000</td>
      <td>2020-05-29</td>
      <td>N</td>
      <td>2021-08-03</td>
    </tr>
  </tbody>
</table>
</div>


# 조건에 부합하는 모든 값 찾기 str.findall()



- 정규표현식을 섞어서 문자 + 숫자 등도 찾을 수 있다.



```python
# 지번 컬럼에서 '\w = 숫자' + '일' 인 데이터 찾기
df['지번'].str.findall('\w+일').head()
```

<pre>
30        []
43     [01일]
75     [02일]
107    [03일]
120    [04일]
Name: 지번, dtype: object
</pre>
# 특정 문자의 위치 찾기 str.find() 



- 시작점 (왼쪽) 부터 검색을 시작해서 위치를 반환한다.

- 일치하는 데이터가 없으면 -1을 return한다.



```python
# 법정동명 컬럼에서 ' ' <- 공백을 찾겠다.
df['법정동명'].str.find(' ').head()

# 모든 값이 '서울특별시 ~구 ~동'형태이다.
# 즉 첫번째 ' '는 서울특별시 바로 뒤 인 5번째 idx 값이다.
```

<pre>
30     5
43     5
75     5
107    5
120    5
Name: 법정동명, dtype: int64
</pre>
## 오른쪽부터 찾기 str.rfind()



- 오른쪽부터 검색을 시작한다.

- sub 옵션으로 부분일치도 찾을 수 있다.



```python
# 법정동명 컬럼의 각 row에서 오른쪽부터 검색했을때 '구'가 처음 등장하는 위치(idx)
df['법정동명'].str.rfind('구').head()
```

<pre>
30     8
43     8
75     8
107    8
120    8
Name: 법정동명, dtype: int64
</pre>
# 문자열 대체하기 str.replace()



```python
# 공백(" ")을 '_'로 replace
df['법정동명'].str.replace(" ",'_').head()
```

<pre>
30     서울특별시_종로구_청운동
43     서울특별시_종로구_청운동
75     서울특별시_종로구_청운동
107    서울특별시_종로구_청운동
120    서울특별시_종로구_청운동
Name: 법정동명, dtype: object
</pre>
# 원하는 문자열 추출하기 str.extract()



- () 내에 패턴을 지정해야 한다.

- 패턴과 일치하는 단어가 없으면 NaN이 출력된다.



```python
# 단일 조건
df['법정동명'].str.extract('(\w*시)').head()
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>서울특별시</td>
    </tr>
    <tr>
      <th>43</th>
      <td>서울특별시</td>
    </tr>
    <tr>
      <th>75</th>
      <td>서울특별시</td>
    </tr>
    <tr>
      <th>107</th>
      <td>서울특별시</td>
    </tr>
    <tr>
      <th>120</th>
      <td>서울특별시</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 중복조건 : '|' 를 통해 중복 조건을 지정할 수 있다.
# 일치 조건이 없다면 NaN이 출력된다.
df['법정동명'].str.extract('(\w*시)|( \w*동)').head()
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
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>서울특별시</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>43</th>
      <td>서울특별시</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75</th>
      <td>서울특별시</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>107</th>
      <td>서울특별시</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>120</th>
      <td>서울특별시</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


# 문자열 길이 채우기 str.pad(width=, side=, fillchar='')



- 문자열 길이가 고정되어 특정 문자열 수 만큼 값을 채워줘야 할때 활용한다.

- with로 총 몇개의 문자열이 되야 하는지

- side로 문자열값의 left / right 어느쪽을 채울건지

- fillchar로 어떤걸로 채울건지 지정할 수 있다.



```python
# 각 rows의 문자열 len()한 값이 20이 되도록
# 문자열값의 오른쪽부터 
# '+'를 사용해서 채운다

df['법정동명'].str.pad(width=20, side='right', fillchar='+').head()
```

<pre>
30     서울특별시 종로구 청운동+++++++
43     서울특별시 종로구 청운동+++++++
75     서울특별시 종로구 청운동+++++++
107    서울특별시 종로구 청운동+++++++
120    서울특별시 종로구 청운동+++++++
Name: 법정동명, dtype: object
</pre>
## 좌/우 동시에 width만큼 채워넣기 : str.center()



```python
# side를 생략하고, pad대신에 center을 사용하면 양쪽에 지정한 문자열로 width 값이 될때까지 채운다.
df['법정동명'].str.center(width=30, fillchar='+').head()
```

<pre>
30     ++++++++서울특별시 종로구 청운동+++++++++
43     ++++++++서울특별시 종로구 청운동+++++++++
75     ++++++++서울특별시 종로구 청운동+++++++++
107    ++++++++서울특별시 종로구 청운동+++++++++
120    ++++++++서울특별시 종로구 청운동+++++++++
Name: 법정동명, dtype: object
</pre>
## 왼쪽부터 0으로 채우기 : str.zfill()



```python
df['법정동명'].str.zfill(width=20).head()
```

<pre>
30     0000000서울특별시 종로구 청운동
43     0000000서울특별시 종로구 청운동
75     0000000서울특별시 종로구 청운동
107    0000000서울특별시 종로구 청운동
120    0000000서울특별시 종로구 청운동
Name: 법정동명, dtype: object
</pre>
# 공백 제거 strip()



```python
# 예제용 df
df3 = pd.DataFrame({'col1':['abcde  ',' FFFFghij ','abCCe   '],
                    'col2':['   fgHAAij  ',' fghij ','lmnop   ']})
df3
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
      <th>col1</th>
      <th>col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>abcde</td>
      <td>fgHAAij</td>
    </tr>
    <tr>
      <th>1</th>
      <td>FFFFghij</td>
      <td>fghij</td>
    </tr>
    <tr>
      <th>2</th>
      <td>abCCe</td>
      <td>lmnop</td>
    </tr>
  </tbody>
</table>
</div>



```python
test1 = df3['col1'].str.strip()  # 앞 뒤 공백을 제거
test1.iloc[1]# 확인
```

<pre>
'FFFFghij'
</pre>

```python
test2 = df3['col1'].str.lstrip()  # 앞 공백을 제거
test2.iloc[1]# 확인
```

<pre>
'FFFFghij '
</pre>

```python
test3 = df3['col1'].str.rstrip()  # 뒤 공백을 제거
test3.iloc[1]# 확인
```

<pre>
' FFFFghij'
</pre>
# 대소문자 변경


## 소문자 변경 str.lower()



```python
df3['col1'].str.lower()
```

<pre>
0       abcde  
1     ffffghij 
2      abcce   
Name: col1, dtype: object
</pre>
## 대문자 변경 str.upper()



```python
df3['col1'].str.upper()
```

<pre>
0       ABCDE  
1     FFFFGHIJ 
2      ABCCE   
Name: col1, dtype: object
</pre>
## 소문자 to 대문자 / 대문자 to 소문자 한번에! swapcase()



```python
df3['col1'].str.swapcase()
```

<pre>
0       ABCDE  
1     ffffGHIJ 
2      ABccE   
Name: col1, dtype: object
</pre>
# Reference



- [꿀벌개발일지](https://ohgyun.com/768)

- [stackoverflow](https://stackoverflow.com/questions/41087619/pandas-merge-how-to-avoid-unnamed-column/41088706)

- [yg's blog](https://yganalyst.github.io/data_handling/memo_9/)

