---
title: "[Programmers school] 코딩 기초 트레이닝 Day 5"
cover: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1920&h=1080&fit=crop"
date: 2023-09-11
categories:
  - [personal-study, coding-test]
tags:
  - 코드 처리하기
  - 등차수열의 특정한 항만 더하기
  - 주사위게임2
  - 원소들의 곱과 합
  - 이어 붙인 수
toc: true
---
코드 처리하기, 등차수열의 특정한 항만 더하기, 주사위게임2, 원소들의 곱과 합, 이어 붙인 수

## 1. 코드 처리하기


💡 문제설명



- 문자열 `code`가 주어집니다.

`code`를 앞에서부터 읽으면서 만약 문자가 "1"이면 `mode`를 바꿉니다. `mode`에 따라 `code`를 읽어가면서 문자열 `ret`을 만들어냅니다.

`mode`는 0과 1이 있으며, `idx`를 0 부터 `code의 길이 - 1` 까지 1씩 키워나가면서 `code[idx]`의 값에 따라 다음과 같이 행동합니다.

- `mode`가 0일 때
    - `code[idx]`가 "1"이 아니면 `idx`가 짝수일 때만 `ret`의 맨 뒤에 `code[idx]`를 추가합니다.
    - `code[idx]`가 "1"이면 `mode`를 0에서 1로 바꿉니다.
- `mode`가 1일 때
    - `code[idx]`가 "1"이 아니면 `idx`가 홀수일 때만 `ret`의 맨 뒤에 `code[idx]`를 추가합니다.
    - `code[idx]`가 "1"이면 `mode`를 1에서 0으로 바꿉니다.

문자열 `code`를 통해 만들어진 문자열 `ret`를 return 하는 solution 함수를 완성해 주세요.

단, 시작할 때 `mode`는 0이며, return 하려는 `ret`가 만약 빈 문자열이라면 대신 "EMPTY"를 return 합니다.


🔒 제한 사항



- 1 ≤ `code`의 길이 ≤ 100,000
- `code`는 알파벳 소문자 또는 "1"로 이루어진 문자열입니다.


💡 입출력 예



| code | result |
| --- | --- |
| "abc1abc1abc" | "acbac" |

- • `code`의 각 인덱스 `i`에 따라 다음과 같이 `mode`와 `ret`가 변합니다.

| i | code[i] | mode | ret |
| --- | --- | --- | --- |
| 0 | "a" | 0 | "a" |
| 1 | "b" | 0 | "a" |
| 2 | "c" | 0 | "ac" |
| 3 | "1" | 1 | "ac" |
| 4 | "a" | 1 | "ac" |
| 5 | "b" | 1 | "acb" |
| 6 | "c" | 1 | "acb" |
| 7 | "1" | 0 | "acb" |
| 8 | "a" | 0 | "acba" |
| 9 | "b" | 0 | "acba" |
| 10 | "c" | 0 | "acbac" |

- 따라서 "acbac"를 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(code):
    answer = ''
    return answer
