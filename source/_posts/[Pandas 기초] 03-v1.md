---
title: "[Pandas] 03. Series 데이터 연산과 탐색기법"
cover: "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=1920&h=1080&fit=crop"
date: 2023-11-25
categories:
  - [personal-study, pandas]
tags: []
toc: true
---
## 🚦 Summary
- Series데이터의 다양한 연산에 대해 다룹니다.
- Series안에 있는 숫자, 문자 데이터의 연산을 어떻게 하는지에 대한 예시코드와 함께 내용을 정리합니다.
- 또한 Series 데이터의 다양한 탐색기법 및 다른 데이터와의 상호작용 등에 대해 다룹니다.

```python

# 필요 라이브러리 로드

import numpy as np

import pandas as pd

```

## Series 데이터의 연산

- Pandas의 Series는 Index를 가진 1차원 배열의 형태입니다.

- Series에서 데이터 연산은 기본적으로 Index를 기준으로 이뤄집니다.

- 연산은 간단한 산술연산자를 사용해서 수행할 수 있고, 이는 Series의 각 원소별로 개별적으로 적용됩니다.

```python

# 과일 가격 Series

prices = pd.Series([1000, 2000, 1500], index=['apple', 'banana', 'strawberry'])

# 과일 수량 Series

quantities = pd.Series([3, 2, 5], index=['apple', 'banana', 'strawberry'])

print("Prices:\n", prices)

print("Quantities:\n", quantities)

```

    Prices:

     apple         1000

    banana        2000

    strawberry    1500

    dtype: int64

    Quantities:

     apple         3

    banana        2

    strawberry    5

    dtype: int64

- 이 코드는 'apple', 'banana', 'strawberry'를 Index로 가지는 Series 두 개를 생성합니다. 하나는 각 과일의 가격을, 다른 하나는 수량을 나타냅니다.

- 이제 이 두 Series를 사용하여 기본적인 산술 연산을 해보겠습니다. 각 과일의 총 가격을 계산해보겠습니다.

```python

# 과일별 총 가격 계산

total_cost = prices * quantities

print("Total cost per fruit:\n", total_cost)

```

    Total cost per fruit:

     apple         3000

    banana        4000

    strawberry    7500

    dtype: int64

- 이 코드는 'prices'와 'quantities' Series를 곱하여 각 과일의 총 가격을 계산합니다.

- 연산은 동일한 Index를 가진 요소 간에 이루어졌음을 알 수 있습니다.

- 이제 실제 산술연산의 다양한 적용 예시를 살펴보겠습니다.

## 산술연산

- Series간의 산술연산은 각 Index에 해당하는 값 끼리 수행됩니다.

- 기본적인 연산은 사칙연산이 있습니다.

- 앞서 생성한 price와 quantiles 로 사칙연산의 예시를 작성해보겠습니다.

```python

# 과일 가격에 10% 할인 적용

discounted_prices = prices * 0.9

print("Discounted Prices:\n", discounted_prices)

```

    Discounted Prices:

     apple          900.0

    banana        1800.0

    strawberry    1350.0

    dtype: float64

- 이 코드는 각 과일의 가격에 10% 할인을 적용한 결과를 보여줍니다.

- 할인된 가격은 기존 가격에 0.9를 곱하여 계산된 것입니다.

- 위의 예제는 Index가 서로 일치하는 Series간의 연산입니다. 하지만 Series간 Index가 서로 일치하지 않는 경우는 어떻게 되는걸까요?

## Index가 일치하지 않는 Series간의 연산

- Pandas에서 두 Series를 연산할 때, Index가 완전히 일치하지 않는 경우가 있습니다.

- 이 경우, 일치하지 않는 Index에 대해서는 결과가 NaN(결측치) 로 표시됩니다.

- 이러한 상황은 데이터 누락, 실수로 Index가 잘못된 지정된 경우 종종 발생합니다.

- 기존 과일에 새로운 과일을 추가해서 Series의 Index가 일치하지 않는 경우에 대한 연산 결과와 처리 방법을 정리해보겠습니다.

```python

# 새로운 과일 추가

new_quantities = pd.Series([1, 2, 3, 4], index=['apple', 'banana', 'strawberry', 'kiwi'])

# 새로운 수량과 기존 가격의 곱셈 시도

total_cost_with_new = prices * new_quantities

print("Total cost with new fruits:\n", total_cost_with_new)

```

    Total cost with new fruits:

     apple         1000.0

    banana        4000.0

    kiwi             NaN

    strawberry    4500.0

    dtype: float64

- 새로운 과일인 kiwi를 추가하여 quanties의 Index가 기존보다 한개 늘어나서 price와 Index 길이가 불일치하게 됩니다.

- 그리고 결과를 보면 kiwi의 가격이 입력되어야 할 부분에는 NaN값이 출력된 것을 볼 수 있습니다.

