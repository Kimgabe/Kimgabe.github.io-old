---
layout : single
title:  "[스터디노트] Day16 기초수학"
categories: studynote
toc: true
highlight: false
header:
  teaser: /assets/images/unsplash/study_note.jpg
  overlay_image: /assets/images/unsplash/study_note.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/842ofHC6MaI)"
tags:
  - 조합
  - Combination
  - 확률
  - Probability
---


# 💡공부한 내용

---

- 조합
- 조합(파이썬)
- 확률
- 확률(파이썬)

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **조합**
    - 주어진 집합에서 일부 요소를 선택하는 경우의 수를 '조합'이라고 하며, 순서는 고려하지 않는 것이 순열과의 차이 특징이며 다음과 같이 수식으로 표현합니다.  $nCr = \frac{n!}{r!(n-r)!}$
    - 사용예시 : 5명의 사람 중에서 3명을 선택하는 경우의 수는 $5C3 = \frac{5!}{3!(5-3)!}$으로 계산
- **조합(파이썬)**
    - **내장 함수 사용:** 파이썬에서는 math 모듈의 **`comb`** 함수를 사용하여 조합을 계산할 수 있습니다.
    
    ```python
    # 내장함수로 구현
    import math
    print(math.comb(5, 3))  # 결과: 10
    
    # 사용자 정의 함수로 구현
    def combination(n, r):
        return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    
    print(combination(5, 3))  # 결과: 10.0
    ```
    
- **확률**
    - **정의:** 어떤 사건(event)가 일어날 가능성을 수치로 나타낸 것. 보통 특정 사건의 경우의 수를 전체 경우의 수로 나눠서 표현하며 수식으로 표현하면 $P(E) = \frac{n(E)}{n(S)}$ 입니다.
    - 사용예시**:** 주사위를 던졌을 때 6이 나올 확률은 $P(6) = \frac{1}{6}$ 입니다.
- **확률(파이썬)**
    - **확률 계산:** 파이썬에서는 확률을 계산하기 위해 직접 수식을 사용합니다.
    
    ```python
    P_6 = 1/6
    print(P_6)  # 결과: 0.16666666666666666
    ```
    

# ✍️ 오늘의 혼잣말

---

- 순열과 조합을 잘 구분해서 개념정의를 하고, 각각 어떤식으로 활용할수 있는지에 대한 이해를 하는게 필요해 보인다.