```


💭 문제 해석



- `code` 라는 인자로 `abc1abc1abc` 가 입력되면 이를 조건에 따라 `mode`를 바꿔가면서 문자열 출력값을 바꿔 `ret` 라는 출력값으로 저장되어야 함
- `mode`가 바꾸는 기준은 `code`에 입력된 문자열로 기본값은 0이며 `code[idx]` 가 1일때 `mode`가 1로 바뀐다.
- `mode`가 0일 때 출력조건
    - `code[idx]` 의 문자가 숫자가 아닌 알파뱃이면서, idx가 짝수일때만 `ret`의 맨뒤에 `code[idx]` . 즉, `abc1abc1abc` 중 `n 번째 idx`의 문자열을 append
    - `code[idx]` 의 문자가 `1` 인 경우 `mode`를 0에서 1로 변환
- `mode` 가 1일 때 출력조건
    - `code[idx]` 의 문자가 숫자가 아닌 알파뱃이면서, idx가 홀수일때만 `ret`의 맨뒤에 `code[idx]` . 즉, `abc1abc1abc` 중 `n 번째 idx`의 문자열을 append
    - `code[idx]` 의 문자가 `1` 인 경우 `mode`를 1에서 0으로 변환
- return 하려는 `ret`가 비어있으면 “EMPTY”를 출력해야 함


⚙ 문제 풀이 계획



- `ret = ' '` 로 `mode = 0` 으로 기본 값을 설정
- code를 iteration하고 idx를 추출하여 판단하도록 for문 설정
- mode가 0일때와 1일때의 로직이 다르게 작동해야 함
- 조건문으로 `code[idx]` 가 “1” 인지 아닌지를 최우선적으로 판별
    - 이 값에 따라 mode가 계속 바뀌어야 하기 때문
- `code[idx]` 가 “1” 이 아닌 경우 mode 값을 0으로 설정하고 필요한 작업을 설정
    - `code[idx]` 가 “1”이라면 mode값을 1로 설정하고 pass
    - idx가 짝수이면 `code[idx]`를 `ret`에 append


⌨️ 입력한 코드



```python
def solution(code):
    ret = ''  # 결과를 저장할 빈 문자열
    mode = 0  # 초기 모드는 0
    
    # 코드의 길이만큼 반복
    for idx in range(len(code)):
        char = code[idx]  # 현재 문자
        # 모드가 0일 때
        if mode == 0:
            # idx가 짝수이고, 문자가 "1"이 아니면 ret에 추가
            if idx % 2 == 0:
                ret += char
            # 문자가 "1"이면 모드 변경
            if char == '1':
                mode = 1
        # 모드가 1일 때
        else:
            # idx가 홀수이면 ret에 추가
            if idx % 2 != 0:
                ret += char
            # 문자가 "1"이면 모드 변경
            if char == '1':
                mode = 0

    # ret가 빈 문자열이면 "EMPTY" 반환
    return ret if ret else "EMPTY"

# 테스트
solution(code) 

# 출력값 : "acb1ac"
```


❓ 오답 원인



- `code[idx]` 에서 추출되는 “1” 은 mode를 바꾸는 기준점으로서만 작동해야함.
- 바꿔 말하자면 “1”은 짝수,홀수번째 조건에 해당 되어도 ret에는 추가가 되지 않아야 함
- 인지하고 있는 내용이었지만 코드에 이러한 처리를 하도록 하지 않음
- mode별 조건문에서 ret에 문자열을 추가하는 조건에 “1”이 아닌 경우를 and조건으로 추가해야 함


✅ 제출한 답



```python
def solution(code):
    ret = ''  # 결과를 저장할 빈 문자열
    mode = 0  # 초기 모드는 0
    
    # 코드의 길이만큼 반복
    for idx in range(len(code)):
        char = code[idx]  # 현재 문자
        
        # 모드가 0일 때
        if mode == 0:
            # idx가 짝수이고, 문자가 "1"이 아니면 ret에 추가
            if idx % 2 == 0 and char != '1':
                ret += char
            # 문자가 "1"이면 모드 변경
            elif char == '1':
                mode = 1
        # 모드가 1일 때
        else:
            # idx가 홀수이면 ret에 추가
            if idx % 2 != 0 and char != '1':
                ret += char
            # 문자가 "1"이면 모드 변경
            elif char == '1':
                mode = 0
                
    # ret가 빈 문자열이면 "EMPTY" 반환
    return ret if ret else "EMPTY"

# 테스트
print(solution("abc1abc1abc"))  # 출력: "acbac"
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"abc1abc1abc"
기댓값 〉	"acbac"
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 문자열을 처리하는 다양한 방법과 조건문, 반복문을 이해해야하고, 데이터 타입에 대한 이해가 있어야 풀 수 있는 문제
- 이전까지 풀던 문제보다 문제가 너무 길고 서술이 많아서 처음에 좀 당황했는데, 막상 정리하고 보니 로직이 명확해서 상대적으로 풀기 어려운 문제는 아니었다.
- 복잡한 문제를 보면 겁먹지 말고 한줄 한줄 로직을 정리해서 풀어나가야 겠다.

