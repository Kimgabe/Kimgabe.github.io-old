---
title: "[Programmers school] 코딩 기초 트레이닝 Day 8"
cover: "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1920&h=1080&fit=crop"
date: 2023-09-14
categories:
  - [personal-study, coding-test]
tags:
  - 간단한 논리 연산
  - 주사위 게임 3
  - 글자 이어 붙여 문자열 만들기
  - 9로 나눈 나머지
  - 문자열 여러번 뒤집기
toc: true
---
조건문, 문자열 개념을 응용한 다양한 문제를 풀었습니다.

## 1. 간단한 논리연산

---



💡 문제설명



- boolean 변수 `x1`, `x2`, `x3`, `x4`가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.
    - (`x1` ∨ `x2`) ∧ (`x3` ∨ `x4`)


🔒 제한 사항



- None

---



💡 입출력 예



- 입출력 예 #1
    - 예제 1번의 `x1`, `x2`, `x3`, `x4`로 식을 계산하면 다음과 같습니다.
        
        (`x1` ∨ `x2`) ∧ (`x3` ∨ `x4`) ≡ (F ∨ T) ∧ (T ∨ T) ≡ T ∧ T ≡ T
        
        따라서 true를 return 합니다.
        
- 입출력 예 #2
    - 예제 2번의 `x1`, `x2`, `x3`, `x4`로 식을 계산하면 다음과 같습니다.
        
        (`x1` ∨ `x2`) ∧ (`x3` ∨ `x4`) ≡ (T ∨ F) ∧ (F ∨ F) ≡ T ∧ F ≡ F
        
        따라서 false를 return 합니다.
        
- ∨과 ∧의 진리표는 다음과 같습니다.

| x | y | x ∨ y | x ∧ y |
| --- | --- | --- | --- |
| T | T | T | T |
| T | F | T | F |
| F | T | T | F |
| F | F | F | F |

---



🎓 문제풀이 코드(기본 세팅)



```python
def solution(x1, x2, x3, x4):
    answer = True
    return answer
```

---



💭 문제 해석



- boolean 변수 4개가 주어지고 이에 대한 참과 거짓을 반환해야 함
- python에서 논리연산자는 and, or 를 통해 연산함
- x ∧ y 는 x and y 를 의미
- x ∨ y 는 x or y 를 의미


⚙ 문제 풀이 계획



- 문제에 입력된 식을 논리연산식으로 표현

---



✅ 제출한 답



```python
def solution(x1, x2, x3, x4):
		# x1 ∨ x2 : x1 or x2
		# x3 ∨ x4 : x3 or x4
		# (x1 ∨ x2) ∧ (x3 ∨ x4) 에서 ∧ 는 and 연
    return (x1 or x2) and (x3 or x4)
```


➡️ 실행결과



```python
테스트 1
입력값 〉	false, true, true, true
기댓값 〉	true
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	true, false, false, false
기댓값 〉	false
실행 결과 〉	테스트를 통과하였습니다.
```

---



🤔 피드백



- 문제에서 얘기하는 식이 논리연산자라는 점을 알지 못해서 초반에 풀지 못했음
- 제목을 보고 논리 연산자라는 것은 이해를 했는데 python으로 어떻게 구현하지? 라는 생각에 막막했던 것 같음
- 기호를 몰랐어도 진리표를 보고 두 연산식에 대한 결과를 비교해서 연산식을 추론할 수는 있을 것 같다.
    - T ∨ T = T
    - T ∨ F = T
    - F ∨ T = T
    - F ∨ F = F
    - 를 통해 두 변수중 하나라도 T이면 결과가 T이므로 or라고 유추할 수 있고
    - T ∧ T = T
    - T ∧ F = F
    - F ∧ T = F
    - F ∧ F = F
    - 를 통해 두 변수가 모두 T일때만 결과가 T이므로 and 연산자라고 추정할 수 있음

---


---


## 2. 주사위 게임 3

---



💡 문제설명



- 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
    - 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
    - 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 $(10 \times p + q)^2$ 점을 얻습니다.
        
        2
        
    - 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 $(p + q) \times |p-q|$점을 얻습니다.
    - 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
    - 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
- 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 `a`, `b`, `c`, `d`로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- `a`, `b`, `c`, `d`는 1 이상 6 이하의 정수입니다.

---