- 이처럼 **Series에서 Index가 일치하지 않는 데이터간의 연산은 NaN 값으로 표시** 됩니다.

## Series에서의 NaN값 처리하기

- 위와 같이 Index가 pair하지 않아서 발생하는 NaN값은 데이터 분석과정에서 문제가 될 수 있으므로 적절히 처리할 필요가 있습니다.

- Pandas에서는 주로 `dropna()` 를 사용해서 NaN값을 가진 행 그 자체를 일괄삭제하거나, `fillna()`를 사용해서 특정 값으로 대체할 수 있습니다.

```python

# NaN 값 제거

total_cost_no_nan = total_cost_with_new.dropna()

print("Total cost without NaN:\n", total_cost_no_nan)

# NaN 값을 0으로 대체

total_cost_filled = total_cost_with_new.fillna(0)

print("Total cost with NaN replaced by 0:\n", total_cost_filled)

```

    Total cost without NaN:

     apple         1000.0

    banana        4000.0

    strawberry    4500.0

    dtype: float64

    Total cost with NaN replaced by 0:

     apple         1000.0

    banana        4000.0

    kiwi             0.0

    strawberry    4500.0

    dtype: float64

## Series 데이터의 정렬

- Pandas의 Series데이터는 객체를 값이나 Index를 기준으로해서 정렬할 수 있습니다.

### 값 기준으로 Series 데이터 정렬하기 : sort_values()

- sort_values() 는 Series의 데이터를 값에 따라 정렬하는데 사용됩니다.

- 주요 옵션은 아래와 같습니다.

    - ascending : 정렬순서 결정. True는 오름차순(기본값), False는 내림차순입니다.

    - inplace : 정렬결과를 기존 Series에 바로 적용할지 여부를 결정합니다. True이면 기존 Series가 변경되고 False(기본값)이면 새 Series가 반환됩니다.

    - na_position : 결측치의 위치를 결정합니다. `first`면 결측치가 Series의 맨 앞에 위치하고, last(기본값) 면 결측치가 맨 마지막에 위치합니다.

```python

# 가격을 오름차순으로 정렬

sorted_prices = prices.sort_values()

print("Prices sorted in ascending order:\n", sorted_prices)

# 가격을 내림차순으로 정렬

sorted_prices_desc = prices.sort_values(ascending=False)

print("Prices sorted in descending order:\n", sorted_prices_desc)

```

    Prices sorted in ascending order:

     apple         1000

    strawberry    1500

    banana        2000

    dtype: int64

    Prices sorted in descending order:

     banana        2000

    strawberry    1500

    apple         1000

    dtype: int64

```python

# 가격을 내림차순으로 정렬, 결측치는 먼저 나오도록 설정

sorted_prices_desc = total_cost_with_new.sort_values(ascending=False, na_position='first')

print("Prices sorted in descending order with NaNs first:\n", sorted_prices_desc)

```

    Prices sorted in descending order with NaNs first:

     kiwi             NaN

    strawberry    4500.0

    banana        4000.0

    apple         1000.0

    dtype: float64

- 위에서 만들었던 total_cost_with_new의 NaN값이 가장 먼저 출력되는 것을 볼 수 있습니다. (가격은 내림차순)

### Index 기준으로 Series 데이터 정렬하기 : sort_index()

- Series의 Index를 기준으로도 데이터를 정렬할 수 있습니다.

- sort_index도 sor_values() 처럼 ascending과 inplace 옵션을 가지고 있으며 사용법이 동일합니다.

```python

# Index를 오름차순으로 정렬

sorted_by_index = prices.sort_index()

print("Prices sorted by index in ascending order:\n", sorted_by_index)

# Index를 내림차순으로 정렬

sorted_by_index_desc = prices.sort_index(ascending=False)

print("Prices sorted by index in descending order:\n", sorted_by_index_desc)

```

    Prices sorted by index in ascending order:

     apple         1000

    banana        2000

    strawberry    1500

    dtype: int64

    Prices sorted by index in descending order:

     strawberry    1500

    banana        2000

    apple         1000

    dtype: int64

## Series와  다른 데이터 구조간 상호작용

- Pandas의 Series는 다른 데이터 구조(리스트, 딕셔너리, 넘파이 배열 등)간의 변환과 상호작용이 가능합니다.

- 각 데이터 유형별로 이러한 예시를 소개합니다.

### Series와 리스트

- 리시즈 객체는 리스트로 변환될 수 있으며, 반대로 리스트로부터 Series를 생성할 수도 있습니다.

```python

# Series를 리스트로 변환

prices_list = prices.tolist()

print("Series to List:", prices_list)

# 리스트를 Series로 변환

list_to_series = pd.Series(prices_list)

print("List to Series:\n", list_to_series)

```

    Series to List: [1000, 2000, 1500]

    List to Series:

     0    1000

    1    2000

    2    1500

    dtype: int64

