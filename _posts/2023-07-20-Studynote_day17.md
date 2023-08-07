---
layout : single
title:  "[스터디노트] Day17 기초수학 문제풀이"
categories: [DS17_Bootcamp, 기초수학]
tag: [스터디노트, 문제풀이, 수학알고리즘]
header :
    teaser : "/assets/img/studynote/studynote_day17.png"
---


# 💡공부한 내용

---

- 파이썬으로 수학문제풀이
    - 약수와 소수
    - 소인수와 소인수분해
    - 최대공약수
    - 최소공배수
    - 진법
    - 등차수열
    - 등비수열
    - 시그마
    - 계차수열
    - 피보나치수열
    - 팩토리얼
    - 군수열
    - 순열
    - 조합
    - 확률

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

### 약수와 소수

> **100~1000사이 난수에서 약수, 소수, 소인수 구하기**
> 

```python
import random

# 100과 1000 사이의 난수를 생성
rNum = random.randint(100, 1000)
print(f'rNum = {rNum}')

# 1부터 생성된 난수까지 반복
for num in range(1, rNum + 1):
    # 소수 판별 플래그와 소인수 판별 플래그를 설정
    is_prime = True
    is_factor = False

    # 약수 구하기
    # 생성된 난수를 현재 숫자로 나눴을 때 나머지가 0이면 현재 숫자는 난수의 약수임
    if rNum % num == 0:
        print(f'[약수] {num}')
        is_factor = True  # 약수임을 표시

    # 소수 구하기
    # 1과 자기 자신 외에 어떤 수로도 나누어지지 않는 수가 소수임
    # 따라서 2부터 현재 숫자 -1 까지 반복하며, 현재 숫자를 나눠봅니다.
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False  # 나누어지는 수가 있으면 소수가 아닙니다.
                break

        # 위의 반복문에서 나누어지는 수가 없었다면 현재 숫자는 소수임
        if is_prime:
            print(f'[소수]: {num}')

    # 소인수 구하기
    # 약수이면서 소수인 수가 소인수임
    # 따라서 약수 플래그와 소수 플래그 둘 다 True인 경우 현재 숫자를 소인수로 출력
    if is_factor and is_prime:
        print(f'[소인수]: {num}')
```

```python
rNum = 100
[약수] 1
[소인수]: 1
[약수] 2
[소수]: 2
[소인수]: 2
[소수]: 3
[약수] 4
[약수] 5
[소수]: 5
[소인수]: 5
[소수]: 7
[약수] 10
[소수]: 11
[소수]: 13
[소수]: 17
[소수]: 19
[약수] 20
[소수]: 23
[약수] 25
[소수]: 29
[소수]: 31
[소수]: 37
[소수]: 41
[소수]: 43
[소수]: 47
[약수] 50
[소수]: 53
[소수]: 59
[소수]: 61
[소수]: 67
[소수]: 71
[소수]: 73
[소수]: 79
[소수]: 83
[소수]: 89
[소수]: 97
[약수] 100
```

### 소인수와 소인수분해

> **100부터 1000사이 난수를 소인수분해하고 각각의 소인수에 대한 지수를 출력하는 프로그램 만들기**
> 

```python
import random   

# 100에서 1000 사이의 랜덤한 수를 생성
rNum = random.randint(100, 1000)
print(f'rNum = {rNum}')

# 소인수를 저장할 리스트
soinsuList = []

# 소인수를 찾기 위해 2부터 시작
n = 2

# 생성된 난수가 1이 될 때까지 소인수를 찾는 과정을 반복
while n <= rNum:
    # 현재의 수(n)가 난수(rNum)를 나눌 수 있는지 확인
    if rNum % n == 0:
        # 나눌 수 있다면 그 수는 소인수
        print(f'소인수: {n}')
        # 찾은 소인수를 리스트에 추가
        soinsuList.append(n)
        # 난수를 현재의 수(n)로 나눔
        rNum /= n
    else:
        # 나눌 수 없다면 다음 수로 이동
        n += 1
        
print(f'soinsuList = {soinsuList}')

tempNum = 0
# 소인수 리스트를 순회하며 각 소인수의 개수를 세는 과정
for s in soinsuList:
    # 같은 소인수를 여러번 세지 않기 위해, 현재의 소인수가 이전 소인수보다 클 경우에만 세기
    if tempNum < s:
        print(f'{s}\'s count: {soinsuList.count(s)}')
        # 이전 소인수로 현재 소인수를 설정
        tempNum = s
```

