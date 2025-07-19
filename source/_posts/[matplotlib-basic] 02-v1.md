---
title: "[matplotlib-basic] 02. Barplot, Barhplot"
cover: "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1920&h=1080&fit=crop"
date: 2021-07-23
categories:
  - [personal-study, visualization]
tags:
  - python
  - 시각화
  - visualization
  - matplotlib
  - bar plot
  - 막대그래프
  - barhplot
  - 가로막대 그래프
toc: true
---

[pyplot 공식 도큐먼트](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot)

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

```python
#plt.rc('font', family='NanumBarunGothic') 
plt.rcParams["figure.figsize"] = (12, 9)
```

# 2. Barplot, Barhplot

1개의 canvas 안에 다중 그래프 그리기

## 2-1. 기본 Barplot 그리기

```python
# 데이터 생성
x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

# canvas 크기 설정
plt.figure(figsize=(8, 5))

# plt.bar(x, y)
# bar 그래프로 입력하기
plt.bar(x, y, align='center', alpha=0.7, color='red')

# plt.xticks(x)
# X tick, Y tick 설정
plt.xticks(rotation=20, fontsize = 10)
#plt.yticks(rotation=30)

# X축 & Y축 Label 설정
#plt.xlabel('Subjects')
plt.ylabel('Number of Students')

plt.title('Number of Students by Subjects', fontsize = 20)

plt.show()
```



## 2-2. 기본 Barhplot 그리기

- 일반적인 bar plot에서 tick의 값이 길어서 보기 불편한 경우, 위의 예제 처럼 rotation을 주는 방법도 있지만, 아래와 같이 barhplot으로 변경하여 그려주는 경우 도 있다.

- barh 함수에서는 barplot에서 **xticks로 설정**했던 부분을 **yticks로 변경** 하는 개념이다.

```python
x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

plt.barh(x, y, align='center', alpha=0.7, color='green')
plt.yticks(x)
plt.xlabel('Number of Students')
plt.title('Number of Students by Subjects', fontsize = 20)

plt.show()
```



## 2-3. Barplot에서 비교 그래프 그리기

```python
# 데이터 생성
x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))

# y값을 2개로 (비교대상) 해주는 것이 point
y_1 = [66, 80, 60, 50, 80, 10]
y_2 = [55, 90, 40, 60, 70, 20]

# bar의 넓이 지정
width = 0.35

# subplots 생성
fig, axes = plt.subplots()

# 넓이 설정
# 하나의 그래프를 반으로 쪼개는 개념이 point
axes.bar(x - width/2, y_1, width, align='center', alpha=0.5)
axes.bar(x + width/2, y_2, width, align='center', alpha=0.8)

# xtick 설정
plt.xticks(x)
axes.set_xticklabels(x_label)
plt.ylabel('Number of Students')
plt.title('Number of Students by Subjects', fontsize = 20)

plt.legend(['john', 'peter'])

plt.show()
```



## 2-4. Barhplot에서 비교 그래프 그리기

- 주요 point는 barplot과 동일

- barplot에서 **xticks로 설정**했던 부분을 **yticks로 변경** 하는 것이 차이점

```python
# 데이터 생성
x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))
y_1 = [66, 80, 60, 50, 80, 10]
y_2 = [55, 90, 40, 60, 70, 20]

# 넓이 지정
width = 0.35

# subplots 생성
fig, axes = plt.subplots()

# 넓이 설정
axes.barh(x - width/2, y_1, width, align='center', alpha=0.5, color='green')
axes.barh(x + width/2, y_2, width, align='center', alpha=0.8, color='red')

# xtick 설정
plt.yticks(x)
axes.set_yticklabels(x_label)
plt.xlabel('Number of Students')
plt.title('Number of Students by Subjects', fontsize = 20)

plt.legend(['john', 'peter'])

plt.show()
```



* color: 컬러 옵션

* alpha: 투명도 옵션

**References**

[Matplotlib Document](https://matplotlib.org/)

