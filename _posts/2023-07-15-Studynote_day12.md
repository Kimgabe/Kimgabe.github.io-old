---
layout : single
title:  "[스터디노트] Day12 파이썬 중급문제 풀이(1~7)"
categories: [DS17_Bootcamp, Python Programming]
tag: [스터디노트, 문제풀이, 함수, 모듈, 클래스, 예외처리, 텍스트파일]
header :
    teaser : "/assets/img/studynote/studynote_day12.png"
---

# 💡공부한 내용

---

- 파이썬 중급 강의에서 배운 내용을 종합하여 문제풀이
    - 함수
    - 모듈
    - 클래스
    - 예외처리
    - 텍스트 파일 다루기

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

### 1. 함수

> 비행기 티켓 영수증을 출력하는 함수 만들기
> 
> 
> ---
> 
> - 함수 출력시 대상별 티켓값에 대한 기초정보가 제공되어야 함
> - input()을 이용해 각 대상자별 인원수를 입력받아야 함
> - 영수증은 각 대상별x인원별 total 요금이 얼마인지 한줄씩 출력한뒤, 총인원수, 총금액을 출력해야 함

```python
def print_receipt():
    
    # 가격정보 입력
    childPrice = 18000
    infantPrice = 25000
    adultPrice = 50000
    discountRate = 0.5
    
    # 사용자에게 가격정보 제공
    print("childPrice(24개월 미만):\t", "{:,}원".format(childPrice))
    print("infantPrice(만12세 미만):\t", "{:,}원".format(infantPrice))
    print("adultPrice(만12세 이후):\t", "{:,}원".format(adultPrice))
    print("국가 유공자 및 장애우 할인:\t", "50%")
    
    # 사용자에게 대상정보 입력 받기 = 차후 출력될 대상별 인원수 값
    infants = int(input('유아 입력 : '))
    infants_discount = int(input('할인대상 유아 입력 : '))
    children = int(input('소아 입력 : '))
    children_discount = int(input('할인대상 소아 입력 : '))
    adults = int(input('성인 입력 : '))
    adults_discount = int(input('할인 대상 성인 입력 : '))
    
    # 대상별 총 가격 계산
    total_infants = infants * childPrice + infants_discount * childPrice * discountRate
    total_children = children * infantPrice + children_discount * infantPrice * discountRate
    total_adults = adults * adultPrice + adults_discount * adultPrice * discountRate
    total_price = total_infants + total_children + total_adults
    total_people = infants + infants_discount + children + children_discount + adults + adults_discount
    
    # 영수증 출력
    # 대상별 x 인원별 가격 출력
    print("=" * 40)
    print("유아", infants, "명 요금:", "{:,}원".format(infants * childPrice))
    print("유아 할인 대상", infants_discount, "명 요금 :", "{:,}원".format(infants_discount * childPrice * discountRate))
    print("소아", children, "명 요금 :", "{:,}원".format(children * infantPrice))
    print("소아 할인 대상", children_discount, "명 요금 :", "{:,}원".format(children_discount * infantPrice * discountRate))
    print("성인", adults, "명 요금 :", "{:,}원".format(adults * adultPrice))
    print("성인 할인 대상", adults_discount, "명 요금 :", "{:,}원".format(adults_discount * adultPrice * discountRate))
    print("=" * 40)
    print("Total:", total_people, "명") # 총인원수
    print("Total Price :", "{:,}원".format(total_price)) # 총 가격

print_receipt()
```

```python
childPrice(24개월 미만):	 18,000원
infantPrice(만12세 미만):	 25,000원
adultPrice(만12세 이후):	 50,000원
국가 유공자 및 장애우 할인:	 50%
유아 입력 : 1
할인대상 유아 입력 : 1
소아 입력 : 2
할인대상 소아 입력 : 1
성인 입력 : 2
할인 대상 성인 입력 : 0
========================================
유아 1 명 요금: 18,000원
유아 할인 대상 1 명 요금 : 9,000.0원
소아 2 명 요금 : 50,000원
소아 할인 대상 1 명 요금 : 12,500.0원
성인 2 명 요금 : 100,000원
성인 할인 대상 0 명 요금 : 0.0원
========================================
Total: 7 명
Total Price : 189,500.0원
```

---

### 2. 모듈

> **상품 구매 개수에 따른 할인율을 적용하여 계산 결과가 나오는 프로그램 구현하기**
> 
> 
> ---
> 
> - 상품 구매 개수에 따라 할인율이 결정되는 모듈을 만들어야 함
> - 해당 모듈을 기반으로 계산 결과가 출력되어야 함
> - 아래는 구매개수별 할인율 참조표
>     
>     
>     | 구매개수 | 1개 | 2개 | 3개 | 4개 | 5개 이상 |
>     | --- | --- | --- | --- | --- | --- |
>     | 할인율(%) | 5 | 10 | 15 | 20 | 25 |

