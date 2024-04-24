---
layout: single
title: '"[SQLD] 1일차 : 데이터모델링의 이해 - 05. 식별자(Identifier)"'
categories:
  - sql
tags:
  - sql
  - SQLD
  - 노트정리
  - 식별자
  - Identifier
toc: true
highlight: false
use_math: true
header:
  teaser: /assets/images/SQL/sql_teaser.png
  overlay_image: /assets/images/SQL/sql_teaser.png
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/XJXWbfSo2f0)"
---
## 🚦 Summary
- SQLD 1과목의 5번째 파트인 '식별자(Identifier)' 에 대해 정리한 노트입니다.
- 식별자(Identifier)는 Entity 내에서 각 Instance를 유일하게 구분하기 위해 사용되는 Attribute 또는 Attribute의 조합 입니다.
- 식별자는 주 식별자, 외부 식별자, 복합 식별자로 분류되며, 주 식별자는 유일성, 최소성, 불변성, 존재성의 특징을 가집니다.
- 식별자 관계는 자식 Entity의 주 식별자로 부모의 주 식별자가 상속되는 경우이고, 비식별자 관계는 부모의 주 식별자가 자식에게 FK로만 전달되는 경우를 말합니다.

---

## 📌 Intro.
- 데이터 모델링에서 식별자(Identifier)는 Entity 내의 Instance를 구분하는 핵심 요소로, 유일성과 일관성을 보장하는 중요한 역할을 합니다.
- 이번 포스팅에서는 식별자의 개념과 특징, 분류, 그리고 식별자 관계와 비식별자 관계에 대해 알아볼 예정입니다.

