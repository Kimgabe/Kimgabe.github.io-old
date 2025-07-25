---
title: "[Pandas] 02. Series 데이터 심플 분석(개수, 빈도 등 계산하기)"
cover: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1920&h=1080&fit=crop"
date: 2025-07-18
categories:
  - [personal-study, pandas]
tags:
  - 전처리
  - 시리즈
  - series
  - pandas
  - 판다스
  - size
  - shape
  - len
  - count
  - value_counts
  - mean
  - max
  - min
  - sum
  - median
  - abs
  - cumsum
  - cumprod
  - std
  - var
  - mode
  - corr
  - astype
  - 데이터형변환
  - 산술연산
  - 인덱싱
  - indexing
  - head
  - tail
  - 기초
toc: true
---
## 🚦 Summary
- Pandas 기초 톺아보기 시리즈 두번째 포스팅입니다. 
- Series 데이터의 크기, 모양, unique값, 값의 개수, 값들의 빈도를 확인하는 방법을 정리합니다.
- 그외에 다양한 산술연산방법과 indexing을 통합 Series 요소의 접근방법과 head, tail함수 사용법을 정리합니다.

## 📌 Intro.

- Series에서 사용할 수 있는 다양한 함수에 대해 정리합니다.

- 이 방법들을 알면 Series에 담겨 있는 데이터에 대해 다양한 정보들을 파악할 수 있습니다.

### Series에서 사용할 수 있는 다양한 함수 정리

 - size : Series의 개수 return

 - shape : Series의 shape를 튜플형태로 return

 - unique: Series에서 유일한 값(중복 제거)이 무엇이 있는지 ndarray로 return

 - count : Series에서 NaN을 제외한 값의 개수를 return

 - mean: Series에서 NaN을 제외한 값들의 평균을 return(int, float등 숫자형 데이터에만 적용)

 - value_counts: Series에서 NaN을 제외하고 각 값들의 빈도를 return (숫자형, 문자형 상관없이 모두 적용)

 ---


- 각 기능을 예제코드와 함께 어떻게 작동하는 지를 살펴보겠습니다.

```python

# 필요 라이브러리 불러오기

import numpy as np

import pandas as pd

```

```python

# 마지막 값을 Null로 생성합니다.

# Nan : Not  a Number 을 의미합니다.

# 실제 데이터 분석에도 NaN값이 있는 경우가 많기 때문에 NaN값이 있는 데이터를 어떻게 파악하고 처리하는지 확인하기 위함입니다.

s = pd.Series([1, 1, 2, 1, 2, 2, 2, 1, 1, 3, 3, 4, 5, 5, 7, np.NaN]) # 데이터 생성

s # 결과 확인

```



0     1.0

1     1.0

2     2.0

3     1.0

4     2.0

5     2.0

6     2.0

7     1.0

8     1.0

9     3.0

10    3.0

11    4.0

12    5.0

13    5.0

14    7.0

15    NaN

dtype: float64



## len : Series 의 길이

- 파이썬 프로그래밍 기초에서 배운 내용이 Series에서도 그대로 적용됩니다.

- Series가 담고 있는 요소의 총 개수를 return하는 기능입니다.

- 유의할점은 **NaN(결측치)도 하나의 요소로 취급**하여 출력값에 포함한다는 점입니다.

```python

print(list(s)) # 전체 Series 확인

len(s)

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





16



- Seires에 nan값이 있음에도 이를 카운트해서 16개로 보여주는 것을 알 수 있습니다.

```python

s2 = s.copy() # 차이를 보여주기 위한 샘플

s2.dropna(inplace = True) # nan값을 삭제하는 메서드

len(s2) # 결과출력

```



15



- 기존 Series에서 nan값을 제외한 뒤에는 len()의 결과가 15개로 출력되는 것을 확인할 수 있습니다.

## Series의 크기

- size는 Series내 전체 요소의 개수를 return합니다.

- len()과 비슷하지만 size는 Series 객체의 자체 기능이며 함수가 아니라는 차이점이 있습니다.

- size 또한 len()과 마찬가지로 NaN값을 카운트 합니다.

```python

print(list(s)) # 전체 Series

s.size # 요소 개수 확인

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





16



```python

print(list(s2)) # NaN을 제거한 Series

s2.size # 요소개수 확인

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0]





15



- len() 과 마찬가지로 NaN을 제거한 Series에 대해서는 15개의 값이 있다고 출력하는 것을 확인할 수 있습니다.

## Series의 형태

- shape는 Series 객체에 저장된 총 요소의 개수를 return합니다.

- Series는 1차원 데이터구조이기 때문에, return되는 튜플에는 요소의 개수만 포함되어 있습니다.

```python

print(list(s)) # 전체 Series

s.shape # 형태 출력

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





(16,)



## Series의 unique한 값

