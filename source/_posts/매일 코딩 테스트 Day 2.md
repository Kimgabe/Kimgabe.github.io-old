---
title: "[Programmers school] 코딩 기초 트레이닝 Day 2"
cover: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1920&h=1080&fit=crop"
date: 2023-09-08
categories:
  - [personal-study, coding-test]
tags:
  - 덧셈식 출력하기
  - 문자열 붙여서 출력하기
  - 문자열 돌리기
  - 홀짝 구분하기
  - 문자열 겹쳐쓰기
toc: true
---
## 덧셈식 출력하기


💡 문제설명



- 두 정수 `a`, `b`가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

```python
a + b = c
```


🔒 제한 사항



- • 1 ≤ `a`, `b` ≤ 100


💡 입출력 예



- 입력 #1

```python
4 5
```

- 출력 #1

```python
4 + 5 = 9
```


🎓 문제풀이 코드(기본 세팅)



```python
a, b = map(int, input().strip().split(' '))
print(a + b)
```


💭 문제 해석



- 변수에 할당된 변수를 어떻게 다루느냐가 관건
- 이미 a,b에는 4와 5라는 변수가 map으로 각각 할당되어 있음
- 할당된 변수는 int 형태
- 출력 예시와 같게 출력하려면 문자열로 변경이 필요
- fstring을 써서 코드를 간소화 할 수 있어야 함


⚙ 문제 풀이 계획



- `4 + 5 =` 부분은 string으로 변경하여 출력하게 하고
- 9는 a + b 그대로 출력되게 해야  함


✅ 제출한 답



```python
a, b = map(int, input().strip().split(' '))
#print(a + b)

print(f'{str(a)} + {str(b)} =', a+b)
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"4 5"
기댓값 〉	"4 + 5 = 9"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	4 + 5 = 9
```


🤔 피드백



- 어제 풀었던 문제와 비슷한 내용
- 변수에 할당된 데이터의 유형을 변화시키는 방법과 fstring을 활용하는 방법을 알아야 풀 수 있음

---


## 문자열 붙여서 출력기


💡 문제설명



- 두 개의 문자열 `str1`, `str2`가 공백으로 구분되어 입력으로 주어집니다.
- 입출력 예와 같이 `str1`과 `str2`을 이어서 출력하는 코드를 작성해 보세요.


🔒 제한 사항



- • 1 ≤ `str1`, `str2`의 길이 ≤ 10


💡 입출력 예



- 입력 #1

```python
apple pen
```

- 출력 #1

```python
applepen
```


🎓 문제풀이 코드(기본 세팅)



```python
str1, str2 = input().strip().split(' ')
```


💭 문제 해석



- 문자열 데이터를 다루는 방법을 활용해야 함
- input()된 단어는 `apple pen` 인 것이고 이것이 띄어쓰기를 기준으로 2개의 단어로 나뉘어 각각 str1과 str2에 할당된 것
- 문자열 또한 산술연산자를 통해 출력할 수 있다는 것만 알면 쉽게 풀 수 있음


⚙ 문제 풀이 계획



- 두개의 문자열 변수를 산술연산자(+)를 활용해 print()문에 입력


✅ 제출한 답



```python
str1, str2 = input().strip().split(' ')

print(str1+str2)
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"apple pen"
기댓값 〉	"applepen"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	applepen
```


🤔 피드백



- 문자열 데이터를 산술연산자를 통해 활용할 수 있음을 확인하기 위한 테스트

---


## 문자열 돌리기


💡 문제설명



- 문자열 `str`이 주어집니다.
- 문자열을 시계방향으로 90도 돌려서 아래 입출력 예시와 같이 출력하는 코드를 작성해보세요.


🔒 제한 사항



- 1 ≤ `str`의 길이 ≤ 10


💡 입출력 예



- 입력 #1

```python
abcde
```

- 출력 #1

```python
a
b
c
d
e
```


🎓 문제풀이 코드(기본 세팅)



```python
str = input()
```


💭 문제 해석



- input()되는 값은 `abcde` 라는 문자열
- 문자열을 돌리라는 등의 얘기를 하지만 결국은 for문 활용능력을 보기 위함
- str에 할당된 `abcde`를 iteration하며 한글자씩 print하면 풀 수 있음


⚙ 문제 풀이 계획



- str을 for문에 넣어 iteration하며 한글자씩 print


✅ 제출한 답



```python
str = input()

for vertical in str:
    print(vertical)
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"abcde"
기댓값 〉	"a
b
c
d
e"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	a
b
c
d
e
```


🤔 피드백



- for문의 개념을 이해하고 있다면 쉽게 풀 수 있는 문제

---


## 홀짝 구분하기


💡 문제설명



- 자연수 `n`이 입력으로 주어졌을 때 만약 `n`이 짝수이면 "`n` is even"을, 홀수이면 "`n` is odd"를 출력하는 코드를 작성해 보세요.


🔒 제한 사항



- • 1 ≤ `n` ≤ 1,000


💡 입출력 예



- 입력 #1

```python
100
```

- 출력 #1

```python
100 is even
```

- 입력 #2

```python
1
```

- 출력 #2

```python
1 is odd
```


🎓 문제풀이 코드(기본 세팅)



```python
a = int(input())
```


💭 문제 해석



