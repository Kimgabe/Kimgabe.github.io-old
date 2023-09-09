---
layout : single
title:  "[스터디노트] Day6 파이썬 기초문제 풀이 (연산자, 조건문, 반복문)"
categories: studynote
toc: true
highlight: false
header:
  teaser: /assets/images/unsplash/study_note.jpg
  overlay_image: /assets/images/unsplash/study_note.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/842ofHC6MaI)"
tags:
  - 조건식
  - Condition Evaluation
  - 조건식(if문)
  - Conditional Statement (if)
  - 양자택일 조건문 (if~else문)
  - Binary Conditional Statement (if~else)
  - if~else문과 조건식
  - Conditional Structure with if~else
  - 다자택일 조건문(if~elif문)
  - Multiple Choice Conditional Statement (if~elif)
  - 중첩 조건문
  - Nested Conditional Statement
  - 반복문
  - Loop or Iteration
  - for loop
  - while loop
---

다양한 연산자, 조건문, 반복문 등 그동안 배운 개념을 응용한 파이썬 문제풀이

# 💡공부한 내용

---

- 아래의 파이썬 기초개념들을 응용한 실습 문제 풀이
    - 연산자 (산술연산자, 비교 연산자, 논리 연산자)
    - 조건문 (if, if~else, elif, while)
    - 반복문 (for, while)

# 📝 오늘의 하이라이트

---

<aside>
💡 강의에 나오는 문제를 다양한 파이썬 기초 내용을 바탕으로 재구성해서 풀어보기

</aside>

## 1. 상품가격과 지불금액을 입력하면 거스름돈을 계산하는 프로그램 만들기

- 거스름돈은 지폐와 동전 개수를 최소로 하고, 1원단위는 절사해야 함.

```python
def calculate_change():
    # 상품가격 입력
    while True:
        product_price = input("상품가격을 입력하세요: ")
        if not product_price.isdigit():
            print("상품가격은 숫자로만 입력해야 합니다. 다시 입력해주세요.")
        else:
            break

    # 지불금액 입력
    while True:
        payment_amount = input("지불금액을 입력하세요: ")
        if not payment_amount.isdigit():
            print("지불금액은 숫자로만 입력해야 합니다. 다시 입력해주세요.")
        elif int(payment_amount) < int(product_price):
            print("지불금액이 상품가격보다 작습니다. 다시 입력해주세요.")
        else:
            break

    # 거스름돈 계산
    change = int(payment_amount) - int(product_price)
    change_floor = change // 10 * 10  # 원단위 절사

    # 지폐와 동전 개수 계산
    counts = [0] * 7
    if change_floor >= 50000:
        counts[0] = change_floor // 50000
        change_floor -= counts[0] * 50000
    if change_floor >= 10000:
        counts[1] = change_floor // 10000
        change_floor -= counts[1] * 10000
    if change_floor >= 5000:
        counts[2] = change_floor // 5000
        change_floor -= counts[2] * 5000
    if change_floor >= 1000:
        counts[3] = change_floor // 1000
        change_floor -= counts[3] * 1000
    if change_floor >= 500:
        counts[4] = change_floor // 500
        change_floor -= counts[4] * 500
    if change_floor >= 100:
        counts[5] = change_floor // 100
        change_floor -= counts[5] * 100
    if change_floor >= 10:
        counts[6] = change_floor // 10
        change_floor -= counts[6] * 10

    # 결과 출력
    print("\n")
    print("------------거스름 돈-------------")
    print(f"거스름돈 : {change}원 (원단위 절사)")
    print(f"50,000원권 : {counts[0]}장")
    print(f"10,000원권 : {counts[1]}장")
    print(f"5,000원권 : {counts[2]}장")
    print(f"1,000원권 : {counts[3]}장")
    print(f"500원 동전 : {counts[4]}개")
    print(f"100원 동전 : {counts[5]}개")
    print(f"10원 동전 : {counts[6]}개")
    print("----------------------------------")

# 함수 호출
calculate_change()
```

- 강의는 조건문을 응용해서 풀이하였고 이를 `반복문(for문)`으로 바꿔서 풀어보기

