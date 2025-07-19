---
title: "[matplotlib-basic] 05~06. Histogram & Pie Chart"
cover: "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=1920&h=1080&fit=crop"
date: 2025-07-18
categories:
  - [personal-study, visualization]
tags: []
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

# 5. Histogram

## 5-1. 기본 Histogram 그리기

plt.hist(x, bins= 빈도값) 

- bins : 히스토그램의 빈도수 설정 (설정 값에 따라 히스토그램 모양이 다소 변할 수 있다.)

```python
# 데이터 기초 
N = 100000 # 전체 데이터 수
bins = 30 # histogram 빈도

# 데이터 생성
x = np.random.randn(N)

# 히스토 그램 생성
plt.hist(x, bins=bins)

plt.show()
```



## 5-2. 다중 Histogram 그리기

* sharey: y축을 다중 그래프가 share 할 것인지 여부

* tight_layout: graph의 배치를 자동으로 조절해주어 fit한 graph를 생성하는 기능

```python
# 데이터 기초 
N = 100000 # 전체 데이터 수
bins = 30 # histogram 빈도

# 데이터 생성
x = np.random.randn(N)

# canvas 그리기
fig, axs = plt.subplots(1, 3, 
                        sharey=True, 
                        tight_layout=True
                       )

fig.set_size_inches(12, 5, forward= True) #크기 바꾸기(inch 단위)
# forward=True 로 설정하면 canvas 사이즈가 자동으로 업데이트 된다.
    
# bins 값이 커질수록 더 오밀 조밀한 그래프가 그려진다.
axs[0].hist(x, bins=bins) # bins = 30
axs[1].hist(x, bins=bins*2) # bins = 30*2
axs[2].hist(x, bins=bins*4) # bins = 30*4

plt.show()
```



## 5-3. Y축에 Density 표기

```python
N = 100000
bins = 30

x = np.random.randn(N)

fig, axs = plt.subplots(1, 2, 
                        tight_layout=True
                       )
fig.set_size_inches(9, 3)

# density=True 값을 통하여 Y축에 density를 표기할 수 있다.
# cumulative=True : 누적 분포로 표시하겠다.
axs[0].hist(x, bins=bins, density=True, cumulative=True)
axs[1].hist(x, bins=bins, density=True)

plt.show()
```



# 6. Pie Chart 

**pie chart 옵션**

|Type|Describe|

|---|--------|

| explode|파이에서 툭 튀어져 나온 비율|

|autopct| 퍼센트 자동으로 표기|

|shadow| 그림자 표시|

|startangle| 파이를 그리기 시작할 각도|

**스타일링 parameter**

- texts, autotexts 는 인자를 리턴 받는다.
  - **texts**는 label에 대한 텍스트 효과를 줄때 사용

- **autotexts**는 파이 위에 그려지는 텍스트 효과를 다룰 때 사용.

- **autopct**는 파이 위에 표시되는 %의 소수점 자리수
- %1.1f%% : 소수점 1번째 자리
    
- %1.2f%% : 소수점 2번째 자리

```python
# 세부 설정
labels = ['Samsung', 'Huawei', 'Apple', 'Xiaomi', 'Oppo', 'Etc']
sizes = [20.4, 15.8, 10.5, 9, 7.6, 36.7]
explode = (0.3, 0, 0, 0, 0, 0) #tuple형태 - 각각의 데이터와 mapping 된다.

# texts, autotexts 인자를 활용하여 텍스트 스타일링을 적용
patches, texts, autotexts = plt.pie(sizes, 
                                    explode=explode, # 위에서 설정한 값대로 중심점에서 멀어진다.(튀어 나가는 정도) 
                                    labels=labels,  
                                    autopct='%1.1f%%', # 소수점 1번째 자리까지
                                    shadow=True, 
                                    startangle=90) #labels 의 첫번째 value인 samsung이 그려질 위치

# Title 설정
plt.title('Smartphone pie', fontsize=15)

# label 텍스트에 대한 스타일 적용
# 각 test 별로 설정 위해 loop 사용
for t in texts:
    t.set_fontsize(12)
    t.set_color('gray')

# pie 위의 텍스트에 대한 스타일 적용
# 각 test 별로 설정 위해 loop 사용
for t in autotexts:
    t.set_color("white")
    t.set_fontsize(18)

plt.show()
```



**References**

[Matplotlib Document](https://matplotlib.org/)