---


## 2. 등차수열의 특정한 항만 더하기


💡 문제설명



- 두 정수 `a`, `d`와 길이가 n인 boolean 배열 `included`가 주어집니다. 첫째항이 `a`, 공차가 `d`인 등차수열에서 `included[i]`가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 `included`가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- 1 ≤ `a` ≤ 100
- 1 ≤ `d` ≤ 100
- 1 ≤ `included`의 길이 ≤ 100
- `included`에는 true가 적어도 하나 존재합니다.


💡 입출력 예



| a | d | included | result |
| --- | --- | --- | --- |
| 3 | 4 | [true, false, false, true, true] | 37 |
| 7 | 1 | [false, false, false, true, false, false, false] | 10 |

- 입출력 예 #1
    
    예제 1번은 `a`와 `d`가 각각 3, 4이고 `included`의 길이가 5입니다. 이를 표로 나타내면 다음과 같습니다.
    
    |  | 1항 | 2항 | 3항 | 4항 | 5항 |
    | --- | --- | --- | --- | --- | --- |
    | 등차수열 | 3 | 7 | 11 | 15 | 19 |
    | included | true | false | false | true | true |
    
    따라서 true에 해당하는 1항, 4항, 5항을 더한 3 + 15 + 19 = 37을 return 합니다.
    
- 입출력 예 #2
    
    예제 2번은 `a`와 `d`가 각각 7, 1이고 `included`의 길이가 7입니다. 이를 표로 나타내면 다음과 같습니다.
    
    |  | 1항 | 2항 | 3항 | 4항 | 5항 | 6항 | 7항 |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 등차수열 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
    | included | false | false | false | true | false | false | false |
    
    따라서 4항만 true이므로 10을 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(a, d, included):
    answer = 0
    return answer
```


💭 문제 해석



- 첫항이 `a` 공차가 `d` 인 등차수열을 구현해야 하며, 이중에 입력된 included 라는 list에서 True 인 idx에 해당되는 등차수열 값만 추출해서 더한 뒤 return해야 함


⚙ 문제 풀이 계획



- 첫항이 `a` 공차가 `d` 인 등차수열을 구한다.
- included에서 True인 idx를 찾고 이 idx를 활용해 등차수열의 값이 담긴 list에서 값을 추출한다.
- 추출된 값을 하나의 변수에 append하며 sum한다.


✅ 제출한 답



```python
def solution(a, d, included):
    
    # 등차수열 생성 함수
    def arithmetic_sequence(a, d, n):
        return [a + i * d for i in range(n)]
    
    # included와 등차수열의 길이 통일
    n = len(included)
    
    # 등차수열 생성
    sequence = arithmetic_sequence(a, d, n)
    
    # 등차수열의 합을 저장할 변수 (정수로 초기화)
    answer = 0
    
    # included 길이만큼 순회
    for idx in range(len(included)):
        # included가 True이면, 같은 idx의 등차수열 값을 추출해서 더함
        if included[idx]:
            answer += sequence[idx]
    
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	3, 4, [true, false, false, true, true]
기댓값 〉	37
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	7, 1, [false, false, false, true, false, false, false]
기댓값 〉	10
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 반복문, 배열, 조건문, 함수 등을 복합적으로 활용해야지만 풀 수 있는 문제였다.
- 특히 등차수열에 대한 개념과 이를 구현하는 방법을 알지 못하면 풀 수가 없는 문제

---


## 3. 주사위 게임 2


💡 문제설명



- 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 `a`, `b`, `c`라고 했을 때 얻는 점수는 다음과 같습니다.
    - 세 숫자가 모두 다르다면 `a` + `b` + `c` 점을 얻습니다.
    - 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면  $(a + b + c) \times (a^2 + b^2 + c^2)$ 점을 얻습니다.
