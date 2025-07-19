---
title: "[파이썬 기초] 10. Numpy_ndarray 데이터로 다양한 그래프 그리기"
cover: "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1920&h=1080&fit=crop"
date: 2021-07-14
categories:
  - [personal-study, numpy]
tags:
  - python
  - 그래프 그리기
  - line plot
  - scatter plot
  - 그래프에 주석추가하기
  - grid 추가하기
  - subplot으로 그래프 여러개 그리기
  - histogram그리기
toc: true
---
plot함수를 이용해 numpy 모듈로 추출한 랜덤한 데이터를 시각화 하는 방법을 소개합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```

# 그래프 데이터 생성

```python
x = np.linspace(0, 10, 11) 

# x와 연관이 있도록 생성
y = x ** 2 + x + 2 + np.random.randn(11) #random을 추가해 일종의 noise 추가  

print(x)
print(y)
```


[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
[  3.21296218   4.3128255    9.1887181   14.86129619  22.55897999
  32.65802433  44.95035291  58.63330963  73.56553627  92.3407775
 111.20280392]

# 그래프 출력하기

 - plot함수 (선 그래프), scatter(점 그래프), hist(히스토그램) 등 사용

   - 함수의 parameter 혹은 plt의 다른 함수로 그래프 형태 및 설정을 변경 가능

   - 기본적으로, x, y에 해당하는 값이 필요

## Line plot

```python
plt.plot(x, y)
```


[]



## Scatter plot

```python
plt.scatter(x, y)
```






# 그래프에 주석 추가 

* **x, y 축 및 타이틀**

```python
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.plot(x, y)
```


[]



* **grid 추가**

```python
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.grid(True)
plt.plot(x, y)
```


[]



* **x, y축 범위 지정**

```python
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('X-Y relation')
plt.grid(True)

plt.xlim(0, 20)
plt.ylim(0, 200)

plt.plot(x, y)
```


[]



# plot 함수 parameters

 - 그래프의 형태에 대한 제어 가능

 - [plot함수 도큐먼트](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot)

## 그래프의 색상 변경

```python
plt.plot(x, y, '#ff00ff')
```


[]



## 그래프 선스타일 변경

```python
plt.plot(x, y, '-.')
```


[]



```python
plt.plot(x, y, 'g^')
```


[]



```python
plt.plot(x, y, 'm:')
```


[]



* 그래프 두께 변경

 - linewidth 명시

```python
plt.plot(x, y, 'm:', linewidth=9)
```


[]



* keyword parameter 이용하여 모든 속성 설정

 - https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

 - color

 - linestyle

 - marker

 - markerfacecolor

 - markersize 등등

```python
plt.plot(x, y, color='black', 
          linestyle='--', marker='^',
         markerfacecolor='blue', markersize=10)
```


[]



# subplot으로 여러 그래프 출력하기

 - subplot함수로 구획을 구별하여 각각의 subplot에 그래프 출력

```python
plt.subplot(2, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(2, 2, 2)
plt.plot(x, y, 'g')

plt.subplot(2, 2, 3)
plt.plot(y, x, 'k')

plt.subplot(2, 2, 4)
plt.plot(x, np.exp(x), 'b')
```


[]



# hist함수 사용

 - histogram 생성

 - bins로 historgram bar 개수 설정

```python
data = np.random.randint(1, 100, size=200)
print(data)
```


[99 89 83 43 23  1 14 28 76 75  9 14 39 22 12 71 43 36 13 31 66  1  1 22
 99 83 87 84 88 74 35 56 13 92 98 35 51 27 65 63 61 81 83 38 64 31 72 56
 71  8 77 81 21  6 65 38 54 63 68 76  5 25 48 99 33 24 35 30 50 44  7 84
 68  5 37 43 72 85 40 42 28 57 18 53 80 32 66 18 57 84 24 45 57 75  2  6
 20 85 36 53 77 57  3 97 12 93  4 48 51 21 75  9 15 29 38 37 71 97 42 19
 83 33 83 33 76 55 20 73 88 79 23  3 44 98 89  7  4 88 33 65 52 40 18 72
 65 83 80 87 25 99 46 45 34 31 68  7  7 51 80 61 54 30 13 71 35 62 86 26
 79 78 64  5 23 12 13 49  1 59 48 56 62 25 64 68 75 34 40 36  4 79 46 85
 17 13 14 46  6 95 66  9]


```python
plt.hist(data, bins=20, alpha=0.3)
plt.xlabel('값')
plt.ylabel('개수')
plt.grid(True)
```


