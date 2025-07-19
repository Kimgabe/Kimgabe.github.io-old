---
title: "[파이썬 기초] 11. Numpy_numpy로 로또번호 자동 생성기 만들기"
cover: "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=1920&h=1080&fit=crop"
date: 2021-07-14
categories:
  - [personal-study, numpy]
tags:
  - python
  - 로또 번호 자동생성기
toc: true
---
그동안 정리한 numpy이론을 활용해 로또번호 자동생성기를 함수로 구현하는 방법을 정리합니다.

# 로또 번호 자동 생성기(함수로)를 만드시오

  - 로또는 1 ~ 45 사이의 숫자에서 6개를 random으로 뽑는다. (중복 허용X)

  - 몬테 카를로 방법을 이용하여 구현할 수 있다.

```python
import numpy as np
```

```python

np.random.choice(list, size 명시, 복원/비복원 옵션)

````

```python
def generate_lotto_nums():
    return np.random.choice(np.arange(1, 46), size=6, replace=False) # 비복원 추출 (중복 X)
```

그냥 함수를 반복하면 비복원이기 때문에 매번 실행할때마다 값이 바뀐다.

```python
generate_lotto_nums()
```


array([30, 45, 39,  4,  2, 42])


```python
generate_lotto_nums()
```


array([25, 35,  6,  3, 17,  5])

복원 추출도 함수 실행시 마다 값이 달라지지만, 동일한 값이 나올 수도 있다. 

```python
def generate_lotto_nums2():
    return np.random.choice(np.arange(1, 46), size=6, replace=True) # 복원 추출 (중복 O)
```

```python
generate_lotto_nums2()
```


array([43, 40, 27, 31, 37, 32])


```python
generate_lotto_nums2()
```


array([29,  5, 19, 29, 24, 22])