---
## 과목 범위
![](https://i.imgur.com/nz0ADiv.png)



# 식별자의 개념
- Entity는 Instance들의 집합
- 다만, 여러개의 집합체를 담고 있는 하나의 통에서 는 각각의 Entity를 구분하기 어려움
- 이때, 필요한 것이 각각을 구분하기 위한 '논리적 이름' 인 식별자(Identifier) 임

> 즉, Entity의 각 Instance를 개별적으로 식별하기 위해 사용되는 Relationship 또는 Attribute 들의 조합
> 식별자 = Entity 내 Instance들을 구분할 수 있는 구분자.


# 식별자의 특징
1. 주 식별자에 의해 Entity 내에 모든 <font color="#4f81bd">Instance들이 유일하게 구분</font>되어야 함
2. 주 식별자를 구성하는 Attribute 의 수는 유일성을 만족하는 <font color="#4f81bd">최소의 수</font>가 되어야 함
3. 지정된 주 식별자의 값은 <font color="#4f81bd">자주 변하지 않는 것</font>이어야 함
4. 주 식별자가 지정이 되면 <font color="#4f81bd">반드시 값이 들어와야</font> 함

![](https://i.imgur.com/YYKobtL.png)

# 식별자의 분류
![](https://i.imgur.com/lSOrUy7.png)

- 예시 DB를 통해 각 식별자를 정리해보면 아래와 같음

![](https://i.imgur.com/rQ7kbS5.png)


# 식별자 도출 기준
> 1. 해당 업무에서 자주 이용되는 속성을 주 식별자로 지정한다.
> 2. 명칭, 내역 등과 같이 이름으로 기술되는 것들은 가급적 주 식별자로 지정하지 않는다.
> 3. 복합으로 주 식별자를 구성할 경우 너무 많은 속성이 포함되지 않도록 한다.


![](https://i.imgur.com/OPBx2Mk.png)

- 🤔 위와 같은 Entity에 Attribute 가 있을때 식별자를 선택한다면?
	- 주민등록번호도 식별자 후보가 될 수 는 있으나 해당 업무에서 <font color="#4f81bd">자주 사용하는 사원번호를 주 식별자로 지정</font>하는 것이 더 적합
	- 직원명과 같은 이름은 주 식별자로 적합하지 않음(동명이인이 없다고 해도)
	- 직원번호 + 주민등록번호 와 같이 복합 식별자로 하면 유일성은 보장되지만, 직원번호 자체가 유일성이 보장되기에 굳이 복합 식별자로 만들 필요가 없음

> 사원번호를 주 식별자로 지정하는 것이 가장 적합 함


![](https://i.imgur.com/3Dj3Oz0.png)


# 식별자 관계와 비식별자 관계의 결정
- 데이터 설계에서 식별자 관계와 비식별자 관계를 결정하는 것은 Entity간의 관계를 어떻게 구성할지에 대한 중요한 결정 요소임.

> 1. 외부 식별자(Foreign Indentifier) 는 자기 자신의 Entity에서 필요한 속성이 아니라 다른 Entity 와의 관계를 통해 자식 쪽 Entity에 생성되는 속성을 <font color="#4f81bd">외부 식별자</font>라 하며, 이는 DB 생성시 Foreign Key(FK) 역할을 함
> 2. 자식 Entity 에서 부모 Entity 로 부터 받은 외부식별자를 자신의 <font color="#4f81bd">주 식별자로 이용할 것인지(식별관계)</font> 혹은 <font color="#4f81bd">부모와 연결이 되는 속성으로서만 사용할 것인지를 결정(비식별자 관계)</font> 해야 함

![](https://i.imgur.com/KHq32Gn.png)

1. **외부 식별자(Foreign Identifier)와 외래 키(Foreign Key)의 역할**:
    - 외부 식별자는 한 Entity에서 직접적으로 필요하지 않지만, 다른 Entity와의 관계로 인해 자식 Entity에 추가되는 속성.
    - 즉, 이 속성은 다른 Entity의 주 식별자와의 연결을 나타냄.
    - 데이터베이스에서는 이를 외래 키(FK)라고 하며, 데이터베이스 테이블 간의 논리적인 연결을 만드는 데 사용됨.
      
2. **식별자 관계(Identifying Relationship)와 비식별자 관계(Non-identifying Relationship)의 결정**:
    - 자식 Entity가 부모 Entity로부터 받은 외부 식별자를 자신의 주 식별자로 사용하면, 이를 <font color="#4f81bd">'식별자 관계'</font>라고 함. 
    - 이 경우, <font color="#4f81bd">자식 Entity는 부모 Entity 없이는 존재할 수 없으며</font>, 부모의 식별자가 자식의 식별자에 포함되어 있습니다.
    - 만약 <font color="#4f81bd">자식 Entity에서 외부 식별자를 자신의 주 식별자로 사용하지 않고, 단지 부모 Entity와의 연결 속성으로만 사용</font>한다면, 이를<font color="#4f81bd"> '비식별자 관계'</font>라고 합니다. 여기서 자식 Entity는 자체적인 주 식별자를 가지며, 외래 키는 관계를 맺기 위한 속성으로만 존재합니다.

## Entity 간 관계 유형을 결정하는 요소들
- **업무 특징(Business Characteristics)**: 
  업무에서 요구하는 관계의 성격과 데이터의 사용 방식에 따라 관계 유형이 결정
  
- **자식 Entity의 주 식별자 구성**: 
  자식 Entity가 독립적으로 식별 가능해야 하는지, 아니면 부모 Entity에 종속적인 식별자를 가져야 하는지에 따라 결정 됨
  
- **SQL 전략(SQL Strategy)**: 
  SQL 쿼리의 효율성, 인덱싱 전략, 데이터베이스 성능 최적화 등 데이터베이스 관리 측면에서의 전략에 따라 결정될 수 있음

> 가령, '주문'  Entity는 '고객' Entity 의 '고객번호' 를 FK로 가지고 있을 수 있음. 
> (당연하지만) 만약 '주문' 이 '고객' 없이 존재할 수 없다면, 이는 식별자 관계
> 이때 '고객번호' 는 '주문' Entity의 주 식별자에 포함 됨.

> 반면, 주문에 고유한 '주문번호' 가 있고, '고객번호' 는 단지 '주문' Entity와 '고객' Entity 간의 관계를 맺는 용도로만 사용된다면, 이는 비식별자 관계가 됨.


# 식별자 관계 (Identifying Relationship)

> 식별자 관계(Identifying Relationship)는 <font color="#4f81bd">자식 Entity 의 주 식별자로 부모의 주 식별자가 상속이 되는 경우</font>를 말함.

![](https://i.imgur.com/le1l1IT.png)

- **주 식별자의 상속**: 
  - 자식 Entity는 부모 Entity로부터 주 식별자를 상속받아 자신의 주 식별자로 사용. 
  - 이 경우, 부모 Entity의 주 식별자는 자식 Entity에서 외래 키 역할을 동시에 수행하게 됨.
    
- **자식 Entity의 종속성**: 
  - 식별자 관계에서 자식 Entity는 부모 Entity와의 관계에서만 완전한 식별이 가능.
  -  예를 들어, '주문 항목' Entity는 '주문' Entity의 '주문번호'를 주 식별자로 상속받아 '주문 항목 번호'와 함께 사용하여 각각의 '주문 항목'을 구분
    
- **데이터베이스 무결성**: 
  - 식별자 관계는 데이터베이스의 참조 무결성을 강화.
  - 자식 Entity의 인스턴스가 생성되려면 반드시 유효한 부모 Entity의 인스턴스가 존재해야 하기 때문에, 무결성을 유지하는 데 도움이 됨.
    
- **생명주기**: 
  - 부모와 자식 Entity의 생명주기가 서로 밀접하게 연결됨. 
  - 부모 Entity가 삭제되면 그에 연결된 자식 Entity도 함께 영향을 받을 수 있음. 
  - 즉, '주문' Entity가 삭제되면, 그 '주문'에 속하는 '주문 항목' Entity도 함께 삭제되는 것이 일반적


> 식별자 관계(Identifying Relationship)는 <font color="#4f81bd">자식 Entity 의 주 식별자로 부모의 주 식별자가 상속이 되는 경우</font>를 말함. 
> 즉, <font color="#4f81bd">부모 Entity 의 주 식별자가 자식 Entity의 주 식별자 구성요소로 포함</font>되어, 자식 Entity가 부모 Entity 의 식별자에 의해 '부분적으로' 식별이 될 수 있는 관계를 의미.
> 이 경우, 자식 Entity가 독립적으로 존재하기보단, 부모 Entity 와 강한 연결관계를 가지며, <font color="#4f81bd">부모 Entity 없이는 의미를 갖지 못함</font>.

## 식별자관계 예시
![](https://i.imgur.com/Tp4T1PQ.png)


# 비 식별자 관계(Non-Identifying Relationship)

> 비 식별자 관계(Non-Identifying Relationship) 은 부모 Entity 의 주 식별자가 자식 Entity에 FK 로 전달은 되지만, 자식 Entity의 주 식별자로는 사용되지 않는 경우를 말함.
> 자식 Entity 에서 받은 속성이 반드시 필수가 아니어도 되기때문에 부모 없는 자식이 생성될 수 있음


![](https://i.imgur.com/uWOVoFy.png)


- 자식 Entity가 부모 Entity와의 연결은 되어 있지만, 자체적인 주 식별자를 통해 독리적으로 식별 됨
- 자식 Entity는 부모 Entity 없이도 존재할 수 있으며, 부모 Entity 의 생명주기와 직접적으로 연결되어 있지 않음

## 비식별자 관계의 특징
- 부모 Entity의 주 식별자는 자식 Entity에 외래 키로 포함되지만, 자식 Entity를 유일하게 식별하는 데 사용되지 않음.
- 자식 Entity에는 자체적인 주 식별자가 있으며, 이는 부모 Entity의 식별자와는 독립적임.
- 부모와 자식 Entity 간의 연결은 필수가 아닐 수도 있어, 선택적으로 관계를 가질 수 있음
	- 즉, 자식 Entity에 해당 외래 키 값이 NULL이 될 수도 있음
- 부모 Entity가 삭제되더라도, 자식 Entity는 자신의 주 식별자에 의해 계속 존재할 수 있음


## 비식별자 관계 예시
![](https://i.imgur.com/P7zx7pn.png)

- 방문접수, 인터넷접수, 전화접수 Entity가 접수 Entity로 통합되면서 비 식별자 관계가 된 것.

##  💡식별자 관계로만 설정할 경우의 문제점
### 식별자 관계로만 관계를 설정하는 경우
![](https://i.imgur.com/ASGePZN.png)

- 주문 Entity가 고객 Entity의 고객번호를 식별자로 받음

- **강한 종속성**: 
  - 자식 테이블이 부모 테이블의 기본 키를 자신의 기본 키로 포함하므로, 부모 테이블의 기본 키가 변경되면 자식 테이블의 기본 키도 변경되어야 함. 
  - 이로 인해 데이터의 유지보수가 복잡해질 수 있음.
    
- **유연성 감소**: 
  - 모든 자식 테이블이 부모 테이블에 종속되므로, 독립적인 자료의 추가나 변형이 어려워 짐.
    
- **삭제 제한**: 
  - 부모 테이블의 행이 삭제될 때, 관련된 자식 테이블의 행도 함께 삭제되어야 하는 제약이 생기므로 데이터의 삭제가 제한됨.

### 비식별자 관계로만 관계를 설정하는 경우
![](https://i.imgur.com/6lVzUnR.png)

- 주문 Entity가 주문번호라는 식별자를 별도로 이용

- **참조 무결성 문제**: 
  - 부모 테이블에 존재하지 않는 데이터를 참조할 가능성이 존재하며, 이는 데이터의 일관성을 저해할 수 있음
    
- **조인 성능 저하**: 
  - 비식별자 관계는 별도의 참조 키를 사용하기 때문에, 부모와 자식 테이블 간의 조인이 빈번히 발생할 경우 쿼리 성능이 저하될 수 있음
    
- **데이터 관리 복잡성 증가**: 
  - 관계 설정이 유연해지긴 하지만, 그로 인해 데이터 관리가 더 복잡해지고, 참조 데이터의 일관성을 유지하기 위한 추가적인 작업이 필요할 수 있음.

> 즉, 어느 한가지의 관계 설정방식에만 의존하기보다는, 각 상황과 요구사항에 맞게 두 종류의 관계를 적절하게 혼합해 구성해야 함.


# 식별자관계와 비식별자 관계
- 데이터 모델링 과정에서 식별자 관계와 비 식별자 관계를 취사선택해 연결하는 것은 상당한 기반 지식과 경험이 필요한 작업
- 식별자 관계에서 비식별자 관계를 파악하는 기술이 필요하기 때문
- 주로 아래와 같은 흐름으로 관계 파악을 한다면 합리적으로 관계를 설정할 수 있음

![](https://i.imgur.com/6hMiVyt.png)

- 이를 표로 다시 정리하면 아래와 같음

![](https://i.imgur.com/LFLyn7y.png)


---

## 🎈 Outro.
- 식별자는 Entity 내의 Instance를 유일하게 구분하는 Attribute 또는 Attribute의 조합으로, 데이터 무결성과 일관성을 유지하는 데 핵심적인 역할을 합니다.
- 식별자의 분류와 특징을 이해하고, 식별자 도출 기준을 고려하여 적절한 식별자를 선정하는 것이 중요 합니다.
- 식별자 관계와 비식별자 관계의 차이를 파악하고, 상황과 요구사항에 맞게 두 관계를 적절히 혼합하여 사용하는 것이 효과적인 데이터 모델링의 기반이 될 수 있습니다.