💡 입출력 예



- 입출력 예 #1
    - 예제 1번에서 네 주사위 숫자가 모두 2로 같으므로 1111 × 2 = 2222점을 얻습니다. 따라서 2222를 return 합니다.
- 입출력 예 #2
    - 예제 2번에서 세 주사위에서 나온 숫자가 4로 같고 나머지 다른 주사위에서 나온 숫자가 1이므로 $(10 \times 4 + 1)^2 = 41^2 = 1681$ 점을 얻습니다. 따라서 1681을 return 합니다.
- 입출력 예 #3
    - 예제 3번에서 `a`, `d`는 6으로, `b`, `c`는 3으로 각각 같으므로 $(6 + 3) \times |6 - 3| = 9 \times 3 = 27$ 점을 얻습니다. 따라서 27을 return 합니다.
- 입출력 예 #4
    - 예제 4번에서 두 주사위에서 2가 나오고 나머지 다른 두 주사위에서 각각 5, 6이 나왔으므로 5 × 6 = 30점을 얻습니다. 따라서 30을 return 합니다.
- 입출력 예 #5
    - 예제 5번에서 네 주사위 숫자가 모두 다르고 나온 숫자 중 가장 작은 숫자가 2이므로 2점을 얻습니다. 따라서 2를 return 합니다.

---



🎓 문제풀이 코드(기본 세팅)



```python
def solution(a, b, c, d):
    answer = 0
    return answer
```

---



💭 문제 해석



- 조건문, list, 수학연산을 이해하고 있어야 풀 수 있는 문제
- 4개의 주사위를 굴려서 나온 값의 경우의 수를 가지고 조건에 따른 연산을 해야 하는 문제
- 입력받은 정수 4개를 상호 비교해서 일치여부를 판단하는 코드를 구현해야 함
    - 단순 비교연산자로는 구현이 복잡해짐


⚙ 문제 풀이 계획



- 입력된 정수 a, b, c, d를 비교하여 각 숫자별로 몇번 동일한 수가 나왔는지 count하는 코드 작성
    - 입력받은 정수를 list로 만들어 iterable하게 변경
    - 정수 list를 iteration하면서 정수별 count를 dict에 담기
    - dict를 count수 기준으로 asc하게 sorting
    - count의 unique값을 별도로 계산
- 문제에서 나온 5가지 경우에 대한 조건식을 작성하여 적용
    - 위에서 정리한 값들을 통해 조건식 작성

---



✅ 제출한 답



```python
def solution(a, b, c, d):
    # 초기값 설정
    answer = 0
    # 정수를 리스트로 변환
    num_list = [a, b, c, d]
    # 정수의 개수를 저장할 딕셔너리 생성
    count_dict = {}
    
    # 정수의 개수 계산
    for element in num_list:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    
    # 딕셔너리를 개수가 많은 순으로 정렬
    keys = sorted(count_dict.keys(), key=lambda x: count_dict[x], reverse=True)
    
    # 주사위의 고유한 수를 계산
    unique_dice = len(count_dict)
    
    # 고유한 주사위 값의 개수에 따라 점수 계산
    if unique_dice == 1:
        # 모든 주사위 값이 같을 경우 (예: [2, 2, 2, 2])
        # 입출력 예 #1에 해당
        answer = keys[0] * 1111
    elif unique_dice == 2:
        # 두 종류의 주사위 값이 나온 경우
        if count_dict[keys[0]] == 3:
            # 한 값이 3개, 다른 값이 1개 나온 경우 (예: [4, 4, 4, 1])
            # 입출력 예 #2에 해당
            answer = (10 * keys[0] + keys[1]) ** 2
        else:
            # 두 값이 각각 2개씩 나온 경우 (예: [6, 6, 3, 3])
            # 입출력 예 #3에 해당
            answer = (keys[0] + keys[1]) * abs(keys[0] - keys[1])
    elif unique_dice == 3:
        # 세 종류의 주사위 값이 나온 경우 (예: [2, 2, 5, 6])
        # 입출력 예 #4에 해당
        answer = keys[1] * keys[2]
    else:
        # 모든 주사위 값이 다른 경우 (예: [1, 2, 3, 4])
        # 입출력 예 #5에 해당
        answer = min(num_list)
    
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	2, 2, 2, 2
기댓값 〉	2222
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	4, 1, 4, 4
기댓값 〉	1681
실행 결과 〉	테스트를 통과하였습니다.
테스트 3
입력값 〉	6, 3, 3, 6
기댓값 〉	27
실행 결과 〉	테스트를 통과하였습니다.
테스트 4
입력값 〉	2, 5, 2, 6
기댓값 〉	30
실행 결과 〉	테스트를 통과하였습니다.
테스트 5
입력값 〉	6, 4, 2, 5
기댓값 〉	2
실행 결과 〉	테스트를 통과하였습니다.
```


