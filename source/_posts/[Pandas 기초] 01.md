---
title: "[Pandas] 01. Series 데이터 생성하기(with index, value)"
cover: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1920&h=1080&fit=crop"
date: 2025-07-18
categories:
  - [personal-study, pandas]
tags:
  - series
  - indexing
  - pandas
  - 판다스
  - 시리즈
  - 데이터업데이트
  - 데이터접근
  - 인덱스재사용
toc: true
---
## 🚦Summary
- Pandas 기초 톺아보기 시리즈 첫번째 포스팅입니다.
- Pandas의 기본 객체중 하나인 Series를 다루는 방법을 소개합니다.



```python
import numpy as np
import pandas as pd
```

---


# Series

  - pandas의 기본 객체 중 하나

  - numpy의 ndarray를 기반으로 인덱싱을 기능을 추가하여 1차원 배열을 나타냄

  - index를 지정하지 않을 시, 기본적으로 ndarray와 같이 0-based 인덱스 생성, 지정할 경우 명시적으로 지정된 index를 사용

  - 같은 타입의 0개 이상의 데이터를 가질 수 있음

  - 실제 분석에서 생성하는 경우는 거의 없다.

  - DataFrame에서 파생되는 경우는 많음

## data로만 생성하기

 - index는 기본적으로 0부터 자동적으로 생성

```python
# int로 생성
s1 = pd.Series([1, 2, 3])
s1

# 좌측이 index, 우측이 value
```


0    1
1    2
2    3
dtype: int64


```python
# str형태로 생성
s2 = pd.Series(['a', 'b', 'c'])
s2
```


0    a
1    b
2    c
dtype: object


```python
# 0 ~ 199 값으로 ndarray로 생성
s3 = pd.Series(np.arange(200))
s3
```


0        0
1        1
2        2
3        3
4        4
      ... 
195    195
196    196
197    197
198    198
199    199
Length: 200, dtype: int32

## data, index함께 명시하기

```python
# 앞부분이 value, 뒷부분이 index
s4 = pd.Series([1, 2, 3], [100, 200, 300])
s4
```


100    1
200    2
300    3
dtype: int64


```python
s5 = pd.Series([1, 2, 3], ['a', 'm', 'k'])
s5
```


a    1
m    2
k    3
dtype: int64

## data, index, data type 함께 명시하기

```python
# data, index, data type 순서로 입력
s6 = pd.Series(np.arange(5), np.arange(100, 105), dtype=np.int16)
s6
```


100    0
101    1
102    2
103    3
104    4
dtype: int16

# 인덱스 활용하기

```python
# Series 에서 index값만 출력 가능
s6.index
```


Int64Index([100, 101, 102, 103, 104], dtype='int64')


```python
# Series에서 values만 출력 가능
s6.values
```


array([0, 1, 2, 3, 4], dtype=int16)

## 1. 인덱스를 통한 데이터 접근

```python
# s6이라는 Series 에서 104라는 인덱스의 value출력
s6[104]
```


4


```python
# 105라는 인덱스의 value출력
# 105라는 인덱스는 존재하지 않기 때문에 에러가 난다.
s6[105]
```

## 2. 인덱스를 통한 데이터 업데이트

```python
s6[104] = 70
s6
```


100     0
101     1
102     2
103     3
104    70
dtype: int16


```python
s6[105] = 90
s6[200] = 80
s6
```


100     0
101     1
102     2
103     3
104    70
105    90
200    80
dtype: int64

## 3. 인덱스 재사용하기

```python
# s6의 인덱스를 s7에 활용
s7 = pd.Series(np.arange(7), s6.index)
s7
```


100    0
101    1
102    2
103    3
104    4
105    5
200    6
dtype: int32
