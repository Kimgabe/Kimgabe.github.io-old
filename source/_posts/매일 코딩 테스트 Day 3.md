---
title: "[Programmers school] 코딩 기초 트레이닝 Day 3"
cover: "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1920&h=1080&fit=crop"
date: 2023-09-09
categories:
  - [personal-study, coding-test]
tags:
  - 문자열 섞기
  - 문자 리스트를 문자열로 변환하기
  - 문자열 곱하기
  - 더 크게 합치기
  - 두 수의 연산값 합치기
toc: true
---
문자열 섞기, 문자 리스트를 문자열로 변환하기, 문자열 곱하기, 더 크게 합치기, 두 수의 연산값 합치기
---


## 1. 문자열 섞기


💡 문제설명



- 길이가 같은 두 문자열 `str1`과 `str2`가 주어집니다.
- 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.


🔒 제한 사항



- 1 ≤ `str1`의 길이 = `str2`의 길이 ≤ 10
- `str1`과 `str2`는 알파벳 소문자로 이루어진 문자열입니다.


💡 입출력 예



- 입력 #1

| str1 | str2 | result |
| --- | --- | --- |
| "aaaaa" | "bbbbb" | "ababababab" |


🎓 문제풀이 코드(기본 세팅)



```python
def solution(str1, str2):
    answer = ''
    return answer
```


💭 문제 해석



- 2개의 변수에서 문자열 indexing을 통해 문자열을 추출하는 것을 응용해서 풀어야함


⚙ 문제 풀이 계획



- 반복문으로 각 변수에서 n번째 index의 문자를 추출
- 추출된 문자를 `str1` , `str2` 순서대로 각각 answer라는 변수에 append
- 모든 iteration이 끝난뒤 return


⌨️ 맨 처음 입력한 코드



```python
def solution(str1, str2):
    # 각 변수에서 출력된 문자들이 입력될 변수 초기화
    answer = ''
    # 두 변수의 길이가 같으므로 하나의 변수를 기준으로 iteration 범위 설정
    for idx in range(len(str1)):
        answer += str1[idx] + str2[idx] # 변수의 n번째 index의 문자열 추출해 answer에 할당
    return answer
```


❓ 개선 방향



- 문자열에서 indxing 을 한다는 개념까진 좋은데, idx를 직접 지정하는 것보다 zip함수를 응용하면 더 좋았을 듯
    - zip함수는 여러개의 변수를 동시에 iteration할 수 있음


✅ 제출한 답



```python
def solution(str1, str2):
    # 결과를 저장할 빈 문자열 answer 초기화
    answer = ''
    
    # str1과 str2의 각 문자를 동시에 순회
    for char1, char2 in zip(str1, str2):
        # char1과 char2를 차례대로 answer에 추가
        answer += char1 + char2
        
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"aaaaa", "bbbbb"
기댓값 〉	"ababababab"
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 문자열 슬라이싱, 결합 등의 개념을 알아야 풀 수 있음
- 특히 코드 간소화를 위해 zip함수의 개념을 이해하고 있으면 쉽게 풀 수 있음

---


## 2. 문자열 섞기 응용


💡 문제설명



- 문제1과 달리 `str1` 과 `str2` 의 길이가 다르다면 어떻게 구현해야 할까?


🔒 제한 사항



- `str1`과 `str2`는 알파벳 소문자로 이루어진 문자열입니다.
- `str1`과 `str2`의 문자열 길이는 다를 수 있지만 모두 1~10사이의 길이를 가집니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(str1, str2):
    answer = ''
    return answer
```


💭 문제 해석



- 두개의 변수중 길이가 짧은 변수를 기준으로 문자열 섞기와 긴 변수 기준을오 문자열 섞기 2가지 경우가 발생할 수 있음
    - 두 문자열의 최소 길이 까지만 섞어서 출력한뒤, 나머지는 그대로 두는 경우
    - 더 긴 문자열을 기준으로 출력하되 섞어서 출력하는건 짧은 문자열이 끝나는 부분까지로 하는 경우