- 세 숫자가 모두 같다면 $(a + b + c) \times (a^2 + b^2 + c^2) \times (a^3 + b^3 + c^3)$점을 얻습니다.
- 세 정수 `a`, `b`, `c`가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- `a`, `b`, `c`는 1이상 6이하의 정수입니다.


💡 입출력 예



| a | b | c | result |
| --- | --- | --- | --- |
| 2 | 6 | 1 | 9 |
| 5 | 3 | 3 | 473 |
| 4 | 4 | 4 | 110592 |

- 입출력 예 #1
    - 예제 1번에서 세 주사위 숫자가 모두 다르므로 2 + 6 + 1 = 9점을 얻습니다. 따라서 9를 return 합니다.
- 입출력 예 #2
    - 예제 2번에서 두 주사위 숫자만 같으므로 $(5 + 3 + 3) \times (5^2 + 3^2 + 3^2) = 11 \times 43 = 473$ 점을 얻습니다. 따라서 473을 return 합니다.
- 입출력 예 #3
    - 예제 3번에서 세 주사위 숫자가 모두 같으므로 $(4 + 4 + 4) \times (4^2 + 4^2 + 4^2 ) \times (4^3 + 4^3 + 4^3) = 12 \times 48 \times 192 = 110,592$ 점을 얻습니다. 따라서 110592를 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(a, b, c):
    answer = 0
		return answer
