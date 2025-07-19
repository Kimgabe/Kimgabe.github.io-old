---
title: "[SQL] 「입문」 SQL 첫발 내딛기"
cover: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1920&h=1080&fit=crop"
date: 2020-10-20
categories:
  - [personal-study, sql]
tags: []
toc: true
---
## 🚦 Summary
- 빅데이터 분석가 과정의 SQL수업을 노트로 정리합니다.
- 약 주간 467문제를 풀며 SQL의 기본 개념부터 심화 개념까지 학습합니다.
- 실습은 ORACLE을 사용해서 실습합니다.
- Day 1 : SQL의 기본 개념 및 예제 테이블을 불러와서 조회하는 작업을 배워봅니다.
---


## SQL 기본 개념

- 오라클 = Database software
	- 오라클은 DB분야 세계 점유 80%의 대기업명 이기도함. DB SW를 만든 회사이자 그 SW의 이름이 오라클
- DB = data를 저장하고 관리하는 저장소를 말함

###  SQL = Structure Query Language (구조적 지리 언어)

       = 데이터를 검색하고 조작하는 언어

- SQL을 왜 배워야 하는가?
	- 데이터를 검색하고 다룰려면 무조건 알아야함.

> If 진로가 Data Analyst / Data developer, 많은 업무에서 SQL이 많이 사용됨. So 반드시 SQL을 배워야함.

### SQL의 종류 (총 5가지)

1.      **Query (데이터를 검색하는 언어)**
- 6개의 절이 존재
	- SELECT: 조회하고 싶은 컬럼을 명시합니다.
	- FROM: 데이터를 가져올 테이블을 명시합니다.
	- WHERE: 조건에 맞는 데이터만 선택합니다.
	- GROUP BY: 컬럼 기준으로 데이터를 그룹화합니다.
	- HAVING: 그룹화된 데이터에 대한 조건을 설정합니다.
	- ORDER BY: 결과를 정렬하는 기준을 명시합니다.

2.     **DML 문 (Data Manipulation Language , 데이터 조작 언어)**
	- `insert` = 데이터 입력 언어
	- `update` = 데이터 수정 언어
	- `delete` = 데이터 삭제 언어
	- `merge` = 데이터 입력, 수정, 삭제를 한번에 수행하는 명령어

3.     **DDL 문 (Data Definition Language, 데이터 정의어)**
	- `create` = 생성
	- `alter` = 수정
	- `drop` = 삭제
	- `truncate` = 삭제
	- `rename` = 이름변경

4.     **DCL 문 (Data Control Language, )**
	- `grant` = 데이터를 접근 할 수 있는 권한을 부여하는 것
	- `revoke` = 데이터를 접근 할 수 있는 권한을 취소하는 것 (뺏는것)

5.     **TCL 문 (Transaction Control Language)**
	- `commit` = 현재의 데이터의 상태를 DB에 `영구히` 저장하겠다. (는 뜻)
	- `rollback` = 지금까지 했던 작업을 다 `취소` 하겠다. (는 뜻)
	- `savepoint` = 특정시점까지 `rollback` 하는 기능

> `핵심`은 내가 보고 싶은 데이터를 정확하게 검색해서 보는 `기술`을 배우는 것. = SQL

---


## 001 테이블에서 특정 열(COLUMN) 선택하기

### 데이터 검색하기

```sql
select ename, sql from emp;
```

- `select` = 검색 / 조회 해라
- `ename` = 이름 하고
- `sal` = 월급을
- `from` =무엇으로 부터?
- `emp` = emp라는 table 로 부터
- ` ; ` (세미 콜론) = 세미콜론 앞에 있는 (SQL) 문장 `실행해라` 라는 뜻(명령어)

👉 즉, emp 라는 이름의 테이블에서 이름과 월급을 검색한 결과를 출력해라~!

### emp table의 컬럼정보
empno : 사원번호
ename : 사원이름
sal : 월급
job : 직업
comm : 커미션
mgr : 관리자 번호
hiredate : 입사일
deptno : 부서번호

---


### 오늘의 마무리
문제 1. 이름과 월급과 직업을 출력하시오

- 나의 생각 (정답이었음)
```sql
select ename, sql, job from emp;
```

![](https://i.imgur.com/bxcX5v7.png)

문제 2. 이름와 입사일과 부서번호를 출력하시오 

- 나의 생각 : 맞음
```sql
select ename, hiredate, deptno from emp;
```

![](https://i.imgur.com/f8tktIU.png)
