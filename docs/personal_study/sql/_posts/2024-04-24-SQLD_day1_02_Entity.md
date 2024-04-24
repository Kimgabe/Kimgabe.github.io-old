---
layout: single
title: '"[SQLD] 1일차 : 데이터모델링의 이해 - 02. Entity"'
categories:
  - sql
tags:
  - sql
  - SQLD
  - 노트정리
  - Entity
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
- SQLD 1과목의 2번째 파트인 'Entity' 에 대해 정리한 노트입니다.
- Entity는 데이터 모델링에서 업무에 필요하고 유용한 정보를 저장하고 관리하기 위한 집합적인 것(Thing)을 의미합니다.
- Entity는 반드시 속성(Attribute)을 가지며, 다른 Entity와 최소 한 개 이상의 관계를 맺어야 합니다.
- Entity는 유형에 따라 키 Entity, 일반 Entity, 중심 Entity, 행위 Entity 등으로 분류됩니다.

---

## 📌 Intro.
- 데이터 모델링은 정보 시스템을 구축하기 위한 핵심적인 과정 중 하나로, 복잡한 현실 세계를 체계적으로 표현하고 분석하는 기법입니다. 
- 이번 포스팅에서는 데이터 모델링의 정의와 특징, 데이터베이스 3단계 구조와 데이터 독립성, 그리고 데이터 모델링의 요소와 작업 순서 등에 대해 알아보겠습니다. 데이터 모델링에 대한 이해는 정보 시스템 구축에 참여하는 모든 이해관계자에게 필수적인 지식입니다.

---
## 과목 범위
![](https://i.imgur.com/eHZvhcw.png)



# # Entity 의 개념
- 데이터 모델의 이해 파트에서 정리해본 Entity 의 개념을 확인해보자면 
	- Entity는 사람, 장소, 무건, 사건, 개념 등의 "명사"에 해당
	- Entity는 업무상 관리가 필요한 관심사 에 해당
	- Entity 는 저장이 되기 위한 어떤 것 (Thing)

> Entity : "업무에 필요하고 유용한 정보를 저장하고 관리하기 위한 집합적인 것(Thing)" 


# Entity 와 Instance
![](https://i.imgur.com/xIU1hQy.png)

> Entity : DB에서 데이터를 저장하는 기본 단위
> 구체적이고 명확하게 식별이 가능한 객체, 사건을 의미
> ex) 학생, 교수, 강의

> Instance : Entity 혹은 Relationship 에 대한 구체적인 사례로 DB의 테이블에서 row로 표현 됨
> ex) 학생 Entity의 Instance는 실제로 등록된 각각의 학생을 의미


# Entity 표기법
![](https://i.imgur.com/2YLkyQE.png)

# Entity 의 특징
- 반드시 해당 업무에서 필요하고 관리하고자 하는 정보여야 한다.
- 유일한 식별자에 의해 식별이 되어야 한다.
- 영속적으로 존재하는 Instance의 집합이어야 한다. 
	- '한개' 가 아니라 '두 개 이상' 이어야 한다는 의미
- Entity는 업무 프로세스에 의해 이용되어야 한다.
- Entity 는 반드시 속성(Attribute) 이 있어야 한다.
- Entity는 다른 Entity와 최소 한 개 이상의 관계가 있어야 한다.

![](https://i.imgur.com/1xg3VsW.png)

## Entity 는 반드시 Attribute가 포함되어야 한다.
![](https://i.imgur.com/84prDAs.png)


## Entity 는 다른 Entity 와 최소 한 개 이상의 관계가 존재 해야 한다.
![](https://i.imgur.com/WUUxtB4.png)


### 데이터 모델에서의 관계
- **1:1 관계(One-to-One)**: 한 Entity의 인스턴스가 다른 Entity의 단 하나의 인스턴스와만 관계를 맺는 경우입니다. 예를 들어, 한 사람이 하나의 주민등록번호를 가지는 경우
    
- **1:N 관계(One-to-Many)**: 한 Entity의 인스턴스가 다른 Entity의 여러 인스턴스와 관계를 맺을 수 있는 경우입니다. 예를 들어, 한 강사가 여러 강의를 담당하는 경우
    
- **M:N 관계(Many-to-Many)**: 한 Entity의 여러 인스턴스가 다른 Entity의 여러 인스턴스와 관계를 맺을 수 있는 경우입니다. 예를 들어, 여러 학생이 여러 강의를 수강하는 경우



# Entity 의 분류
![](https://i.imgur.com/HUmgVs9.png)

![](https://i.imgur.com/billRdT.png)


# Entity 의 명명 방식
1. 가능하면 <font color="#4f81bd">현업업무에서 사용하는 용어</font>를 쓴다.
2. 가급적 <font color="#4f81bd">약어를 사용하지 않는다.</font>
3. <font color="#4f81bd">단수 명사</font>를 사용한다.
4. 모든 Entity의 <font color="#4f81bd">이름은 Unique 해야 한다</font>. (중복 x)
5. Entity의 <font color="#4f81bd">생성 의미대로 이름을 부여</font>해야 한다.

---

## 🎈 Outro.
- Entity는 데이터 모델링에서 정보를 저장하고 관리하는 기본 단위로, 속성과 관계를 통해 업무를 표현합니다.
- Entity의 특징을 이해하고, 유형에 따른 분류를 알아두는 것이 중요합니다.
- 현업에서 사용하는 용어를 활용하고, 약어 사용을 자제하며, 단수 명사를 사용하는 등 명명 규칙을 따르는 것이 좋은 Entity 설계의 기반이 됩니다.