### Series와 딕셔너리

- 리스트와 마찬가지로 딕셔너리도 Series와 상호간 변환이 가능합니다.

```python

# Series를 딕셔너리로 변환

prices_dict = prices.to_dict()

print("Series to Dictionary:", prices_dict)

# 딕셔너리를 Series로 변환

dict_to_series = pd.Series(prices_dict)

print("Dictionary to Series:\n", dict_to_series)

```

    Series to Dictionary: {'apple': 1000, 'banana': 2000, 'strawberry': 1500}

    Dictionary to Series:

     apple         1000

    banana        2000

    strawberry    1500

    dtype: int64

### Series와 넘파이 배열

- 마찬가지로 넘파이 배열도 Series와 상호간 변환이 가능합니다.

```python

import numpy as np

# Series를 넘파이 배열로 변환

prices_array = prices.values

print("Series to Numpy Array:", prices_array)

# 넘파이 배열을 Series로 변환

array_to_series = pd.Series(prices_array)

print("Numpy Array to Series:\n", array_to_series)

```

    Series to Numpy Array: [1000 2000 1500]

    Numpy Array to Series:

     0    1000

    1    2000

    2    1500

    dtype: int64

- 이러한 유연한 상호작용은 데이터 전처리나 분석에서 유연성있게 데이터를 조회하고 다룰 수 있게 합니다.

- 경우에 따라 적절한 데이터 형태를 골라 변형하고 가공할 수 있기 때문입니다.

## Series 데이터의 고급 인덱싱(라벨기반 & 위치기반 인덱싱)

- Pandas의 Series에서는 `.loc[]`를 통해 라벨 기반의 인덱싱을 할 수 잇습니다.

- 즉 Index의 값(라벨)을 기준으로 데이터를 선택할 수 있습니다.

- 이 기능을 통해 Series 데이터의 슬라이싱, 단일 라벨 선택, 라벨 리스트 선택(슬라이싱)등 다양한 데이터접근이 가능합니다.

### 라벨기반 인덱싱 : loc

```python

# 단일 라벨 선택

apple_price = prices.loc['apple']

print("Price of apple:", apple_price)

# 라벨 슬라이스

slice_prices = prices.loc['apple':'banana']

print("Slice from apple to banana:\n", slice_prices)

```

    Price of apple: 1000

    Slice from apple to banana:

     apple     1000

    banana    2000

    dtype: int64

### 위치기반 인덱싱 : iloc

- iloc은 위치기반 인덱싱으로 정수의 위치를 기준으로 데이터를 선택합니다.

- 정수 Index에서만 사용가능하며, loc와 마찬가지로 다양한 방식으로 데이터에 접근할 수 있습니다.

```python

# 정수 위치를 사용한 선택

second_item = prices.iloc[1]

print("Second item in the series:", second_item)

# 위치 기반 슬라이스

slice_by_position = prices.iloc[0:2]

print("Slice of the first two items:\n", slice_by_position)

```

    Second item in the series: 2000

    Slice of the first two items:

     apple     1000

    banana    2000

    dtype: int64

### 다중 Index(Multiindex) 사용

- Series에서는 다중 Index(멀티 Index)를 사용해 좀 더 복잡한 데이터 구조를 다룰 수도 있습니다.

- 다중 Index는 하나의 축에 여러 레벨의 Index를 가지도록 해주는 기능입니다.

- 이러한 다중 Index는 복잡한 데이터 구조를 효율적으로 표현하고 조작할 수 있게 합니다.

- 다중 Index를 사용하면 각 레벨별로 서브셋(subset)을 선택하거나, 더 상세한 데이터를 선택해 가공, 분석할 수 있습니다.

```python

# 다중 Index 생성

multi_index_series = pd.Series([10, 20, 30], index=[['fruit', 'fruit', 'vegetable'], ['apple', 'banana', 'carrot']])

print("Multi-index Series:\n", multi_index_series)

# 첫 번째 레벨(과일, 채소)에 접근

fruit_prices = multi_index_series.loc['fruit']

print("Prices of fruits:\n", fruit_prices)

# 두 번째 레벨(특정 과일)에 접근

apple_price = multi_index_series.loc['fruit', 'apple']

print("Price of apple:", apple_price)

```

    Multi-index Series:

     fruit      apple     10

               banana    20

    vegetable  carrot    30

    dtype: int64

    Prices of fruits:

     apple     10

    banana    20

    dtype: int64

    Price of apple: 10

- 위와 같이 다중Index를 통해 데이터를 카테고리별로 그룹화할 수 있습니다.

- 또한, 각 그룹 내에서 세부적인 데이터 접근을 할 수도 있습니다.