```python
# 모듈 만들기 : shopping_module.py

def calculate_discount(price, count):
    discount_rate = [5, 10, 15, 20, 25]
    if count == 1:
        rate = discount_rate[0]
    elif count == 2:
        rate = discount_rate[1]
    elif count == 3:
        rate = discount_rate[2]
    elif count == 4:
        rate = discount_rate[3]
    else:
        rate = discount_rate[4]
    discounted_price = price * (100 - rate) / 100
    return discounted_price, rate

def shopping():
    total_price = 0
    count = 0
    while True:
        choice = int(input("상품을 구매 하시겠어요? 1. 구매 2.종료 "))
        if choice == 1:
            price = int(input("상품 가격 입력  : "))
            total_price += price
            count += 1
        elif choice == 2:
            discounted_price, rate = calculate_discount(total_price, count)
            print(f"할인율 : {rate}%")
            print(f"합계 : {int(discounted_price)} 원")
            break
```

```python
# 모듈 불러와서 함수 실행하기

import shopping_module as sm

if __name__ == "__main__":
    sm.shopping()
```

```python
상품을 구매 하시겠어요? 1. 구매 2.종료 1
상품 가격 입력  : 1000
상품을 구매 하시겠어요? 1. 구매 2.종료 2
할인율 : 5%
합계 : 950 원
```

```python
상품을 구매 하시겠어요? 1. 구매 2.종료 1
상품 가격 입력  : 1000
상품을 구매 하시겠어요? 1. 구매 2.종료 1
상품 가격 입력  : 1500
상품을 구매 하시겠어요? 1. 구매 2.종료 1
상품 가격 입력  : 500
상품을 구매 하시겠어요? 1. 구매 2.종료 1
상품 가격 입력  : 2250
상품을 구매 하시겠어요? 1. 구매 2.종료 2
할인율 : 20%
합계 : 4200 원
```

### 3. 클래스

> **회원가입 클래스와 회원정보 관리하는 클래스 구현하기**
> 
> 
> ---
> 
> - 아래의 기능들이 구현되어야 함
>     - 회원가입 : ID(이메일 형식), 비밀번호 입력받아 회원가입
>     - 전체 회원 조회
>     - 로그인 : 아이디 및 비번 입력하여 로그인하고 로그인 성공/실패 메시지 출력
>     - 회원정보 삭제

```python
# 클래스 생성
# 회원정보 관리 프로그램
class Member: # Member class
    def __init__(self, i, p): # Member class constructor
        self.id = i # Member class attribute(id)
        self.pw = p # Member class attribute(pw)

# 회원정보 관리 모듈
class MemberRepository:
    # MemberRepository class constructor
    def __init__(self):
        self.members = {}
    
    # 회원가입 메서드
    def addMember(self, m):
        self.members[m.id] = m.pw
    
    # 로그인 메서드
    def loginMember(self, i, p):
        isMember = i in self.members
        # 로그인 검증
        if isMember and self.members[i] == p:
            print(f'{i} : Log-in success!!')
        # 아이디가 존재하지 않을 경우
        else:
            print(f'{i} : Log-in failed!!')
    # 회원정보 삭제 메서드            
    def removeMember(self, i, p): # 회원 정보 삭제 (비밀번호 일치 여부는 main 함수에서 확인)
        del self.members[i] # 아이디 삭제
    
    # 모든 회원 정보 출력 메서드    
    def printMembers(self): # 모든 회원 정보 출력
        for mk in self.members.keys(): # 모든 회원 정보 출력
            print(f'ID: {mk}') # 아이디 출력
            print(f'PW: {self.members[mk]}') # 비밀번호 출력
```

```python
# 아이디생성 및 등록

import member as mb
    
mess = mb.MemberRepository()

for i in range(3):
    mId = input('아이디 입력 : ')
    mPw = input('비밀번호 입력 : ')
    mem = mb.Member(mId, mPw)
    mess.addMember(mem)
    
mess.printMembers()
```

```python
아이디 입력 : abc@gmail.com
비밀번호 입력 : 1234
아이디 입력 : def@gmail.com
비밀번호 입력 : 1234
아이디 입력 : ghi@gmail.com
비밀번호 입력 : 1234
ID: abc@gmail.com
PW: 1234
ID: def@gmail.com
PW: 1234
ID: ghi@gmail.com
PW: 1234
```

```python
# 회원정보 확인

mess.printMembers()
```

```python
ID: abc@gmail.com
PW: 1234
ID: def@gmail.com
PW: 1234
ID: ghi@gmail.com
PW: 1234
```

```python
# 로그인
mess.loginMember('abc@gmail.com', '1234')
mess.loginMember('def@gmail.com', '1234')
mess.loginMember('ghi@gmail.com', '1234')
mess.loginMember('ghi@gmail.com', '123')
```