- unque는 Series에서 중복된 값을 제거하고 유일한 값들만을 array 형태로 return합니다.

- 여기서의 특이사항은 NaN값도 유일한 값으로 간주되어 결과값에 포함될 수 있다는 것입니다.

```python

print(list(s)) # 전체 Series

s.unique()

```



array([ 1.,  2.,  3.,  4.,  5.,  7., nan])



## Series의 value의 수 (=count)

- Series에서 count는 NaN값을 제외한 Series 내 요소의 개수를 return합니다.

- len()이나 size()와의 차이점 입니다.

```python

print(list(s)) # 전체 Series

s.count() # NaN값 제외한 Series내 요소의 개수 확인

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





15



## Series의 value_counts

- value_counts 함수는 Series 내 각 값이 출현하는 빈도수를 계산합니다.

- 기본적으로 NaN은 빈도 계산에서 제외 되지만, `dropna = False` 옵션을 함께 사용하면 NaN빈도도 포함시킬 수 있습니다.

- 결과는 빈도수를 기준으로 내림차순으로 정렬됩니다.

    - 정렬을 바꾸고 싶다면 `ascending=True` 를 설정해 오름차순으로 변경할 수 있습니다.

```python

s.value_counts()

```



1.0    5

2.0    4

3.0    2

5.0    2

4.0    1

7.0    1

dtype: int64



## Series의 산술연산

- Pandas의 Series는 다양한 산술연산을 지원합니다.

- 이 연산들은 대부분 NaN(결측치)를 연산에서 자동으로 제외 합니다.

- 이러한 기능은 데이터 분석에서 누락된 데이터를 고려한 정확한 계산을 할 수 있도록 돕는 편리한 기능입니다.

- 하지만 이 연산이 가능하다는 점 때문에 종종 데이터에 결측치가 있다는 것을 잊고 데이터 분석을 하는 경우가 생깁니다.

- 그러므로 항상 **Pandas의 연산은 NaN을 자동으로 제외하고 연산한다** 는 것을 알고 있어야 합니다.

---


- **array는 NaN값이 있을 경우 연산이 되지 않습니다.**

```python

a = np.array([2, 2, 2, 2, np.NaN])

a.mean()

```



nan



- 반면에 **Series는 NaN이 있을 경우 NaN을 제외한 나머지 값으로 연산을 합니다.**

```python

print(list(s)) # 전체 Series

print(s.mean()) # NaN이 있는 Series의 mean 연산

s2.mean() # NaN값이 없는 Series에서의 mean 연산

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]

2.6666666666666665





2.6666666666666665



---


- 위의 mean을 포함해 Pandas의 Seires에서 사용할 수 있는 산술연산의 종류는 아래와 같습니다.    

### 평균(mean)

- mean 함수는 Series 내의 평균값을 계산합니다.

- NaN 값은 평균 계산에서 제외됩니다.

- 사용법은 위에서 사용한 예제와 같습니다.

### 최소값 (min)

- min 함수는 Series 내의 최소값을 찾습니다.

- 여기서도 NaN 값은 계산에 포함되지 않습니다.

```python

print(list(s)) # 전체 Series

s.min() # Series의 최소값 찾기

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





1.0



### 최대값 (max)

- max 함수는 Series 내의 최대값을 계산합니다.

- NaN 값은 최대값 계산에서 제외됩니다.

```python

print(list(s)) # 전체 Series

max(s) # Series의 최대값 찾기

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





7.0



### 합계 (sum)

- sum 함수는 Series의 값들의 합을 return합니다.

- NaN 값은 합계 계산에서 제외됩니다.

- 문자열로 된 Series의 경우 모든 문자열이 연결(concatenation) 됩니다.

```python

print(list(s)) # 전체 Series

s.sum() # Series 요소의 모든 합을 구합니다.

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





40.0



```python

s3 = pd.Series(['a', 'b', 'c', 'd']) # 문자열 Series 만들기

s3.sum() # 문자열 연결

```



'abcd'



### 중앙값 (median)

- median 함수는 Series의 중앙값을 계산합니다.

- 이 계산에서도 NaN 값은 제외됩니다.

```python

print(list(s)) # 전체 Series

s.median() # Series 요소의 중앙값 계산

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





2.0



### 절대값 (abs)

- abs 함수는 Series의 모든 요소의 절대값을 계산합니다.

- 각 요소의 절대값이 개별적으로 return됩니다.

- 개별 요소의 절대값을 보려면 abs() 안에 Series의 개별 요소의 인덱싱(indexing)한 값을 넣어줘야 합니다.

    - 인덱싱(indexing)한 값에 abs()를 적용하는 것(ex : `s[1].abs()` 는 에러가 발생합니다. 아래에 예시를 제공하겠습니다.)