⌨️ 다른 풀이 방식



- 내가 작성한 코드는 별도의 모듈 없이 풀려고 하다보니 너무 하드 코딩이 되어 버렸다.
- 그리고 if~elif 문에서 조건을 너무 세분화해서 코드리뷰하기 불편하다.
- 아래는 Counter 모듈을 사용하고 조건문을 더 간소화 한 버전의 풀이 방

```python
from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]  # 주사위 값들을 리스트에 저장
    count = Counter(dice)  # 각 숫자의 등장 횟수를 센다.
    
    if len(count) == 1:  # 모든 숫자가 같은 경우
        return 1111 * a  # 1111 * a 점수 반환
    elif len(count) == 2:  # 두 가지 숫자가 나온 경우
        for k, v in count.items():
            if v == 3:  # 세 개의 숫자가 같은 경우
                return (10 * k + (dice[0] if dice[0] != k else dice[1])) ** 2  # (10 * p + q) ^ 2 점수 반환
            elif v == 2:  # 두 개씩 같은 숫자가 나온 경우
                other = [key for key, value in count.items() if value == 2]
                return (other[0] + other[1]) * abs(other[0] - other[1])  # (p + q) * |p - q| 점수 반환
    elif len(count) == 3:  # 세 가지 숫자가 나온 경우
        for k, v in count.items():
            if v == 2:  # 두 개의 숫자가 같은 경우
                other = [key for key in count.keys() if key != k]
                return other[0] * other[1]  # q * r 점수 반환
    else:  # 모든 숫자가 다른 경우
        return min(dice)  # 가장 작은 숫자 점수 반환
```


❓ Counter 모듈?



- python기본 라이브러리인 collection에 포함된 클래스
- 주어진 list나 문자열같이 iterable한 객체에 각 원소의 등장 횟수를 count하여 dict 형태로 return
- 예를 들어, **`Counter([1, 1, 2, 3, 4, 3, 2])`**를 실행하면 결과는 **`{1: 2, 2: 2, 3: 2, 4: 1}`** 이 됨
- 이 문제에서는 정수 (a, b, c, d)는 iterable하지 않으므로 list로 변환해 iterable하게 만든후 Counter()에 적용하여 정수별 등장 횟수를 count함

---



🤔 피드백



- 위와 같이 경우의 수가 여러개로 세분화 되는 문제는 경우의 수에 대한 구조를 잘 그려야 되는 것 같다.
- 조금만 분기를 잘못설정해서 구분하고보면 대부분의 로직을 잘 작성해 놓고도 오류가 나서 오답이 나는 경우가 많은 것 같다.

---


---


## 3. 글자 이어 붙여 문자열 만들기

---



💡 문제설명



- 문자열 `my_string`과 정수 배열 `index_list`가 매개변수로 주어집니다. `my_string`의 `index_list`의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- 1 ≤ `my_string`의 길이 ≤ 1,000
- `my_string`의 원소는 영소문자로 이루어져 있습니다.
- 1 ≤ `index_list`의 길이 ≤ 1,000
- 0 ≤ `index_list`의 원소 
💡 입출력 예



| my_string | index_list | result |
| --- | --- | --- |
| "cvsgiorszzzmrpaqpe" | [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7] | "programmers" |
| "zpiaz" | [1, 2, 0, 0, 3] | "pizza" |

- 입출력 예 #1
    - 예제 1번의 `my_string`에서 인덱스 3, 5, 6, 11, 12, 14, 16, 17에 해당하는 글자는 각각 g, o, r, m, r, a, p, e이므로 `my_string`에서 `index_list`에 들어있는 원소에 해당하는 인덱스의 글자들은 각각 순서대로 p, r, o, g, r, a, m, m, e, r, s입니다. 따라서 "programmers"를 return 합니다.
