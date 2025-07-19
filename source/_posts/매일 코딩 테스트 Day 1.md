---
title: "[Programmers school] 코딩 기초 트레이닝 Day 1"
cover: "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1920&h=1080&fit=crop"
date: 2023-09-07
categories:
  - [personal-study, coding-test]
tags:
  - 문자열 다루기
  - upper()
  - lower()
  - islower()
  - isupper()
  - for문
  - escape문자
  - 산술연산자
toc: true
---
문자출력, 대소문자 변경, 산술연산자 응용, 특수문자출력, 문자열 반복 출력하기 등

---


## 1. 문자 출력하기


💡 문제설명



- 문자열 `str`이 주어질 때, `str`을 출력하는 코드를 작성해 보세요.


🔒 제한 사항



- 1 ≤ `str`의 길이 ≤ 1,000,000
- `str`에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.


💡 입출력 예



- 입력 #1

```python
HelloWorld!
```

- 출력 #1

```python
HelloWorld!
```


🎓 문제풀이 코드(기본 세팅)



```python
str = input()

```


💭 문제 해석



- input()함수에 HelloWorld! 라는 문자열을 입력받아서 str이란 변수에 저장한 것을 출력해야 함


⚙ 문제 풀이 계획



- str을 print()문을 활용해 출력


✅ 제출한 답



```python
str = input() # input() 함수를 통해 "HelloWorld!" 를 입력받아 str에 저장

print(str) # str에 저장된 문자열 데이터 출력 by print()문
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"HelloWorld!"
기댓값 〉	"HelloWorld!"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	HelloWorld!
```


🤔 피드백



- 처음에 input()에 직접 HelloWorld! 를 입력해야 하나 고민 했는데 input() 자체가 입력을 받는 거니까 입력창이 뜨면 입력하고 아니면 자동 입력되겠거니! 했는데 그게 맞았음

---


## 2. a와 b 출력하기


💡 문제설명



- 정수 `a`와 `b`가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.


🔒 제한 사항



- -100,000 ≤ `a`, `b` ≤ 100,000


💡 입출력 예



- 입력 #1

```python
4 5
```

- 출력 #1

```python
a = 4
b = 5
```


🎓 문제풀이 코드(기본 세팅)



```python
a, b = map(int, input().strip().split(' '))
print(a + b)
```


💭 문제 해석



- map함수로 입력된 `4 5` 를 각각 a와 b에 할당한 상태
- 변수 a와 b에 할당된 값을 활용해 출력값과 같은 출력이 나오게 해야 함


⚙ 문제 풀이 계획



- 출력과 같은 값이 나오려면 print()문을 활용하되, 줄바꿈(\n), fstring을 사용하면 될 것 같음


✅ 제출한 답



```python
a, b = map(int, input().strip().split(' ')) 

print(f"a = {a}\nb = {b}")
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"4 5"
기댓값 〉	"a = 4
b = 5"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	a = 4
b = 5
```


🤔 피드백



- **`print(f"{a}\n{b}")`**: f-string을 사용해 변수 **`a`**와 **`b`**의 값을 문자열로 만듬
- 이때 띄어쓰기와 줄바꿈(`\n`) 을 활용해 출력값과 동일한 형태로 출력되게 하였음

---


## 3. 문자열 반복해서 출력하기


💡 문제설명



- 문자열 `str`과 정수 `n`이 주어집니다.
- `str`이 `n` 번 반복된 문자열을 만들어 출력하는 코드를 작성해보세요.


🔒 제한 사항



- 1 ≤ `str`의 길이 ≤ 10
- 1 ≤ `n` ≤ 5


💡 입출력 예



- 입력 #1

```python
string 5
```

- 출력 #1

```python
stringstringstringstringstring
```


🎓 문제풀이 코드(기본 세팅)



```python
a, b = input().strip().split(' ')
b = int(b)
```


💭 문제 해석



- a에는 string 이란 변수가, b에는 5라는 변수가 할당된 상태
- 여기서 b의 변수값은 int로 데이터 유형이 변경됨
- 출력 #1과 같은 형태로 출력하려면 산술연산자 개념을 활용해야 함


⚙ 문제 풀이 계획



- string을 5번 연속 출력해야 하므로 변수간 산술연산을 활용해 a를 5번 연속 출력


✅ 제출한 답



```python
a, b = input().strip().split(' ')
b = int(b)

print(a*b)
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"string 5"
기댓값 〉	"stringstringstringstringstring"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	stringstringstringstringstring
```


🤔 피드백



- 데이터의 유형에 대한 이해와 산술연산자 활용능력을 테스트하기 위한 문제

---


## 4. 대소문자 바꿔기


💡 문제설명



- 영어 알파벳으로 이루어진 문자열 `str`이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.


🔒 제한 사항



- 1 ≤ `str`의 길이 ≤ 20
    - `str`은 알파벳으로 이루어진 문자열입니다.


💡 입출력 예



- 입력 #1

