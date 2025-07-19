---
title: "[matplotlib-basic] 03~04. Line Plot & Areaplot(Filled Area)"
cover: "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1920&h=1080&fit=crop"
date: 2025-07-18
categories:
  - [personal-study, visualization]
tags: []
toc: true
---

# 3. Line Plot

```python
# 기본 셋팅
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams["figure.figsize"] = (12, 9)
```

## 3-1. 기본 lineplot 그리기

```python
# 데이터 생성
x = np.arange(0, 10, 0.1)
y = 1 + np.sin(x) # sine 값으로 생성

# 데이터 입력
plt.plot(x, y)

# label & Title 설정
plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin graph', fontsize=18)

# grid 표시
plt.grid()

plt.show()
```



## 3-2. 하나의 canvas에 2개 이상의 그래프 그리기

* color: 컬러 옵션

* alpha: 투명도 옵션

```python
# 데이터 생성
x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x) #sine값
y_2 = 1 + np.cos(x) #cosine 값

# plot에 데이터 각각 입력
plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.3) #plot1
plt.plot(x, y_2, label='1+cos', color='red', alpha=0.7) # plot2

# label & Title 설정
plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

# Grid & Legend 표시
plt.grid()
plt.legend()

# 시각화
plt.show()
```



## 3-3. 마커 스타일링

* marker: 마커 옵션

---


|Type|Describe|Type|Describe|

|---|--------|---|--------|

|**' . '**|point marker|**' , '**|pixel marker|

|**' o '**|	circle marker|**' v '**|	triangle_down marker|

|**' ^ '**|	triangle_up marker|**'  '**|	triangle_right marker|**' 1 '**|	tri_down marker|

|**' 2 '**|	tri_up marker|**' 3 '**|	tri_left marker|

|**' 4 '**|	tri_right marker|**' s '**|	square marker|

|**' p '**|	pentagon marker|**' * '**|star marker|

|**' h '**|	hexagon1 marker|**' H '**|	hexagon2 marker|

|**' + '**|	plus marker|**' x '**|	x marker|

|**' D '**|	diamond marker|**' d '**|	thin_diamond marker|

|'**&#124;**'|vline marker|'_'|hline marker|

```python
# 데이터 생성
x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

# 데이터 입력 & 마커 설정
plt.plot(x, y_1, label='1+sin', color='blue', alpha=0.3, marker='o')
plt.plot(x, y_2, label='1+cos', color='red', alpha=0.7, marker='+')

# label & Title 설정
plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

# Grid & Legend 설정
plt.grid()
plt.legend()

# 시각화
plt.show()
```



### 3-4 라인 스타일 변경하기

* linestyle: 라인 스타일 변경 옵션

| Type | Describe            | Type | Describe          |
| ---- | ------------------- | ---- | ----------------- |
| '-'  | solid line style    | '--' | dashed line style |
| '-.' | dash-dot line style | ':'  | dotted line style |

```python
# 데이터 생성
x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

# 데이터 입력, 마커 & linestyle 설정
plt.plot(x, y_1, label='1+sin', color='blue', linestyle=':')
plt.plot(x, y_2, label='1+cos', color='red', linestyle='-.')

# label & Title 설정
plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

# Grid & Legend 표시
plt.grid()
plt.legend()

# 시각화
plt.show()
```



# 4. Areaplot (Filled Area)

- lineplot에서 line의 밑 부분을 색칠하는 그래프

- matplotlib에서 area plot을 그리고자 할 때는 **fill_between 함수**를 사용하면 된다.

```python
# 데이터 생성
y = np.random.randint(low=5, high=10, size=20)
y
```


array([7, 5, 8, 6, 5, 8, 8, 8, 6, 6, 5, 6, 8, 6, 9, 9, 5, 6, 7, 9])

## 4-1. 기본 areaplot 그리기

plt.fill_between(x,y, color='색상', alpha= 투명도값) 

```python
# 데이터 생성
x = np.arange(1,21)

# 5 ~ 10 사이의 수를 20개로 쪼개서 데이터 생성 (데이터는 int 형)
y =  np.random.randint(low=5, high=10, size=20) 

# fill_between으로 색칠
plt.fill_between(x, y, color="green", alpha=0.6)

# 시각화
plt.show()
```



## 4-2. 경계선을 굵게 그리고 area는 옅게 그리는 효과 적용

- alpha값의 수치를 낮게 조정한 뒤, 동일한 plot을 한번 더 그려주면 된다.

- 옅게 그린 그림 위에 진한 그래프를 덧그리는 방식

```python
plt.fill_between( x, y, color="green", alpha=0.3)
plt.plot(x, y, color="green", alpha=0.8)
```


[]



## 4-3. 여러 그래프를 겹쳐서 표현

- 여러개의 plot의 alpha값을 서로 다르게 주는 것이 포인트

- 어차피 겹치는 부분은 진해지기 때문에 겹치지 않는 부분에서의 구분을 명확하게 하기 위해 alpha값을 다르게 하는게 좋다.

- 이때 alpha값은 연하게 하는 것이 좋다. (겹치면 진해지기 때문)

```python
# 데이터 생성
x = np.arange(1, 10, 0.05)
y_1 =  np.cos(x)+1
y_2 =  np.sin(x)+1
y_3 = y_1 * y_2 / np.pi

# 하나의 canvas에 여러개의 그래프 그리기
plt.fill_between(x, y_1, color="green", alpha=0.1)
plt.fill_between(x, y_2, color="blue", alpha=0.2)
plt.fill_between(x, y_3, color="red", alpha=0.3)
```






**References**

[Matplotlib Document](https://matplotlib.org/)