```python
rNum = 536
소인수: 2
소인수: 2
소인수: 2
소인수: 67
soinsuList = [2, 2, 2, 67]
2's count: 3
67's count: 1
```

### 최대공약수

> **100부터 1000사이의 2개의 난수에 대해 공약수와 최대공약수를 출력하고, 서로소인지 출력하는 프로그램 만들기**
> 

```python
import random

# 100부터 1000까지의 랜덤한 두 수를 생성
rNum1 = random.randint(100, 1000)
rNum2 = random.randint(100, 1000)

print(f'rNum1: {rNum1}')
print(f'rNum2: {rNum2}')

maxNum = 0

# 두 수 중 작은 수까지 반복하면서 공약수를 찾음. 이때 range 함수의 끝점은 포함되지 않으므로 1을 더해줌
for n in range(1, min(rNum1, rNum2) + 1):
    # 두 수를 n으로 나눴을 때 모두 나머지가 0이면 n은 두 수의 공약수
    if rNum1 % n == 0 and rNum2 % n == 0:
        print(f'{rNum1}과 {rNum2}의 공약수는 {n}이야.')
        maxNum = n  # 최대공약수를 업데이트
        
print(f'최대공약수: {maxNum}')

# 최대공약수가 1이면 두 수는 서로소
if maxNum == 1:
    print(f'{rNum1}과 {rNum2}는 서로소야.')
```

```python
rNum1: 190
rNum2: 452
190과 452의 공약수는 1이야.
190과 452의 공약수는 2이야.
최대공약수: 2
```

### 최소공배수

> **100부터 1000사이의 2개의 난수에 대해서 최대공약수와 최소공배수를 출력하는 프로그램 만들기**
> 

```python
import random

# 100부터 1000 사이의 랜덤한 두 개의 숫자를 생성한다.
rNum1 = random.randint(100, 1000)
rNum2 = random.randint(100, 1000)

print(f'rNum1 = {rNum1}')
print(f'rNum2 = {rNum2}')

maxNum = 0  # 최대공약수를 저장할 변수

# 두 수 중 작은 수까지 반복한다.
for n in range(1, (min(rNum1, rNum2)+1)):
    # 만약 n이 두 수의 공약수라면, maxNum에 n을 저장한다.
    # 이렇게 하면 반복이 끝나는 시점의 maxNum는 최대공약수가 된다.
    if rNum1 % n == 0 and rNum2 % n == 0:
        maxNum = n

print(f'최대공약수: {maxNum}')  # 최대공약수 출력

# 최소공배수는 두 수의 곱을 최대공약수로 나눈 값이다.
minNum = (rNum1 * rNum2) // maxNum
print(f'최소공배수 : {minNum}')  # 최소공배수 출력
```

```python
rNum1 = 510
rNum2 = 899
최대공약수: 1
최소공배수 : 458490
```

### 진법

> 각 진법별로 전환하는 프로그램 만들기
> 

