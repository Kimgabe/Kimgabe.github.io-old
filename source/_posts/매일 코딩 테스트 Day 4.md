---
title: "[Programmers school] 코딩 기초 트레이닝 Day 4"
cover: "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=1920&h=1080&fit=crop"
date: 2023-09-10
categories:
  - [personal-study, coding-test]
tags:
  - n의 배수
  - 공배수
  - 홀짝에 따라 다른값 반환하기
  - 조건 문자열
  - flag에 따라 다른값 반환하기
toc: true
---
n의 배수, 공배수, 홀짝에 따라 다른값 반환하기, 조건 문자열, flag에 따라 다른값 반환하기
---


## 1. n의 배수


💡 문제설명



- 정수 `num`과 `n`이 매개 변수로 주어질 때, `num`이 `n`의 배수이면 1을 return `n`의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.


🔒 제한 사항



- 2 ≤ `num` ≤ 100
- 2 ≤ `n` ≤ 9


💡 입출력 예



| num | n | result |
| --- | --- | --- |
| 98 | 2 | 1 |
| 34 | 3 | 0 |

- 입출력 예 #1
    - 98은 2의 배수이므로 1을 return합니다.
- 입출력 예 #2
    - 32는 3의 배수가 아니므로 0을 return합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(num, n):
    answer = 0
    return answer
```


💭 문제 해석



- 나머지 개념을 응용한다면 쉽게 풀 수 있는 문제
- 특정 정수의 배수가 되는 경우는 해당 정수로 나눈 값이 0이되는 경우이다.


⚙ 문제 풀이 계획



- 조건문을 사용해서 `num % n` 이 0이면 숫자 1을 출력하고, 아닌 경우 0을 출력하도록 작성


⌨️ 입력한 코드(오답)



```python
def solution(num, n):
    if num % n == 0:
        answer = f"{num}은 {n}의 배수이므로 1을 return합니다."
    else:
        answer = f"{num}은 {n}의 배수가 아니므로 0을 return합니다."
    return answer
```


❓ 오답 원인



- 입출력 예에서 fstring을 활용한 ‘문장’ 을 출력하는 것이 답이라고 생각했는데, 실제 답은 경우에 따라 1인지 0인지만 출력하면 되는 것이었음
- `입출력 예` 에 제시된 표만 보면 되는데, `입출력 예 설명` 부분을 `출력값` 이라고 오해해서 오답 발생


⌨️ 입력한 코드 1



```python
def solution(num, n):
    if num % n == 0:
        answer = 1
    else:
        answer = 0
    return answer
```


❓ 개선방향



- 양자택일식의 간단한 조건문은 삼항연산자를 쓰면 더 간결한 코드로 풀어 낼 수 있음


✅ 제출한 답



```python
def solution(num, n):
    return 1 if num % n == 0 else 0
```


➡️ 실행결과



```python
테스트 1
입력값 〉	98, 2
기댓값 〉	1
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	34, 3
기댓값 〉	0
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 문제를 읽을때 `입출력 예` 를 더 중점적으로 볼 것
- 나머지의 개념과 조건문을 사용할 수 있다면 손쉽게 풀 수 있는 문제

---


## 2. 공배수


💡 문제설명



- 정수 `number`와 `n`, `m`이 주어집니다. `number`가 `n`의 배수이면서 `m`의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.


🔒 제한 사항



- 10 ≤ `number` ≤ 100
- 2 ≤ `n`, `m` 
💡 입출력 예



| number | n | m | result |
| --- | --- | --- | --- |
| 60 | 2 | 3 | 1 |
| 55 | 10 | 5 | 0 |

입출력 예 #1

- 60은 2의 배수이면서 3의 배수이기 때문에 1을 return합니다.

입출력 예 #2

- 55는 5의 배수이지만 10의 배수가 아니기 때문에 0을 return합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(number, n, m):
    answer = 0
    return answer
```


💭 문제 해석



- 1번 문제와 마찬가지로 나머지 개념과 조건문을 응용하면 풀 수 있음
- 두 가지 조건을 모두 만족하는 경우가 추가되었으므로 `and` 조건으로 조건문을 추가하면 풀 수 있음


⚙ 문제 풀이 계획



- `number % n` 과 `number % m` 이 모두 0인경우에 1을 출력하도록 조건문 설정


✅ 제출한 답



```python
def solution(number, n, m):
    return 1 if number % n == 0 and number % m ==0 else 0
