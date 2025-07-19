---
title: "[파이썬 기초] 03. Numpy_ndarray 인덱싱 & 슬라이싱"
cover: "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=1920&h=1080&fit=crop"
date: 2021-07-14
categories:
  - [personal-study, numpy]
tags:
  - python
  - indexing
  - 1차원 벡터 인덱싱
  - index로 특정 위치 값 바꾸기
  - index의 값 바꾸기
  - 2차원 행렬 인덱싱
  - 3차원 텐서 인덱싱
  - 벡터
  - 행렬
  - 텐서
  - 슬라이싱
  - 1차원 벡터 슬리이싱
  - 2차원 행렬 슬라이싱
  - 3차원 텐서 슬라이싱
toc: true
---
array형태의 데이터를 다양한 차원별로 인덱싱하고 슬라이싱하는 방법을 정리합니다.

```python
import numpy as np
```

# 인덱싱

 - 파이썬 리스트와 동일한 개념으로 사용

 - ,를 사용하여 각 차원의 인덱스에 접근 가능

## 1차원 벡터 인덱싱

```python
# 1에서 부터 9 까지의 1차원 ndarray 생성 
array1 = np.arange(start=1, stop=10)
print("array1:",array1)
```


array1: [1 2 3 4 5 6 7 8 9]


```python
# index는 0 부터 시작하므로 array1[2]는 3번째 index 위치의 데이터 값을 의미
value = array1[2]
print('value:',value)
print(type(value))
```


value: 3



```python
print("맨 앞의 값:", array1[0]) # 양수 인덱스 (맨 앞 요소)
```


맨 앞의 값: 1


```python
print('앞에서 세번째 값:',array1[3])
```


앞에서 세번째 값: 4


```python
print('맨 뒤의 값:',array1[-1], ', 맨 뒤에서 두번째 값:',array1[-2])
```


맨 뒤의 값: 9 , 맨 뒤에서 두번째 값: 8

### index로 특정 위치값 출력하기

```python
array1[0]
```


1


```python
array1[-1]
```


9

### index의 값 바꾸기

```python
array1[3] = 100
print(array1)
```


[  1   2   3 100   5   6   7   8   9]

## 2차원 행렬 인덱싱

- 인덱싱을 하면 결과물은 차원수가 줄어들거나 변형되어 출력된다.

```python
array2 = np.arange(15).reshape(3, 5) #5행 2열로 reshape
print(array2)
```


[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]


```python
# x의 0번째 행
print("array2[0]:", array2[0]) # 양수 인덱스 (맨 앞 요소)

# 기존은 2차원 행렬이지만 1차원으로 변경되어 출력
```


array2[0]: [0 1 2 3 4]


```python
# x의 1번째 행, -1번째(마지막) 열
print("(row=1,col=-1) index 가리키는 값:", array2[1,-1])
```


(row=1,col=-1) index 가리키는 값: 9


```python
print('(row=0,col=1) index 가리키는 값:', array2[0,1] )
```


(row=0,col=1) index 가리키는 값: 1


```python
print('(row=1,col=0) index 가리키는 값:', array2[1,0] )
```


(row=1,col=0) index 가리키는 값: 5


```python
print('(row=2,col=2) index 가리키는 값:', array2[2,2] )
```


(row=2,col=2) index 가리키는 값: 12

## 3차원 텐서 인덱싱

```python
# 4행 3열 array를 3차원(3개)으로 생성
array3 = np.arange(36).reshape(3, 4, 3)
print(array3)
```


[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]]

 [[12 13 14]
  [15 16 17]
  [18 19 20]
  [21 22 23]]

 [[24 25 26]
  [27 28 29]
  [30 31 32]
  [33 34 35]]]


```python
# 0번째 index위치의 4행 3열의 array를 출력
print("array3[0]:\n",array3[0])
```


array3[0]:
 [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]


```python
# 1번째 index위치의 4행 3열의 array를 출력
print("array3[1]:\n",array3[1])
```


array3[1]:
 [[12 13 14]
 [15 16 17]
 [18 19 20]
 [21 22 23]]


```python
# 4행 3열의 array에서 0번째 array에서 1번째 행에 있는 값 출력
print('(array=1, rows=2) index 가리키는 값:', array3[0,1] )
```


(array=1, rows=2) index 가리키는 값: [3 4 5]


```python
# 4행 3열의 array에서 1번째 array에서 2번째 행에 있는 값 출력
print('(array=1,rows=2) index 가리키는 값:', array3[1,2] )
```


