---
title: "[matplotlib-basic] 00. matplotlib 기본옵션 설정하는 법"
cover: "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=1920&h=1080&fit=crop"
date: 2021-07-22
categories:
  - [personal-study, visualization]
tags:
  - - python - 시각화 - visualization - matplotlib - canvas - subplot - title - fontsize - tick - x축 - y축 - legend - marker - linestyle - color - alpha - 투명도 - grid - 이미지저장
toc: true
---

# matplotlib.pyplot의 기본적인 canvas 그리기와 스타일링 예제

[pyplot 공식 도큐먼트](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot)

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 불필요한 경고 표시 생략
import warnings
warnings.filterwarnings(action = 'ignore')
```

```python
#plt.rc('font', family='NanumBarunGothic')  # font 설정 #font는 영구 설정으로 변경할 수도 있다.
plt.rcParams["figure.figsize"] = (12, 9) # 캔버스 크기 변경
```

## 1. 밑 그림 그리기

### 1-1. 단일 그래프

```python
## data 생성
data = np.arange(1, 100) # 1~99 의 데이터 생성
```

```python
data
```


array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
       35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
       52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
       69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
       86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])


```python
## plot - 기본적인 line graph를 그리는 함수
plt.plot(data) # data에 담긴 값들로 matplotlib을 사용해 line graph를 그리겠다. 

## 그래프를 시각화 해서 출력하는 코드
plt.show()
```



### 1-2. 다중 그래프 (multiple graphs)

#### 1개의 Canvas 안에 다중 그래프를 그리기

- 이때, data에 직접 값을 +, -, *, / 등의 연산 작용을 하여 data 변형을 할 수 도 있다.

---


명령어

```python

plt.plot(data)

```

```python
# 그래프용 데이터 생성
data = np.arange(1, 51) # 데이터 생성
data2 = np.arange(51, 101) # 데이터 생성

# 첫 번째 그래프 데이터 입력
plt.plot(data)

# 두 번째 그래프 데이터 입력
plt.plot(data2)

# 세 번째 그래프 데이터 입력
plt.plot(data2+50) 

# 그래프 시각화
plt.show()
```



#### 2개의 figure로 나누어서 다중 그래프 그리기

* figure()는 새로운 그래프 canvas를 생성한다.

plt.figure() 명령어 아래에 

plt.plot(data) 가 들어오게 되면, 새로운 캔버스에 그래프가 그려진다.

```python
data = np.arange(100, 201)
plt.plot(data)

data2 = np.arange(200, 301)

plt.figure() # figure()는 새로운 그래프를 생성하는 명령어이다.

# 위에 plt.figure() 를 선언했기 때문에, 아래의 data2의 plot은 새로운 canvas에 그려지게 된다.
plt.plot(data2)

plt.show()
```





### 1-3. 여러개의 plot을 그리는 방법 (subplot)

plt.subplot(row, column, index) 을 사용한다.

콤마 없이 숫자만 입력할 수도 있다.

plt.subplot(211)

![image-3.png](attachment:image-3.png)

#### plt.subplot(row, column, index) 로 그리기

```python
# 데이터 생성
data = np.arange(100, 201)
data2 = np.arange(200, 301)

# canvas 그리기 - 위의 그림 참조
plt.subplot(2, 1, 1) # row가 2, column이 1인 그래프 중 1번째 index에 그래프를 그려라
plt.plot(data)

plt.subplot(2, 1, 2) # row가 2, column이 1인 그래프 중 2번째 index에 그래프를 그려라
plt.plot(data2)

plt.show()
```



#### plt.subplot(콤마생략) ver.

```python
data = np.arange(100, 201)
# 콤마를 생략하고 row, column, index로 작성가능
# 211 -> row: 2, col: 1, index: 1
plt.subplot(211)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(212)
plt.plot(data2)