⚙ 문제 풀이 계획



- case1
    - 문자열 최소 길이 구한 뒤
    - 최소 길이 까지 반복하며 출력(문제1의 답 응용)
    - 긴 문자열이 담긴 변수의 나머지 부분 answer에 할당
    - 출력
- case2
    - 문자열의 길이 각각 계산
    - 두 문자열의 최대 길이까지 반복해서 answer에 append
    - 출력


✅ 제출한 답(case 1)



```python
def solution(str1, str2):
    # 결과를 저장할 빈 문자열 answer 초기화
    answer = ''
    
    # 두 문자열의 최소 길이 구하기
    min_length = min(len(str1), len(str2))
    
    # 최소 길이까지만 반복하며 문자열 결합
    for char1, char2 in zip(str1[:min_length], str2[:min_length]):
        answer += char1 + char2
    
    # 남은 부분을 answer에 추가
    answer += str1[min_length:] + str2[min_length:]
    
    return answer
```


✅ 제출한 답(case 2)



```python
def solution(str1, str2):
    # 결과를 저장할 빈 문자열 answer 초기화
    answer = ''
    
    # 두 문자열의 길이 구하기
    len1, len2 = len(str1), len(str2)
    
    # 두 문자열의 최대 길이까지 반복
    for i in range(max(len1, len2)):
        if i 
🤔 피드백



- 문제를 풀기 위해 여러가지 경우의 수를 산정하고 그에 맞춰 코드를 재구성 하는 부분이 어려웠음

---


## 3. 문자 리스트를 문자열로 변환하기


💡 문제설명



- 문자들이 담겨있는 배열 `arr`가 주어집니다.
- `arr`의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.


🔒 제한 사항



- 1 ≤ `arr`의 길이 ≤ 200
    - `arr`의 원소는 전부 알파벳 소문자로 이루어진 길이가 1인 문자열입니다.


💡 입출력 예



| arr | result |
| --- | --- |
| ["a","b","c"] | "abc" |


🎓 문제풀이 코드(기본 세팅)



```python
def solution(arr):
    answer = ''
    return answer
```


💭 문제 해석



- arr은 list형태, list에 있는 각 key별 value들을 한개씩 추출해서 새로운 변수에 담을 수 있는지 확인하는 문제


⚙ 문제 풀이 계획



- for문으로 arr에서 하나의 value씩 추출한 뒤
- answer 변수에 append한뒤
- 최종 결과를 출


✅ 제출한 답



```python
def solution(arr):
    # 결과를 저장할 빈 문자열 answer 초기화
    answer = ''
    
    # 배열 arr에 들어있는 각 문자에 대해 반복
    for char in arr:
        # 현재 문자 char를 문자열 answer에 추가
        answer += char
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	["a", "b", "c"]
기댓값 〉	"abc"
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- for문, 문자열 연결 그리고 배열 또는 list에 대한 기본 개념을 알면 쉽게 풀 수 있는 문제
- 문자열을 연결하는 방법이 산술연산자를 응용하거나 위와 같이 append를 응용하는 방법등 다양하다는 점을 알아야 풀기 쉬울 수 있다.

---


## 4. 문자열 곱하기


💡 문제설명



- 문자열 `my_string`과 정수 `k`가 주어질 때, `my_string`을 `k`번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.


🔒 제한 사항



- 1 ≤ `my_string`의 길이 ≤ 100
- `my_string`은 영소문자로만 이루어져 있습니다.
- 1 ≤ `k` ≤ 100


💡 입출력 예



| my_string | k | result |
| --- | --- | --- |
| "string" | 3 | "stringstringstring" |
| "love" | 10 | "lovelovelovelovelovelovelovelovelovelove" |


⚙ 입출력 예 설명



입출력 예 #1

- 예제 1번의 `my_string`은 "string"이고 이를 3번 반복한 문자열은 "stringstringstring"이므로 이를 return 합니다.

입출력 예 #2