```python
abc@gmail.com : Log-in success!!
def@gmail.com : Log-in success!!
ghi@gmail.com : Log-in success!!
ghi@gmail.com : Log-in failed!!
```

```python
# 회원정보 삭제
mess.removeMember('abc@gmail.com','1234')

# 결과 확인
mess.printMembers()
mess.loginMember('abc@gmail.com', '1234')
```

```python
ID: def@gmail.com
PW: 1234
ID: ghi@gmail.com
PW: 1234
abc@gmail.com : Log-in failed!!
```

> 회원관리 클래스를 조금 더 현실성 있게 업그레이드 해보기
> 
> 
> ---
> 
> - 실제 인터넷에서 작동하는 것처럼 다양한 조건문과 로직을 넣어서 구현해보기
> - 입력한 아이디와 비밀번호에 조건(예: 특수문자,길이 등)을 구현하고 규칙에 맞지 않으면 오류 메시지 출력 및 재입력 하도록 구현
> - 회원정보 조회시 기존 정보와 조회에서 없는 경우 오류메시지 출력하기 등
> - 회원 가입 및 관리 클래스 : member_management.py
>     - SignUP : 회원가입
>     - MemberManagement : 회원정보 조회, 로그인 검증, 회원정보 삭제

```python
# member_management.py 코드

import re  # 정규 표현식 사용을 위한 모듈 임포트
import pickle  # 객체 저장 및 로드를 위한 모듈 임포트

class SignUp:
    # 회원가입 기능 구현 파트
    # 회원가입후 정상 종료시 회원정보 저장
    # 회원가입후 비정상 종료시 회원정보 저장 안함
    # 새로 시작시 저장된 회원정보 불러오기
    def __init__(self):
        try:
            with open('members.pkl', 'rb') as file:  # 저장된 회원정보 파일 열기
                self.members = pickle.load(file) # 파일 내용을 딕셔너리로 로드
                print("기존에 저장된 회원정보가 있습니다. 로딩하시겠습니까?")
                choice = input("1. 예\n2. 아니요\n선택: ")  # 사용자 선택 입력
                if choice == "1": 
                    print("저장된 사용자 정보를 불러옵니다.")
                else:
                    print("새로운 회원정보 관리를 시작합니다.")
                    self.members = {}
        except FileNotFoundError:  # 파일 없을 경우
            print("새로운 회원정보 관리를 시작합니다.")
            self.members = {}  # 빈 딕셔너리로 초기화

    def register(self, email, password): # 회원가입 메서드
        # 회원가입 당시에 기준에 맞춰 검증을 했기 때문에 바로 등록
        self.members[email] = password  # 회원 정보 저장
        return "회원가입에 성공하였습니다."

class MemberManagement: # 회원 관리 클래스
    """
    기능 구현 파트
    """
    def __init__(self): 
        self.signup = SignUp()  # 회원가입 객체 생성

    def all_members(self): 
        for email, pw in self.signup.members.items():  # 모든 회원 정보 출력
            print(f"ID: {email}\nPW: {pw}") # 아이디와 비밀번호 출력

    def login(self, email, password): 
            # 로그인 검증
            if email in self.signup.members and self.signup.members[email] == password: # 아이디와 비밀번호가 일치할 경우
                print(f"{email} : Log-in success!!")
            else: # 아이디와 비밀번호가 일치하지 않을 경우
                print(f"{email} : Log-in failed!!")

    def delete_member(self, email, password): 
        # 회원 정보 삭제 (비밀번호 일치 여부는 main 함수에서 확인)
        del self.signup.members[email] # 아이디 삭제
        #print(f"{email} : 회원 정보가 삭제되었습니다.")

    def main(self):
        try:
            while True:  # 무한 반복
                print("===== 회원 관리 시스템에 오신걸 환영합니다. =====")
                print("< 메뉴를 선택하세요 > ")
                print("1. 회원가입\n2. 전체 회원 조회\n3. 로그인\n4. 회원정보 삭제\n5. 종료")
                choice = input("선택: ")  # 사용자 선택
                print("-" * 40)  # 경계선 출력

                """
                회원가입시 아이디와 비밀번호를 특정 형식에 맞게 입력받도록 구현
                """
                if choice == "1":  # 회원가입
                    print("===== 회원가입을 진행합니다. =====")
                    print("아이디는 이메일 형식으로 입력해주세요.") 
                    while True:  # 무한 반복
                        email = input("아이디 입력: ")
                        # 아이디 형식 검증
                        if not re.match(r"[^@]+@[^@]+\.[^@]+", email): # 이메일 형식이 아닐 경우
                            print("이메일 형식에 맞게 다시 입력해주세요.")
                            continue # 다시 입력
                        print("비밀번호는 6자 이상, 숫자와 특수문자를 포함해야 합니다.")
                        password = input("비밀번호 입력: ")
                        # 비밀번호 형식 검증 (숫자와 특수문자를 포함한 6자 이상)
                        if not re.match(r"^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,}$", password):
                            print("비밀번호는 숫자와 특수문자를 조합해야 합니다. 다시 입력해주세요.")
                            continue
                        # 아이디 및 비밀번호 조건 충족 여부 확인
                        result = self.signup.register(email, password) # 회원가입 메서드 호출
                        print(result) # 회원가입 결과 출력
                        if result == "회원가입에 성공하였습니다.":
                            break # 회원가입 성공시 무한 루프 탈출
                        
                elif choice == "2":  # 전체 회원 조회
                    print("===== 전체 회원 정보를 조회합니다. =====")
                    self.all_members() # 모든 회원 정보 출력

                elif choice == "3":  # 로그인
                    while True:
                        email = input("아이디 입력: ")  # 아이디 입력
                        # 기존에 있는 아이디인지 확인
                        if email not in self.signup.members:
                            print("등록되지 않은 아이디 입니다. 가입정보를 다시 확인해주세요!")
                            continue
                        
                        # 아이디 형식 검증
                        if not re.match(r"[^@]+@[^@]+\.[^@]+", email): # 이메일 형식이 아닐 경우
                            print("아이디는 이메일 형식입니다. 아이디를 다시 확인해주세요!")
                            continue # 다시 입력

                        password = input("비밀번호 입력: ")  # 비밀번호 입력
                        if email in self.signup.members and self.signup.members[email] == password: # 아이디와 비밀번호가 일치할 경우
                            print(f"{email} : Log-in success!!")
                            break  # 로그인 성공시 무한 루프 탈출
                        else:
                            print("비밀번호가 일치하지 않습니다. 비밀번호를 다시 확인해주세요.")

                        
                elif choice == "4":  # 회원정보 삭제
                    print("===== 회원정보를 삭제합니다. =====")
                    while True : # 내부 루프
                        email = input("삭제할 아이디 입력: ")
                        if email not in self.signup.members: # 아이디가 존재하지 않을 경우
                                    print("등록되지 않은 아이디입니다. 다시 입력해주세요.")
                                    continue  # 다시 입력
                        password = input("삭제할 아이디의 비밀번호 입력: ") # 비밀번호 입력
                        if self.signup.members[email] != password: # 비밀번호가 일치하지 않을 경우
                            print("비밀번호가 틀립니다. 다시 입력해주세요.")
                            continue  # 다시 입력
                        self.delete_member(email, password) # 회원 정보 삭제 메서드 호출
                        break  # 무한 루프 탈출
                    print(f"{email} : 회원정보가 삭제되었습니다.") # 삭제 완료 메시지 출력

                elif choice == "5":  # 종료
                    print("===== 회원 관리 시스템을 종료합니다. =====")
                    print("시스템을 종료합니다.") # 종료 메시지 출력
                    break  # 무한 루프에서 빠져나가 종료

                else:  # 잘못된 선택
                    print("잘못된 선택입니다.")
                
                print("-" * 40)  # 경계선 출력
        finally:
            with open('members.pkl', 'wb') as file: # 회원 정보를 파일로 저장
                pickle.dump(self.signup.members, file)  # 종료 시 회원 정보를 파일로 저장
```