plt.show()
```



두 그래프 모두 각각의 canvas마다 x,y축의 label이 다른 것을 알 수 있다.

다음의 그림처럼 canvas를 구성할 수도 있다.

![image.png](attachment:image.png)

```python
data = np.arange(100, 201)
plt.subplot(1, 3, 1) # row 는1, column은 3인 캔버스에서 1번째 index위치
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(1, 3, 2) # row 는1, column은 3인 캔버스에서 2번째 index위치
plt.plot(data2)

data3 = np.arange(300, 401) 
plt.subplot(1, 3, 3) # row 는1, column은 3인 캔버스에서 3번째 index위치
plt.plot(data3)

plt.show()
```



### 1-4. 여러개의 plot을 그리는 방법 (subplots) - s가 더 붙는다.

- 각 데이터 마다 subplot(row, column, index) 를 하는 것이 아니라, 전체 캔버스 모양을 잡아 놓고 시작한다.

fit, axes = plt.subplots(행의 갯수, 열의 갯수) 로 지정한다.

각 plot의 위치는 axes[row, column] 각 좌표값을 입력해 표현한다.

![image-2.png](attachment:image-2.png)

```python
data = np.arange(1, 51)
# data 생성

# 밑 그림
fig, axes = plt.subplots(2, 3)