- 입출력 예 #2
    - 예제 2번의 `my_string`에서 인덱스 0, 1, 2, 3에 해당하는 글자는 각각 z, p, i, a이므로 `my_string`에서 `index_list`에 들어있는 원소에 해당하는 인덱스의 글자들은 각각 순서대로 p, i, z, z, a입니다. 따라서 "pizza"를 return 합니다.

---



🎓 문제풀이 코드(기본 세팅)



```python
def solution(my_string, index_list):
    answer = ''
    return answer
```

---



💭 문제 해석



- 문자열 인덱싱과 list를 다루는 기본 개념을 알아야 풀 수 있는 문제
- 주어진 문자열 `my_string` 에서 `index_list` 를 참고해 새로운 문자열로 만들고 return해야 한다.


⚙ 문제 풀이 계획



- 정답을 담을 빈 문자열 `answer` 생성
- `index_list` 를 순회하며 idx 번호 추출
- 추출된 idx에 해당하는 문자를 `my_string` 에서 추출
- 추출된 문자를 `answer` 에 추가

---



✅ 제출한 답



```python
def solution(my_string, index_list):
    # 문자열 담을 변수 생성
    answer = ''
    # index_list를 순회하며 idx 추출
    for idx in index_list:
        # 추출한 idx에 해당되는 문자를 answer에 추가
        answer += my_string[idx]
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
기댓값 〉	"programmers"
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	"zpiaz", [1, 2, 0, 0, 3]
기댓값 〉	"pizza"
실행 결과 〉	테스트를 통과하였습니다.
```

---



🤔 피드백



- 기본 개념만 인식하고 있다면 쉽게 풀 수 있는 문제

---


---


## 4. 9로 나눈 나머지

---



💡 문제설명



- 음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
- 이 사실을 이용하여 음이 아닌 정수가 **문자열** number 로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.


🔒 제한 사항



- 1 ≤ `number`의 길이 ≤ 100,000
- `number`의 원소는 숫자로만 이루어져 있습니다.
- `number`는 정수 0이 아니라면 숫자 '0'으로 시작하지 않습니다.

---



💡 입출력 예



| number | result |
| --- | --- |
| "123" | 6 |
| "78720646226947352489" | 2 |

- 입출력 예 #1
    - 예제 1번의 `number`는 123으로 각 자리 숫자의 합은 6입니다. 6을 9로 나눈 나머지는 6이고, 실제로 123 = 9 × 13 + 6입니다. 따라서 6을 return 합니다.
- 입출력 예 #2
    - 예제 2번의 `number`는 78720646226947352489으로 각자리 숫자의 합은 101입니다. 101을 9로 나눈 나머지는 2이고, 실제로 78720646226947352489 = 9 × 8746738469660816943 + 2입니다. 따라서 2를 return 합니다.

---



🎓 문제풀이 코드(기본 세팅)



```python
def solution(number):
    answer = 0
    return answer
```

---



💭 문제 해석



- 문자열 처리와 산술연산을 이해하고 있어야 풀 수 있는 문제
- number를 % 9 한 결과가 같이 설명되어서 혼란이 될 수 있으나 여기에 휘말리면 안되는 문제
- 문제는 문자열로된 number의 각 자리수의 합을 구하고, 그것을 9로 나눈 나머지를 return하는 것
- number가 123이면 각 숫자의 합은 1 + 2 + 3 = 6이고, 이를 9로 나는 나머지는 6이므로 6을 return하면 된다.


⚙ 문제 풀이 계획



- number에서 각 문자를 Int로 바꾼뒤 더하여 값을 구하고 이를 9로 나눈 나머지를 return 한다.

---



✅ 제출한 답



```python
def solution(number):
    # number의 각 숫자 값을 담을 변수
    total_sum = 0
    # number 을 iteration하면서 숫자 추출
    for digit in number:
        # 추출된 숫자를 int로 변환하여 더함
        total_sum += int(digit)
    return total_sum % 9
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"123"
기댓값 〉	6
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	"78720646226947352489"
기댓값 〉	2
실행 결과 〉	테스트를 통과하였습니다.
```

---



🤔 피드백



- 문제에서 실제 필요로 하는 것이 무엇인지, 코드로 구현해야 하는 것이 무언인지를 핵심을 잘 파악하는게 중요함

---


---