```python
# 실행코드로 기능 확인

import member_management as mm # 클래스로 저장된 모듈 불러오기

management_instance = mm.MemberManagement() # 인스턴스 생성
management_instance.main() # main 메서드 실행
```

```python
새로운 회원정보 관리를 시작합니다.
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 1
----------------------------------------
===== 회원가입을 진행합니다. =====
아이디는 이메일 형식으로 입력해주세요.
아이디 입력: abc
이메일 형식에 맞게 다시 입력해주세요.
아이디 입력: abc@gmail.com
비밀번호는 6자 이상, 숫자와 특수문자를 포함해야 합니다.
비밀번호 입력: hello
비밀번호는 숫자와 특수문자를 조합해야 합니다. 다시 입력해주세요.
아이디 입력: abc@gmail.com
비밀번호는 6자 이상, 숫자와 특수문자를 포함해야 합니다.
비밀번호 입력: hello1234!!
회원가입에 성공하였습니다.
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 1
----------------------------------------
===== 회원가입을 진행합니다. =====
아이디는 이메일 형식으로 입력해주세요.
아이디 입력: def@gmail.com
비밀번호는 6자 이상, 숫자와 특수문자를 포함해야 합니다.
비밀번호 입력: hello1234@@
회원가입에 성공하였습니다.
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 1
----------------------------------------
===== 회원가입을 진행합니다. =====
아이디는 이메일 형식으로 입력해주세요.
아이디 입력: ghi@gmail.com
비밀번호는 6자 이상, 숫자와 특수문자를 포함해야 합니다.
비밀번호 입력: hello1234##
회원가입에 성공하였습니다.
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 6
----------------------------------------
잘못된 선택입니다.
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 2
----------------------------------------
===== 전체 회원 정보를 조회합니다. =====
ID: abc@gmail.com
PW: hello1234!!
ID: def@gmail.com
PW: hello1234@@
ID: ghi@gmail.com
PW: hello1234##
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 3
----------------------------------------
아이디 입력: abc
등록되지 않은 아이디 입니다. 가입정보를 다시 확인해주세요!
아이디 입력: abc@gmail.com
비밀번호 입력: hello1234
비밀번호가 일치하지 않습니다. 비밀번호를 다시 확인해주세요.
아이디 입력: abc@gmail.com
비밀번호 입력: hello1234!!
abc@gmail.com : Log-in success!!
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 4
----------------------------------------
===== 회원정보를 삭제합니다. =====
삭제할 아이디 입력: abc
등록되지 않은 아이디입니다. 다시 입력해주세요.
삭제할 아이디 입력: abc@gmail.com
삭제할 아이디의 비밀번호 입력: hello1234
비밀번호가 틀립니다. 다시 입력해주세요.
삭제할 아이디 입력: abc@gmail.com
삭제할 아이디의 비밀번호 입력: hello1234!!
abc@gmail.com : 회원정보가 삭제되었습니다.
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 2
----------------------------------------
===== 전체 회원 정보를 조회합니다. =====
ID: def@gmail.com
PW: hello1234@@
ID: ghi@gmail.com
PW: hello1234##
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 5
----------------------------------------
===== 회원 관리 시스템을 종료합니다. =====
시스템을 종료합니다.
```