```


➡️ 실행결과



```python
테스트 1
입력값 〉	60, 2, 3
기댓값 〉	1
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	55, 10, 5
기댓값 〉	0
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 나머지, 조건문, and 조건 설정 3가지를 알면 풀 수 있는 문제

---


## 3. 홀짝에 따라 다른 값 반환하기


💡 문제설명



- 양의 정수 `n`이 매개변수로 주어질 때, `n`이 홀수라면 `n` 이하의 홀수인 모든 양의 정수의 합을 return 하고 `n`이 짝수라면 `n` 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- • 1 ≤ `n` ≤ 100


💡 입출력 예



| n | result |
| --- | --- |
| 7 | 16 |
| 10 | 220 |

- 입출력 예 #1
    - 예제 1번의 `n`은 7로 홀수입니다. 7 이하의 모든 양의 홀수는 1, 3, 5, 7이고 이들의 합인 1 + 3 + 5 + 7 = 16을 return 합니다.
- 입출력 예 #2
    - 예제 2번의 `n`은 10으로 짝수입니다. 10 이하의 모든 양의 짝수는 2, 4, 6, 8, 10이고 이들의 제곱의 합인 $2^2 + 4^2 + 6^2 + 8^2 + 10^2 = 4 + 16 + 36 + 64 + 100 = 220$ 을 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(n):
    answer = 0
    return answer
```


💭 문제 해석



- 정수 n이 2로 나눠진다면 짝수, 아니면 홀수 라는 개념을 적용해서 짝수/홀수를 판단할 수 있음
- 나머지는 조건식에 따라 덧셈 또는 제곱근 연산을 하여 변수에 담아내면 풀 수 있음


⚙ 문제 풀이 계획



- 입력된 정수 `n` 이 짝수인지 홀수 인지 판별
- 0부터 입력된 정수 `n` 이하의 짝수/홀수를 같은 방식으로 판별 하며 추출(for 문사용)
    - 추출된 수들을 조건에 맞게 연산
        - 짝수인 경우 : 덧셈 연산을 하여 answer 변수에 추가
        - 홀수인 경우 : 제곱근 연산을 하여 answer 변수에 추가


⌨️ 입력한 코드



```python
def solution(n):
    odd = 0  # 홀수를 저장할 변수
    even = 0  # 짝수를 저장할 변수

    # n이 홀수인 경우
    if n % 2 != 0:
        for num in range(0, n+1):  # 0부터 n까지 순회
            if num % 2 != 0:  # 홀수인 경우
                odd += num  # 홀수 더하기
        answer = odd  # 결과 저장

    # n이 짝수인 경우
    else:
        for num in range(0, n+1):  # 0부터 n까지 순회
            if num % 2 == 0:  # 짝수인 경우
                even += num ** 2  # 짝수의 제곱 더하기
        answer = even  # 결과 저장

    return answer  # 결과 반환
```


❓ 오답 원인



- 조건이 여러개로 나뉘다보니 코드가 많이 길어 지고 있음
- 최초의 정수 `n` 이 홀수 인지 짝수인지를 구분하는건 불가피해도 나머지는 더 간결하게 작성할 수 있음
- list comprehension 개념을 적용해서 풀면 더 쉽게 풀어낼 수 있을 것 같다.


✅ 제출한 답



```python
def solution(n):
    if n % 2 != 0:
        # n이 홀수인 경우, 1부터 n까지의 홀수들의 합을 구합니다.
        return sum([num for num in range(1, n+1) if num % 2 != 0])
    else:
        # n이 짝수인 경우, 0부터 n까지의 짝수들의 제곱의 합을 구합니다.
        return sum([num ** 2 for num in range(0, n+1) if num % 2 == 0])
```


➡️ 실행결과



```python
테스트 1
입력값 〉	7
기댓값 〉	16
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	10
기댓값 〉	220
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 홀수와 짝수 구분부터, for문, 조건문 등 다양한 요소들을 활용해야 했다.
- 조건문을 사용해서 한단계씩 풀어간 것은 좋은데 list comprehension과 sum 개념을 생각하지 못한건 다소 아쉽다.

---


## 4. 조건 문자열


💡 문제설명



- 문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.
- 두 수가 `n`과 `m`이라면
    - ">", "=" : `n` >= `m`
    - "", "!" : `n` > `m`
    - ""중 하나고, `eq`는 "="와 "!"중 하나입니다. 그리고 두 정수 `n`과 `m`이 주어질 때, `n`과 `m`이 `ineq`와 `eq`의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.


🔒 제한 사항



- • 1 ≤ `n`, `m` ≤ 100


💡 입출력 예



