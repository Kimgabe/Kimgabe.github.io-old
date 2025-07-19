---
title: "[파이썬 기초] 04. Numpy_ndarray 데이터 형태를 바꾸기(ravel, flatten, reshape)"
cover: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1920&h=1080&fit=crop"
date: 2021-07-14
categories:
  - [personal-study, numpy]
tags:
  - python
  - ndarray 형태바꾸기
  - np.ravel
  - np.flatten
  - np.reshape
  - array의 차원바꾸기
  - 이미지 벡터화
toc: true
---
ndarray의 형태와 차원을 바꾸는 방법을 정리합니다. 해당 개념은 차후 딥러닝 베이스의 이미지 분석에 필수적인 개념입니다.

```python
import numpy as np
```

데이터 형태 바꾸기

- 데이터의 차원, 각 차원의 값을 변경할 수 있다.

# ravel &  np.ravel

  - 다차원배열을 1차원으로 변경

  - 'order' 파라미터

    - 'C' - row 우선 변경 (default 값)

    - 'F - column 우선 변경

```python
array1 = np.arange(15).reshape(3, 5)
print(array1)

# order = 'C'로 '행'을 기준으로 배열이 생성되어있다.
```


[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

np 내장함수의 ravel

```python
# 열 기준으로 다차원 배열을 1차원으로 변경
np.ravel(array1, order='F')
```


array([ 0,  5, 10,  1,  6, 11,  2,  7, 12,  3,  8, 13,  4,  9, 14])

일반 함수의 ravel

```python
temp = array1.ravel()
print(temp)
```


[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

차이는 없다. 기능도 동일하다!

```python
print(temp)
print(array1)
```


[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

# flatten

 - 다차원 배열을 1차원으로 변경

 - **ravel과의 차이점: copy를 생성하여 변경함(즉 원본 데이터가 아닌 복사본을 반환)**

 - 'order' 파라미터

   - 'C' - row 우선 변경

   - 'F - column 우선 변경

## 2차원 array를 1차원으로 만들기

```python
array2 = np.arange(15).reshape(3, 5)
print(array2)
```


[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]


```python
temp2 = array2.flatten(order='F') # order='F' 컬럼 우선 변경
print(temp2) 

# 각 행의 1열, 2열, 3열 순으로 1차원 배열이 되었다.
```


[ 0  5 10  1  6 11  2  7 12  3  8 13  4  9 14]


```python
temp2[0] = 100
print(temp2)
```


[100   5  10   1   6  11   2   7  12   3   8  13   4   9  14]


```python
print(array2)
```


[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

flatten은 copy를 생성하여 변경하기 때문에 temp2의 특정값을 100으로 바꾸어도 기존 array2에는 영향이 없다.

## 3차원 array를 1차원으로 만들기

```python
array3 = np.arange(30).reshape(2, 3, 5)
print(array2)
```


[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]


```python
array2.ravel()
```


array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])


```python
array3.flatten()
```


array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

# reshape 함수

 - array의 shape을 다른 차원으로 변경하는 함수

 - 주의할점은 reshape한 후의 결과의 전체 원소 개수와 이전 개수가 같아야 가능

 - 사용 예) 이미지 데이터 벡터화 - 이미지는 기본적으로 2차원 혹은 3차원(RGB)이나 트레이닝을 위해 1차원으로 변경하여 사용 됨

```python
array1 = np.arange(36)
print("array1:\n",array1,"\n")
print("array1의 shape :",array1.shape,"\n")
print("array1의 차원:",array1.ndim,"\n")
```


array1:
 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35] 

array1의 shape : (36,) 

array1의 차원: 1 



```python
# flat한 배열을 6행 6열로 변경
y = array1.reshape(6, 6) # 6*6 = 36 으로 기존의 arange와 동일해야 한다.

print("y:\n",y,"\n")
print("y의 shape:",y.shape,"\n")
print("y의 차원:",y.ndim,"차원")
```


y:
 [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]] 

y의 shape: (6, 6) 

y의 차원: 2 차원

---


- 6행 6열을 -1로 써서 생성할 수도 있다.

- "36개의 수를 6행으로 만들고 싶다" -> 무조건 6행이 올 수 밖에 없다. -> -1을 써준다.

- 앞에서 정리한 것처럼 reshape를 할때는 요소의 수가 동일해야 한다. 이를 계산하기 복잡할때는 -1 기능을 활용하면 편리하다.

```python
y2 = array1.reshape(6,-1)
print("y2:\n",y2,"\n")
```


y2:
 [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]] 



```python
# 역으로도 가능
y3 = array1.reshape(-1,6)
print("y3:\n",y3,"\n")
```


y3:
 [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]] 



```python
# 행*열 이 원본의 원소수와 다르면 변형되지 않는다.
y4 = array1.reshape(6,5)
print("y4:\n",y4,"\n")
```

```python
k = array1.reshape(3, 3, 4)

print("y:\n",y,"\n")
print("y의 shape:",y.shape,"\n")
print("y의 차원:",y.ndim,"차원")
```


y:
 [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]] 

y의 shape: (6, 6) 

y의 차원: 2 차원


```python
k2 = array1.reshape(3, 3, -1)

print("k2:\n",k2,"\n")
print("k2의 shape:",k2.shape,"\n")
print("k2의 차원:",k2.ndim,"차원")
```


k2:
 [[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]

 [[24 25 26 27]
  [28 29 30 31]
  [32 33 34 35]]] 

k2의 shape: (3, 3, 4) 

k2의 차원: 3 차원

동일한 방식으로 3개의 요소중 2개가 정해지면 나머지 한개는 -1을 통해 python이 자동으로 계산하도록 할 수 있다.