(array=1,rows=2) index 가리키는 값: [18 19 20]


```python
#4행 3열의 1번째 array에서 2번째 행에서 1번째 값을 출력
print('(array=1, row=2, col=1의 ) index 가리키는 값:', array3[1,2,1] )
```


(array=1, row=2, col=1의 ) index 가리키는 값: 19

# 슬라이싱

 - 리스트, 문자열 slicing과 동일한 개념으로 사용

 - ,를 사용하여 각 차원 별로 슬라이싱 가능

 - indexing과 달리 slicing을 해도 차원이 바뀌지는 않는다.

## 1차원 벡터 슬라이싱

```python
array1 = np.arange(10)
print(array1)
```


[0 1 2 3 4 5 6 7 8 9]


```python
print("array1[1:]:",array1[1:])
```


array1[1:]: [1 2 3 4 5 6 7 8 9]

## 2차원 행렬 슬라이싱

```python
array2 = np.arange(10).reshape(2, 5)
print(array2)
```


[[0 1 2 3 4]
 [5 6 7 8 9]]


```python
print("array2[0, :2]:",array2[0, :2])
```


array2[0, :2]: [0 1]


```python
print("array2[:1, :2]:",array2[:1, :2])
```


array2[:1, :2]: [[0 1]]


```python
print("array2[:, :2]:\n",array2[:, :2])
```


array2[:, :2]:
 [[0 1]
 [5 6]]

출력값은 동일한 2차원으로 indexing처럼 차원값이 변하지는 않는다.

```python
# indexing을 하게 되면 당연히 차원값도 변경이 될 수 있다.
print("array2[0, :2]:",array2[0, :2])
```


array2[0, :2]: [0 1]


```python
# indexing이 없이 출력한다면 차원값은 변하지 않으면서 동일한 값을 출력할 수 있다.
print("array2[:1, :2]:",array2[:1, :2])
```


array2[:1, :2]: [[0 1]]

## 3차원 텐서 슬라이싱

```python
array3 = np.arange(54).reshape(2, 9, 3)
print(array3)
```


[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]
  [12 13 14]
  [15 16 17]
  [18 19 20]
  [21 22 23]
  [24 25 26]]

 [[27 28 29]
  [30 31 32]
  [33 34 35]
  [36 37 38]
  [39 40 41]
  [42 43 44]
  [45 46 47]
  [48 49 50]
  [51 52 53]]]


```python
print("array3[:1, :2, :]:\n",array3[:1, :2, :])
```


array3[:1, :2, :]:
 [[[0 1 2]
  [3 4 5]]]


```python
print("array3[:1, :2, :]:\n",array3[:1, :2, :])
```


array3[:1, :2, :]:
 [[[0 1 2]
  [3 4 5]]]

## Boolean indexing

```python
array1 = np.arange(start=1, stop=10)
print(array1)
```


[1 2 3 4 5 6 7 8 9]


```python
# array1의 값에서 5이상 T/F  출력
var1 = array1 > 5
print("var1:",var1)
print(type(var1))
```


var1: [False False False False False  True  True  True  True]



```python
# [ ] 안에 array1 > 5 Boolean indexing을 적용 
print(array1,"\n")
array3 = array1[array1 > 5]
print('array1 > 5 불린 인덱싱 결과 값 :', array3)
```


[1 2 3 4 5 6 7 8 9] 

array1 > 5 불린 인덱싱 결과 값 : [6 7 8 9]


```python
# ndarray형태로 T/F 생성
boolean_indexes = np.array([False, False, False, False, False,  True,  True,  True,  True])

# 생성된 T/F 기준과 array1 비교하여 필터링 -> True인 값만 []에 담긴다.
array3 = array1[boolean_indexes]
print('불린 인덱스로 필터링 결과 :', array3)
```


불린 인덱스로 필터링 결과 : [6 7 8 9]


```python
indexes = np.array([5,6,7,8])
array4 = array1[ indexes ]
print('일반 인덱스로 필터링 결과 :',array4)
```


일반 인덱스로 필터링 결과 : [6 7 8 9]


```python
# 응용
# for 문으로 T/F 추출하기
array1d = np.arange(start=1, stop=10)
target = []

for i in range(0, 9):
    if array1d[i] > 5:
        target.append(array1d[i])

array_selected = np.array(target)
print(array_selected)
```


[6 7 8 9]


```python
print(array1d[array1 > 5])
```


[6 7 8 9]