- 예제 2번의 `my_string`은 "love"이고 이를 10번 반복한 문자열은 "lovelovelovelovelovelovelovelovelovelove"이므로 이를 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(my_string, k):
    answer = ''
    return answer
```


💭 문제 해석



- 산술연산자를 활용해 문자열을 연속 출력하는 것을 확인하는 문제


⚙ 문제 풀이 계획



- answer에 할당된 문자열을 k번 곱하는 산술연산식 작성


✅ 제출한 답



```python
def solution(my_string, k):
    answer = my_string * k
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	"string", 3
기댓값 〉	"stringstringstring"
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	"love", 10
기댓값 〉	"lovelovelovelovelovelovelovelovelovelove"
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 문자열을 곱해서도 출력할 수 있음을 알고 있으면 쉬운 개념

---


## 5. 더 크게 합치기


💡 문제설명



- 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
    - 12 ⊕ 3 = 123
    - 3 ⊕ 12 = 312
- 양의 정수 `a`와 `b`가 주어졌을 때, `a` ⊕ `b`와 `b` ⊕ `a` 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
- 단, `a` ⊕ `b`와 `b` ⊕ `a`가 같다면 `a` ⊕ `b`를 return 합니다.


🔒 제한 사항



- 1 ≤ `a`, `b` 
💡 입출력 예



| a | b | result |
| --- | --- | --- |
| 9 | 91 | 991 |
| 89 | 8 | 898 |


💡 입출력 예



- 입출력 예 #1
    - `a` ⊕ `b` = 991 이고, `b` ⊕ `a` = 919 입니다. 둘 중 더 큰 값은 991 이므로 991을 return 합니다.
- 입출력 예 #2
    - `a` ⊕ `b` = 898 이고, `b` ⊕ `a` = 889 입니다. 둘 중 더 큰 값은 898 이므로 898을 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(a, b):
    answer = 0
    return answer
```


💭 문제 해석



- 각 변수에 할당된 값은 숫자 같지만 문제와 같이 ‘str’로서 ‘붙어서’ result와 같은 형태가 되야 한다.
- 즉, 숫자형태로 입력된 문자열을 이어 붙이는 것과 같은 것
- 하지만 그 결과를 비교할때는 숫자로서 비교를 해야 함
- 변수의 데이터 타입을 자유롭게 변형할 수 있어야 하며 비교연산자를 사용할 수 있어야 하며, 조건에 따라 출려값이 달라져야 하므로 조건문도 응용할 수 있어야 한다.


⚙ 문제 풀이 계획



- 두개의 변수를 문자열로 변환하여 숫자형태로 이어 붙이기
- 조건문을 통해 두 변수를 숫자로서 값 비교
- 비교된 값중에 큰 값을 answer에 할당하고 출력


⌨️ 입력한 코드



```python
def solution(a, b):
    # a와 b를 문자열로 변환 후 이어 붙여 result1에 저장
    result1 = str(a) + str(b)
    # b와 a를 문자열로 변환 후 이어 붙여 result2에 저장
    result2 = str(b) + str(a)
    
    # 최종 결과값을 저장할 변수 answer 초기화
    answer = 0
    # result1과 result2를 정수로 변환한 뒤 비교
    if int(result1) > int(result2):
        # result1이 더 큰 경우 answer에 저장
        answer = int(result1)
    else:
        # result2가 더 큰 경우 answer에 저장
        answer = int(result2)
    
    # 최종 결과값 answer 반환
    return answer
```


❓ 코드 피드백



- 문제 풀이의 의도는 제대로 시도하였으나 코드가 더 간소화 될 수 있음
- 일종의 하드 코딩으로 문제 풀이한 것
- 사실 다른 개념은 모두 동일하더라도 조건문 없이 `max()` 함수만 사용해도 손쉽게 풀 수 있다.


✅ 제출한 답



```python
def solution(a, b):
		# a와 b를 문자열로 변환 후 이어 붙여 각각 result1, result2에 저장
    result1 = str(a) + str(b)
    result2 = str(b) + str(a)
    
		# max()함수를 활용해 두 변수중 큰 값을 answer에 할
    answer = max(int(result1), int(result2))
    
    return answer