```python
# 10진수를 입력받기 위해 사용자에게 입력을 요청
dNum = int(input('10진수 입력: '))

# 입력받은 10진수를 2진수로 변환해서 출력.
print('2진수 : {}'.format(bin(dNum)))
# 10진수를 8진수로 변환해서 출력. 
print('8진수 : {}'.format(oct(dNum)))
# 10진수를 16진수로 변환해서 출력. '
print('16진수 : {}'.format(hex(dNum)))

# 문자열로 된 2진수를 10진수로 변환해서 출력
print('2진수(10101) -> 10진수({})'.format(int('10101', 2)))
# 문자열로 된 8진수를 10진수로 변환해서 출력
print('8진수(135) -> 10진수({})'.format(int('135', 8)))
# 문자열로 된 16진수를 10진수로 변환해서 출력
print('16진수(5f) -> 10진수({})'.format(int('5f', 16)))

# 문자열로 된 2진수를 먼저 10진수로 바꿔서 그걸 8진수로 변환해서 출력. '0o' 제거 위해 [2:] 사용
print('2진수(10101) -> 8진수({})'.format(oct(int('10101', 2))[2:]))
# 2진수를 먼저 10진수로 바꿔서 그걸 16진수로 변환해서 출력. '0x' 제거 위해 [2:] 사용
print('2진수(10101) -> 16진수({})'.format(hex(int('10101', 2))[2:]))

# 문자열로 된 8진수를 먼저 10진수로 바꿔서 그걸 2진수로 변환해서 출력. '0b' 제거 위해 [2:] 사용
print('8진수(675) -> 2진수({})'.format(bin(int('675', 8))[2:]))
# 8진수를 먼저 10진수로 바꿔서 그걸 16진수로 변환해서 출력. '0x' 제거 위해 [2:] 사용
print('8진수(675) -> 16진수({})'.format(hex(int('675', 8))[2:]))
```

```python
10진수 입력: 15
2진수 : 0b1111
8진수 : 0o17
16진수 : 0xf
2진수(10101) -> 10진수(21)
8진수(135) -> 10진수(93)
16진수(5f) -> 10진수(95)
2진수(10101) -> 8진수(25)
2진수(10101) -> 16진수(15)
8진수(675) -> 2진수(110111101)
8진수(675) -> 16진수(1bd)
```

### 등차수열

> **사용자가 임의로 생성한 등차수열의 일반항, n번째 항의 값과 합을 구하는 프로그램 만들기**
> 

```python
# 사용자로부터 첫 번째 항(a1), 공차(d), 구하고 싶은 항의 위치(n)을 입력
a1 = int(input("첫 번째 항을 입력하세요: "))
d = int(input("공차를 입력하세요: "))
n = int(input("구하고 싶은 항의 위치를 입력하세요: "))

# 빈 리스트를 생성 이 리스트에 n번째 항까지의 수열 값을 저장
sequence = []

# for문을 사용하여 n번째 항까지의 등차수열 값을 계산하고 리스트에 추가
for i in range(1, n+1):
    an = a1 + (i-1)*d
    sequence.append(an)

# n번째 항의 값과 n번째 항까지의 등차수열을 출력
print("n번째 항의 값은 ", sequence[-1])
print("n번째 항까지의 등차수열: ", sequence)

# 등차수열의 합 공식인 S_n = n/2*(2*a1 + (n-1)*d)를 사용하여 n번째 항까지의 합을 계산
s_n = n/2*(2*a1 + (n-1)*d)
print("n번째 항까지의 합은 ", s_n)
```

```python
첫 번째 항을 입력하세요: 1
공차를 입력하세요: 3
구하고 싶은 항의 위치를 입력하세요: 10
n번째 항의 값은  28
n번째 항까지의 등차수열:  [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
n번째 항까지의 합은  145.0
```

### 등비수열

> **사용자가 임의로 생성한 등차수열의 일반항, n번째 항의 값과 합을 구하는 프로그램 만들기**
> 

```python
def get_nth_term(a1, ratio, n):
    return a1 * (ratio ** (n - 1))  # n번째 항 계산

def get_sum_to_nth(a1, ratio, n):
    # 등비수열의 합 공식
    if ratio == 1:  # 공비가 1인 경우
        return a1 * n
    return a1 * (ratio ** n - 1) // (ratio - 1)  # n번째 항까지의 합 계산

# 사용자로부터 입력 받기
a1 = int(input("첫 번째 항(a1) 값을 입력: "))
ratio = int(input("공비(ratio) 값을 입력: "))
n = int(input("n번째 항을 알고 싶은 값을 입력: "))

# n번째 항까지의 등비수열 출력
sequence = [get_nth_term(a1, ratio, i) for i in range(1, n+1)]
print(f"1부터 {n}번째 항까지의 등비수열: {sequence}")
print(f"1부터 {n}번째 항까지의 합: {get_sum_to_nth(a1, ratio, n)}")
```

