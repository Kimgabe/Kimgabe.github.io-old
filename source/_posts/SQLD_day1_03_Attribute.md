---
title: "[SQLD] 1일차 : 데이터모델링의 이해 - 03. 속성(Attribute)"
cover: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1920&h=1080&fit=crop"
date: 2024-04-24
categories:
  - [personal-study, sql]
tags: []
toc: true
---
## 🚦 Summary
- SQLD 1과목의 3번째 파트인 'Attribute(속성)' 에 대해 정리한 노트입니다.
- Attribute는 Entity를 구성하는 세부 정보로, 업무에서 필요로 하는 Instance에서 관리하고자 하는 의미상 더 이상 분리되지 않는 최소 데이터 단위를 의미합니다.
- Attribute는 Entity의 주 식별자에 함수적 종속성을 가져야 하며, 하나의 Attribute에는 한 개의 값만을 가집니다.
- Attribute는 특성에 따라 기본, 설계, 파생 속성으로 분류되며, Entity 구성 방식에 따라 단일값, 다중값, 복합, 반복 속성으로 분류됩니다.

---


## 📌 Intro.
- Attribute는 Entity의 특징을 나타내는 핵심 요소로, 데이터 모델링에서 중요한 역할을 담당합니다.
- 이번 포스팅에서는 Attribute의 개념과 특징, 분류 방법, 그리고 명명 규칙에 대해 정리할 예정입니다.
- Attribute에 대한 이해는 효과적인 데이터 모델링을 위해 필수적인 요소 이므로, 데이터 모델링이란 과목의 핵심 요소중 하나라 할 수 있습니다.

---


## 과목 범위
![](https://i.imgur.com/sAOM6ba.png)

# Attribute의 개념
- 데이터 모델의 이해 파트에서 Attribute에 대해 아래와 같이 정의한 바 있음

> Attribute : Entity를 구성하는 세부 정보 = Entity 의 특징
> ex) 학생 이라는 Entity에는 학번, 이름 ,주소 등의 속성(Attribute)이 있을 수 있음

- 이러한 Attribute를 정의하는 기준은 아래의 3가지라 할 수 있음
	1. 업무에서 필요로 한다.
	2. 의미상 더이상 분리되지 않는다.
	3. Entity를 설명하고 Instance의 구성요소가 된다.

> 즉, Attribute란 "업무에서 필요로 하는 Instance에서 관리하고자 하는 의미상 더이상 분리됮 않는 최소 데이터 단위" 를 말함

# Entity , Instance, Attribute의 관계
1. 한 개의 Entity 는 두 개 이상의 Instance 집합이어야 한다.
2. 한 개의 Entity 는 두 개 이상의 Attribute를 갖는다.
3. 한 개의 Attribute는 한 개의 Attribute Value를 갖는다.

![](https://i.imgur.com/VDl2FDI.png)

- Attribute는 Entity 에 속한 Entity에 대한 자세하고 구체적인 정보를 나타냄
- 각각의 Attribute는 구체적인 값(value) 를 갖게 됨
- ex) 
	- 이름, 주소, 생년월일 등은 각각의 Value를 대표하는 Attribute 임
	- 홍길동, 서울시 강서구, 1967년 12월 31일 은 각각의 '이름' 이라는 Entity에 대한 구체적인 값이며 이를 Attribute Value(속성(Attribute) 값) 이라 함.

## Attribute 의 표기법
![](https://i.imgur.com/W6MLmzJ.png)

1. Attribute  명의 기재한다.
2. 해당 Attribute가 식별자인지 아닌지 표시한다.
3. 해당 속성(Attribute)이 필수값(`*`) 인지 선택값(`0`) 인지 표시 한다.

> 이때, 속성(Attribute)의 표기법은 엔티티 내에 이름을 포함하여 표현한다.

# Attribute 의 특징
1. Entity와 마찬가지로 반드시 해당업무에 필요하고 관리하고자 하는 정보여야 한다.
   - ex) 강사의 교재 이름
2. 정규화 이론에 근간해 정해진 주 식별자에 함수적 종속성(Attribute)을 가져야 한다.
   - 즉, 특정 Entity의 속성(Attribute)이 그 Entity의 주 식별자 (Primary Key) 에 의해 유일하게 결정되어야 한다는 의미
3. 하나의 속성(Attribute)에는 한 개의 값만을 가진다. 
   - 하나의 속성(Attribute)에 여러 개의 값이 있는 다중 값일 경우 별도의 Entity를 이용해 분리한다.

> 정규화 이론 
> 데이터베이스의 설계를 개선하기 위해 데이터의 중복을 제거하고, 무결성을 확보하는 과정
> 쉽게 말해 DB내에 중복값없이 Unique한 값만 남도록 전처리 하는 것

> 🤔 함수적 종속성(Attribute)?
> 하나의 속성(Attribute)이 다른 속성(Attribute)에 의존하는 관계를 의미

>  🤔주 식별자(Primary Key)?
>  Entity내에서 각 Instance를 유일하게 식별할 수 잇있는 속성(Attribute) 또는 속성(Attribute)의 조합>  

2번의 내용에 대한 예시
 👉"강사 Entity에서 '강사번호' 라는 Primary key가 있을 때, '교재 이름' 이라는 속성(Attribute)은 해당 '강사번호' 에 함수적 종속성(Attribute)을 가져야 한다" 는 의미

# 속성(Attribute)의 분류 (feat. 특성에 따른 분류)
![](https://i.imgur.com/DrrlCqd.png)

## 분류별 속성(Attribute) 예시
![](https://i.imgur.com/HC7tduQ.png)

# 속성(Attribute)의 분류 (feat. Entity 구성방식에 따른 분류)
![](https://i.imgur.com/KKd4843.png)

## Entity 구성방식에 따른 속성(Attribute) 분류 예시
![](https://i.imgur.com/wXP2EfW.png)

# 도메인(Domain)
1. 각 속성(Attribute)은 가질 수 있는 값의 범위가 잇는데, 이를 속성(Attribute)의 도메인(Domain) 이라 함
2. 학생이라는 Entity 가 있을 때 학점이라는 속성(Attribute)의 도메인은 0.0 ~ 4.5 사이의 실수값이며, 주소라는 속성(Attribute)은 길이가 20자리 이내인 문자열(String) 로 정의
3. 각 속성(Attribute)은 도메인 이외의 값을 갖지 못함

# 속성(Attribute)을 명명하는 방법
1. 해당 업무에서 사용하는 이름을 부여 한다.
2. 서술 식 속성(Attribute) 명은 사용하지 않는다. 
3. 약어 사용은 가급적 제한 한다.
4. 가급적, 전체 데이터모델에서 유일성을 확보하는 것이 좋다.

---


## 🎈 Outro.
- Attribute는 Entity의 세부 정보를 나타내는 최소 데이터 단위로, 업무에서 필요로 하는 정보를 관리하는 데 핵심적인 역할을 합니다.
- Attribute의 특징을 이해하고, 특성과 Entity 구성 방식에 따른 분류를 알아두는 것이 중요합니다.
- 업무에서 사용하는 이름을 부여하고, 서술식 명명과 약어 사용을 자제하며, 전체 데이터 모델에서 유일성을 확보하는 것이 좋은 Attribute 설계의 기반이 됩니다.