```python
# 저장한 피클 파일(회원정보) 잘 로딩 되는지 확인

if __name__ == "__main__":
    mm = MemberManagement()
    mm.main()  # 클래스 내 메서드로 프로그램 실행
```

```python
기존에 저장된 회원정보가 있습니다. 로딩하시겠습니까?
1. 예
2. 아니요
선택: 1
저장된 사용자 정보를 불러옵니다.
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 2
----------------------------------------
===== 전체 회원 정보를 조회합니다. =====
ID: def@gmail.com
PW: hello1234@@
ID: ghi@gmail.com
PW: hello1234##
----------------------------------------
===== 회원 관리 시스템에 오신걸 환영합니다. =====
< 메뉴를 선택하세요 > 
1. 회원가입
2. 전체 회원 조회
3. 로그인
4. 회원정보 삭제
5. 종료
선택: 5
----------------------------------------
===== 회원 관리 시스템을 종료합니다. =====
시스템을 종료합니다.
```

---

### 4. 예외처리

> **예외 처리를 포함한 회원가입 프로그램 구현하기**
> 
> 
> ---
> 
> - 이름, 메일주소, 비밀번호, 주소, 연락처를 입력받아 회원가입을 해야 함
> - 누락된 입력사항이 있는 경우 에러 메시지를 출력해야 함

```python
# 예외처리 클래스 생성

class EmptyDataException(Exception):
    def __init__(self, i):
        super().__init__(f'{i} is empty!') # 예외 메시지 설정
        
def checkInputData(n, m, p, a, ph):
    # 각 매개변수가 비어있는지 확인하고, 비어있다면 예외 발생
    if n == '':
        raise EmptyDataException('name')
    elif m == '':
        raise EmptyDataException('mail')
    elif p == '':
        raise EmptyDataException('password')
    elif a == '':
        raise EmptyDataException('address')
    elif ph == '':
        raise EmptyDataException('phone')

class RegistMember():
    def __init__(self,n,m,p,a,ph):
        # 회원 정보를 인스턴스 변수에 저장
        self.m_name = n
        self.m_mail = m
        self.m_pw = p
        self.m_addr = a
        self.m_phone = ph
        print('Membership complete!!') # 가입 완료 메시지 출력
        
    def printMemberInfo(self): # 회원 정보 출력 메서드
        print(f'm_name:{m_name}')
        print(f'm_mail:{m_mail}')
        print(f'm_pw:{m_pw}')
        print(f'm_addr:{m_addr}')
        print(f'm_phone:{m_phone}')
```

```python
# 사용자로부터 입력 받기
m_name = input('이름 입력 : ')
m_mail = input('메일 주소 입력 : ')
m_pw = input('비밀번호 입력 : ')
m_addr = input('주소 입력 : ')
m_phone = input('연락처 입력 : ')

try:
    checkInputData(m_name, m_mail, m_pw, m_addr, m_phone) # 입력 검사
    newMember = RegistMember(m_name, m_mail, m_pw, m_addr, m_phone) # 회원 등록
    newMember.printMemberInfo() # 회원 정보 출력
    
except EmptyDataException as e: # 입력이 비어 있는 경우 예외 처리
    print(e)
```

