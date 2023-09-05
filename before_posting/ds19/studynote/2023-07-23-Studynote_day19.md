---
layout : single
title:  "[스터디노트] Day19 자료구조/알고리즘"
categories: studynote
toc: true
highlight: false
header:
  teaser: /assets/images/unsplash/study_note.jpg
  overlay_image: /assets/images/unsplash/study_note.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/842ofHC6MaI)"
tags:
  - 튜플 아이템 정렬
  - Tuple Item Sorting
  - 튜플과 for문
  - Tuples and for Loops
  - 튜플과 while문
  - Tuples and while Loops
  - 딕셔너리
  - Dictionary
  - 딕셔너리 조회
  - Dictionary Lookup
  - 딕셔너리 추가
  - Adding to Dictionary
  - 딕셔너리 생성
  - Dictionary Creation
  - 딕셔너리 수정
  - Dictionary Modification
  - keys()와 values()
  - keys() and values()
  - 딕셔너리 삭제
  - Dictionary Deletion
  - 딕셔너리 유용한 기능
  - in
  - len()
  - clear()
  - Useful Dictionary Functions
---


# 💡공부한 내용

---

- **튜플 아이템 정렬:** 튜플 내의 아이템 정렬 방법
- **튜플과 for문:** for문을 이용한 튜플 순회
- **튜플과 while문:** while문을 이용한 튜플 순회
- **딕셔너리:** 파이썬의 딕셔너리 자료구조
- **딕셔너리 조회:** 딕셔너리 내용 조회 방법
- **딕셔너리 추가:** 딕셔너리에 새로운 요소 추가 방법
- **딕셔너리 생성:** 새로운 딕셔너리 생성 방법
- **딕셔너리 수정:** 딕셔너리 내용 수정 방법
- **keys()와 values():** 딕셔너리의 키와 값 조회
- **딕셔너리 삭제:** 딕셔너리 아이템 삭제 방법
- **딕셔너리 유용한 기능(in, len(), clear()):** 다양한 딕셔너리 관련 유용한 기능

<aside>
📌 자료구조문제풀이는 17일차 기초수학 문제 풀이와 같이 풀이하여 정리

</aside>

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **튜플 아이템 정렬:** 튜플은 불변(immutable)하므로 정렬을 위해 잠시 리스트로 변환해야 함.
    
    ```python
    my_tuple = (4, 2, 5)
    sorted_tuple = tuple(sorted(my_tuple))
    ```
    
- **튜플과 for문 : 튜플도 리스트 처럼 순회 가능. `for`**와 **`while`** 문 모두 사용 가능.
    
    ```python
    my_tuple = (1, 2, 3, 4, 5)
    
    for item in my_tuple:
        print(item)  # 1, 2, 3, 4, 5가 차례로 출력
    ```
    
- 튜플과 **while문:** 튜플도 리스트처럼 순회 가능. **`for`**와 **`while`** 문 모두 사용 가능.
    
    ```python
    my_tuple = (1, 2, 3, 4, 5)
    index = 0
    
    while index < len(my_tuple):
        print(my_tuple[index])  # 1, 2, 3, 4, 5가 차례로 출력
        index += 1
    ```
    
- **딕셔너리:** 키와 값을 쌍으로 가지는 자료구조. 생성, 조회, 추가, 수정, 삭제 등 다양한 연산 가능.
    
    ```python
    my_dict = {'name': 'John', 'age': 30}
    ```
    
- **딕셔너리 조회/추가/수정:** 딕셔너리 내의 특정 키값 조회, 새로운 키와 값을 추가, 기존 키의 값을 수정.
    
    ```python
    # 조회
    print(my_dict['name'])  # John
    
    # 추가
    my_dict['city'] = 'New York'
    
    # 수정
    my_dict['age'] = 31
    ```
    
- **keys()와 values():** 딕셔너리의 모든 키와 값 조회.
    
    ```python
    print(my_dict.keys())   # dict_keys(['name', 'age', 'city'])
    print(my_dict.values()) # dict_values(['John', 31, 'New York'])
    ```
    
- **딕셔너리 삭제/유용한 기능:** 특정 키의 쌍을 삭제하거나, 특정 키가 있는지 확인, 길이 조회 등.
    
    ```python
    # 삭제
    del my_dict['city']
    
    # 키 확인
    print('name' in my_dict)  # True
    
    # 길이 조회
    print(len(my_dict))       # 2
    
    # 모든 아이템 삭제
    my_dict.clear()
    ```
    

---

<aside>
💡 배운 개념을 응용한 예제 문제

</aside>

### 1. 학생 이름과 성적을 출력하는 프로그램 만들기

- 학생 이름과 성적을 딕셔너리로 관리

```python
students_scores = {
    '김철수': 85,
    '이영희': 92,
    '박지민': 76,
    '최민수': 90,
    '장현지': 95
}
```

- 학생들의 성적을 내림차순으로 정렬하고 상위 3명의 이름과 성적을 작성하는 프로그램 만들기

```python
# 학생의 성적을 튜플의 리스트로 변환
scores_list = [(name, score) for name, score in students_scores.items()]

# 성적을 기준으로 내림차순 정렬
sorted_scores = sorted(scores_list, key=lambda x: x[1], reverse=True)

# 상위 3명의 이름과 성적을 출력
for i in range(3):
    print(f'{sorted_scores[i][0]}: {sorted_scores[i][1]}점')
```

# ✍️ 오늘의 혼잣말

---

- 복습을 하면서 튜플과 딕셔너리에 대한 이해를 얻을 수 있었다. 특히 딕셔너리의 다양한 메서드와 튜플의 불변성 등을 항상 염두하고 코드에 활용해야 한다.
- 이 때문인지 실제 프로젝트하거나 일할때 수정이 손쉬운 리스트를 많이 활용했던 것 같다.
- 앞으로는 딕셔너리 기능들을 어떻게 활용할지 더 깊게 고민해봐야 될 것 같다.