```python

print(list(s)) # 전체 Series

s.abs() # Series 모든 요소의 절대값 계산

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





0     1.0

1     1.0

2     2.0

3     1.0

4     2.0

5     2.0

6     2.0

7     1.0

8     1.0

9     3.0

10    3.0

11    4.0

12    5.0

13    5.0

14    7.0

15    NaN

dtype: float64



```python

abs(s[1]) # 1번째 요소인 1.0의 절대값 구하기

```



1.0



- `s[1].abs()` 는 에러가 발생합니다.

- Series에서 인덱싱(indexing)을 통해 return된 개별 요소는 더이상 Series 객체가 아니라 파이썬의 기본 데이터 타입 또는 Numpy 데이터 타입이기 때문입니다.

```python

s[1].abs()

```

### 누적합 (cumsum)

- cumsum 함수는 Series의 누적합을 계산합니다.

- NaN 값은 누적합에서 제외되며, 이전 값의 합에 영향을 주지 않습니다.

- Series내 요소의 모든 값의 합에 대한 결과값만을 return하는 sum과 달리 cumsum은 Series내의 각 요소별 합의 결과를 순차적으로 보여줍니다.

    - 이렇게 출력되는 결과는 새로운 Series 형태의 데이터 입니다.

```python

print(list(s)) # 전체 Series

s.cumsum() # Series의 누적합 계산

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





0      1.0

1      2.0

2      4.0

3      5.0

4      7.0

5      9.0

6     11.0

7     12.0

8     13.0

9     16.0

10    19.0

11    23.0

12    28.0

13    33.0

14    40.0

15     NaN

dtype: float64



### 누적곱 (cumprod)

- cumprod 함수는 Series의 누적곱을 계산합니다.

- 특이사항으로 NaN 값은 누적곱에서 1로 간주됩니다.

- 하지만 이는 말그대로 연산이 이뤄지도록 하기 위한 것으로 실제 결과에 영향을 미치지는 않습니다.

- comsum과 마찬가지로 각 요소별 곱의 결과를 순차적으로 return하며, 이 결과는 별도의 Series 형태의 데이터 입니다.

```python

print(list(s)) # 전체 Series

s.cumprod()

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





0          1.0

1          1.0

2          2.0

3          2.0

4          4.0

5          8.0

6         16.0

7         16.0

8         16.0

9         48.0

10       144.0

11       576.0

12      2880.0

13     14400.0

14    100800.0

15         NaN

dtype: float64



### 표준편차 (std)

- std 함수는 Series의 표준편차를 계산합니다.

- NaN 값은 표준편차 계산에서 제외됩니다.

```python

print(list(s)) # 전체 Series

s.std() # Series 전체 요소의 표준편차 계산

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





1.8387366263150309



### 분산 (var)

- var 함수는 Series의 분산을 계산합니다.

- NaN 값은 분산 계산에서 제외됩니다.

```python

print(list(s)) # 전체 Series

s.var() # Series 전체 요소의 분산 계산

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





3.380952380952382



### 최소공배수 (mode)

- mode 함수는 Series 내에서 가장 자주 등장하는 값을 찾습니다.

- NaN 값은 모드 계산에 포함되지 않습니다.

```python

print(list(s)) # 전체 Series

s.mode() # Series 전체의 최소공배수 찾기

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





0    1.0

dtype: float64



### 상관계수 (corr)

- corr 함수는 두 Series 간의 상관계수를 계산합니다.

- 이 함수는 두 Series 사이의 선형 관계의 강도를 측정합니다.

```python

print(list(s)) # 전체 Series

print(list(s2)) # 전체 Series

s.corr(s2) # s와 s2의 상관관계

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]

[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0]





1.0



- NaN을 제외하고는 모든 요소의 값이 같기 때문에 상관관계가 당연히 1이 될 수 밖에 없습니다.

- 값이 다른 샘플데이터를 만들어서 다시 시도해 보겠습니다.

```python

# 길이가 15인 랜덤한 값으로 구성된 Series 생성

length = 15

random_series = pd.Series(np.random.random(length))

random_series

print(list(s)) # 전체 Series

print(list(random_series)) # 전체 Series

s.corr(random_series) # s와 s2의 상관관계

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]

[0.8015840785303865, 0.005453483300369322, 0.5745111223172886, 0.4918370215535973, 0.1478151507689779, 0.5190110106184694, 0.10120792797267708, 0.38001592607542733, 0.12882417243336652, 0.5180457975464019, 0.5782982515527354, 0.15407029291725383, 0.24316476267899223, 0.10233089871557155, 0.8917142775321586]





0.1891842434201723



### 자료형 변환 (astype)

- astype 함수는 Series의 데이터 타입을 다른 타입으로 변환합니다.

