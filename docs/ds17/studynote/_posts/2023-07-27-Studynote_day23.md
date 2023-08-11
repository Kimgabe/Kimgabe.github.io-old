---
layout : single
title:  "[스터디노트] Day23 자료구조/알고리즘"
categories: studynote
header:
  teaser: /assets/images/unsplash/study_note.jpg
  overlay_image: /assets/images/unsplash/study_note.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/842ofHC6MaI)"
tags:
  - 하노이탑
  - Towers of Hanoi
  - 병합 정렬
  - Merge Sort
  - 퀵 정렬
  - Quick Sort
---


# 💡공부한 내용

---

- 하노이탑 (이론/실습)
- 병합 정렬 (이론/실습)
- 퀵 정렬 (이론/실습)

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **하노이탑**
    - **정의**: 세 개의 기둥을 활용하여 원판을 옮기는 퍼즐로, 작은 원판이 큰 원판 위에 올라가지 않도록 규칙이 있음
    - **핵심 내용**: 원판 n개를 옮기는 데 2^n - 1회의 이동이 필요하며, 재귀적인 방법으로 해결 가능
    - **예제 코드**:
        
        ```python
        def hanoi(n, from_pole, to_pole, aux_pole):
            if n == 1:
                print(from_pole, "->", to_pole)  # 원판 1개를 옮기는 경우
            else:
                hanoi(n-1, from_pole, aux_pole, to_pole)  # 중간 기둥을 이용하여 n-1개 원판 옮기기
                print(from_pole, "->", to_pole)          # 가장 큰 원판을 목표 기둥으로 옮기기
                hanoi(n-1, aux_pole, to_pole, from_pole)  # 중간 기둥의 n-1개 원판을 목표 기둥으로 옮기기
        ```
        
- **병합 정렬**
    - 데이터 리스트를 반으로 나눈후 각각 정렬하고, 다시 합치는 과정을 반복하는 정렬 방법
    - 병합정렬 작동 방식
        - 리스트를 반으로 나누고 가장 작은 단위로 최대한 쪼갠다.
        - 쪼개진 작은 단위 내에서 정렬을 한 뒤, 다시 병합한다.
        - 이때 병합하는 리스트간 정렬을 수행한다.
        - 이를 지속 반복해 최종 정렬을 한다.
        
        ```python
        def merge_sort(arr):
            if len(arr) <= 1: return arr # 길이가 1 이하면 반환
        
            mid = len(arr) // 2
            left = merge_sort(arr[:mid]) # 왼쪽 부분 리스트 정렬
            right = merge_sort(arr[mid:]) # 오른쪽 부분 리스트 정렬
        
            return merge(left, right) # 정렬된 부분 리스트 병합
        
        def merge(left, right):
            result = []
            while left and right:
                # 왼쪽과 오른쪽의 첫 원소를 비교해 작은 값 추가
                result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
            return result + left + right # 남은 원소들 추가
        ```
        
- **퀵 정렬**
    - 데이터 리스트에서 하나의 값을 선택하고, 그 값을 기준으로 큰 값과 작은 값을 나눈 뒤 정렬하는 방법
    - 퀵 정렬 작동 방식
        - 리스트에서 중앙 값을 기준(pivot)으로 설정한다.
        - 기준값과 리스트내의 다른 값들을 각각 비교해서 기준값 보다 작은 것은 왼쪽, 큰 것은 오른쪽으로 나눈다.
        - 나누어진 2개의 리스트를 각각 정렬한다.
        - 정렬된 리스트를 병합한다.
        
        ```python
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr # 길이가 1 이하면 반환
        
            pivot = arr[len(arr) // 2] # 중간 값 피벗으로 선택
            lesser_arr = [x for x in arr if x < pivot] # 피벗보다 작은 값 모음
            equal_arr = [x for x in arr if x == pivot] # 피벗과 같은 값 모음
            greater_arr = [x for x in arr if x > pivot] # 피벗보다 큰 값 모음
        
            # 작은 값, 같은 값, 큰 값 순으로 재귀적 정렬
            return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
        ```
        

# ✍️ 오늘의 혼잣말

---

- 어제 고민했던 재귀를 응용하는 문제인 하노이탑을 드디어 적용해봤다.
- 솔직히 재귀만 가지고 공부할때는 ‘큰 문제를 쪼갠다’ 라는게 잘 와닿지 않았는데 하노이탑에 재귀를 적용해보니 어떤 식으로 작용하는지가 조금 더 이해가 되는 것 같다.