- 자연수 n은 input()함수로 받아서 입력되는 수이고 각각 100과 1이 입력된다.
- 파이썬에 자체적으로 숫자가 홀인지 짝인지 구분하는 코드는 없음
- 다만 나머지 개념을 통해 짝수인지 아닌지 알 수 있음
    - 자연수 n을 2로 나눈 나머지가 0이면 짝수, 아니면 홀수


⚙ 문제 풀이 계획



- if문과 나머지개념을 활용해서 print문 작


✅ 제출한 답



```python
a = int(input())

if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"100"
기댓값 〉	"100 is even"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	100 is even
테스트 2
입력값 〉	"1"
기댓값 〉	"1 is odd"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	1 is odd
```


🤔 피드백



- if문과 나머지 개념을 이해하고 있다면 쉽게 풀 수 있는 문제
- if문에서 elif문으로 예외 케이스를 추가할 수도 있었지만, 사실상 홀/짝 구분 문제에선 elif 케이스가 없으므로 작성하지 않았음.
- 하지만 실무에서는 내 머리속에서는 ‘이분법’ 의 결론밖에 없는 경우라도 내가 모르는 제3의 케이스가 있을 수도 있으니까 elif를 고려하는게 더 좋지 않을까 생각은 함.

---


## 문자열 겹쳐쓰기


💡 문제설명



- 문자열 `my_string`, `overwrite_string`과 정수 `s`가 주어집니다. 문자열 `my_string`의 인덱스 `s`부터 `overwrite_string`의 길이만큼을 문자열 `overwrite_string`으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- `my_string`와 `overwrite_string`은 숫자와 알파벳으로 이루어져 있습니다.
- 1 ≤ `overwrite_string`의 길이 ≤ `my_string`의 길이 ≤ 1,000
- 0 ≤ `s` ≤ `my_string`의 길이 - `overwrite_string`의 길이


💡 입출력 예



| my_string | overwrite_string | s | result |
| --- | --- | --- | --- |
| "He11oWor1d" | "lloWorl" | 2 | "HelloWorld" |
| "Program29b8UYP" | "merS123" | 7 | "ProgrammerS123" |

입출력 예 #1

- 예제 1번의 `my_string`에서 인덱스 2부터 `overwrite_string`의 길이만큼에 해당하는 부분은 "11oWor1"이고 이를 "lloWorl"로 바꾼 "HelloWorld"를 return 합니다.

입출력 예 #2

- 예제 2번의 `my_string`에서 인덱스 7부터 `overwrite_string`의 길이만큼에 해당하는 부분은 "29b8UYP"이고 이를 "merS123"로 바꾼 "ProgrammerS123"를 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(my_string, overwrite_string, s):
    answer = ''
    return answer
```


💭 문제 해석



- 문자열 parsing에 대한 내용을 알아야 풀 수 있는 문제
- 판단의 기준이 되는 문자열은 `my_string`이고 시작점이 되는 index번호는 `s` 가 된다. 그리고 시작점 `s` 부터 몇글자를 출력할지는 `len(overwrite_string)` 이 된다.


⚙ 문제 풀이 계획



- overwrite_string의 길이를 구하기
- overwrite_string 만큼 바꿔질 부분을 구하기
- 계산된 모든 값들을 더해서 정답 생성


✅ 제출한 답



```python
def solution(my_string, overwrite_string, s):
    # overwrite_string의 길이를 구하기
    parse_n = len(overwrite_string)
    
    # 시작 인덱스(s)에서 overwrite_string의 길이만큼 더한 값을 구하기
    parse_n2 = s + parse_n
    
    # my_string의 0부터 s까지의 부분과,
    # overwrite_string, 
    # my_string의 s + len(overwrite_string) 이후 부분을 합치기
    answer = my_string[:s] + overwrite_string + my_string[parse_n2:]
    
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"He11oWor1d", "lloWorl", 2
기댓값 〉	"HelloWorld"
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	"Program29b8UYP", "merS123", 7
기댓값 〉	"ProgrammerS123"
실행 결과 〉	테스트를 통과하였습니다.
```


⌨️ 개선한 코드



```python
def solution(my_string, overwrite_string, s):
    # answer 변수를 초기화
    answer = ''
    
    # my_string의 0부터 s까지의 부분을 answer에 추가
    answer += my_string[:s]
    
    # overwrite_string을 answer에 추가
    answer += overwrite_string
    
    # my_string에서 s + len(overwrite_string) 이후의 부분을 answer에 추가
    answer += my_string[s + len(overwrite_string):]
    
    return answer
```


❓ 무엇이 바뀌었는가?



- 기존 코드는 일단 가독성이 너무 떨어짐
- 변수를 별도로 설정해서 미리 합쳐질 변수의 index값 등을 계산하였으나 최종 `answer` 를 작성하는 과정에서 보면 한번에 이해하기 어려움
- 그래서 `answer` 라는 변수를 초기화한 뒤에 append기능을 활용해 하나씩 추가하는 식으로 단계별로 구분을 지었음
- 이렇게 하고 나니 코드 가독성이 더 좋아지고 내용을 이해하는 것도 더 쉬워졌음


🤔 피드백



- 문자열 슬라이싱, 문자열결합, 변수할당, 함수정의 등에 대해 이해하고 있어야 풀 수 있는 문제
- 문제풀이를 단계별로 나눈뒤 한단계씩 구현하는 것이 문제풀이에도, 코드리뷰에도 더 좋다는 점을 깨달음

---


![](/images/coding-test/프로그래머스-공지용.gif)

---