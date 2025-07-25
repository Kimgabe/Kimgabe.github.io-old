---
title: "[Cheat Sheet] [Pre-processing] 형변환을 활용한 효율적인 데이터 전처리팁 모음"
cover: "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1920&h=1080&fit=crop"
date: 2023-11-21
categories:
  - [personal-study, cheat_sheet]
tags: []
toc: true
---
## 🚦 Summary 
- Series 데이터 생성시 사용하는 옵션인 dtype를 활용한 효율적이면서 유용한 데이터 변환 방법과 사례들을 소개합니다.

## 📌 Intro.
- pandas의 series를 공부하다보면 series 데이터 생성시에 dtype을 지정할 수 있다는 것을 배웁니다.

- 이러한 형변환 기능을 통해 다양한 유형의 데이터를 좀 더 손쉽고 효율적으로 바꾸거나 생성할 수 있는 팁을 정리해 공유합니다.

### 숫자로된 string형태의 데이터 만들기

- 일반적으로 숫자로된 형태의 시리즈 데이터를 만들려면 "" 또는 ''를 숫자에 둘러줘야합니다.

- 이를 여러개의 숫자에 작업하려면 실제로 굉장히 많은 타이핑을 해야 합니다.

- 하지만 dtype을 통해 이를 좀 더 효율적으로 생성할 수 있습니다.

```python

import pandas as pd

```

```python

# 숫자지만 문자열 타입의 데이터로 만들 때

number_series = pd.Series(['1', '2', '3'], index=['idx1', 'idx2', 'idx3'], dtype=str)

print(type(number_series), ',', number_series[0], ',', type(number_series[0]))

```



 , 1 , 



- 생성된 number_seires는 시리즈 형태의 데이터 이며 그 안에 담긴 0번째 인자는 string 임을 알 수 있습니다.

- 이를 좀 더 손쉽게 생성해 보도록 하겠습니다.

```python

# 숫자 리스트를 문자열로 변환하는 경우

number_series = pd.Series([1, 2, 3], index=['idx1', 'idx2', 'idx3'], dtype=str)

print(type(number_series), ',', number_series[0], ',', type(number_series[0]))

```



 , 1 , 



- 단순히 ' '를 둘러주는 것을 생략하였을 뿐이지만 실제로 타이핑하는 것에 대한 부담이 현저히 줄게 됩니다.

- 이와 같이 시리즈 생성시에 입력하는 옵션값이 dtype를 이용해 숫자값을 가진 string형태의 시리즈 데이터를 더욱 효율적으로 생성했습니다.

---


- 위와 같이 입력의 번고로움을 줄이는 방식은 아니지만 'dytpe'을 응용한 손쉬운 데이터 변환이라는 방법에서 몇가지 예시가 더 있습니다.ㅋ

### 날짜 데이터 입력 간소화

- 일반적으로 날짜형태의 데이터를 입력한다고 해도 날짜형식으로 변경되지는 않으며, 별도의 변경작업을 거쳐야 합니다.

```python

# 문자열 형태로 날짜 데이터 입력

date_series = pd.Series(['2020-01-01', '2020-01-02', '2020-01-03'])

print(type(date_series), ',', date_series[0], ',', type(date_series[0]))

```



 , 2020-01-01 , 



- 하지만 아래와 같이 dtype을 통해 손쉽게 생성과 동시에 datetime형태의 데이터로 변경할 수 있습니다.

```python

# dtype을 이용해 날짜 데이터 타입으로 자동 변환

# datetime64[ns]에서 ns는 nano sec을 의미

date_series = pd.Series(['2020-01-01', '2020-01-02', '2020-01-03'], dtype='datetime64[ns]')

print(type(date_series), ',', date_series[0], ',', type(date_series[0]))

```



 , 2020-01-01 00:00:00 , 



- 원래대로라면 생성된 데이터에 astype()를 써서 변경해야 합니다.

```python

date_series = pd.Series(['2020-01-01', '2020-01-02', '2020-01-03'])

date_series = date_series.astype('datetime64[ns]')

print(type(date_series), ',', date_series[0], ',', type(date_series[0]))

```



 , 2020-01-01 00:00:00 , 



### 범주형 데이터를 수치형으로 손쉽게 변환하기