```python
이름 입력 : hong gil dong
메일 주소 입력 : 
비밀번호 입력 : 1234
주소 입력 : Korea seoul
연락처 입력 : 010-1234-5678
mail is empty!
```

```python
이름 입력 : hong gil dong
메일 주소 입력 : hong@gmail.com
비밀번호 입력 : 1234
주소 입력 : seoul Korea
연락처 입력 : 010-1234-5678
Membership complete!!
m_name:hong gil dong
m_mail:hong@gmail.com
m_pw:1234
m_addr:seoul Korea
m_phone:010-1234-5678
```

> 기본 내용 응용해서 코드 개선해보기
> 
> 
> ---
> 
> - 중복된 입력 프로세스 제거
>     - 매 항목마다 input()으로 입력받아야 하는 것을 반복문을 활용하여 간소화
> - 예외 처리 통합
>     - EmptyDataException을 통해 항목을 입력할때마다 누락이 있으면 즉각적으로 피드백
> - printMemberInfo 수정
>     - 기존 코드는 클래스 인스턴스 변수를 활용하지 않고 지역변수만 참조하여 이를 수정
> - 구조화 및 함수화
>     - 회원가입 로직을 별도로 함수화(signup)하여 여러번 사용 가능하도록 수정
> - 입력값 검증 분리하기
>     - checkInputData함수를 signup함수 내에 실행하도록 수정해 하나의 코드에서 모든 과정이 일어나도록 수정

```python
# 클래스 생성

# 사용자가 누락된 데이터를 입력한 경우 발생하는 예외
class EmptyDataException(Exception):
    def __init__(self, i):
        super().__init__(f'{i} is empty!')  # 누락된 입력 항목 이름을 예외 메시지로 전달

# 회원 정보를 저장하는 클래스
class RegistMember():
    def __init__(self, n, m, p, a, ph):
        self.m_name = n
        self.m_mail = m
        self.m_pw = p
        self.m_addr = a
        self.m_phone = ph
        print('Membership complete!!')  # 회원 가입 완료 메시지 출력

    # 회원 정보를 출력하는 메서드
    def printMemberInfo(self):
        print(f'm_name: {self.m_name}')
        print(f'm_mail: {self.m_mail}')
        print(f'm_pw: {self.m_pw}')
        print(f'm_addr: {self.m_addr}')
        print(f'm_phone: {self.m_phone}')

# 사용자 입력 프롬프트
input_prompts = ['이름 입력', '메일 주소 입력', '비밀번호 입력', '주소 입력', '연락처 입력']
# 입력 항목의 키(예외 메시지에서 사용)
input_keys = ['name', 'mail', 'password', 'address', 'phone']
input_values = []
```

```python
# 실행코드

def signup():
    # 입력 프롬프트와 입력 키를 정의
    input_prompts = ['이름 입력', '메일 주소 입력', '비밀번호 입력', '주소 입력', '연락처 입력']
    input_keys = ['name', 'mail', 'password', 'address', 'phone']
    input_values = []  # 입력 값을 저장할 리스트

    # 각 프롬프트와 키를 반복하면서 입력 받기
    for prompt, key in zip(input_prompts, input_keys):
        value = input(f'{prompt} : ')  # 사용자로부터 입력 받음
        if value == '':  # 입력 값이 없을 경우 예외 발생
            raise EmptyDataException(key)
        input_values.append(value)  # 입력 값을 리스트에 추가

    try:
        # 회원 정보를 입력 값으로 사용하여 RegistMember 클래스의 인스턴스 생성
        newMember = RegistMember(*input_values)
        newMember.printMemberInfo()  # 회원 정보 출력
    except EmptyDataException as e:  # 누락된 입력 사항 발생 시 에러 메시지 출력
        print(e)

# 함수 호출하여 회원가입 진행
signup()
```

```python
이름 입력 : 홍길동
메일 주소 입력 : abc@gmail.com
비밀번호 입력 : 1234
주소 입력 : Korea
연락처 입력 : 010-1234-5678
Membership complete!!
m_name: 홍길동
m_mail: abc@gmail.com
m_pw: 1234
m_addr: Korea
m_phone: 010-1234-5678
```

### 5. 텍스트파일

> **텍스트 파일 읽기/쓰기 프로그래밍**
> 

```python
# 모듈 생성(diary.py)

import time

# 일기 쓰기 함수
def writeDiary(u, fileName, d):
    lt = time.localtime()  # 현재 시간을 가져옴
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S %p", lt)  # 시간을 문자열 형태로 변환
    
    filePath = u + fileName + '.txt'  # 파일 경로 설정
    with open(filePath, "a") as f:  # 파일을 열어 내용을 추가함
        f.write(f'[{timeStr}] {d}\n')  # 시간과 일기 내용을 기록
        
# 일기 읽기 함수
def readDiary(u, fileName):
    filePath = u + fileName + '.txt'  # 파일 경로 설정
    with open(filePath, "r") as f:  # 파일을 열어 읽음
        dates = f.readlines()  # 모든 라인을 읽어 리스트로 반환
        return dates  # 읽은 내용을 반환
```