```python
def calculate_change():
    # 상품가격 입력
    while True:
        product_price = input("상품가격을 입력하세요: ")
        if not product_price.isdigit():
            print("상품가격은 숫자로만 입력해야 합니다. 다시 입력해주세요.")
        else:
            break

    # 지불금액 입력
    while True:
        payment_amount = input("지불금액을 입력하세요: ")
        if not payment_amount.isdigit():
            print("지불금액은 숫자로만 입력해야 합니다. 다시 입력해주세요.")
        elif int(payment_amount) < int(product_price):
            print("지불금액이 상품가격보다 작습니다. 다시 입력해주세요.")
        else:
            break

    # 거스름돈 계산
    change = int(payment_amount) - int(product_price)
    change_floor = change // 10 * 10  # 원단위 절사

    # 지폐와 동전 개수 계산
    denominations = [50000, 10000, 5000, 1000, 500, 100, 10] #지폐 및 동전 종류
    counts = [] # 개수 
    for denomination in denominations:
        # 거스름돈을 각 지폐&동전별 로 나누어 개수를 count에 저장
        # 거스름돈(change_floor)이 32,765원 기준
        # denomination 50,000의 count값은 0
        count = change_floor // denomination
        counts.append(count)
        # denomination 을 제외한 나머지 거스름돈 계산
        change_floor -= count * denomination
        # 남은 denomination에 대해 반복 적용하며 각 종류별 개수 도출

    # 결과 출력
    print("\n")
    print("------------거스름 돈-------------")
    print(f"거스름돈 : {change}원 (원단위 절사)")
    print(f"50,000원권 : {counts[0]}장")
    print(f"10,000원권 : {counts[1]}장")
    print(f"5,000원권 : {counts[2]}장")
    print(f"1,000원권 : {counts[3]}장")
    print(f"500원 동전 : {counts[4]}개")
    print(f"100원 동전 : {counts[5]}개")
    print(f"10원 동전 : {counts[6]}개")
    print("----------------------------------")

# 함수 호출
calculate_change()
```

---

## 2. 성적계산 및 비교하는 프로그램 만들기

- 국어, 영어, 수학점수 입력 후 총점, 평균, 최고점수과목, 최저점수 과목, 최고점수와 최저점수 차이를 출력하는 코드 만들기
- fstring을 최대한 응용해서 진짜 프로그램처럼 만들어 보기

```python
def calculate_grades():
    # 국어 점수 입력
    korean = int(input("국어 점수: "))

    # 영어 점수 입력
    english = int(input("영어 점수: "))

    # 수학 점수 입력
    math = int(input("수학 점수: "))

    # 총점 계산
    total = korean + english + math

    # 평균 계산
    average = total / 3

    # 최고 점수와 최저 점수 구하기
    max_score = 0
    min_score = 100
    
    # 최고점 구하기
    # 과목별로 점수를 비교하며 max_score를 갱신
    if korean > max_score:
        max_score = korean
    if english > max_score:
        max_score = english
    if math > max_score:
        max_score = math

    # 최저점 구하기
    # 과목별로 점수를 비교하며 min_score를 갱신
    if korean < min_score:
        min_score = korean
    if english < min_score:
        min_score = english
    if math < min_score:
        min_score = math

    # 최고, 최저 점수 차이 계산
    score_difference = max_score - min_score

    # 결과 출력
    print("\n------------성적 계산기-------------")
    print("국어 점수 : {} 점".format(korean))
    print("영어 점수 : {} 점".format(english))
    print("수학 점수 : {} 점".format(math))
    print("총점 : {} 점".format(total))
    print("평균 : {:.2f} 점".format(average))
    print("----------------------------------------")
    print("최고 점수 과목(점수) : ", end="")
    if korean == max_score:
        print("국어({}점)".format(max_score))
    elif english == max_score:
        print("영어({}점)".format(max_score))
    else:
        print("수학({}점)".format(max_score))

    print("최저 점수 과목(점수) : ", end="")
    if korean == min_score:
        print("국어({}점)".format(min_score))
    elif english == min_score:
        print("영어({}점)".format(min_score))
    else:
        print("수학({}점)".format(min_score))

    print("최고, 최저 점수 차이 : {}점".format(score_difference))

# 함수 호출
calculate_grades()
```

