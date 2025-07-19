---
title: "[matplotlib-basic] 01. Scatter plot 그리기"
cover: "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=1920&h=1080&fit=crop"
date: 2021-07-22
categories:
  - [personal-study, visualization]
tags:
  - python
  - 시각화
  - visualization
  - matplotlib
  - scatter plot
toc: true
---

[pyplot 공식 도큐먼트](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot)

```python
# 기본 셋팅
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams["figure.figsize"] = (12, 9)
```

# Scatter plot

## 1-1. x, y, colors, area 설정하기

* colors 는 임의 값을 color 값으로 적용시켜 준다.

* area는 점의 넓이를 의미. 값이 커지면 당연히 넓이도 커진다.

```python
# 데이터 설정
x = np.random.rand(50)
y = np.random.rand(50)

# 색상 설정
colors = np.arange(50) # 각 50개의 데이터에 맞춰서 랜덤한 색상을 부여

# 크기 설정
area = x * y * 1000
```

```python
area
```


array([ 37.95018598, 300.01925415, 692.27558084, 304.51349504,
       121.99215104,   4.05493055, 639.86659894, 208.52101016,
       247.81898794,  12.36017373, 262.06500427, 267.09442891,
         8.35424379, 250.30261102,  40.90107202, 153.18312173,
        16.61023992, 209.47891914, 360.61215133, 156.50115582,
        71.78868914, 253.36523807, 161.12662803, 201.54999764,
        60.64591569, 347.56073728,  35.4892699 , 249.35996003,
       392.92485661, 432.18884366,   3.86021645, 793.5599259 ,
       352.77511523, 154.27487036,  63.20718849,  81.6918669 ,
       109.2708914 , 223.65253878,  38.39688811,  72.15004734,
        46.9205611 ,  14.08595106, 108.30204514,  10.07158843,
       151.32110288,  31.53992612,   5.17302256,  86.67229901,
       234.1705057 , 138.22034294])

area의 값의 크기에 따라 scatter plot의 원의 크기가 정해진다.

## 기본 scatter plot

```python
plt.scatter(x, y)
plt.show()
```



## 설정 적용한 scatter plot

```python
plt.scatter(x, y, s=area, c=colors)
plt.show()
```



## 1-4. cmap과 alpha

* cmap에 컬러를 지정하면, 모든 데이터가 동일한 컬러 값을 갖도록 할 수 있다.

* alpha값은 투명도. 0 ~ 1 사이의 값을 지정해 줄 수 있고, 0에 가까울 수록 투명한 값을 가진다.

```python
np.random.rand(50)
```


array([0.17855519, 0.66183269, 0.10481482, 0.17998781, 0.4765388 ,
       0.86946316, 0.49740556, 0.83233928, 0.645037  , 0.4754405 ,
       0.26172988, 0.89756865, 0.9142389 , 0.49787243, 0.66915227,
       0.68819688, 0.98967534, 0.0245832 , 0.786606  , 0.25019281,
       0.19565497, 0.5633611 , 0.83573295, 0.03122505, 0.56388789,
       0.49801134, 0.08744029, 0.27115852, 0.45967745, 0.54505432,
       0.15456455, 0.59830877, 0.81781497, 0.81545865, 0.57706866,
       0.35005356, 0.86856862, 0.87279454, 0.78772023, 0.16289437,
       0.1889643 , 0.78159562, 0.05807334, 0.65889227, 0.94353457,
       0.53635536, 0.48983861, 0.11179634, 0.34417505, 0.13060473])


```python
# canvas 크기 설정
plt.figure(figsize=(12, 6))

plt.subplot(131) # row 1개, column은 3개 그 중 1번째 index
plt.scatter(x, y, s=area, cmap='blue', alpha=0.1)
plt.title('alpha=0.1')

plt.subplot(132) # row 1개, column은 3개 그 중 2번째 index
plt.title('alpha=0.5')
plt.scatter(x, y, s=area, cmap='blue', alpha=0.5)

plt.subplot(133) # row 1개, column은 3개 그 중 3번째 index
plt.title('alpha=1.0')
plt.scatter(x, y, s=area, cmap='blue', alpha=1.0)

plt.show()
```