```python
첫 번째 항(a1) 값을 입력: 2
공비(ratio) 값을 입력: 3
n번째 항을 알고 싶은 값을 입력: 6
1부터 6번째 항까지의 등비수열: [2, 6, 18, 54, 162, 486]
1부터 6번째 항까지의 합: 728
```

### 시그마

> **사용자가 임의로 지정한 a1, 공비, n번째 항을 기준으로 값을 출력하는 프로그램 만들기**
> 

```python
def compute_sequence_value_and_sum(a1, ratio, n):
    # n번째 항의 값을 계산
    nth_value = a1 * (ratio ** (n - 1))
    # 1부터 n번째 항까지의 합계 계산
    total_sum = a1 * (ratio ** n - 1) / (ratio - 1)

    return nth_value, total_sum

def main():
    # 사용자로부터 a1, 공비, n 입력받기
    a1 = int(input("첫 번째 항(a1) 값을 입력하세요: "))
    ratio = int(input("공비를 입력하세요: "))
    n = int(input("몇 번째 항(n)까지의 값을 알고 싶은지 입력하세요: "))

    # 계산 함수 호출
    nth_value, total_sum = compute_sequence_value_and_sum(a1, ratio, n)

    # 결과 출력 (1000단위마다 쉼표 추가)
    print(f"{n}번째 항의 값: {format(nth_value, ',')}")
    print(f"1부터 {n}번째 항까지의 합: {format(total_sum, ',')}")

# 프로그램 실행
main()
```

```python
첫 번째 항(a1) 값을 입력하세요: 2
공비를 입력하세요: 2
몇 번째 항(n)까지의 값을 알고 싶은지 입력하세요: 30
30번째 항의 값: 1,073,741,824
1부터 30번째 항까지의 합: 2,147,483,646.0
```

### 계차수열

> **사용자가 입력한 수열의 계차를 추론하여 계산하기**
> 

```python
def find_differences(seq):
    """수열의 차를 구하는 함수"""
    # 인접한 항목 간의 차를 계산
    return [seq[i+1] - seq[i] for i in range(len(seq)-1)]

def determine_pattern(differences):
    """2차 계차수열의 계수를 찾는 함수"""
    # 차의 차 (2차 계차)를 계산
    second_diff = find_differences(differences)
    
    # 2차 방정식의 계수 a를 찾음 (2차 계차 / 2)
    a = second_diff[0] / 2
    
    # 2차 방정식의 계수 b를 찾음 (첫 번째 차 - 2 * a)
    b = differences[0] - 3 * a
    
    # 2차 방정식의 계수 c를 찾음 (첫 번째 항목 - a - b)
    c = seq[0] - b - a
    
    return a, b, c

def nth_term_formula(n, a, b, c):
    """2차 방정식 형태의 일반항을 계산하는 함수"""
    # an^2 + bn + c 형태의 2차 방정식으로 n항의 값을 계산
    return a*n**2 + b*n + c

def get_series_value(seq, n):
    """주어진 수열과 n 값을 바탕으로 n항의 값을 계산하는 함수"""
    # 수열의 차를 구함
    differences = find_differences(seq)
    
    # 2차 계차수열의 계수를 찾음
    a, b, c = determine_pattern(differences)
    
    # n항의 값을 계산
    value = nth_term_formula(n, a, b, c)
    
    # 값을 쉼표로 구분된 형식으로 반환
    return format(int(value), ",")

# 사용자로부터 수열의 처음 4~5개 항목을 입력받음
seq = [int(x) for x in input("수열의 처음 4~5개 항목을 쉼표로 구분하여 입력하세요: ").split(",")]
# 알고 싶은 회차의 값을 입력받음
n = int(input("알고 싶은 회차의 값을 입력하세요: "))

# 결과 출력
print(get_series_value(seq, n))
```

```python
수열의 처음 4~5개 항목을 쉼표로 구분하여 입력하세요: 2,5,11,20
알고 싶은 회차의 값을 입력하세요: 11
167
```

### 피보나치수열