---

## 3. 수학문제 계산 풀이 프로그램 만들기

- 197개의 빵과 152개의 우유를 17명의 학생에게 동일하게 나눠줘야함. 한명의 학생이 갖게 되는 빵과 우유 개수를 구하고 남는 빵과 우유 개수 출력하기.

```python
def distribute_bread_and_milk():
    bread_count = 197
    milk_count = 152
    student_count = 17

    bread_per_student = bread_count // student_count
    milk_per_student = milk_count // student_count

    remaining_bread = bread_count % student_count
    remaining_milk = milk_count % student_count

    print("한 명의 학생이 받는 빵의 개수: {}개".format(bread_per_student))
    print("한 명의 학생이 받는 우유의 개수: {}개".format(milk_per_student))
    print("남는 빵의 개수: {}개".format(remaining_bread))
    print("남는 우유의 개수: {}개".format(remaining_milk))

distribute_bread_and_milk()
```

---

## 4. 과목점수를 입력하면 각종 지표를 계산해주는 프로그램 만들기

- 반복문을 응용해서 한줄씩 과목별 지표 계산 결과를 도출하기

```python
def calculate_scores(국어, 영어, 수학, 과학, 국사):
    # 평균 점수들
    avg_scores = {'국어': 85, '영어': 82, '수학': 89, '과학': 75, '국사': 94}

    # 입력 점수들
    scores = [국어, 영어, 수학, 과학, 국사]
    subjects = ['국어', '영어', '수학', '과학', '국사']

    # 총점과 평균
    total = sum(scores)
    average = total / len(scores)

    print('-' * 70)
    print("총점:", total, f"(평균과의 편차: {total - average * len(scores)})")

    # 과목별 점수와 평균과의 편차 출력
    for i, subject in enumerate(subjects):
        print(f"{subject}: {scores[i]}({scores[i] - avg_scores[subject]})", end=', ')
    print('\n' + '-' * 70)

    # 각 과목별 편차와 막대그래프
    for i, subject in enumerate(subjects):
        deviation = scores[i] - avg_scores[subject]

        # 편차에 따른 막대그래프 생성
        if deviation >= 0:
            graph = '+' * int(deviation)
        else:
            graph = '-' * int(abs(deviation))
        
        print(f"{subject} 편차: {graph}({deviation})")  # 과목명을 직접 넣음
    print('-' * 70)

# 예시로 함수 호출
calculate_scores(100, 60, 70, 50, 80)
```

```python
----------------------------------------------------------------------
총점: 360 (평균과의 편차: 0.0)
국어: 100(15), 영어: 60(-22), 수학: 70(-19), 과학: 50(-25), 국사: 80(-14), 
----------------------------------------------------------------------
국어 편차: +++++++++++++++(15)
영어 편차: ----------------------(-22)
수학 편차: -------------------(-19)
과학 편차: -------------------------(-25)
국사 편차: --------------(-14)
----------------------------------------------------------------------
```

---

## 5. 난수를 이용해서 홀짝 게임 구현하기

- 실제 강의에서 정답 코드는 if~elif를 응용해서 모든 경우에 대해 작성을 했지만, 최대한 간결하게 작성하고 싶었다.

```python
import random

def odd_even_game(user_choice):
    # 난수 생성 (1부터 100 사이)
    random_number = random.randint(1, 100)
    
    # 난수가 홀수인지 짝수인지 판별
    if random_number % 2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    
    # 사용자의 선택과 난수의 홀짝 판별 결과가 일치하는지 확인
    if user_choice == result:
        print(f"빙고!! 결과는 {random_number} {result}!! 였습니다.")
    else:
        print(f"실패!! 결과는 {random_number} {result}!! 였습니다.")

# 사용자로부터 홀/짝 선택 입력 받기
user_choice = input("홀수 또는 짝수를 선택하세요(홀수/짝수): ")

# 홀짝 게임 함수 호출
odd_even_game(user_choice)
```