```python

print(list(s)) # 전체 Series

str_s = s.astype(str) # 숫자값들을 문자열 데이터로 변경

print(s.sum()) # 숫자일때의 sum

print(str_s.sum()) # 같은 모양을 문자로 변환한 Series의 sum

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]

40.0

1.01.02.01.02.02.02.01.01.03.03.04.05.05.07.0nan



## index를 활용하여 멀티플한 값에 접근하기

- Pandas Series는 index를 활용해 데이터에 접근할 수 있습니다.

- 이 기능을 잘 활용하면 데이터 전처리, 분석 과정에서 데이터를 효율적으로 추출할 수 있습니다.

### 단일 값에 접근하기

- index를 사용해 Series의 특정 요소에 접근할 수 있습니다.

- 예를 들어, `s[5]` 는 Series s의 여섯번째 요소(index 5)에 접근합니다.

- 이 방식으로 특정 데이터 포인트를 확인하거나 처리할 수 있습니다.

```python

# index로 단일값에 접근하는 경우

s[5]

```



2.0



- 다만 이렇게 추출된 데이터는 Series 형태의 데이터가 아니라는 점을 알고 있어야 추가적인 데이터 처리를 할 수 있습니다.

- 단일 값에 접근했을때 추출되는 데이터는 'Pandas Series 원소' 타입 데이터 입니다.

- 이 Pandas Series 원소 타입의 경우 세부 데이터 타입은 실제 Series의 원소를 따릅니다.

    - `s[5]` 에 있는 원소의 데이터 타입이 정수형이라면, return되는 값도 정수형입니다.

- 주의할 점은, 이렇게 return된 데이터는 Series의 메소드를 적용할 수 없다는 것 입니다.

### 여러값에 동시에 접근하기

- index의 배열을 사용하면 Series의 여러 요소에 동시에 접근할 수 있습니다.

- 예를들어 `s[[5, 7, 8, 10]]` 을 사용하면 s Series에서 5,7,8,10번째 index에 해당하는 값들에 접근할 수 있습니다.

- 이 방법을 통해 여러 데이터 포인트를 동시에 분석하거나 비교할 수 있습니다.

- 이렇게 접근한 데이터들의 sort_values() 함수를 적용해 값을 도출해 보겠습니다.

```python

# 5, 7, 8, 10 번째 index의 값에 대한 value_counts

s[[5, 7, 8, 10]].value_counts()

```



1.0    2

2.0    1

3.0    1

Name: count, dtype: int64



- 기존에 s 라는 Series에 적용했던 value_counts()와 비교해서 보자면 아래와 같습니다.

```python

# 두 value_counts 결과 계산

value_counts_all = s.value_counts().sort_index()

value_counts_selected = s[[5, 7, 8, 10]].value_counts().sort_index()

# 두 결과를 하나의 DataFrame으로 합치기

df = pd.DataFrame({

    'All Values': value_counts_all,

    'Selected Values': value_counts_selected

})

# NaN 값을 공백으로 처리

df = df.fillna('')

df

```





## Series의 head와 tail

- Pandas에서 제공하는 head와 tail 함수는 데이터의 상위 또는 하위 일부를 빠르게 살펴보는데 유용합니다.

- 이 함수들은 데이터 탐색이나 전처리 과정에서 굉장히 자주 사용되는 함수입니다.

### head 함수

- head함수는 Series나 DataFrame의 상위 n개 요소를 return합니다.

- 기본적으로 상위 5개의 요소를 return하며, 괄호안에 특정 수를 지정하여 원하는 개수만큼 출력할 수도 있습니다.

    - 공식문서에는 괄호안에 n = 숫자 형태로 입력하게 되어 있지만 숫자만 입력해도 동일하게 작동합니다.

```python

print(list(s)) # 전체 Series

s.corr(s2) # s와 s2의 상관관계

s.head(n=7) # Series의 상위 7개 요소 return

```



[1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 5.0, 5.0, 7.0, nan]





0    1.0

1    1.0

2    2.0

3    1.0

4    2.0

5    2.0

6    2.0

dtype: float64



```python

s.head(7) # n = 을 쓰지 않아도 동일하게 작동합니다.

```



0    1.0

1    1.0

2    2.0

3    1.0

4    2.0

5    2.0

6    2.0

dtype: float64



```python

s.head() # Series의 상위 5개 요소 return(기본값)

```



0    1.0

1    1.0

2    2.0

3    1.0

4    2.0

dtype: float64



### tail 함수

- tail함수는 Series나 DataFrame의 하위 n개의 요소를 return합니다.

- 이 함수 역시 기본적으로 하위 5개 요소를 return합니다.

- 또한, 괄호안에 숫자를 입력해 원하는 개수만큼 return하도록 할 수도 있습니다.

```python

s.tail()

```



11    4.0

12    5.0

13    5.0

14    7.0

15    NaN

dtype: float64