```python
# 사용자로부터 n값을 입력받음.
inputN = int(input('n 입력 :'))

# n번째 피보나치 수와 n항까지의 합을 저장할 변수 초기화
valueN = 0
sumN = 0

# n-2와 n-1의 피보나치 수를 저장할 변수 초기화
valuePreN2 = 0
valuePreN1 = 0

# 피보나치 수열의 시작 항 설정
n = 1
# n이 사용자가 입력한 값(inputN)까지 반복
while n <= inputN:
    # 첫 번째와 두 번째 항의 경우 값이 1이므로 예외 처리
    if n == 1 or n ==2:
        valueN = 1
        # 현재 값(1)을 두 개의 이전 항 변수에 모두 할당
        valuePreN2 = valueN
        valuePreN1 = valueN
        # n항의 값을 총 합에 더하기
        sumN += valueN
        # 다음 항으로 이동
        n += 1
        
    else:
        # n-2 항과 n-1 항의 합을 현재 항의 값으로 설정
        valueN = valuePreN2 + valuePreN1
        # 현재의 n-1 항 값을 n-2 항 변수에 할당
        valuePreN2 = valuePreN1
        # 현재 항의 값을 n-1 항 변수에 할당
        valuePreN1 = valueN
        # 현재 항의 값을 총 합에 더하기
        sumN += valueN
        # 다음 항으로 이동
        n += 1

# n번째 항의 값과 n항까지의 합을 출력
print('{}번째 항의 값: {}'.format(inputN, valueN))    
print('{}번째 항까지의 합: {}'.format(inputN, sumN))
```

```python
n 입력 :10
10번째 항의 값: 55
10번째 항까지의 합: 143
```

### 팩토리얼

> • 팩토리얼을 구현하는 파이썬 프로그램을 만들되, 반복문을 이용한 함수와 재귀함수를 이용해서 구현하고, 파이썬에서 제공하는 모듈을 사용해서 만들기
> 

```python
# 반복문을 이용한 팩토리얼
def facFun1(n):
    
    fac = 1                 # 초기 팩토리얼 값 설정
    for n in range(1, n + 1): # 1부터 입력된 n까지 반복
        fac = fac * n          # 현재 fac 값에 n을 곱함
        
    return fac                # 계산된 팩토리얼 값 반환
    
    
num = int(input('input number: '))  # 사용자로부터 숫자 입력 받기
print(f'{num}!: {facFun1(num)}')    # 입력 받은 숫자의 팩토리얼 출력
```

```python
input number: 6
6!: 720
```

```python
# 재귀함수를 이용한 팩토리얼
def facFun2(n):
    
    if n == 1:                  # n이 1일 경우
        return n                 # n 반환 (재귀 종료 조건)
        
    return n * facFun2(n - 1)     # n과 facFun2(n-1)의 결과값을 곱하여 반환
    
num = int(input('input number: '))  # 사용자로부터 숫자 입력 받기
print(f'{num}!: {facFun2(num)}')    # 입력 받은 숫자의 팩토리얼 출력
```

```python
input number: 6
6!: 720
```

```python
import math                           # math 모듈 가져오기

def facFun3(n):
    result = math.factorial(n)        # math 모듈의 factorial 함수 사용
    return "{:,}".format(result)      # 결과값을 쉼표로 구분하여 반환

num = int(input('input number: '))  # 사용자로부터 숫자 입력 받기
print(f'{num}!: {facFun3(num)}')    # 입력 받은 숫자의 팩토리얼 출력
```

```python
input number: 6
6!: 720
```

### 군수열

> 아래의 수열의 합이 최초 100을 초과하는 n번째 항의 값과 n을 출력하는 프로그램 만들기
> 
> 
> <수열>
> 
> $\frac{1}{1},\frac{1}{2},\frac{2}{1},\frac{1}{3},\frac{3}{1},\frac{1}{4},\frac{2}{3},\frac{3}{2},\frac{4}{1},\frac{1}{5},\frac{2}{4}...$
> 