- 통상적으로 범주형 데이터를 수치형으로 변환하기 위해서는 Label Encoding이나 One-Hot Encoding을 사용해야 합니다.

- low, medium, high라는 데이터에 대해 Label encoding과 One-Hot Encoding을 적용하는 코드는 아래와 같습니다.

---


#### 레이블 인코딩을 통한 범주형 데이터의 수치화

- 레이블 인코딩은 각 범주를 숫자 값으로 변환합니다. 아래와 같이 세개의 범주 'low', 'medium', 'high' 가 있는 경우 이 데이터를 각각 0, 1, 2로 매핑하여 수치로 변경 합니다.

```python

from sklearn.preprocessing import LabelEncoder

# 범주형 데이터

categories = ['low', 'medium', 'high']

# 레이블 인코더 생성 및 피팅

label_encoder = LabelEncoder()

label_encoded = label_encoder.fit_transform(categories)

print(type(label_encoded), label_encoded)

```



 [1 2 0]



- 하지만 dtype를 사용하면 좀 더 손쉽게 범주형 데이터를 수치형으로 변경할 수 있습니다.

```python

# dtype을 이용해 범주형 데이터를 수치형으로 변환

category_series = pd.Series(['low', 'medium', 'high'], dtype='category')

category_encoded = category_series.cat.codes

print(type(category_encoded))

print(category_encoded) # 좌측은 index, 우측은 값

```





0    1

1    2

2    0

dtype: int8



- 라벨 인코딩과 시리즈의 dtype 변경방법모두 문자열을 알파뱃순으로 숫자를 할당하기 때문에 high가 0이 됩니다.

- 이런 방식의 인코딩을 하는 것은 원한 인코딩고 간이 범주데이터가 가지고 잇는 순서나 중요도를 없애고 개별 데이터로서 보기위한 변환이기 때문임을 명심해야 합니다.

### 정수형 데이터를 부동소수점으로 변환하기

- 일반적인 정수형 데이터를 시리즈로 만들면 단순히 int64 type의 데이터가 됩니다.

```python

# 정수형 데이터 입력

integer_series = pd.Series([1, 2, 3])

print(type(integer_series), ',', integer_series[0], ',', type(integer_series[0]))

```



 , 1 , 



- 이러한 데이터를 생성할 때 dtype를 float로 지정하면 소수점을 가진 숫자 데이터로 일괄 변경이 가능합니다.

```python

# dtype을 이용해 정수형 데이터를 부동소수점으로 변환

float_series = pd.Series([1, 2, 3], dtype=float)

print(type(float_series), ',', float_series[0], ',', type(float_series[0]))

```



 , 1.0 , 



### bool 타입 시리즈의 빠른 생성

- 보통 시리즈로 bool타입의 데이터를 만들려면 문자열로 입력한뒤에 각 문자에 T/F를 맵핑해 줘야 합니다.

```python

# 불리언 데이터를 문자열로 입력

boolean_series = pd.Series(['True', 'False', 'True', 'False'])

print(type(boolean_series[0]))

# 문자열 데이터를 불리언 타입으로 변환

boolean_series = boolean_series.map({'True': True, 'False': False})

print(type(boolean_series[0]))

```









- 하지만 dtype를 사용한다면 아래와 같이 1줄의 코드로 bool타입의 데이터를 만들 수 있습니다.

```python

# 직접 불리언 타입으로 데이터 생성

boolean_series = pd.Series([True, False, True, False], dtype=bool)

print(type(boolean_series[0]), boolean_series[0])

```



 True



---


## ✔️ Outro.

- 판다스의 시리즈에 대해 공부하다가 우연히 발견하게 된 효율적인 데이터 변환 및 생성 방법에 대해 정리를 해봤습니다.

- 사실 맨 처음 제공한 숫자로된 str 데이터를 만드는 방법을 제외하고는 통상적인 dtype을 쓰는 방법에 대한 소개에 더 가까운 글이 되었습니다.

- 하지만 단순히 각 형태에 맞는 format으로 시리즈 데이터를 생성하면 대체로 그 타입에 맞는 데이터들이 생성되는 것에 비해 몇몇 데이터는 그러한 점이 적용되지 않습니다.

- 이번 포스팅에서 예시로 든 것들이 그런 데이터 타입의 대표적인 예시들이라 볼 수 있습니다.