## 5. 문자열 여러번 뒤집기

---



💡 문제설명



- 문자열 `my_string`과 이차원 정수 배열 `queries`가 매개변수로 주어집니다. `queries`의 원소는 [s, e] 형태로, `my_string`의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. `my_string`에 `queries`의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- `my_string`은 영소문자로만 이루어져 있습니다.
- 1 ≤ `my_string`의 길이 ≤ 1,000
- `queries`의 원소는 [s, e]의 형태로 0 ≤ s ≤ e 
💡 입출력 예



- 예제 1번의 `my_string`은 "rermgorpsam"이고 주어진 `queries`를 순서대로 처리하면 다음과 같습니다.

| queries | my_string |
| --- | --- |
|  | "rermgorpsam" |
| [2, 3] | "remrgorpsam" |
| [0, 7] | "progrmersam" |
| [5, 9] | "prograsremm" |
| [6, 10] | "programmers" |

- 따라서 "programmers"를 return 합니다.

---



🎓 문제풀이 코드(기본 세팅)



```python
def solution(my_string, queries):
    answer = ''
    return answer
```

---



💭 문제 해석



- 문자열 인덱싱, 파이썬 슬라이싱 개념을 이해하고 있어야 풀 수 있는 문제
- queries에 입력된 query를 통해 my_string의 s 부터 e 까지의 문자를 뒤집어라 = 순서를 바꿔라
- query가 적용될 부분과 그렇지 않은 부분간을 slice해서 처리한뒤 다시 합쳐야 한다.


⚙ 문제 풀이 계획



- queries 배열 순회하며 s,e 라는 query 추출하기
- 추출된 query에 따라 my_string에서 뒤집을 부분 찾아내고 뒤집기
- 뒤집은 부분을 원래 my_string의 s, e 위치에 입력

---



✅ 제출한 답



```python
def solution(my_string, queries):
    # query 추출
    for s,e in queries:
        # query만큼 슬라이싱 하기
        # [s:e+1] : 뒤집을 부분
        # [::-1] : 나머지 문자열
        reversed_part = my_string[s:e+1][::-1]  
        
        # 뒤집은 문자열을 원래 위치에 적용
        # my_string[:s] : s 이전까지 문자열 가져오기 (뒤집을 부분 이전 문자 원본)
        # reversed_part : 뒤집어진 부분
        # my_string[e+1] : 뒤집을 부분 이전 원본 & 뒤집을 부분 제외한 나머지 원본
        my_string = my_string[:s] + reversed_part + my_string[e+1:]  
        
    return my_string
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]
기댓값 〉	"programmers"
실행 결과 〉	테스트를 통과하였습니다.
```


⌨️ 다른 풀이 방법



- 문자열 자체는 중간에 바꾸는 등의 작업을 할 수 없음
- 그러나 문자열을 list로 변환하면 중간의 문자를 업데이트 할 수 있음
- 내장함수인 reversed()를 이용해 list내 특정 구간만을 뒤집을 수 있다.
- 그리고 뒤집어진 list를 다시 문자열로 변환하기 위해 join 을 사용한다.
    - join은 앞에 호출된 문자열을 구분자로 사용해 입력된 리스트의 요소들을 하나의 문자열로 합치는 기능을 한다.

```python
def solution(my_string, queries):
    my_list = list(my_string)  # 문자열을 리스트로 변환

    for s, e in queries:  # queries 배열 순회
        # 리스트의 s부터 e까지 구간을 뒤집음
        my_list[s:e+1] = reversed(my_list[s:e+1])
        
    return ''.join(my_list)  # 리스트를 문자열로 변환 후 반환
```

---



🤔 피드백



- 문자열을 슬라이싱 할때 범위가 주어지면 그 범위를 그대로 쓸게 아니라 +1 해야 함을 자꾸 까먹는다 (idx는 0부터 시작)
- 사소한 것이지만, 이거 하나로 오답이 되어버리니 늘 신경을 잘 써야 하는 부분
- 가급적 내장함수없이 하드 코딩으로 풀어보려고 하는데 그래도 기본 내장함수도 잘 알고 있어야 빠르게 문제를 풀 수 있을것 같다.
- 좋은 풀이 예시는 많이 보고 찾아보는게 좋은 것 같다.

---


![](/images/coding-test/프로그래머스-공지용.gif)

---