```


💭 문제 해석



- 조건문과 비교연산자를 활용해서 각 조건에 맞는 수식을 작성하는 것이 필요


⚙ 문제 풀이 계획



- 3개의 경우에 대한 조건문을 각각 작성


⌨️ 입력한 코드



```python
def solution(a, b, c):
    answer = 0
    # 모든 숫자가 다른 경우
    if a != b and b != c and a != c:
        answer = a + b + c
    # 두 숫자가 같고 다른 하나는 다른 경우
    elif a == b or a == c or b == c:
        answer = (a+b+c) * (a**2 + b**2 + c**2)
    # 모든 숫자가 같은 경우
    else:
        answer = (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    return answer
```


❓ 오답 원인



- `else` 조건인 `a == b == c` 가 구조상 절대 실행될 수가 없는 구조 이기 때문
    - `a == b == c` 인 경우 2번째 조건문인 `a==b or a == c or b == c` 를 만족해서 `else` 문으로 넘어가기전에 2번째 조건문을 실행하게 됨
- 따라서 조건문의 순서를 바꿀 필요가 있음


✅ 제출한 답



```python
def solution(a, b, c):
    answer = 0
    # 모든 숫자가 같은 경우
    if a == b == c:
        answer = (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    # 2개의 숫자는 같은데 나머지 하나는 다른 경우
    elif a == b or a == c or b == c:
        answer = (a+b+c) * (a**2 + b**2 + c**2)
    # 3개의 숫자가 모두 다른 경우
    else:
        answer = a + b + c
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	2, 6, 1
기댓값 〉	9
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	5, 3, 3
기댓값 〉	473
실행 결과 〉	테스트를 통과하였습니다.
테스트 3
입력값 〉	4, 4, 4
기댓값 〉	110592
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 처음에 문제를 쉽게 보고 개별 건에 대한 조건문만 작성하면 된다고 생각했는데 이게 오답의 원인
- 이러한 비교연산자 문제에서 if~elif 형태로 작성하게 되면 작성이 되는 순서도 중요하다는 점을 알게 되었음

---


## 4. 원소들의 곱과 합


💡 문제설명



- 정수가 담긴 리스트 `num_list`가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.


🔒 제한 사항



- 2 ≤ `num_list`의 길이 ≤ 10
- 1 ≤ `num_list`의 원소 ≤ 9


💡 입출력 예




| num_list | result |
| --- | --- |
| [3, 4, 5, 2, 1] | 1 |
| [5, 7, 8, 3] | 0 |

- 입출력 예 #1
    - 모든 원소의 곱은 120, 합의 제곱은 225이므로 1을 return합니다.
- 입출력 예 #2
    - 모든 원소의 곱은 840, 합의 제곱은 529이므로 0을 return합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(num_list):
    answer = 0
    return answer
```


💭 문제 해석



- 하드 코딩으로 풀자면 list내의 모든 원소를 연산하는 방법과 비교연산자 개념을 이용해 풀이하는 문제
- 좀 더 쉽게 접근하자면 numpy의 np.prod를 응용하거나 reduce 를 이용해서 풀 수 도 있음
    - [np.prod](http://np.prod) : 배열의 모든 요소의 곱을 계산하는 numpy 내장 함수
    - reduce : functools 모듈의 내장함수로 주어진 함수와 리스트(또는 순회가능한 객체)를 입력받아 리스트의 요소를 왼쪽에서 오른쪽으로 누적하면서 함수를 적용하는 내장함수
        - 여기서는 operator의 mul 기능을 이용해 num_list 배열내의 인자들을 왼쪽부터 오른쪽 방향으로 누적하면서 곱셈 연산을 하는


⚙ 문제 풀이 계획



- for문으로 list내의 원소를 iteration하며 곱을 직접 계산
- sum을 이용해 list내 모든 원소의 합을 구한뒤 제곱근 계산
- 두 값을 비교해서 0 또는 1을 출력
- 하드코딩 방식으로 작성해서 풀어본 뒤 나머지 2가지 방법으로도 풀어보기


⌨️ 최초 작성 코드



```python
def solution(num_list):
    # 모든 요소의 곱을 계산
    product_of_elements = 1
    for num in num_list:
        product_of_elements *= num
    
    # 모든 요소의 합을 계산
    sum_of_elements = sum(num_list)
    
    # 합의 제곱과 모든 요소의 곱을 비교
    return 1 if product_of_elements 
❓ 개선방향



- 파이썬의 numpy와 reduce를 활용해서 다양한 방법으로 풀어보기
    - 모든 요소의 곱을 계산하는 부분을 좀 더 간결하게 할 수 있음


✅ 제출한 답



```python
# numpy로 푸는 버전
import numpy as np

def solution(num_list):
    product_of_elements = np.prod(num_list)  # 모든 요소의 곱
    sum_of_elements = np.sum(num_list)  # 모든 요소의 합
    return 1 if product_of_elements 
➡️ 실행결과



```python
테스트 1
입력값 〉	[3, 4, 5, 2, 1]
기댓값 〉	1
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	[5, 7, 8, 3]
기댓값 〉	0
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 조건에 따른 연산을 할 수 있다면 어렵지 않게 풀 수 있는 문제
- 하드코딩으로 하는 방법외에 다른 방법도 있을 수 있음을 배움

---


## 5. 이어 붙인 수


💡 문제설명



- 정수가 담긴 리스트 `num_list`가 주어집니다. `num_list`의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.


🔒 제한 사항



- 2 ≤ `num_list`의 길이 ≤ 10
- 1 ≤ `num_list`의 원소 ≤ 9
- `num_list`에는 적어도 한 개씩의 짝수와 홀수가 있습니다.


💡 입출력 예



| num_list | result |
| --- | --- |
| [3, 4, 5, 2, 1] | 393 |
| [5, 7, 8, 3] | 581 |

- 입출력 예 #1
    - 홀수만 이어 붙인 수는 351이고 짝수만 이어 붙인 수는 42입니다. 두 수의 합은 393입니다.
- 입출력 예 #2
    - 홀수만 이어 붙인 수는 573이고 짝수만 이어 붙인 수는 8입니다. 두 수의 합은 581입니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(num_list):
    answer = 0
    return answer
```


💭 문제 해석



- 홀수와 짝수를 구분하는 방법과 조건문, 산술연산자등을 응용해서 풀이하는 문제
- 이어붙인다는 개념이 `int` 형태의 숫자를 이어 붙이는 것이 아니고 `str` 형태의 숫자를 이어 붙이는 것
- 두 변수를 합할때는 `int` 로서 합해야 함


⚙ 문제 풀이 계획



- 하드 코딩으로 푼다면 for문으로 list를 순환하면서 나머지를 이용해 홀수와 짝수를 구분하고, 조건문에 따라 각각 별개의 변수(even, odd)에 담은뒤
- return할때 int로 변환해서 덧셈 연산하여 return


⌨️ 최초 작성 코드



```python
def solution(num_list):
    # 홀수와 짝수를 도출할 변수 초기화
    even = ''
    odd = ''
    
    # num_list를 순회하며 홀짝 구분
    for num in num_list:
        # 짝수인 경우
        if num % 2 == 0:
            even += str(num) # even 변수에 문자로 변환하여 append
        # 홀수인 경우
        else:
            odd += str(num) # odd 변수에 문자로 변환하여 append
    return int(even) + int(odd) # 두 변수의 합 return
```


❓ 개선방향



- 좀 더 간결하게 코드를 작성하는 방법을 적용해보고 싶었음
- 개념을 찾다보니 lambda를 적용해서 풀어낼 수 있을 것 같았음
    - list내에서 주어진 조건을 만족하는 것만 return하는 filter() 함수와
    - 개별적으로 return되는 값들을 모아 다시 배열로 만들어 주는 map() 함수
    - 그리고 이러한 결과들을 연결해주는 join() 함수를 응용하면 풀 수 있음


✅ 제출한 답



```python
def solution(num_list):
    even = ''.join(map(str, filter(lambda x: x % 2 == 0, num_list))) # 짝수만 추출해서 이어 붙이기
    odd = ''.join(map(str, filter(lambda x: x % 2 != 0, num_list))) # 홀수만 추출해서 이어 붙이기
    
		# 짝수와 홀수의 합 return
		# even과 odd가 빈 문자열일 경우를 고려해 if even and odd else int(even or odd) 부분을 넣음
    return int(even) + int(odd) if even and odd else int(even or odd)
```

- 입력된 함수의 가장 우측부터 좌측방향으로 한단계씩 연산되며 진행(`filter → map → join`)
- filter 함수 : 주어진 함수의 조건을 만족하는 요소만 걸러내어 반환 (1 단계)
    - `lambda x: x % 2 == 0` : num_list의 개별 인자 x가 짝수인지 확인하는 lambda 함수
    - `lambda x: x % 2 != 0` : num_list의 개별 인자 x가 홀수인지 확인하는 lambda 함수
    - **`num_list`**가 **`[3, 4, 2, 5, 1]`**이라면, 짝수는 `[4, 2]` 를 반환하고 홀수는 `[3, 5, 1]` 을 반환
- map 함수 : 주어진 함수를 적용해서 새로운 리스트(정확히는 iterator) 생성하는 함수로 여기서는 lambda 함수의 결과를 적용 (2단계)
    - `map(str, [4, 2])` 가 입력되어 입력된 `[4, 2]` 의 각 요소에 str()이 적용되어  `['4', '2']` 가 return
    - `map(str, [3, 5, 1])` 가 입력되어 `[3, 5, 1]` 의 각 요소에 str()이 적용되어  `['3', '5', '1']` 가 return
- join 함수 : 문자열 리스트를 하나의 문자열로 연결하는 함수 (3단계)
    - `''.join(['4','2'])` 가 되어서 문자열 `'42'`  를 return
    - `''.join(['3', '5', '1'])` 가 되어서 문자열 `'351'`  를 return
- 각각 연산된 결과(`even` , `odd` ) 를 `int` 로 변환하여 덧셈한뒤 return


➡️ 실행결과



```python
테스트 1
입력값 〉	[3, 4, 5, 2, 1]
기댓값 〉	393
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	[5, 7, 8, 3]
기댓값 〉	581
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 간단하게 풀려고 하면 그리 어려운 문제는 아니었던 것 같은데, 생소한 개념인 lambda나 다른 함수들을 복합적으로 적용하려고 하니까 조금 어려운 문제가 되어 버렸다.

---


---


![](/images/coding-test/프로그래머스-공지용.gif)