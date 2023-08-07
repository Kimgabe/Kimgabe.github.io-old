---
layout : single
title:  "[스터디노트] Day21 자료구조/알고리즘"
categories: [DS17_Bootcamp, 자료구조/알고리즘]
tag: 스터디노트
header :
    teaser : "/assets/img/studynote/studynote_day21.png"
---


# 💡공부한 내용

---

- **버블 정렬** 알고리즘
- **삽입 정렬** 알고리즘
- **선택 정렬** 알고리즘
- **최댓값** 알고리즘

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **버블 정렬**
    - **정의:** 인접한 두 원소를 비교하여 정렬하는 방법. 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘.
    - **필요성:** 사람들의 키 순서대로 줄 세우기 등 실생활에서 자주 사용됨.
    
    ```python
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n): # 전체 배열을 순회
            for j in range(0, n-i-1): # 마지막에 정렬된 원소를 제외하고 순회
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]  # 인접한 두 원소 비교 후 교환
    ```
    
- **삽입 정렬**
    - **정의:** 각 숫자를 이미 정렬된 부분 배열에 적절한 위치에 삽입하여 정렬하는 방식.
    - **필요성:** 작은 데이터셋의 경우, 카드를 정렬할 때 사용하는 방식처럼 실생활에서도 적용 가능.
    
    ```python
    def insertion_sort(arr):
        for i in range(1, len(arr)): # 첫 원소는 정렬된 것으로 간주, 나머지를 순회
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j] # 원소를 오른쪽으로 이동
                j -= 1
            arr[j + 1] = key # 적절한 위치에 원소 삽입
    
    ```
    
- **선택 정렬**
    - **정의:** 전체 리스트에서 가장 작은 값을 찾아 첫 번째 위치와 교환하며 정렬하는 방법.
    - **필요성:** 학생들의 성적 순서대로 정리할 때 유용함.
    - **활용 방법:**
    
    ```python
    pythonCopy code
    def selection_sort(arr):
        for i in range(len(arr)): # 전체 배열 순회
            min_idx = i
            for j in range(i+1, len(arr)): # 현재 원소 다음부터 끝까지 순회
                if arr[min_idx] > arr[j]:
                    min_idx = j # 최소값 위치 저장
            arr[i], arr[min_idx] = arr[min_idx], arr[i] # 최소값을 앞으로 보냄
    ```
    
- **최댓값**
    - **정의:** 주어진 숫자 중에서 가장 큰 값을 찾는 연산.
    - **필요성:** 매출액이 가장 높은 제품을 찾는 등의 상황에서 활용 가능.
    
    ```python
    def find_max(arr):
        max_val = arr[0] # 첫 원소를 최댓값으로 가정
        for num in arr:
            if num > max_val:
                max_val = num # 더 큰 값이 있으면 갱신
        return max_val
    ```
    

# ✍️ 오늘의 혼잣말

---

- 알고리즘이라는 분야가 처음엔 매우 어려워 보였다. 그러나 실제로 코드로 구현하면서 조금은 이해가 되기 시작했다. 이러한 기본적인 정렬 알고리즘은 프로그래밍의 기본이자 복잡한 문제를 해결하는데 분명히 도움이 될 것이다.
- 몇일, 몇시간의 강의로 모든걸 마스터하긴 힘들겠지만 반복하면서 기초를 탄탄히 다지도록 노력해야겠다.