```python
aBcDeFg
```

- 출력 #1

```python
AbCdEfG
```


🎓 문제풀이 코드(기본 세팅)



```python
str = input()
```


💭 문제 해석



- 문자열데이터를 다루는 함수중 upper()와 lower()를 활용하는 문제
- 또한, 대소문자 구분을 위해 islower(), isupper()를 활용해 각각의 문자가 대문자인지 소문자인지도 판별해야 함
- 변환된 문자를 새로운 변수에 할당하기 위해 append 기능을 활용해야 함


⚙ 문제 풀이 계획



- 입력된 문자가 대문자와 소문자가 섞여있기 때문에 대문자에게는 lower()를 적용해야 하고, 소문자에게는 upper()를 적용해야 함
- for loop을 활용해서 문제를 풀어야 함
- 변경된 문자가 입력될 가상 변수를 1개 생성한뒤 입력된 문자(aBcDeFg) 를 하나씩 순환하면서 대문자, 소문자로 각각 변경하여 가상 변수에 할당
- 할당된 가상변수를 다시 str에 할당한 뒤 print()


✅ 제출한 답



```python
str = input()

str_converted = '' # 변환된 문자열을 저장할 빈 문자열 생성

# 원본 문자열의 각 문자에 대해 반복문 적용
for char in str:
    # char가 소문자인 경우
    if char.islower():
        # 소문자를 대문자로 변환한 뒤 str_converted에 추가
        str_converted += char.upper()
    # char가 대문자인 경우
    if char.isupper():
        # 대문자를 소문자로 변환한 뒤 str_converted에 추가
        str_converted += char.lower()

str = str_converted # 변환된 문자열을 다시 str에 할당
print(str)
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"aBcDeFg
"
기댓값 〉	"AbCdEfG"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	AbCdEfG
```


🤔 피드백



- 파이썬의 다양한 함수를 활용하는 능력을 테스트 하기 위함
- 반복문, 문자열 preprocessing, if절 등을 사용하지 않으면 문제를 풀기 어려움

---


## 5. 특수문자 출력하기


💡 문제설명



- 다음과 같이 출력하도록 코드를 작성해 주세요.


🔒 제한 사항



- None


💡 입출력 예



- 입력 #1

```python
None
```

- 출력 #1

```python
!@#$%^&*(\'"<>?:;
```


🎓 문제풀이 코드(기본 세팅)



```python
print('hello world!')
```


💭 문제 해석



- `!@#$%^&*(\'"<>?:;`
- 특수문자를 출력할때 escape 문자를 활용하는 방법을 테스트하는 내용
- 모든 특수문자는 아니지만 일부 특수문자는 escape문자를 활용해야만 파이썬에서 ‘문자열(string)’로 인식할 수 있음


⚙ 문제 풀이 계획



- 문자로서 출력하기 위해 escape문자를 써야 하는 특수문자에 대해 적용이 필요
- 적용 대상 특수문자
    - 작은 따옴표 : ‘
    - 큰 따옴표 : “
    - 백슬레시 : \
- escape문자가 적용된 특수문자 예시
    - **`\'`**: 작은따옴표
    - **`\"`**: 큰따옴표
    - **`\\`**: 백슬래시


✅ 제출한 답



```python
print("!@#$%^&*(\\'\"<>?:;")
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"이 문제는 입력이 없습니다."
기댓값 〉	"!@#$%^&*(\'"<>?:;"
실행 결과 〉	테스트를 통과하였습니다.
출력 〉	!@#$%^&*(\'"<>?:;
```


🤔 피드백



- escape문자에 대한 개념을 알아야지만 풀 수 있는 문제
- 특히 자주 쓰이는 작은/큰 따옴표와 백슬레시를 문자열로 출력하고자 할 때 어떻게 적용가능한지는 종종 쓰이는 것이니 잘 기억해둘 필요가 있음
- escape 문자는 문자열 내에서 특수한 기능을 수행하거나 특수 문자를 출력할 때 사용하는 문자
- Python에서는 백슬래시(**`\`**)를 사용하여 escape 문자를 표현
- 자주사용되는 escape문자의 예시들
    - **줄바꿈 (`\n`)**: 새로운 줄을 시작
        
        ```python
        print("Hello\nWorld")
        ```
        
        ```python
        Hello
        World
        ```
        
    - **탭 (`\t`)**: 탭 간격을 띄우기
        
        ```python
        print("Hello\tWorld")
        ```
        
        ```python
        Hello World
        ```
        
    - **백스페이스 (`\b`)**: 커서를 하나 뒤로 이동
        
        ```python
        print("Helloo\b World")
        ```
        
        ```python
        Hello World
        ```
        
    - **캐리지 리턴 (`\r`)**: 커서를 해당 줄의 처음으로 이동
        
        ```python
        print("World\rHello")
        ```
        
        ```python
        Hello
        ```

---


![](/images/coding-test/프로그래머스-공지용.gif)
---