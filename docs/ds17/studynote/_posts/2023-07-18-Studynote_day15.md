---
layout : single
title:  "[스터디노트] Day15 기초수학"
categories: studynote
toc: true
highlight: false
header:
  teaser: /assets/images/unsplash/study_note.jpg
  overlay_image: /assets/images/unsplash/study_note.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/842ofHC6MaI)"
tags:
  - 시그마
  - Summation (Sigma)
  - 계차수열
  - Recursive Sequence
  - 피보나치 수열
  - Fibonacci Sequence
  - 팩토리얼
  - Factorial
  - 군 수열
  - Arithmetic Sequence
  - 순열
  - Permutation
---

# 💡공부한 내용

---

- 시그마
- 계차수열
- 계차수열(파이썬)
- 피보나치 수열
- 팩토리얼
- 군 수열
- 군 수열(파이썬)
- 순열
- 순열(파이썬)

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **시그마(Σ, Sigma)** : 시그마는 수학에서 수열의 합을 나타내는 기호 특정 수열의 항을 모두 더하는 연산을 간략하게 표현할 수 있으며  $\sum_{i=1}^{n} i$ 형태로 표현.
    - 여기서 i는 시작값, n은 끝값을 의미
- **계차수열**: 수열에서 연속되는 두 항의 차이가 일정한 수열을 의미합니다. 일반항으로 표현하면 $a_n = a_{n-1} + d$ 형태가 되며, 이때 d는 공차를 의미
- **계차수열(파이썬)**:
    
    ```python
    # 내장 함수로 구현
    sequence = [a + d * i for i in range(n)] # a는 초기값, d는 공차, n은 항의 개수
    
    # 함수생성 버전
    def arithmetic_sequence(a, d, n):
        return [a + d * i for i in range(n)]
    ```
    
- **피보나치 수열**: 피보나치 수열은 각 항이 바로 앞의 두 항의 합으로 이루어진 수열입니다. 첫 번째와 두 번째 항을 1로 두고, 세 번째 항부터 이전 두 항의 합으로 계산됩니다. 수식으로 표현하면 $F(n) = F(n-1) + F(n-2)$ 로 나타낼 수 있으며, 최종 수식은  $F(1) = F(2) = 1$ 입니다.
- **팩토리얼**: 팩토리얼은 양의 정수 n에 대해 1부터 n까지의 정수를 모두 곱한 값을 의미합니다. 수식으로는 $n! = 1 \times 2 \times \ldots \times n$ 로 표현
- **군 수열**: 군 수열은 여러 개의 수열이 모여 하나의 큰 수열을 이루는 형태를 의미합니다. 군은 특정한 규칙에 따라 수열의 항을 구성하며, 각 군 내에서의 수열의 형태는 동일
- **군 수열(파이썬)**:
    
    ```python
    # 내장 함수로 구현
    group_sequence = [n**2 for n in range(10)] # 제곱 규칙의 군 수열
    
    # 함수생성 버전
    def group_sequence(n):
        return [i**2 for i in range(n)]
    ```
    
- **순열**: 순열은 n개의 원소 중 r개를 중복없이 나열하는 것을 의미합니다. 순열의 개수는 $nPr = \frac{n!}{(n - r)!}$ 로 계산할 수 있으며, 원소의 순서가 결과에 영향을 미칩니다.
- **순열(파이썬)**:
    
    ```python
    # 내장 함수로 구현
    from itertools import permutations
    perm = permutations([1, 2, 3]) # 1, 2, 3의 모든 순열
    
    # 함수생성 버전
    def get_permutations(arr):
        from itertools import permutations
        return permutations(arr)
    ```
    

# ✍️ 오늘의 혼잣말

---

- 수학은 어제도 생각했지만 끝이 없는 부분이다. 개념을 이해하고 어디에 어떻게 적용할지 고민을 계속 해봐야 한다.
- 특히 나는 데이터 분석/사이언티스트를 목표로 하고 있기 때문에 어떤 수치 데이터들을 어떻게 활용해서 분석할 수 있을지 고민해야 한다.