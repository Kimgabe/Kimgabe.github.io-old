---
title: "[SQLD] 1일차 : 데이터모델링의 이해 - 04. 관계(Relationship)"
cover: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1920&h=1080&fit=crop"
date: 2024-04-24
categories:
  - [personal-study, sql]
tags: []
toc: true
---
## 🚦 Summary
- SQLD 1과목의 4번째 파트인 '관계(Relationship)' 에 대해 정리한 노트입니다.
- 관계(Relationship)는 Entity의 Instance 사이의 논리적인 연관성 또는 행위로서 서로에게 연관성이 부여된 상태를 의미합니다.
- 관계는 존재에 의한 관계와 행위에 의한 관계로 분류되며, 관계명, 관계차수, 관계 선택 사양으로 표기됩니다.
- 관계차수는 1:1, 1:M, M:N으로 분류되며, 관계선택사양은 필수 관계와 선택 관계로 나뉩니다.

---


## 📌 Intro.
- 데이터 모델링에서 관계(Relationship)는 Entity 간의 연관성을 나타내는 중요한 개념입니다.
- 이번 포스팅에서는 관계의 정의와 분류, 표기법, 그리고 관계를 정의할 때 고려해야 할 사항들에 대해 알아볼 예정입니다.

---


## 과목 범위
![](https://i.imgur.com/shqolpw.png)

# 관계의 정의
- 사전적 정의로는 '상호 연관성' 이 있는 상태를 의미
  
> 즉, "Entity의 Instance 사이의 논리적인 연관성으로 존재의 형태로서 혹은 행위로서 서로에게 연관성이 부여된 상태"  를 의미

## DB에서 관계가 있는 데이터의 예시
![](https://i.imgur.com/7cRbIhY.png)

> Instance 사이의 논리적인 연관성이 있거나, 행위로서 서로에게 연관성이 부여된 상태

- 위 이미지는 DB의 두 Entity(강사, 수강생) 간의 관계를 나타내고 있음
- '강의한다' 라는 관계로 두 Entity 가 연결되어 있음을 표현 한 것
- '강사' Entity는 '강사번호' 라는 PK를 , '수강생' Entity는 '강사번호' 를 FK로 갖고 있음.
- 이 두 Entity 는 2가지 이유로 연관성이 부여되었다고 할 수 있음
	- 논리적 연관성 : 
		- 한 강사가 여러 수강생을 가르치는 관계가 성립할 수 있음
		- 즉, 교육이라는 도메인 상황에서 '강사'와 '수강생' 사이에는 논리적 연관성이 존재 함
	- 행위로서의 연관성 :
		- '강의한다' 라는 행위는 강사와 수강생 사이에서 일어나는 '행위' 이므로 연관성이 있음

# 관계의 페어링(Pairing)
- Entity안에 Instance가 개별적으로 관계를 가지는 것을 Pairing이라고 하며, 이때 Pairing의 집합을 관계라고 할 수 있음
	- 개별 Instance가 각각 다른 종류의 관게를 가지고 있다면 두 Entity  사이에  두 개 이상의 관계 형셩될 수 있음
	- 각각의 Entity Instance 들은 자신이 관련된 Instance들과 관계의 Occurance로 참여하는 형태를 Relationship Pairing 이라고 함.

> Occurance : Instance와 유사한 개념으로 주로 Entity 내에서 각각의 데이터 항목이나 Record를 지칭할 때 사용.
> 또한, 주로 Instance가 DB에서 실제로 발생하는 것을 '강조' 할때 사용
> ex) 주문 Entity 가 발생하면 특정 주문번호를 가진 하나의 주문을 의미함. 

![](https://i.imgur.com/tZhmGep.png)

- 강사인 '정성철' 은 수강생인 '이춘식'과 '황종하' 에게 강의를 하는 형태로 관계를 맺고 있으며 이 관계는 두 개의 별도의 페어링으로 표현되어 있음
- 강사 조시형은 수강생 황종하에게 강의를 하는 형태로 연결되어 있으며, 이 또한 하나의 패어링을 형성함.
- 즉, Entity내에 Instance와 Instance 사이에 관계가 설정되어 있는 Occurance 를 Relationship Pairing 이라 할 수 있음
- 위와 같이 각각의 인스턴스가 관련된 인스턴스들과 참여하고 있는 모든 관계를 합쳐서 '관계의 발생(relationship occurrence)'이라고 하며, 이러한 발생들의 집합이 전체 '관계(pairing)'를 형성하는 것

- '강사'와 '수강생'이라는 두 Entity 사이에 "강의한다"라는 관계가 있습니다. 이 관계는 강사가 수강생에게 강의를 하는 행위를 나타냄
    
- '강사' Entity의 각 인스턴스(예: 정성철, 조시형)는 '수강생' Entity의 인스턴스들(예: 이춘식, 황종하)과 개별적인 연관성을 가질 수 있습니다. 각 인스턴스 사이의 연관성은 특정 강사가 특정 수강생에게 강의를 한다는 사실을 나타냄
    
- 이렇게 각 인스턴스 간의 연관성을 모아보면, "강의한다"라는 전체적인 관계를 도출할 수 있습니다. 다시 말해, 모든 강사와 수강생 간의 연관성이 집합되어 "강의한다"는 관계가 구체화됨.

> 즉, 이 이미지와 설명은 각 인스턴스가 개별적으로 가질 수 있는 연관성들을 모두 합쳐서 전체 '강의한다'라는 관계를 도출하고 있다는 것을 의미합니다. 이 관계는 데이터베이스에서 해당 Entity들 사이의 논리적인 연결을 나타내는 중요한 부분입니다.

# 관계의 분류 (feat. 존재에 의한 관계)
![](https://i.imgur.com/B4olInX.png)

- "소속 된다" 는 것은 '행위에 따른 이벤트' 가 아닌 말그대로 '소속' 이 되어 있기 때문에 형성 되는 것
- 즉, 존재의 형태에 의해 관계가 이미 형성되어 있는 것

# 관계의 분류 (feat. 행위에 의한 관계)
![](https://i.imgur.com/fAKw4ap.png)

- 주문 Entity의 '주문번호' 는 고객이 '주문' 이라는 행위를 하면서 발생이 됨
- 즉, 두 Entity 사이의 관계는 행위에 의한 관계가 되는 것

# 관계의 표기법
- 관계를 표기하는 방법은 3가지로 분류되며, 각 방법에 따라 관계명, 관계차수, 관계 선택 사양으로 분류 함.

![](https://i.imgur.com/hUzHnsK.png)

## 관계명
- Entity 가 관계에 참여하는 형태를 지칭
- 각각의 관계는 두 개의 관계명을 갖고 있음
- 각각의 관계명에 의해 두 가지의 관점으로 표현될 수 있음

![](https://i.imgur.com/SSOHVpR.png)

> 관계 시작점(The Beginning) : Entity의 관계가 시작되는 편
> 관계 끝점(The End) : 시작된 관계를 받는 편

- 관계 시작점과 끝점 모두 관계이름을 가져야 하며, 참여자의 관점에 따라 관계이름이 Active하게 혹은 Passive하게 명명됨.

### 관계 명명 규칙
- 애매한 동사는 피한다.
	- ex) 
		- 관계된다, 관련이 있다, ~이다, ~한다 등
		- 구체적이지가 않은 표현이라 어떤 행위가 있는지 또는 두 참여자간 어떤 상태가 존재하는지 파악이 어려움
- 현재형으로 표현 한다.
	- ex) 
		- '수강을 신청했다.',  '강의를 할 것이다.' 는 ❌ 
		- '수강 신청한다.', '강의를 한다.' ⭕ 

## 관계 차수
- 두 개의 Entity 간 관계에서 참여자의 수를 표현하는 것을 관계 차수(Cardinality) 라고 함
- 가장 일반적인 관계 차수 표현 방법은 1:M, 1:1, M:N 임.

### 관계차수 1:1
> 한 Entity의 인스턴스가 다른 Entity의 단 하나의 인스턴스와만 관계를 맺는 경우입니다. 예를 들어, 한 사람이 하나의 주민등록번호를 가지는 경우

![](https://i.imgur.com/kR66Gs5.png)

- 관계에 참여하는 각각의 Entity는 관계를 맺는 다른 Entity에 대해 오직 1개의 관계만을 갖고 있음

### 관계차수 1:M
> 한 Entity의 인스턴스가 다른 Entity의 여러 인스턴스와 관계를 맺을 수 있는 경우
> 예를 들어, 한 강사가 여러 강의를 담당하는 경우

![](https://i.imgur.com/yD4JFJH.png)

- 한 명의 사원은 한 부서에 소속되고, 한 부서에는 여러 사원이 소속된다.

### 관계차수 M:N
> 한 Entity의 여러 인스턴스가 다른 Entity의 여러 인스턴스와 관계를 맺을 수 있는 경우.
> 예를 들어, 여러 학생이 여러 강의를 수강하는 경우

![](https://i.imgur.com/EW8lo5n.png)

- 관계에 참여하는 각각의 Entity는 관계를 맺는 다른 Entity에 대해 하나 혹은 그 이상의 수와 관계를 갖고 있음

## 관계선택사양(Optionality)
> 데이터 모델링에서 특정 Entity간의 관계가 필수적인지, 선택적인지를 나타내는 것

- 즉, 관계의 존재 여부와 관련된 규칙을 정의할 때 사용하며, 각 관계에 대해 어느정도의 유연성을 허용할지 결정하는 요소

- **필수 관계(Mandatory Relationship)**: 한 엔터티의 인스턴스가 다른 엔터티와 반드시 관계를 가져야 할 때 이를 필수 관계라고 함.
	- 예시 1) 모든 주문에는 반드시 고객이 있어야 하는 경우, 주문과 고객 사이의 관계는 필수적이라 할 수 있음
	    
- **선택 관계(Optional Relationship)**: 한 엔터티의 인스턴스가 다른 엔터티와 관계를 가질 수도 있고 안 가질 수도 있을 때 이를 선택 관계라고 함.
	-  예를 들어, 직원이 부서에 소속될 수도 있지만, 아직 소속되지 않은 경우도 있을 수 있음.

![](https://i.imgur.com/2A7LW14.png)

- 고객은 여러개의 주문을 할 수도, 한개의 주문을 할 수도 있음(Optional 관계)
- 반면에 '주문' 은 반드시 고객이 있어야지만 발생하는 것으로 필수적(Mandatory) 관계 임.

### 관계 정의 시 체크 사항
> 1. 두 개의 Entity 사이에 관심있는 연관규칙이 존재 하는가?
> 2. 두 개의 Entity 사이에 정보의 조합이 발생되는가?
> 3. 업무기술서, 장표에 관계 연결에 대한 규칙이 서술되어 있는가?
> 4. 업무기술서, 장표에 관계 연결을 가능하게 하는 동사(Verb) 가 있는가?

1. **연관 규칙의 존재 여부 확인**:
    - 두 엔터티 사이에 특정한 연관 규칙이 존재하는지 확인해야 함
    - 예시: '고객'과 '주문' 엔터티 사이에는 '고객은 하나 이상의 주문을 할 수 있다'는 연관 규칙이 존재할 수 있음
      
2. **정보 조합의 발생 여부 확인**:
    - 두 엔터티를 조합했을 때, 새로운 의미 있는 정보가 만들어지는지 확인
    - 예시: '학생'과 '과목' 엔터티를 조합하여 '수강'이라는 새로운 의미의 정보가 생성 됨.
      
3. **업무기술서 및 장표의 관계 규칙 서술 여부**:
    - 업무를 설명하는 문서나 장표에 각 엔터티 간의 관계에 대한 규칙이 명시되어 있는지 확인
    - 예시: 업무기술서에 '한 의사는 여러 환자를 담당할 수 있고, 한 환자는 한 명의 의사에게 진료받는다'라는 관계가 서술되어 있을 수 있음

4. **업무기술서 및 장표에 관계 연결 동사의 존재 여부**:
    - 엔터티 사이의 관계를 표현하는 데 사용되는 동사가 업무기술서나 장표에 포함되어 있는지 확인.
    - 예시: '도서관' 엔터티와 '도서' 엔터티 사이에 '대출한다', '반납한다' 등의 동사가 사용되어 관계를 명시

# DB에서 관계 읽는 법
> 1. 기준(Source) Entity 한 개 (One) 또는 각(Each) 으로 읽는다.
> 2. 대상(Target) Entity 의 관계 참여도 즉 개수(하나, 하나 이상)을 읽는다.
> 3. 관계선택 사양과 관계 명을 읽는다.

![](https://i.imgur.com/Rp7KGpE.png)

- 관계 읽는법대로 위 DB를 읽으면 다음과 같음
	- 기준 Entity = 고객 
	- 대상 Entity = 주문
	- 관계 선택사양 및 관계명 : 주문한다(관계명)

>  고객 한 명(One)이 하나 이상의 주문을 주문한다.

- 위 DB의 전체적인 관계의 개요는 아래와 같음음
![](https://i.imgur.com/RsdlM9S.png)

---


## 🎈 Outro.
- 관계(Relationship)는 Entity 간의 논리적인 연관성을 나타내는 핵심 요소로, 데이터 모델링에서 중요한 역할을 담당합니다.
- 관계의 분류와 표기법을 이해하고, 관계 정의 시 연관 규칙, 정보 조합, 규칙 서술, 연결 동사 등을 고려하는 것이 중요합니다.
- 데이터베이스에서 관계를 읽는 법을 배울 때는 기준 Entity, 대상 Entity, 관계 선택 사양 및 관계명을 순서대로 파악하는 것이 좋습니다.
