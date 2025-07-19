---
title: "[파이썬 기초] 08. Numpy_Boolean indexing으로 조건에 맞는 데이터 선택하기"
cover: "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=1920&h=1080&fit=crop"
date: 2021-07-14
categories:
  - [personal-study, numpy]
tags:
  - python
  - boolean indexing
  - 다중조건
toc: true
---
ndarray를 bool list를 통해 인덱싱하는 방법에 대해 정리합니다.

# Boolean indexing

  - ndarray 인덱싱 시, bool 리스트를 전달하여 True인 경우만 필터링하는 것

  - ndarray 에서 굉장히 자주 사용되는 기능

* 브로드캐스팅을 활용하여 ndarray로 부터 bool list 얻기

 - e.g) 짝수인 경우만 찾아보기

```python
import numpy as np
```

```python
# 1과 100사이 10개의 간격씩으로 해서 int값들로 무작위 생성
x = np.random.randint(1, 100, size=10)
print("x:",x)
```


x: [25 95 44  3 23 41 81 58 33 18]


```python
# 2는 scalar(상수) 이기 때문에 브로드 캐스팅이 가능하다.
x % 2 == 0
```


array([False, False,  True, False, False, False, False,  True, False,
        True])

- 필터 조건을 설정하여 변수 선언

- 통상적으로 어떤 필터값을 만들어 적용할때 mask를 씌운다 라고 한다.

- 그래서 boolean의 변수를 만들면 주로 mask를 많이 붙인다. 

## bool list로 boolean indexing 적용하기

```python
# even number : 짝수
# array에서 even number만을 필터링 해주는 mask생성
even_mask = x % 2 == 0
print(even_mask)
```


[False False  True False False False False  True False  True]


```python
# even_mask에서 True인 경우의 값들만 필터링이 되었다.
print("x:",x,"\n")
print("The even number among the array x is :", x[even_mask])
```


x: [25 95 44  3 23 41 81 58 33 18] 

The even number among the array x is : [44 58 18]

numpy의 boolean indexing을 사용하면 기존의 loop을 사용하는 방식을 하지 않고도 값을 필터링 할 수 있다.

```python
a = x.tolist()
even_number=[]

for i in a:
    if i % 2 == 0:
        even_number.append(i)

print("The even number among the array x is :",even_number)
```


The even number among the array x is : [44, 58, 18]

## 한번에 boolean indexing 적용하기

```python
x[x % 2 == 0]
```


array([44, 58, 18])


```python
# 30보다 큰 x값만 추려내기
x[x > 30]
```


array([95, 44, 41, 81, 58, 33])

#  다중조건 사용하기

 - 파이썬 논리 연산지인 and, or, not 키워드 사용 불가

 - & - AND 

 - | - OR 

## AND 조건

```python
# 조건 1 : 짝수
x % 2 == 0
```


array([False, False,  True, False, False, False, False,  True, False,
        True])


```python
# 조건 2 : 30 이상인 수
x 
array([ True, False, False,  True,  True, False, False, False, False,
        True])


```python
# AND 조건 적용 : 짝수이면서 30이상인 수만 출력하기
x[(x % 2 == 0) & (x 
array([18])

## OR 조건

```python
# 조건 1 : 30보다 작은 값
x 
array([ True, False, False,  True,  True, False, False, False, False,
        True])


```python
# 조건 2 : 50보다 큰 값
x > 50
```


array([False,  True, False, False, False, False,  True,  True, False,
       False])


```python
# OR 조건 적용 :  30보다 작거나, 50보다 큰 값들만 출력
x[(x  50)]
```


array([25, 95,  3, 23, 81, 58, 18])

# 예제) 2019년 7월 서울 평균기온 데이터

 - 평균기온이 25도를 넘는 날수는?

 - 평균기온이 25를 넘는 날의 평균 기온은?

```python
temp = np.array(
        [23.9, 24.4, 24.1, 25.4, 27.6, 29.7,
         26.7, 25.1, 25.0, 22.7, 21.9, 23.6, 
         24.9, 25.9, 23.8, 24.7, 25.6, 26.9, 
         28.6, 28.0, 25.1, 26.7, 28.1, 26.5, 
         26.3, 25.9, 28.4, 26.1, 27.5, 28.1, 25.8])
```

```python
len(temp)
```


31

## 평균기온이 25도를 넘는 날수?

```python
# len(temp[temp > 25.0])

print("평균기온이 25도를 넘는 날의 수는",len(temp[temp > 25.0]),"입니다.")
```


평균기온이 25도를 넘는 날의 수는 21 입니다.


```python
# True는 기본적으로 정수연산에서 1임을 활용
# temp가 25이상이면 True -> 인 값들만 sum
print("평균기온이 25도를 넘는 날의 수는",np.sum(temp > 25.0),"입니다.")
```


평균기온이 25도를 넘는 날의 수는 21 입니다.

## 평균기온이 25를 넘는 날의 평균 기온은?

```python
# np.mean(temp[temp > 25.0])
print("평균기온이 25도를 넘는 날의 평균 기온은",np.mean(temp[temp > 25.0]),"도 입니다.")
```


평균기온이 25도를 넘는 날의 평균 기온은 26.857142857142858 도 입니다.