```python
# 실행코드 생성 및 실행
import os
import diary

# 현재 실행 경로를 가져옴
uri = os.getcwd() + '/'

members =  {}  # 회원 정보를 저장할 딕셔너리

# 회원 정보 출력 함수
def printMembers():
    for m in members.keys():
        print(f'ID: {m} \t PW: {members[m]}')

while True:
    selectNum = int(input('1.회원가입, 2.한줄일기쓰기, 3.일기보기, 4.종료'))

    if selectNum == 1:  # 회원가입 선택
        mId = input('input ID: ')
        mPw = input('input PW: ')
        members[mId] = mPw  # ID와 PW를 저장
        printMembers()

    elif selectNum == 2:  # 일기 쓰기 선택
        mId = input('input ID: ')
        mPw = input('input PW: ')

        # 로그인 검사
        if mId in members and members[mId] == mPw:
            print('login success!!')
            fileName = 'myDiary_' + mId
            data = input('오늘 하루 인상 깊은 일을 기록하세요. ')
            diary.writeDiary(uri, fileName, data)  # 일기 쓰기 함수 호출
        else:
            print('login failed!!')
            printMembers()

    elif selectNum == 3:  # 일기 읽기 선택
        mId = input('input ID: ')
        mPw = input('input PW: ')

        # 로그인 검사
        if mId in members and members[mId] == mPw:
            print('login success!!')
            fileName ='myDiary_' + mId
            datas = diary.readDiary(uri, fileName)  # 일기 읽기 함수 호출
            for d in datas:
                print(d, end='')
        else:
            print('login fail!!')
            printMembers()

    elif selectNum == 4:  # 종료 선택
        print('Bye~')
        break
```

```python
1.회원가입, 2.한줄일기쓰기, 3.일기보기, 4.종료1
input ID: hello
input PW: 1234
ID: hello 	 PW: 1234
1.회원가입, 2.한줄일기쓰기, 3.일기보기, 4.종료2
input ID: I got lotto!!
input PW: 1234
login failed!!
ID: hello 	 PW: 1234
1.회원가입, 2.한줄일기쓰기, 3.일기보기, 4.종료2
input ID: hello
input PW: 1234
login success!!
오늘 하루 인상 깊은 일을 기록하세요. I got lotto!!
1.회원가입, 2.한줄일기쓰기, 3.일기보기, 4.종료3
input ID: hello
input PW: 1234
login success!!
[2023-08-06 01:19:37 AM] I got lotto!!
1.회원가입, 2.한줄일기쓰기, 3.일기보기, 4.종료4
Bye~
```

> 기본 코드 응용해 프로그램 개선하기
> 
> 
> ---
> 
> - 함수 세분화 및 모듈화
>     - 기존의 일기 쓰기/읽기 기능 외에 회원가입, 일기 쓰기/읽기, 로그인 모두 독립된 함수로 구성
> - 회원정보 유지
>     - 기존의 메모리에만 일시적으로 저장하는게 것이 아닌 프로그램 종료시 회원정보를 별도의 파일(members.txt)에 저장하고 차후 재실행해도 정보를 불러올 수 있도록 개선
> - 로그인 기능 개선
>     - members.txt의 내용을 기반으로 입력정보를 읽어와서 검토하기
> - 날짜 처리
>     - 기존 time모듈에서 datetime모듈로 변환
> - 코드 정리
>     - 각 기능별 코드를 함수로 정리해서 유지보수를 조금 더 고려하기!

