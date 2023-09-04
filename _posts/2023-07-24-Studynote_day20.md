---
layout : single
title:  "[스터디노트] Day20 자료구조/알고리즘"
categories: [ds19_Bootcamp, 자료구조/알고리즘, Study Note]
tag: 스터디노트
header :
    teaser : "/assets/img/studynote/studynote_day20.png"
---


# 💡공부한 내용

---

- 선형검색 알고리즘
- 이진검색 알고리즘
- 순위 알고리즘

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

### 선형검색

- **개념과 필요성**: 데이터의 처음부터 끝까지 순서대로 검색하여 원하는 값을 찾는 방법. 정렬되지 않은 데이터에서 주로 사용됨.
- **예제 코드**:

```python
def linear_search(data, target):
    # 찾고자 하는 대상이 있는 인덱스를 담을 리스트 생성
    result = [i for i in range(len(data)) if data[i] == target]
    # 결과가 있으면 해당 인덱스 반환
    if result:
        return f"{target}을(를) 찾은 인덱스: {result}"
    # 결과가 없으면 해당 내용 반환
    return f"{target}은(는) 리스트 내에 없습니다."
```

### 이진검색

- **개념과 필요성**: 정렬된 데이터에서 중간 값과 찾으려는 값을 비교하며 검색하는 방법. 검색 속도가 빠르므로 큰 데이터에서 효율적.
- **예제 코드**:

```python
def binary_search(data, target):
    low = 0                  # 검색 범위의 최소 인덱스
    high = len(data) - 1     # 검색 범위의 최대 인덱스
    while low <= high:
        mid = (low + high) // 2  # 중앙 인덱스 계산
        if data[mid] == target:  # 중앙 값이 타겟과 일치하면 인덱스 반환
            return f"{target}은(는) 인덱스 {mid}에 위치하고 있습니다."
        elif data[mid] < target: # 중앙 값이 타겟보다 작으면 범위를 오른쪽으로 조정
            low = mid + 1
        else:                    # 중앙 값이 타겟보다 크면 범위를 왼쪽으로 조정
            high = mid - 1
    return f"{target}은(는) 리스트 내에 없습니다." # 타겟을 찾지 못하면 해당 내용 반환
```

### 순위

- **개념과 필요성**: 데이터 내의 요소가 어떤 기준에 따라 어떠한 순위를 가지는지를 결정. 성적이나 점수 등을 기준으로 순위를 매기는 경우에 활용.
- **예제 코드**:

```python
import pandas as pd

def rank(data):
    rank_list = [0] * len(data)     # 순위를 담을 리스트 초기화
    for i in range(len(data)):     # 각 값에 대해
        # 현재 값보다 작은 값의 개수를 세고 +1 하여 순위를 계산
        rank_list[i] = sum(x < data[i] for x in data) + 1
    # DataFrame을 생성하여 값과 순위를 함께 반환
    df = pd.DataFrame({'값': data, '순위': rank_list})
    return df
```

# ✍️ 오늘의 혼잣말

---

- 오늘은 파이썬으로 선형검색, 이진검색, 순위를 구현해보면서 이론과 실습을 병행해봤다.
- 알고리즘 파트는 수학에 이어서 참 어려운 부분이다. 내용만 볼때는 이해가 쉽고 할 수 있을 것 같은데, 막상 어딘가에 적용하려고 하면 좀 쉽지 않다.
- 요는 개념을 이해하고, 그것을 어디에 어떻게 적용할지 아는 것. 매번 노트 쓸때마다 강조하지만 ‘개념’ 이 제일 중요한 파트인것 같다.