---
title: "[파이썬 기초] 09. Numpy_선형대수 연산하기(linalg 서브모듈 )"
cover: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1920&h=1080&fit=crop"
date: 2021-07-14
categories:
  - [personal-study, numpy]
tags:
  - python
  - ndarray
  - 선형대수
  - linalg
  - np.linalg
  - 행렬내적구하기
  - 전치행렬구하기
  - 역행렬
  - 정방행렬
  - 항등행렬
toc: true
---
numpy의 선형대수 연산을 위한 linalg 서브모듈의 활용방법에 대해 정리합니다.

```python
import numpy as np

# numpy float 출력 옵션 변경
np.set_printoptions(formatter={'float_kind': lambda x: "{0:0.5f}".format(x)})
```

# np.linalg.inv

 - 역행렬을 구할 때 사용

 - 모든 차원의 값이 같아야 함 (정방행렬 : 정사각형)

 - 역행렬 : 원래의 행렬과 특정 행렬(a)를 곱했을때 항등 행렬이 나오면 원래 행렬의 역행렬이라 한다.

     - 항등 행렬 : 주대각선이 모두1 나머지가 0인 행렬     

```python
x = np.random.rand(3, 3)
print(x)
```


[[0.53986 0.79960 0.74414]
 [0.00917 0.45658 0.65357]
 [0.91142 0.43624 0.05484]]


```python
# 행렬의 곱을 구하는 방법 1 ('@'을 사용)
x @ np.linalg.inv(x)
```


array([[1.00000, 0.00000, -0.00000],
       [-0.00000, 1.00000, -0.00000],
       [0.00000, -0.00000, 1.00000]])


```python
# 행렬의 곱을 구하는 방법2
np.matmul(x, np.linalg.inv(x))
```


array([[1.00000, 0.00000, -0.00000],
       [-0.00000, 1.00000, -0.00000],
       [0.00000, -0.00000, 1.00000]])


```python
y = np.random.rand(3, 4)
print(y)
```


[[0.91117 0.41043 0.72529 0.43821]
 [0.07191 0.83217 0.08042 0.61041]
 [0.13546 0.30789 0.91989 0.23166]]


```python
# 역행렬 연산
y @ np.linalg.inv(y)
```

- Last 2 dimensions of the array must be square : 즉 차원값이 정방행렬이 아니어서 역행렬 연산이 되지 않는다.

```python
z = np.random.rand(3, 3, 3)
print(z)
```


[[[0.20120 0.02166 0.17710]
  [0.44432 0.87087 0.70554]
  [0.90233 0.26423 0.43722]]

 [[0.84251 0.80231 0.01184]
  [0.20520 0.44978 0.81096]
  [0.09792 0.33678 0.38137]]

 [[0.76238 0.11469 0.96316]
  [0.11062 0.01190 0.28967]
  [0.73781 0.72039 0.58027]]]

차원이 늘어나도 같은 형태라면 역행렬 연산이 가능하다.

```python
# 역행렬 연산
z @ np.linalg.inv(z)
```


array([[[1.00000, 0.00000, -0.00000],
        [0.00000, 1.00000, -0.00000],
        [0.00000, 0.00000, 1.00000]],

       [[1.00000, 0.00000, -0.00000],
        [0.00000, 1.00000, -0.00000],
        [0.00000, -0.00000, 1.00000]],

       [[1.00000, 0.00000, 0.00000],
        [0.00000, 1.00000, 0.00000],
        [0.00000, 0.00000, 1.00000]]])

# np.linalg.solve

 - Ax = B 형태의 선형대수식 솔루션을 제공

 - 예제) 호랑이와 홍학의 합 : 25 호랑이 다리와 홍학 다리의 합은 64

   - x + y = 25 (홍학의 수 + 호랑이의 수)

   - 2x + 4y = 64 (홍학의 다리수 + 호랑이의 다리수 )

 $$\begin{pmatrix} 1 & 1 \\ 2 & 4 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}= \begin{pmatrix} 25 \\ 64 \end{pmatrix}$$

```python
A = np.array([[1, 1], [2, 4]])
B = np.array([25, 64])

x = np.linalg.solve(A, B)
print(x)
```


[18.00000 7.00000]


```python
# 실제 정답 확인
np.allclose(A@x, B)
```


True

# 행렬 내적 구하기

행렬 내적은 행렬의 곱을 의미하며, 두 행렬 A와 B의 내적은 np.dot() 함수를 통해 계산할 수 있다.

![product.png](assets/images/numpy/inner_product.png)

출처 : https://media.vlpt.us/post-images/dscwinterstudy/11890d50-38fc-11ea-8a14-7ddb1d5b4b35/%ED%96%89%EB%A0%AC%EA%B3%B1.png

```python
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

dot_product = np.dot(A, B)
print('행렬 내적 결과:\n', dot_product)
```


행렬 내적 결과:
 [[19 22]
 [43 50]]

# 전치 행렬 구하기

- 전치 행렬 :  행과 열의 위치를 교환한 원소로 구성한 행렬

- transpose 함수를 사용해 계산한다.

```python
A = np.array([[1, 2],
              [3, 4]])
transpose_mat = np.transpose(A)
print('A의 전치 행렬:\n', transpose_mat)
```


A의 전치 행렬:
 [[1 3]
 [2 4]]
