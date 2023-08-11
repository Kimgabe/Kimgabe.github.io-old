---
layout : single
title:  "[스터디노트] Day13 기초수학"
categories: studynote
toc: true
highlight: false
header:
  teaser: /assets/images/unsplash/study_note.jpg
  overlay_image: /assets/images/unsplash/study_note.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/842ofHC6MaI)"
tags:
  - 약수와 소수
  - Divisors and Primes
  - 약수와 소수(파이썬)
  - Divisors and Primes 
  - 소인수와 소인수분해
  - Prime Factors and Prime Factorization
  - 소인수와 소인수분해(파이썬)
  - Prime Factors and Prime Factorization 
  - 최대공약수
  - Greatest Common Divisor
  - 최대공약수(파이썬)
  - Greatest Common Divisor 
  - 최소공배수
  - Least Common Multiple
  - 최소공배수(파이썬)
  - Least Common Multiple 
  - 진법
  - Number Bases
  - 진법(파이썬)
  - Number Bases 
  - 수열
  - Sequences
  - 등차수열
  - Arithmetic Sequences
  - 등차수열(파이썬)
  - Arithmetic Sequences 
---

# 💡공부한 내용

---

- 약수와 소수: 수학적 개념 이해
- 약수와 소수(파이썬): 파이썬을 이용한 구현 방법
- 소인수와 소인수분해: 수학적 개념 이해
- 소인수와 소인수분해(파이썬): 파이썬을 이용한 구현 방법
- 최대공약수: 수학적 개념 이해
- 최대공약수(파이썬): 파이썬을 이용한 구현 방법
- 최소공배수: 수학적 개념 이해
- 최소공배수(파이썬): 파이썬을 이용한 구현 방법
- 진법: 수학적 개념 이해
- 진법(파이썬): 파이썬을 이용한 진법 변환 방법
- 수열
- 등차수열
- 등차수열(파이썬)

<aside>
📌 파이썬 중급 문제풀이는 12일차 스터디 노트에 별도로 정리

</aside>

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **약수와 소수**: 약수는 어떤 수를 나누어 떨어지게 하는 수, 소수는 1과 자기 자신만이 약수인 1보다 큰 자연수를 말한다.
    - **파이썬으로 약수 구하기**
    
    ```python
    def find_divisors(n):
    		# %는 나머지 연산자로, n을 i로 나눈 나머지가 0이면 약수
        return [i for i in range(1, n+1) if n % i == 0] 
    ```
    
    - **파이썬으로 소수 판별하기**
    
    ```python
    def is_prime(n):
        if n < 2:
            return False # 1은 소수가 아님
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: # %는 나머지 연산자로, 나머지가 0이면 소수가 아님
                return False 
        return True
    ```
    
- **소인수와 소인수분해**: 소인수는 소수이면서 약수인 수. 소인수분해는 어떤 수를 소인수의 곱으로 표현하는 것.
    - **파이썬으로 소인수분해하기**
    
    ```python
    def prime_factors(n):
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0: # %는 나머지 연산자로, 나머지가 0이면 소인수
                factors.append(divisor) # 나머지가 0이면 factor list에 입력
                n //= divisor # //=는 나누고 몫을 변수에 할당하는 코드
            divisor += 1
        return factors
    ```
    
- **최대공약수와 최소공배수**: 두 수의 공통된 약수 중 가장 큰 수가 최대공약수, 두 수의 공통된 배수 중 가장 작은 수가 최소공배수.
    - **파이썬으로 최대공약수 구하기**
    
    ```python
    import math
    
    # 내장함수 사용
    def gcd_lcm(a, b):
        return math.gcd(a, b), (a * b) // math.gcd(a, b) # 최대공약수와 최소공배수
    
    # 내장함수를 사용하지 않은 버전
    def gcd_lcm_manual(a, b):
        gcd = a
        lcm = b
        while b != 0:
            a, b = b, a % b
            gcd = a
        lcm *= gcd // math.gcd(a, lcm)
        return gcd, lcm
    ```
    
    - **파이썬으로 최소공배수 구하기**
    
    ```python
    def lcm(x, y):
        return x * y // math.gcd(x, y) # 최소공배수는 두 수의 곱을 최대공약수로 나눈 값
    lcm_value = lcm(48, 18)
    ```
    
- **진법**: 자릿수를 표현하기 위해 사용하는 기수(예: 10진법, 2진법).
    - **파이썬으로 진법 변환하기**
    
    ```python
    # 내장함수 사용
    binary_number = bin(10)  # bin은 2진법으로 변환하는 내장함수, '0b1010'
    octal_number = oct(10)   # oct은 8진법으로 변환하는 내장함수, '0o12'
    hexadecimal_number = hex(10) # hex는 16진법으로 변환하는 내장함수, '0xa'
    
    # 내장함수를 사용하지 않은 버전
    def convert_base(num, base):
        result = ''
        while num > 0:
            result = str(num % base) + result
            num = num // base
        return result
    ```
    
- 수**열, 등차수열**:
    - **파이썬으로 등차수열 만들기**
    
    ```python
    # 등차수열 생성 함수
    def arithmetic_sequence(n, a, d):
        return [a + d * i for i in range(n)] # 첫 항부터 n개의 항까지 등차수열 생성
    ```
    

# ✍️ 오늘의 혼잣말

---

- 수학적 개념은 실제 코드를 작성하고 사용하려면 필수적으로 알아야 하는 개념으로 사용방법을 잘 알아둬야 함.
- 지금까지 업무를 하면서나 프로젝트를 하면서는 적극 활용하지는 못했지만, 개념적으로 알고 응용할 준비가 되어 있어야 상황이 왔을때 사용할 수 있을 것 같다.