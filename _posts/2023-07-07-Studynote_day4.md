---
layout : single
title:  "[스터디노트] Day4 파이썬 기초"
categories: [AIFFEL_7th_Bootcamp, Python Programming, Study Note]
tag: 스터디노트
header :
    teaser : "/assets/img/studynote/studynote_day4.png"
---


# 💡공부한 내용

---

- **산술연산자(곱셉과 나눗셈)**
- **산술 연산자(나머지와 몫)**
- **산술연산자(거듭제곱)**
- **복합연산자**

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **산술연산자(곱셉과 나눗셈)**: 곱셉과 나눗셈은 기본적인 수학 연산으로 다양한 문제 해결에 활용된다.
    
    예제 코드:
    
    ```python
    num1 = 6
    num2 = 3
    multiplication = num1 * num2  # 곱셈
    division = num1 / num2  # 나눗셈
    
    print("곱셈 결과:", multiplication)
    print("나눗셈 결과:", division)
    ```
    
- **산술 연산자(나머지와 몫)**: 나머지와 몫을 구하는 연산자는 특별한 계산이 필요할 때 유용하다.
    
    예제 코드:
    
    ```python
    num1 = 7
    num2 = 3
    remainder = num1 % num2  # 나머지
    quotient = num1 // num2  # 몫
    
    print("나머지:", remainder)
    print("몫:", quotient)
    ```
    
- **산술연산자(거듭제곱)**: 거듭제곱 연산자는 숫자의 제곱을 계산할 때 사용된다.
    
    예제 코드:
    
    ```python
    base = 2
    exponent = 3
    power = base ** exponent  # 거듭제곱
    
    print("거듭제곱 결과:", power)
    ```
    
- **복합연산자**: 복합연산자는 연산과 할당을 한 번에 수행하여 코드를 간결하게 만든다.
    
    예제 코드:
    
    ```python
    num = 5
    num += 3  # num = num + 3과 동일
    num *= 2  # num = num * 2와 동일
    
    print("최종 결과:", num)
    ```
    

# ✍️ 오늘의 혼잣말

---

- 다양한 연산자들을 학습하며 프로그래밍에서 수학을 어떻게 적용하는지를 정리했다.
- 복합연산자는 코드를 더욱 간결하고 명료하게 만드는 좋은 방법이라고 한다.
    - 근데 솔직히 가끔은 `직관적으로 보자마자 이해가 되는 코드`가 더 좋은 코드 아닐까? 싶을 때가 있다.
    - num +=3 은 num이라는 변수에 3이라는 int 형태의 데이터를 ‘+’한다. 인데, 복합연산자를 보면서 결국은 다시 치환해서 생각을 해야 하니까?!
    - 라는 흔한 문과생의 푸념이었다 🤣