---

## 6. 미세먼지 기준치에 따른 차량운행 가능여부 판별 프로그램 만들기

- 미세먼지 수치, 차량종류, 차량번호를 입력하면 아래의 조건에 따라 운행 가능 여부 출력

<조건>

- 미세먼지 측정 수치가 150 이하면 차량 5부제 실시
- 미세먼지 측정 수치가 150을 초과하면 차량 2부제 실시
- 차량 2부제를 실시하더라도 영업용 차량은 5부제 실시


```python
from datetime import datetime

def check_driving_availability():
    fine_dust = int(input("미세먼지 수치 입력: "))
    vehicle_type = int(input("차량 종류 선택(1. 승용차, 2. 영업용차): "))
    vehicle_number = int(input("차량 번호 입력: ")) # 4자리 차량 번호

    print("-" * 50)
    current_time = datetime.now() # 현재 시간을 얻음
    print(current_time.strftime('%Y년 %m월 %d일 %H시 %M분 %S.%f초')) # 현재 시간 출력
    print("-" * 50)

    # 오늘 날짜를 기준으로 2부제 또는 5부제 판단
    today_date = current_time.day
    if fine_dust > 150:
        # 미세먼지 수치가 150 초과인 경우 2부제 적용
        even_odd = 2
        print("차량2부제 적용")
    else:
        # 미세먼지 수치가 150 이하인 경우 5부제 적용
        even_odd = 5

    # 영업용 차량은 무조건 5부제 적용
    if vehicle_type == 2:
        even_odd = 5

    # 운행 가능 여부 판단
    if even_odd == 2 and today_date % 2 != vehicle_number % 2:
        print("차량 2부제로 금일 운행제한 대상 차량입니다!")
    elif even_odd == 5 and today_date % 5 == vehicle_number % 5:
        print("차량 5부제로 금일 운행제한 대상 차량입니다!")
    else:
        print("금일 운행 가능합니다!")

    print("-" * 50)
    
check_driving_availability()
```


```python
미세먼지 수치 입력: 200
차량 종류 선택(1. 승용차, 2. 영업용차): 1
차량 번호 입력: 5859
--------------------------------------------------
2023년 07월 09일 01시 23분 10.943995초
--------------------------------------------------
차량2부제 적용
금일 운행 가능합니다!
--------------------------------------------------
```

- 조건문을 통해 미세먼지 수치에 따른 판별을 하도록 구현하는 것은 그리 어렵지 않았다.
- 문제는 ‘오늘 날짜’ 에 따른 차량 2부제 또는 5부제를 결정하는 것
    - 차량 2부제와 5부제의 기준을 논리로 구현해야 하는 것이 조금 헷갈렸다.

---

## 7. **PC에서 생성한 난수를 사용자가 맞추는 게임 구현하기**

- C가 난수 1~1000을 발생하면, 사용자가 숫자(정수)를 입력한다.
- 사용자가 난수를 맞추면 게임이 종료된다.
- 만약, 못 맞추게 되면 난수와 사용자 숫자의 크고 작음을 출력한 후 사용자한데 다시 기회를 준다.
- 최종적으로 사용자가 시도한 횟수를 출력한다.

```python
import random

# PC가 난수 1~1000을 발생하고, 사용자가 숫자(정수)를 입력하여 난수를 맞추는 함수
def guess_random_number():
    pc_number = random.randint(1, 1000)  # PC가 1에서 1000 사이의 난수를 생성

    tries = 0  # 시도 횟수 초기화

    while True:
        user_guess = int(input("숫자를 입력하세요: "))  # 사용자가 숫자(정수)를 입력

        tries += 1  # 시도 횟수 증가

        if user_guess == pc_number:  # 사용자 입력값과 난수가 일치하면
            print(f"축하합니다! 정답을 맞추셨습니다. 사용한 횟수: {tries}")
            break  # 게임 종료
        elif user_guess > pc_number:  # 사용자 입력값이 난수보다 크면
            print("난수보다 작습니다.")
        else:  # 사용자 입력값이 난수보다 작으면
            print("난수보다 큽니다.")

guess_random_number()
```