| ineq | eq | n | m | result |
| --- | --- | --- | --- | --- |
| "" | "!" | 41 | 78 | 0 |

- 입출력 예 #1
    - 20  78은 거짓이기 때문에 0을 return합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(ineq, eq, n, m):
    answer = 0
    return answer
```


💭 문제 해석



- 함수에 입력된 문자열들을 조합해서 나올 수 있는 경우의 수만큼 조건문을 적용해서 각각의 경우에 대한 연산결과를 return해야 함


⚙ 문제 풀이 계획



- 문제에 나온대로 두 수의 크기를 비교하는 경우의 수 4가지를 각각 조건문으로 구현
- 그 안에 비교식이 성립하는 경우와 아닌 경우를 다시 각각 조건문으로 구현


⌨️ 입력한 코드



```python
def solution(ineq, eq, n, m):
    answer = 0  # 결과를 저장할 변수 초기화(조건 불만족시 0이 return되는 용도)

    # ineq이 '>' 이고 eq이 '=' 일 경우
    if ineq == ">" and eq == "=":
        if n >= m:  # n이 m보다 크거나 같을 경우
            answer = 1  # 결과값을 1로 설정

    # ineq이 '' 이고 eq이 '!' 일 경우
    elif ineq == ">" and eq == "!":
        if n > m:  # n이 m보다 클 경우
            answer = 1  # 결과값을 1로 설정

    # ineq이 '
❓ 오답 원인



- 문제를 1차원적으로 푼다고 가정했을 때 지금도 충분히 조건을 만족하면서 풀어내고 있음
- 다만 조금 더 손쉽게 풀 수 있는 방법은 없는걸까 찾아보다가 새로운 방법을 발견


✅ 제출한 답



```python
def solution(ineq, eq, n, m):
		# 문제에 제시된 조건을 튜플형태의 dict로 설정
    conditions = {
        (">", "="): n >= m,
        ("", "!"): n > m,
        ("
➡️ 실행결과



```python
테스트 1
입력값 〉	"", "!", 41, 78
기댓값 〉	0
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 조건식과 비교식을 잘 설정한다면 차근 차근 풀어낼 수 있는 문제
- 조건을 복잡하게 쓰지 않고 dict을 활용해서 풀 수도 있다는 점은 미처 알지 못했던 부분
- 문제 풀이에 대한 로직이 명확하다면 쉽게 적용할 수 있을지는 모르겠으나 바로 떠올려서 풀 수 있는 방법은 아닌 것 같음
- 개인적으로는 글을써도 풀어쓰는걸 좋아해서 그런지 dict를 응용해서 푸는 문제 같은 경우는 한번에 이해가 되지 않아 선호가 되지 않는 방식이긴하다.

---


## 5. flag에 따라 다른 값 반환하기


💡 문제설명



- 두 정수 `a`, `b`와 boolean 변수 `flag`가 매개변수로 주어질 때, `flag`가 true면 `a` + `b`를 false면 `a` - `b`를 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- -1,000 ≤ `a`, `b` ≤ 1,000


💡 입출력 예



| a | b | flag | result |
| --- | --- | --- | --- |
| -4 | 7 | true | 3 |
| -4 | 7 | false | -11 |

- 입출력 예 #1
    - 예제 1번에서 `flag`가 true이므로 `a` + `b` = (-4) + 7 = 3을 return 합니다.
- 입출력 예 #2
    - 예제 2번에서 `flag`가 false이므로 `a` - `b` = (-4) - 7 = -11을 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(a, b, flag):
    answer = 0
    return answer
```


💭 문제 해석



- flag에 따른 연산식을 각각 조건으로 설정해서 return하도록 하는 문제


⚙ 문제 풀이 계획



- flag가 True인 경우와 아닌 경우에 대한 연산식을 조건문으로 작성


✅ 제출한 답



```python
def solution(a, b, flag):
    return a + b if flag == True else a - b
```


➡️ 실행결과



```python
테스트 1
입력값 〉	-4, 7, true
기댓값 〉	3
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	-4, 7, false
기댓값 〉	-11
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 오늘 계속 풀었던 문제들을 이해하고 있다면 손쉽게 풀 수 있었음
- 조건문을 활용한 조건에 따른 산술연산을 구현할 수 있어야 함
- 1번 `n의 배수` 문제 처럼 양자택일식의 간단한 조건문은 삼항연산자를 쓰면 더 간결한 코드로 풀어 낼 수 있음을 응용해서 빠르게 풀어낼 수 있음

---


![](/images/coding-test/프로그래머스-공지용.gif)

---