```python
def find_term_exceeding_sum(target_sum):
    term = 1           # 항의 번호 초기화
    total_sum = 0      # 합계 초기화
    
    while True:        # 무한 반복
        # 대각선 항 계산
        for i in range(term, 0, -1):
            current_value = i / (term + 1 - i)  # 현재 항의 값 계산
            total_sum += current_value          # 합계에 현재 항 더하기
            if total_sum > target_sum:          # 합계가 목표값을 초과하는지 확인
                return current_value, term       # 초과한다면 현재 항의 값과 번호 반환
        
        term += 1       # 항의 번호 증가

def display_result():
    value, term_number = find_term_exceeding_sum(100)   # 함수 호출로 항의 값과 번호 획득
    formatted_value = "{:,.2f}".format(value)           # 값의 포맷 지정 (쉼표와 소수점 두자리까지 표시)
    print(f"{term_number}번째 항의 값은 {formatted_value}이고, 합이 최초로 100을 초과합니다.")

display_result()
```

```python
10번째 항의 값은 2.67이고, 합이 최초로 100을 초과합니다.
```

### 순열

> • 카드 7장을 일렬로 나열하되, 2,4,7 카드가 서로 이웃하도록 나열하는 모든 경우의 수를 구하는 프로그램 만들기
> 
> 
> <문제 풀이 로직>
> 
> 1. 2, 4, 7이 서로 이웃하는 경우의수 (6가지) 구하기
> 2. 각 경우의 수별로 나머지 카드를 배치하는 경우의 수 계산
> 3. 모든 경우의 수를 합하여 결과 출력

```python
# permutations 함수를 사용(주어진 데이터에서 순열을 구하는 함수)
from itertools import permutations

def find_adjacent_cases():
    # 로직 1: 2, 4, 7이 서로 이웃하는 6가지 경우의 수를 먼저 구한다.
    print("\n로직 1: 2, 4, 7이 서로 이웃하는 6가지 경우의 수를 먼저 구한다.")
    
    # 1부터 7까지의 숫자로 모든 순열(7개를 선택하는) 구하기
    all_cases = permutations(range(1, 8), 7)
    valid_cases = []
    
    # 각 순열을 확인
    for case in all_cases:
        # 5번째 위치까지만 2,4,7의 조합이 시작될 수 있기 때문에 5번 반복
        for i in range(5):
            # 연속된 3개의 카드가 2,4,7인 경우를 확인
            if set(case[i:i+3]) == {2, 4, 7}:
                # 해당 경우를 유효한 경우의 수로 추가
                valid_cases.append(case)
                break
                
    return valid_cases

def calculate_remaining_cases(valid_cases):
    # 로직 2: 각 경우의 수에 대하여 나머지 카드를 배치하는 경우의 수를 계산한다.
    print("\n로직 2: 각 경우의 수에 대하여 나머지 카드를 배치하는 경우의 수를 계산한다.")
    return len(valid_cases)

def format_thousands(num):
    # 숫자를 1000단위마다 쉼표로 구분하는 문자열로 변환
    return "{:,}".format(num)

def count_valid_cases():
    valid_cases = find_adjacent_cases()
    result = calculate_remaining_cases(valid_cases)
    
    # 로직 3: 모든 경우의 수를 합하여 결과를 출력한다.
    print("\n로직 3: 모든 경우의 수를 합하여 결과를 출력한다.\n")
    print(f"카드 7장을 일렬로 나열하되, 2, 4, 7 카드가 서로 이웃하도록 나열하는 경우의 수는 총 {format_thousands(result)}가지 입니다.")

# 실행
count_valid_cases()
```

```python
로직 1: 2, 4, 7이 서로 이웃하는 6가지 경우의 수를 먼저 구한다.

로직 2: 각 경우의 수에 대하여 나머지 카드를 배치하는 경우의 수를 계산한다.

로직 3: 모든 경우의 수를 합하여 결과를 출력한다.

카드 7장을 일렬로 나열하되, 2, 4, 7 카드가 서로 이웃하도록 나열하는 경우의 수는 총 720가지 입니다.
```

### 조합

> ${}_9C_4 와 {}_6C_2 를 구하는 프로그램 만들기$
조합을 구하는 공식은 ${}_nC_k = \frac{n!}{k!(n-k)!}$
> 
> 
> 여기서 𝑛! 는 팩토리얼로 𝑛×(𝑛−1)×⋯×2×1 을 의미
> 