```python
난수를 맞춰보세요 (1~1000): 500
난수보다 작습니다.
난수를 맞춰보세요 (1~1000): 750
난수보다 작습니다.
난수를 맞춰보세요 (1~1000): 865
난수보다 작습니다.
난수를 맞춰보세요 (1~1000): 950
난수보다 큽니다.
난수를 맞춰보세요 (1~1000): 900
난수보다 큽니다.
난수를 맞춰보세요 (1~1000): 890
난수보다 큽니다.
난수를 맞춰보세요 (1~1000): 874
난수보다 작습니다.
난수를 맞춰보세요 (1~1000): 880
난수보다 작습니다.
난수를 맞춰보세요 (1~1000): 885
난수보다 작습니다.
난수를 맞춰보세요 (1~1000): 888
난수보다 큽니다.
난수를 맞춰보세요 (1~1000): 886
난수보다 작습니다.
난수를 맞춰보세요 (1~1000): 887
축하합니다! 정답을 맞추셨습니다. 사용한 횟수: 12
```

- 접근 방식은 정석이 맞는데 매번 내가 입력한 값과 난수를 비교해서 수를 입력하는 단순한 로직인데 판단이 오래걸렸다.
- 그래서 이걸 그냥 컴퓨터가 동일한 논리로 하면 훨씬 빠르지 않을까? 라는 생각에 혼자 프로그램 추가 생성

```python
def solve_random_number(pc_number):
    # 난수를 맞추기 위한 범위 설정
    low = 1
    high = 1000
    tries = 0  # 시도 횟수 초기화

    while True:
        mid = (low + high) // 2  # 범위의 중간값 계산
        tries += 1  # 시도 횟수 증가

        if mid == pc_number:  # 중간값이 난수와 같다면 정답을 맞춘 경우
            print(f"축하합니다! 정답을 맞추셨습니다. 사용한 횟수: {tries}")
            return tries
        elif mid > pc_number:  # 중간값이 난수보다 크다면 난수는 중간값보다 작은 범위에 있음
            print(f"{mid}보다 작습니다.")
            high = mid - 1  # 범위를 중간값보다 작은 값으로 조정
        else:  # 중간값이 난수보다 작다면 난수는 중간값보다 큰 범위에 있음
            print(f"{mid}보다 큽니다.")
            low = mid + 1  # 범위를 중간값보다 큰 값으로 조정
```

```python
pc_number = random.randint(1, 1000) # 난수를 생성

solve_random_number(pc_number) # 난수를 추론
```

```python
500보다 큽니다.
750보다 작습니다.
625보다 작습니다.
562보다 큽니다.
593보다 큽니다.
609보다 큽니다.
617보다 작습니다.
613보다 작습니다.
축하합니다! 정답을 맞추셨습니다. 사용한 횟수: 9
```

- 수기로 입력하며 풀때는 1분 이상 걸렸지만, 코드로 구현하고 나니 1초도 안걸릴 정도로 간단한 로직으로도 풀 수 문제였다.
- 이런식의 간단, 단순 반복되는 작업이나 기초적인 알고리즘 적용이 가능한 부분에서는 확실히 컴퓨터를 따라갈수가 없는 것 같다.

# ✍️ 오늘의 혼잣말

---

- 그냥 문제 읽고 막연하게 생각나는데로 코드를 짜다보니 체계 적이지 못하거나 깔끔하지 않게 나오는 경우가 많아서 수정/보완 하느라 시간을 많이 잡아먹는다.
- 문제 요구사항을 명확하게 파악하고, 작성 구조 및 논리를 먼저 생각한 뒤에 한줄 한줄 작성하는 습관을 들여야 할 것 같다.
- 단순하게 강의만 듣고 쉐도잉하듯이 코딩하는것도 좋지만, 똑같은 문제를 다른 방식으로는 풀어볼 수 없을까를 고민해보려고 했다. 그 과정이 꽤 골치가 아팠지만 재밌기도 했다.