axes[0, 0].plot(data) 
axes[0, 1].plot(data * data)
axes[0, 2].plot(data ** 3)
axes[1, 0].plot(data % 10)
axes[1, 1].plot(-data)
axes[1, 2].plot(data // 20)

plt.tight_layout() # 그래프를 tight하게 해서 가독성이 좋게 출력되도록 조정하는 옵션
plt.show()
```



# 2. 주요 스타일 옵션

```python
from IPython.display import Image

# 출처: matplotlib.org
Image('https://matplotlib.org/_images/anatomy.png')
```



## 2-1. Title

plt.title('    ')

```python
# 데이터를 바로 plot에 입력 ([x 좌표], [y좌표])
plt.plot([1, 2, 3], [3, 6, 9]) 
plt.plot([1, 2, 3], [2, 4, 9])

# 타이틀 & font 설정
plt.title('This is the title')

# 시각화
plt.show()
```



### Title 의 fontsize 조정

```python
plt.plot([1, 2, 3], [3, 6, 9])
plt.plot([1, 2, 3], [2, 4, 9])

# 타이틀 & font 설정
plt.title('Increase Font size of the Title', fontsize=20)

plt.show()
```



## 2-2. X, Y축 Label 설정

```python
# 데이터 입력
plt.plot([1, 2, 3], [3, 6, 9]) 
plt.plot([1, 2, 3], [9, 6, 3])

# 타이틀 & font 설정
plt.title('Label 설정 예제', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('수요', fontsize=20) # x label 
plt.ylabel('공급', fontsize=20) # y label

plt.show()
```



## 2-3. X, Y 축 Tick 설정 (rotation)

Tick :  X, Y축에 위치한 눈금

```python
plt.plot(np.arange(10), np.arange(10)*2)
plt.plot(np.arange(10), np.arange(10)**2)
plt.plot(np.arange(10), np.log(np.arange(10)))

# 타이틀 & font 설정
plt.title('X, Y 틱을 조정', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()
```



## 2-4. 범례(Legend) 설정 

```python
# 데이터르 plot에 바로 입력
plt.plot(np.arange(10), np.arange(10)*2)
plt.plot(np.arange(10), np.arange(10)**2)
plt.plot(np.arange(10), np.log(np.arange(10)))

# 타이틀 & font 설정
plt.title('범례(Legend) 설정 예제', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# legend 설정
plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

plt.show()
```



## 2-5. X와 Y의 한계점(Limit) 설정

xlim(), ylim()

```python
plt.plot(np.arange(10), np.arange(10)*2)
plt.plot(np.arange(10), np.arange(10)**2)
plt.plot(np.arange(10), np.log(np.arange(10)))

# 타이틀 & font 설정
plt.title('This is the title', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# legend 설정
plt.legend(['10 * 2', '10 ** 2', 'log'], fontsize=15)

# x, y limit 설정 - 데이터 보다 범위를 작게 설정하면, 설정한 범위내로 잘라서 표현
plt.xlim(0, 5)
plt.ylim(0.5, 10)

plt.show()
```



## 2-6. 스타일 세부 설정 - 마커, 라인, 컬러

스타일 세부 설정은 마커, 선의 종류 설정, 그리고 컬러가 있으며, 문자열로 세부설정을 하게 됩니다.

[세부 도큐먼트 확인하기](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot)

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

**' D '**|	diamond marker|**' d '**|	thin_diamond marke|

|' **&#124;** '|	vline marker| '_'	|hline marker|

### Marker 설정

```python
# 데이터 입력 & 마커 설정
plt.plot(np.arange(10), np.arange(10)*2, marker='o', markersize=5)
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', markersize=10)
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', markersize=15)
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='|', markersize=20)

# 타이틀 & font 설정
plt.title('마커 설정', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()
```



### Linestyle 설정

**line의 종류**

|Type|Describe|Type|Describe|

|---|--------|---|--------|

|**'-'**| solid line style|**'--'** |dashed line style|

|**'-.'**| dash-dot line style|**':'**| dotted line style|

```python
# 데이터 입력, 마커 & linestyle 설정
plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='o', linestyle='-')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='v', linestyle='--')
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='+', linestyle='-.')
plt.plot(np.arange(10), np.arange(10)*2 - 40, marker='*', linestyle=':')

# 타이틀 & font 설정
plt.title('다양한 선의 종류 예제', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()
```



### Color 설정

**color의 종류**

|Type|Describe|Type|Describe|

|---|--------|---|--------|

|**'b'**| blue|**'g'**| green|

|**'r'**| red|**'c'**| cyan|

|**'m'**| magenta|**'y'**| yellow|

|**'k'** |black|**'w'** |white|

```python
# 데이터 입력 , 마커 & linestyle & 색상 설정
plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')

# 타이틀 & font 설정
plt.title('색상 설정', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()
```



### Alpha 설정 (투명도)

```python
# 데이터 입력 , 마커 & linestyle & 색상 & alpha(투명도)설정
plt.plot(np.arange(10), np.arange(10)*2, color='b', alpha=0.1)
plt.plot(np.arange(10), np.arange(10)*2 - 10, color='b', alpha=0.3)
plt.plot(np.arange(10), np.arange(10)*2 - 20, color='b', alpha=0.6)
plt.plot(np.arange(10), np.arange(10)*2 - 30, color='b', alpha=1.0)

# 타이틀 & font 설정
plt.title('투명도 (alpha) 설정', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.show()
```



### 그리드 설정

```python
# 데이터 입력 , 마커 & linestyle & 색상 설정
plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')

# 타이틀 & font 설정
plt.title('그리드 설정', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# grid 옵션 추가
plt.grid()

plt.show()
```



# 이미지 저장 및 활용

## 방법 1. 함수 사용

plt.savefig('타이틀.확장자', 'dpi=300')

- dpi는 해상도를 의미, 반드시 적지 않아도 된다.

- 해당 note가 위치한 directory에 저장된다.

```python
# 데이터 입력 , 마커 & linestyle & 색상 설정
plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='-', color='b')
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', linestyle='--', color='c')
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', linestyle='-.', color='y')
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', linestyle=':', color='r')

# 타이틀 & font 설정
plt.title('그리드 설정', fontsize=20)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=20)
plt.ylabel('Y축', fontsize=20)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

# grid 옵션 추가
plt.grid()

# Save image
plt.savefig('Example of set grid.png', dpi=300)

plt.show()
```



## 방법 2) 직접 다운로드

- 시각화된 그래프 우클릭 -> 다른 이름으로 저장 -> 저장 위치 및 확장자 설정

![image-2.png](attachment:image-2.png)