```python
# 팩토리얼 함수 정의
def factorial(num):
    result = 1
    for i in range(1, num + 1): # 1부터 num까지 반복
        result *= i # 곱셈 연산 수행
    return result

# 조합 함수 정의
def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k)) # 조합 공식 계산

# 1000단위마다 쉼표를 넣는 함수 정의
def format_with_comma(num):
    return format(num, ',') # 쉼표 포맷 사용

# 실행 함수 정의
def calculate_combinations():
    comb1 = combination(9, 4) # 9C4 계산
    comb2 = combination(6, 2) # 6C2 계산

    # 결과 출력
    print("9C4 = ", format_with_comma(comb1))
    print("6C2 = ", format_with_comma(comb2))

# 함수 실행
calculate_combinations()
```

```python
9C4 =  126
6C2 =  15
```

### 확률

> 박스에 '꽝'이 적힌 종이가 6장있고, '선물'이 적힌 종이가 4장 있을때, 파이썬을 이용해 꽝 3장과 선물 3장을 뽑는 확률 출력하기
> 
> 
> 문제를 해석하면 '꽝' 3장과 '선물' 3장을 뽑는 확률을 구하라는 것으로 이를 조합의 개념을 사용해 풀어낼 수 있음.
> 

```python
# math 모듈에서 comb 함수(조합 계산)를 가져옴
from math import comb

def calculate_probability():
    # '꽝' 3장을 뽑는 경우의 수 계산
    cases_losers = comb(6, 3)
    print(f"'꽝' 3장을 뽑는 경우의 수: {cases_losers}")
    
    # '선물' 3장을 뽑는 경우의 수 계산
    cases_gifts = comb(4, 3)
    print(f"'선물' 3장을 뽑는 경우의 수: {cases_gifts}")
    
    # 꽝 3장과 선물 3장을 뽑는 경우의 수 계산
    selected_cases = cases_losers * cases_gifts
    print(f"'꽝' 3장과 '선물' 3장을 동시에 뽑는 경우의 수: {selected_cases}")
    
    # 전체 경우의 수 계산
    total_cases = comb(10, 6)
    print(f"전체 경우의 수: {total_cases}")
    
    # 확률 계산
    probability = selected_cases / total_cases
    print(f"확률: {probability:.5f}")
    
    return probability

def formatted_print(probability):
    # 확률을 백분율로 변환 후 쉼표로 1000단위 구분하여 출력
    formatted_probability = "{:,.2f}".format(probability * 100)
    print(f"확률 (포맷 변환 후): {formatted_probability}%")

if __name__ == "__main__":
    probability = calculate_probability()
    formatted_print(probability)
```

```python
'꽝' 3장을 뽑는 경우의 수: 20
'선물' 3장을 뽑는 경우의 수: 4
'꽝' 3장과 '선물' 3장을 동시에 뽑는 경우의 수: 80
전체 경우의 수: 210
확률: 0.38095
확률 (포맷 변환 후): 38.10%
```

# ✍️ 오늘의 혼잣말

---

- 수학적 개념을 파이썬으로 풀어내는 것은 상당히 복잡한 작업이다.
- 이번 개념을 익히고 연습하면서 드는 가장 큰걱정은 어떻게 써먹어야 할지 자체를 모르면 어쩌지? 라는 생각
- 이건 약간은 수학적 머리랑 연관된 부분이라 어떤 문제를 보고 “아~ 이건 순열 개념으로 풀어야 쉽겠다!” 라는 생각이 들어야 할텐데, 그런 부분을 잘 모르겠다.
- 이번에 강의들을때도 문제들을 보면 ‘순열’파트 니까 ‘순열로 풀겠거니’ 생각은 하지만 솔직히 바로 바로 떠오르진 않았다.
- 결국 여기는 경험의 영역이 아닐까 싶다. 지금의 나로선 당장 드라마틱하게 해결할 수 없는 부분이므로 그저 지금 배우는 내용들을 잘 습득하려 애를 쓰는게 최선!