```python
import datetime

def register():
    # 회원 가입 함수
    while True: # 중복된 아이디가 없을 때까지 반복
        ID = input("input ID : ") # 사용자로부터 ID를 입력 받음
        with open('members.txt', 'r') as f: # 기존 회원 정보 읽기
            if any(line.split()[0] == ID for line in f): # 아이디 중복 체크
                print("기존에 있는 아이디입니다. 다른 아이디로 가입해주세요.") # 중복 메시지 출력
                continue # 다시 아이디 입력 받기
        PW = input("input PW : ") # 사용자로부터 비밀번호를 입력 받음
        with open('members.txt', 'a') as f: # 회원 정보를 저장할 파일열기
            f.write(f'{ID} {PW}\n') # ID와 비밀번호를 파일에 저장
        print(f'ID : {ID}\tPW: {PW}') # 저장된 회원 정보 출력
        break # 중복된 아이디가 없으므로 반복 종료

def write_diary(ID):
    # 일기 쓰기 함수
    with open(f'{ID}_diary.txt', 'a') as f:  # 사용자의 ID로 일기 파일열기
        diary = input("오늘 하루 인상 깊은 일을 기록하세요. ")  # 일기 내용을 입력 받기
        timestamp = datetime.datetime.now().strftime('[%Y-%m-%d %I:%M:%S %p]')  # 현재 시간을 문자열로 변환
        f.write(f'{timestamp} {diary}\n')  # 일기와 시간을 파일에 저장
        print(timestamp, diary)  # 저장된 일기 출력

def read_diary(ID):
    # 일기 읽기 함수
    with open(f'{ID}_diary.txt', 'r') as f:  # 사용자의 ID로 일기 파일 열기
        print(f.read())  # 파일의 내용을 전부 읽어서 출력

def login():
    # 로그인 함수
    ID = input("input ID: ")  # 사용자로부터 ID를 입력 
    PW = input("input PW: ")  # 사용자로부터 비밀번호를 입력 
    with open('members.txt', 'r') as f:  # 회원 정보가 저장된 파일 열기
        for line in f:
            if line.strip() == f'{ID} {PW}':
                print("login success!!")  # 로그인 성공 시 출력
                return ID  # 로그인 성공 시 ID를 반환
    print("login failed!!")  # 로그인 실패 시 출력
    return None  # 로그인 실패 시 None 반환

def main():
    while True:
        # 메뉴 선택
        choice = int(input('1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 '))  # 사용자로부터 메뉴를 숫자로 선택
        if choice == 1:
            register()  # 회원 가입 함수 호출
        elif choice == 2:
            ID = login()  # 로그인 함수 호출
            if ID:
                write_diary(ID)  # 일기 쓰기 함수 호출
        elif choice == 3:
            ID = login()  # 로그인 함수 호출
            if ID:
                read_diary(ID)  # 일기 읽기 함수 호출
        elif choice == 4:
            print("종료합니다.")  # 종료 메시지 출력
            break  # 무한 반복문 종료
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")  # 잘못된 입력 시 출력

if __name__ == '__main__':
    main()  # main 함수 실행
```

```python
1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 1
input ID : myname
input PW : 1234
ID : myname	PW: 1234
1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 2
input ID: myname
input PW: 1234
login success!!
오늘 하루 인상 깊은 일을 기록하세요. i edited original code!
[2023-08-06 01:33:30 AM] i edited original code!
1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 3
input ID: myname
input PW: 1234
login success!!
[2023-08-06 01:33:30 AM] i edited original code!

1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 4
종료합니다.
```

```python
# 회원정보가 이상없이 저장되어 있는지 확인

import os

# 현재 작업 경로를 가져옵니다.
current_path = os.getcwd()
print(f"현재 작업 경로: {current_path}")

# 현재 경로에 'members.txt' 파일이 있는지 확인합니다.
if os.path.exists(os.path.join(current_path, 'members.txt')):
    print("'members.txt' 파일이 현재 경로에 존재합니다.")
else:
    print("'members.txt' 파일이 현재 경로에 존재하지 않습니다.")
```

```python
현재 작업 경로: ../[Zero-base]_Study_Note/01.Lecture_note/Ch1.python(basic)
'members.txt' 파일이 현재 경로에 존재합니다.
```

```python
# 기존 회원정보 불러와지는지 확인

if __name__ == '__main__':
    main()  # main 함수 실행
```

```python
1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 1
input ID : myname
기존에 있는 아이디입니다. 다른 아이디로 가입해주세요.
input ID : hello
기존에 있는 아이디입니다. 다른 아이디로 가입해주세요.
input ID : newID
input PW : 1234
ID : newID	PW: 1234
1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 2
input ID: hello
input PW: 1234
login success!!
오늘 하루 인상 깊은 일을 기록하세요. 코드를 수정해보았다.
[2023-08-06 01:34:27 AM] 코드를 수정해보았다.
1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 3
input ID: hello
input PW: 1234
login success!!
[2023-08-06 01:34:27 AM] 코드를 수정해보았다.

1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 3
input ID: myname
input PW: 1234
login success!!
[2023-08-06 01:33:30 AM] i edited original code!

1. 회원가입, 2.한줄일기쓰기, 3.한줄일기보기, 4.종료 4
종료합니다.
```

# ✍️ 오늘의 혼잣말

---

- 오랜만에 하는 기초는 생각보다 정말 어렵기도.. 버겁기도 했다. 예전에 기초를 소홀히 했다는 증거
- 그래도 한줄씩 작성하고 수정하면서 조금씩 나아지고 있음을 느낀다.
- 기본적인 내용을 강의로 듣고 정리하는건 사실 오래 걸릴일이 아닌데, 괜히 조금만 더 고쳐보자고 욕심내서 사소한거 하나 하나 고치고 바꾸려다 보니 시간을 엄청 잡아먹는다.
- 실제로 일하게 될때도 이런 고민을 해야 할지도 모른다.
    - 코드의 정확성과 기능성 향상이냐 빠른 제작과 배포냐
    - 판단 기준을 고민해봐야 할 부분이다.