```


➡️ 실행결과



```python
테스트 1
입력값 〉	9, 91
기댓값 〉	991
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	89, 8
기댓값 〉	898
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 각 변수에 할당된 데이터 타입을 자유롭게 변환할 수 있으면 어렵지 않게 풀 수 있는 문제
- 처음엔 하드 코딩으로 조건문으로 풀었지만, max()함수를 먼저 떠올리지 못한게 아쉬웠음

---


## 6. 두 수의 연산값 비교하기


💡 문제설명



- 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
    - 12 ⊕ 3 = 123
    - 3 ⊕ 12 = 312
- 양의 정수 `a`와 `b`가 주어졌을 때, `a` ⊕ `b`와 `2 * a * b` 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.
- 단, `a` ⊕ `b`와 `2 * a * b`가 같으면 `a` ⊕ `b`를 return 합니다.


🔒 제한 사항



- • 1 ≤ `a`, `b` 
💡 입출력 예



| a | b | result |
| --- | --- | --- |
| 2 | 91 | 364 |
| 91 | 2 | 912 |


💡 입출력 예



- 입출력 예 #1
    - `a` ⊕ `b` = 291 이고, `2 * a * b` = 364 입니다. 둘 중 더 큰 값은 364 이므로 364를 return 합니다.
    - `a` ⊕ `b` = 912 이고, `2 * a * b` = 364 입니다. 둘 중 더 큰 값은 912 이므로 912를 return 합니다.


🎓 문제풀이 코드(기본 세팅)



```python
def solution(a, b):
    answer = 0
    return answer
```


💭 문제 해석



- 이전문제랑 풀기 위한 개념은 모두 동일
- ⊕ 연산을 하는 경우에는 string으로, 비교하고 출력할때는 int형태로 연산해야 함


⚙ 문제 풀이 계획



- 비교를 위해 문제 조건에 맞게 두 개의 변수를 생성
- 생성된 변수를 조건문에 따라 비교한뒤 answer에 할당


⌨️ 입력한 코드



```python
def solution(a, b):
    # a와 b변수를 문제에 맞게 생성하여 result1, result2 변수에 각각 할당
    result1 = str(a) + str(b)
    result2 = 2 * a * b
    
    # 최종 결과값을 저장할 변수 answer 초기화
    answer = 0
    # result1과 result2를 정수로 변환한 뒤 비교
    if int(result1) > int(result2):
        # result1이 더 큰 경우 answer에 저장
        answer = int(result1)
    # result2가 더 큰 경우 answer에 저장
    elif int(result1) 
❓ 코드 피드백



- 문제 풀이의 의도는 제대로 시도하였으나 코드가 더 간소화 될 수 있음
- 사실 answer 를 이런식으로 여러번 할당할 필요 없이 바로 return 하도록 하는 것이 더 간결할 수 있음


✅ 제출한 답



```python
def solution(a, b):
    result1 = int(str(a) + str(b))  # a와 b를 문자열로 변환한 뒤 이어붙이고, 다시 정수로 변환
    result2 = 2 * a * b  # 2 * a * b의 결과를 저장

    # 두 결과를 비교하여 더 큰 값을 반환
    if result1 > result2:
        return result1  # result1이 더 크면 result1 반환
    elif result1 
➡️ 실행결과



```python
테스트 1
입력값 〉	2, 91
기댓값 〉	364
실행 결과 〉	테스트를 통과하였습니다.
테스트 2
입력값 〉	91, 2
기댓값 〉	912
실행 결과 〉	테스트를 통과하였습니다.
```


🤔 피드백



- 다양한 데이터 타입들을 활용하고, 비교 연산자, 다중 조건문을 활용하여야 풀 수 있는 문제
- 문제풀이 예시에 `answer = 0` 라고 되어 있다고 해서 굳이 그걸 쓰려고 한게 오히려 코드를 더 복잡하게 만든 것 같다.

---


![](/images/coding-test/프로그래머스-공지용.gif)
---