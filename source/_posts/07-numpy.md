---
title: "[파이썬 기초] 07. Numpy_broadcasting 이해 및 활용하기"
cover: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1920&h=1080&fit=crop"
date: 2021-07-14
categories:
  - [personal-study, numpy]
tags:
  - python
  - broadcasting
  - 브로드캐스팅
  - 서로다른 shape의 numpy끼리 연산하는 방법
  - scalar
  - 상수
toc: true
---
서로 다른 차원의 numpy끼리 연산하는 방법인 broadcasting의 개념에 대해 소개합니다.

```python
import numpy as np
```

# 브로드캐스팅

  - 기본적으로 numpy의 연산은 Shape이 같은 두 ndarray에 대한 연산만이 가능하다.

  - 하지만, 서로 Shape이 다른 numpy끼리도 연산이 가능한 경우가 있다. 이를 브로드 캐스팅(Shape을 맞춤)이라 한다.

# 브로드캐스팅 Rule

 - [공식문서](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html#general-broadcasting-rules)

 - 뒷 차원에서 부터 비교하여 Shape이 같거나, 차원 중 값이 1인 것이 존재하면 가능

![브로드캐스팅 예](https://www.tutorialspoint.com/numpy/images/array.jpg)

    - 출처: https://www.tutorialspoint.com/numpy/images/array.jpg 

- 위의 그림에서 2번째 numpy는 사실상 (1x3)이다. => 즉, 차원 중 값이 1이 있는 경우에 해당

- 그러므로 브로드 캐스팅 Rule을 만족하여 연산이 가능해진다.

## Shape이 같은 경우의 연산

```python
x = np.arange(15).reshape(3, 5)
y = np.random.rand(15).reshape(3, 5)
print("x:\n",x,"\n")
print("y:\n",y)
```


x:
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]] 

y:
 [[0.09750476 0.03329158 0.4588553  0.41886341 0.88091397]
 [0.05444735 0.49626685 0.07778171 0.71429232 0.0817233 ]
 [0.6663016  0.07144051 0.39546019 0.573171   0.06219814]]


```python
# 각 index가 매칭되는 값들끼리 더해서 동일한 shape의 행렬이 나온다.
x + y
```


array([[ 0.09750476,  1.03329158,  2.4588553 ,  3.41886341,  4.88091397],
       [ 5.05444735,  6.49626685,  7.07778171,  8.71429232,  9.0817233 ],
       [10.6663016 , 11.07144051, 12.39546019, 13.573171  , 14.06219814]])


```python
x * y
```


array([[0.        , 0.03329158, 0.91771061, 1.25659024, 3.52365589],
       [0.27223674, 2.97760112, 0.544472  , 5.71433857, 0.7355097 ],
       [6.66301595, 0.78584561, 4.74552231, 7.45122304, 0.87077392]])

### Scalar(상수)와의 연산

```python
# 상수는 어떠한 shape의 numpy라도 연산이 가능
x + 2 
```


array([[ 2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16]])


```python
x * 2
```


array([[ 0,  2,  4,  6,  8],
       [10, 12, 14, 16, 18],
       [20, 22, 24, 26, 28]])


```python
x ** 2
```


array([[  0,   1,   4,   9,  16],
       [ 25,  36,  49,  64,  81],
       [100, 121, 144, 169, 196]], dtype=int32)


```python
x % 2 == 0
```


array([[ True, False,  True, False,  True],
       [False,  True, False,  True, False],
       [ True, False,  True, False,  True]])

# Shape이 다른 경우 연산

```python
a = np.arange(12).reshape(4, 3) # 4행 3열
print("a는\n:",a,"\n")
print("a의 shape는 :",a.shape,"\n")

b = np.arange(100, 103)
print("b는\n:",b,"\n")
print("b의 shape는 :",b.shape,"\n")
```


a는
: [[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]] 

a의 shape는 : (4, 3) 

b는
: [100 101 102] 

b의 shape는 : (3,) 



```python
a + b
```


array([[100, 102, 104],
       [103, 105, 107],
       [106, 108, 110],
       [109, 111, 113]])


```python
c = np.arange(1000, 1004)
print("c는\n:",c,"\n")
print("c의 shape는 :",c.shape,"\n")

d = b.reshape(1, 3)
print("d는\n:",d,"\n")
print("d의 shape는 :",d.shape)
```


c는
: [1000 1001 1002 1003] 

c의 shape는 : (4,) 

d는
: [[100 101 102]] 

d의 shape는 : (1, 3)


```python
a + c
```

```python
print("a의 shape는 :",a.shape,"\n")
print("c의 shape는 :",c.shape,"\n")
```


a의 shape는 : (4, 3) 

c의 shape는 : (4,) 


- a와 c의 shape를 보면 둘다 앞차원이 4 배열을 갖고 있어 브로드캐스팅이 가능할 것 처럼 보인다.

- 하지만 브로드 캐스팅은 **뒤 차원부터 비교** 를 하기 때문에 에러가 발생하는 것

```python
a + d
```


array([[100, 102, 104],
       [103, 105, 107],
       [106, 108, 110],
       [109, 111, 113]])


```python
print("a의 shape는 :",a.shape,"\n")
print("d의 shape는 :",d.shape)
```


a의 shape는 : (4, 3) 

d의 shape는 : (1, 3)

- 동일한 이유로 a와 d는 뒤쪽 차원이 동일한 shape이기 때문에 연산이 가능하다. (b가 연산이 가능한 이유와 동일)

- + d의 경우 차원값이 1인 것이 들어 있으므로 가능

