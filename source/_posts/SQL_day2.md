---
title: "[SQL] SQL의 기본 SELECT문 ~ 비교연산자(LIKE)"
cover: "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1920&h=1080&fit=crop"
date: 2020-10-21
categories:
  - [personal-study, sql]
tags: []
toc: true
---
## 🚦 Summary
- 빅데이터 분석가 과정의 SQL수업을 노트로 정리합니다.
- 약 4주간 467문제를 풀며 SQL의 기본 개념부터 심화 개념까지 학습합니다.
- Day 2 : SQL의 기본 개념 및 COLUMN 선택방법, 연결연산자, 중복제거, order by절, where절, 산술연산자, 비교연산자 에 대해 배우고 실습 문제를 정리합니다.
---


## 001 테이블에서 특정 열(COLUMN) 선택하기

```sql
select ename, sql from emp;
```

- select = 조회 / 선택해라
- ename, sal 등등 = 'COLUMN' 이라고 함
- from = ~로 부터
- emp = emp table
- ; = 앞의 명령어를 '실행해라'

문제 3. emp 테이블에 컬럼이 무엇이 있는지 확인하시오

```sql
desc emp
```
```sql
describe emp
```

- 두 가지 방법으로 조회할 수 있음

![](https://i.imgur.com/iRDWqnD.png)

문제 4. 이름, 월급, 커미션을 출력하시오

```sql
select ename, sql, comm from emp;
```
![](https://i.imgur.com/OMhv0ON.png)

> 💡 Tip. SQL 입력시 주의 사항
-  SQL 은 대/소문자를 가리지 않고 모두 동일한 문자로 인식합니다.

소문자 : 
```sql
select ename, sal from emp;
```

대문자 : 
```sql
SELECT ENAME, SAL FROM EMP;
```

- 어느 것으로 하든 결과는 아래와 같이 동일합니다.

![](https://i.imgur.com/On2Vthi.png)

### SQL 에서 '절'은 다음 라인으로 '분리'해서 작성한다
- 절의 종류
	- SELECT: 조회하고 싶은 컬럼을 명시합니다.
	- FROM: 데이터를 가져올 테이블을 명시합니다.
	- WHERE: 조건에 맞는 데이터만 선택합니다.
	- GROUP BY: 컬럼 기준으로 데이터를 그룹화합니다.
	- HAVING: 그룹화된 데이터에 대한 조건을 설정합니다.
	- ORDER BY: 결과를 정렬하는 기준을 명시합니다.

> 💡 Tip. 실제 작업을 하다보면 내용이 길어지기 때문에 옆으로 늘리지 말고 아래로 내리자!

- 들여쓰기('tap 버튼')를 사용해서 SQL의 '가독성'을 높이는 것이 중요!

![](https://i.imgur.com/xnT9VFS.png)

 👉SQL 코딩한 것에서 에러를 찾기에는 '소문자'가 더 좋음! -> 그러니 가급적 소문자로 입력하는 것이 좋습니다.

문제 5. 이름, 직업, 입사일, 부서번호를 출력하시오 

- 내 생각 : 정답
```sql
select ename job, hiredate, deptno;
	-- 들여쓰기 적용
	from emp; 
```
![](https://i.imgur.com/D6QbdWv.png)

문제 6. emp 테이블에 모든 컬럼을 검색하시오.

```sql
desc emp
```

>💡 Tips. 검색된 컬럼을 더 많이 확인하기(화면 가로 사이즈 조절)

- 결과 화면의 가로사이즈 조절하는 명령어

```sql
set lines 300
```

- 수치는 임의로 사용해보면서 조절 하면 됩니다.

- 추가로 직전에 입력했던 명령어들을 다시 입력하기 귀찮다면 `/ + 엔터` 로  동일 명령어를 반복하도록 할 수 있습니다.

![](https://i.imgur.com/7sEbeVI.png)

---


## 002 테이블에서 모든 열(COLUMN) 출력하기

```sql
select *
	from emp;
```

- 위와 같이 `*` 를 입력해 `전체` 를 조회하도록 할 수 있습니다.
-  * (특수문자 별) 은 asterisk (아스탈리스크) 라고 하며, 모든 컬럼을 다 선택할때 사용합니다.

![](https://i.imgur.com/onY9EST.png)

문제 7. detp table에 모든 컬럼을 출력하시오 

```sql
select *
	from dept;
```

![](https://i.imgur.com/Mrstrmv.png)

> dept 는 부서 테이블이고 컬럼은 3개가 있는데 다음과 같습니다.
> 	deptno = 부서번호
> 	dname = 부서명
> 	loc = 부서위치

- 결과값에서 각 데이터의 한 행은 `row` 라고 합니다.

## 003 컬럼 별칭을 사용하여 출력되는 컬럼명 변경하기

- 컬럼 별칭이란, 컬럼명 대신에 다른 컬럼명을 지정할때 사용하는 문법입니다.
- 주로, 컬럼명 뒤에 'as'를 쓰고, 컬럼별칭을 작성한다. 그러면 결과가 출력될때 컬럼 별칭이 출력됩니다.
  💡Tip. 'as' 는 생략 가능! 하나 가급적 써주는게 코드 가독성이 더  좋습니다!

```sql
select ename as 이름, sal as 월급
	from emp;
```

![](https://i.imgur.com/hwedwo8.png)

- 'as' 다음에 나오는 별칭으로 변경되어 테이블이 출력됨!

문제 8. 이름과 입사일과 부서호를 출력하는데 컬럼명이 한글로 이름, 입사일, 부서번호로 출력되게 하시오.

```sql
select ename 이름, hiredate 입사일, deptno 부서번호
	from emp;
```

- 위에도 언급 했지만 가급적인 `as` 는 써주는게 좋습니다.
- 제 3자가 코드를 보고 리팩토링 하거나 할 때 유용하기 때문입니다.

```sql
select ename as 이름 hiredate as 입사일 deptno as 부서번호
	from emp;
```

![](https://i.imgur.com/ikKRuT1.png)

문제 9. 이름과 월급을 출력하는데, 컬럼명이 아래와 같이 출력되게 하시오.
Employee name, Salary (대소문자 구문 , 띄어쓰기도 적용되어야 함)

```sql
select ename as "Employee name", sal as "Salary"
	from emp;
```

![](https://i.imgur.com/uToVK3h.png)

- 컬럼별칭에 대소문자를 구분하고 싶거나 공백문자 혹은 특수문자를 넣으려면 양쪽에 더블 쿼테이션 마크 (") 를 둘러줘야 함!

## 004 연결 연산자 사용하기( || )
- 연결 연산자는 두 컬럼의 데이터를연결해서 출력하는 연산자를 의미함

![](https://i.imgur.com/UXU2AJu.png)

- 테이블간 연결 응용 예시

![](https://i.imgur.com/x1MtPpg.png)

> 💡 Tip. 명령어 입력했는데 컬럼 하나만 오류나서 그것만 수정하고 싶을때
1.      ed (or edit) + 엔터 -> 메모장에 수식이 입력된채로 열림
2.     메모장 안에서 수정하고 싶은 명령어 수정 (맨 밑에 / 표시 있으니 ; 입력하면 안됨)
3.     저장 하고 나가기
4.     다시 도스창에서 / + 엔터 ( / + 엔터 = 직전에 입력한 명령어를 다시 입력하라는 뜻)

문제 10. 아래와 같이 결과를 출력하시오.
KING 의 직업은 PRESIDENT 입니다. 와 같은 양식으로 14명이 나오게 하시오.

```sql
select ename || '의 직업은 ' || job || ' 입니다.'
	from emp;
```

![](https://i.imgur.com/nOo6VOj.png)

문제 11. 위의 결과에서 출력되는 컬럼명을 사원정보라는 한글로 출력되게 하시오.

```sql
select ename || ' 의 직업은 ' || job || ' 입니다.'  as 사원정보
	from emp;
```

![](https://i.imgur.com/SUQScmM.png)

---


## 005 중복된 데이터를 제거해서 출력하기(DISTINCT)

- distinct 키워드를 컬럼명 앞에 작성하고 실행하면 중복된 데이터를 제거하고 출력할 수 있습니다.

![](https://i.imgur.com/5XpsCMc.png)

문제 12. 부서번호를 출력하는데 중복을 제거해서 출력하시오.

```sql
select distinct deptno
	from emp;
```

![](https://i.imgur.com/k4Y3rtf.png)

- distinct 뒤에 컬럼명 쓰고, 그 뒤에 다른 컬럼명을 여러 개 쓰면 분리되지 않습니다.

---


##  006 데이터를 정렬해서 출력하기(ORDER BY)

- `order by` 절은 데이터를 정렬하는 절이고, select 문장에 맨마지막에 기술합니다.
- `order by` 뒤에 정렬할 컬럼명 , 그 뒤에 정렬하는 방법 순으로 입력합니다.

```sql
select ename, sal
	from emp
	order by sal asc;
```

![](https://i.imgur.com/CQE4Kbj.png)

- asc = 올림차순-낮은 값이 위로 오게
- desc = 내림차순-높은 값이 위로 오게

문제 13. 이름과 월급을 출력하는데, 월급이 높은 사원부터 출력하시오.

```sql
select ename, sal
	from emp
	order by sal desc;
```

![](https://i.imgur.com/buMBY8L.png)

문제 14. 이름과 입사일을 출력하는데, 최근에 입사한 사원부터 출력하시오.

```sql
select ename, hiredate
	from emp
	order by hiredate desc;
```

![](https://i.imgur.com/4Zp2C9f.png)

점심시간 문제) 이름과 월급과 부서번호를 출력하는데 부서번호가 10번, 20번, 30번 순으로 출력되게 하고, 컬럼명이 한글로 이름, 월급, 부서번호로 출력되게 하시오.

```sql
select ename as 이름, sal as 월급, deptno as 부서번호
	from emp
	order by deptno asc;
```

![](https://i.imgur.com/IXdc71g.png)

### 여러 컬럼에 동시 적용 가능한 `order by` 절
- 말그대로 `order by` 절은 1개의 컬럼에만 적용되는 것이 아니라 여러 컬럼에 동시에 적용시킬 수 있습니다.

```sql
select ename, deptno, sal
	from emp
	order by detpno asc, sal desc;
```

- 위 쿼리는 부서번호는 asc로 정렬한 뒤, 그 값을 기준으로 sal이 desc하게 정렬되도록 하는 명령어 입니다.

![](https://i.imgur.com/LJQUe7k.png)

>  💡현업에서 컬럼명이 너무 길거나, 많을때 팁!!

- 컬럼 순서에 맞는 번호로 대체하여 입력하면 빠르게 쿼리를 작성할 수 있습니다.
- 하지만 쿼리의 가독성을 생각하면 가급적 돌아가더라도 테이블명을 제대로 써주는게 좋긴 합니다!

```sql
select ename, detptno, sal
	from emp
	order by 2 asc, 3 desc;
```

![](https://i.imgur.com/w3qLTHN.png)

문제 15. 이름과 직업과 입사일을 출력하는데, 직업은 ABCD 순으로 정렬해서 출력하고 그렇게 출력한 값을 기준으로 입사일을 먼저 입사한 사람부터 출력되게 하시오.

```sql
select ename, job, hiredate
	from emp
	order by job asc, hiredate asc;
```

![](https://i.imgur.com/Kx8fIv9.png)

----


## 007 WHERE절 배우기 1(숫자 데이터 검색)

- where 절을 사용하면, 특정 조건에 대한 데이터만 선별해서 출력할 수 있습니다.

```sql
select ename, sal
	from emp
	where sal = 3000;
```

![](https://i.imgur.com/rzc7sKK.png)

문제 16. 사원번호가 7788번인 사원의 사원번호와 이름과 월급을 출력하시오 

```sql
select empno, ename, sal
	from emp
	where empno = 7788;
```

![](https://i.imgur.com/o47k4uk.png)

문제 17. 30번 부서번호에서 근무하는 사원들의 이름과 월급과 부서번호를 출력하세요

```sql
select ename, sal, deptno
	from emp
	where deptno = 30;
```

![](https://i.imgur.com/SPiYiwe.png)

문제 18. 문제 17의 결과를 월급이 높은 사원순으로 출력하시오.

```sql
select ename, sal, deptno
	from emp
	where deptno = 30
	order by sal desc;
```

![](https://i.imgur.com/KMZwIgA.png)

문제 19. 부서번호가 20번인 사원들의 이름과 입사일과 부서번호를 출력하는데 최근에 입사한 사원부터 출력하시오.

```sql
select ename, hiredate, deptno
	from emp
	where deptno = 20
	order by hiredate desc;
```

![](https://i.imgur.com/0NwXFzC.png)

---


## 008 WHERE절 배우기 2(문자와 날짜 검색)

- where 절로 검색할때 숫자와는 다르게 문자는 양쪽에 싱글 쿼테이션 마크를 둘러줘야 합니다.

![](https://i.imgur.com/wBO4nmm.png)

- SQL은 대소문자를 구분하지 않으나, 데이터는 대소문자를 구분합니다. 
- 따라서 `where` 등으로 지정할 때 대/소문자를 명확하게 구분 해줘야 합니다.
- 현재 emp table 의 경우 소문자로 하면 데이터가 없기 때문에 결과값이 나오지 않습니다.

![](https://i.imgur.com/0EKGuVO.png)

- 그 외에도 문자와 날짜 데이터는 singe quatation 이 없으면 날짜 데이터로서 식별을 하지 못합니다.

![](https://i.imgur.com/uN11j5g.png)

- 쉽게 말하자면 singel quatation 마크안에 있는 데이터는 '문자 또는 날짜이다' 라고 오라클에게 알려주는 것이라 할 수 있습니다.

문제 20. 직업이 salesman 인 사원들의 이름과 월급과 직업을 출력하시오

```sql
select ename, sal, job
	from emp
	where job = 'SALESMAN';
```

![](https://i.imgur.com/cIuPkgb.png)

문제 21. 81년 11월 17일에 입사한 사원의 이름과 입사일을 출력하시오.

```sql
select ename, hiredate
	from emp
	where hiredate = '81/11/17';
```

![](https://i.imgur.com/j29Oyoz.png)

>  💡Tip. 날짜 검색을 할때는 연도/월/일 순으로 검색을 하면 됩니다. 
>  단, dataformat의 경우 사용하는 나라마다 순서가 다를 수 있습니다.

- 예를 들어, 미국이나 영국에서의 날짜 검색은 일/월/년 순서 입니다. 
- 반대로 한국에서는 년/월/일 순입니다.

---


## 009 산술 연산자 배우기(\*, /, +, -)
```sql
select ename, sal, sal + 3000
	from emp;
```

- emp 테이블에서 ename과 sal 그리고 각 sal 에 3000을 더한 값을 출력합니다.

![](https://i.imgur.com/O7EJZYS.png)

문제 22. 이름과 연봉 (sal\*12) 을 출력하는데 컬럼명을 한글로 이름, 연봉으로 출력하시오.

```sql
select ename as 이름, sal*12  as 연봉
	from emp;
```

![](https://i.imgur.com/4b5IRmj.png)

문제 23. 위의 결과를 다시 출력하는데 연봉이 36000인 사원들의 이름과 연봉을 출력하시오.

```sql
select ename as 이름, sal*12 as 연봉
	from emp
	where sal*12 = 36000;
```

![](https://i.imgur.com/XCGvhBu.png)

🤔 위에서 `sal*12` 를 `연봉` 이라고 alies를 정했는데 왜 이걸 사용하지 않았을까?

![](https://i.imgur.com/XjM1mks.png)

- 오라클이 내부적으로 실행하는 순서는 from 절 -> where 절 -> select 절 순서입니다.
- 즉, 코딩 순서와 실행 순서는 다릅니다.
- 그렇기 때문에 위의 명령어가 실행되지 않는 것 입니다.

> 코딩 순서 : select 👉 from 👉 where
> 실제 실행 순서 : from 👉 where 👉 select

### 💡 SQL 6개 쿼리문의 입력순서와 실행순서
**코딩 순서:**
`SELECT` 👉 `FROM` 👉 `WHERE` 👉 `GROUP BY` 👉 `HAVING` 👉 `ORDER BY`

**실제 실행 순서:**
`FROM` 👉 `WHERE` 👉 `GROUP BY` 👉 `HAVING` 👉 `SELECT` 👉 `ORDER BY`

**참고:**
- `SELECT` 문은 필수이며, 항상 맨 처음에 작성해야 합니다.
- `FROM` 문은 필수이며, `SELECT` 문 다음에 작성해야 합니다.
- 나머지 쿼리 문들은 선택 사항이며, 위 순서대로 작성해야 합니다.

문제 24. 이름과 연봉을 출력하는데 연봉이 높은 사원부터 출력하시오.

```sql
select ename, sal*12
	from emp
	order by sal*12 desc;
```

![](https://i.imgur.com/z0oRv5N.png)

문제 25. 아래의 SQL에서 더하기가 먼저 실행되게 하려면?

```sql
select ename, sal + 200 * 2
	from emp;
```

```sql
select ename, (sal+200)*2
	from emp;
```

![](https://i.imgur.com/yZki6bh.png)

- 정답은 일반 수학 공식처럼 괄호를 사용하면 된다! 입니다.

----


## 010 비교 연산자 배우기 1(〉, 〈, 〉=,〈=, =, !=,〈〉, ^=)

 - !=,〈〉, ^= 는 모두 '같지 않거나' 를 의미 (3가지) (사실상 같지 않다./ 다르다)
- 실제로는 != 를 제일 많이 쓰는 편입니다.
- 아래 2개의 부등호도 잘 혼동하는 부등호 입니다.
	- >= + 숫자 는 '숫자' 보다 크거나 같다.(=이상)
	- =150;
```

![](https://i.imgur.com/OM5PlEX.png)

문제 27. 월급이 3000 이상인 사원들의 월급과 이름을 출력하시오.

```sql
select ename, sal
	from emp
	where sal >= 3000;
```

![](https://i.imgur.com/luoL4C6.png)

문제 28. 직업이 SALESMAN 이 아닌 사원들의 이름과 직업을 출력하시오.

```sql
select ename, job
	from emp
	where job != 'SALESMAN';
```

![](https://i.imgur.com/raLjUok.png)

- 문자와 날짜는 반드시 양쪽에 싱글 쿼테이션 마크를 둘러줘야 합니다.

> 💡 Tips. 더블 쿼테이션 마크는 오라클 전체를 통틀어서 딱 하나의 케이스에서만 사용합니다. 컬럼별칭 사용할때 공백문자, 특수문자, 대소문자를 구분해서 컬럼별칭을 출력하고자 할때만 사용한다. (그 외의 모든 케이스는 싱글쿼테이션!!)

문제 29. 월급이 2400 이하인 사원들의 이름과 월급을 출력하는데, 월급이 높은 사원부터 출력하시오

```sql
select ename, sal
	from emp
	order by sal desc;
```

![](https://i.imgur.com/sDSeljF.png)

문제 30. 월급이 1000에서 3000 사이인 사원들의 이름과 월급을 출력하시오.

- 풀이 1 : between 을 사용해서 범위를 지정하는방법

```sql
select ename, sal
	from emp
	where sal between 1000 and 3000;
```

- 풀이 2 : and 를 사용해서 조건을 지정하는 방법

```sql
select ename, sal
	from emp
	where sal >= 1000 and sal  🚫 명령어 속 %가 와일드 카드가 되려면 앞에 반드시 like 가 와야합니다. 
>  예를들어 equal 을 쓴뒤 %를 입력하면 말그대로 퍼센트의 의미로 받아들여집니다.

문제 33. 이름의 끝 글자가 T로 '끝나는' 사원들의 이름을 출력하시오.

```sql
	select ename
		from emp
		where ename like '%T';
```

![](https://i.imgur.com/kdnUtHN.png)

문제 34. 81년도에 입사한 사원들의 이름과 입사일을 출력하는데 between / and 사용하지 않고 like를 사용해서 출력하시오.

- 생각했던 답 : 오답

```sql
select ename, hiredate
	from emp
	where hiredate like '81/%/%';
```

✔️ 오답체크

**1. `LIKE` 연산자의 패턴 매칭 방식:**
- `%`는 0개 이상의 임의 문자를 나타냅니다.
- `_`는 단일 문자를 나타냅니다.

따라서 `hiredate LIKE '81/%/%'`는 다음과 같은 조건에 맞는 레코드를 모두 선택합니다.

- `hiredate`의 첫 번째 문자는 `8`입니다.
- `hiredate`의 두 번째 문자는 `1`입니다.
- `hiredate`의 세 번째 문자는 임의 문자입니다.
- `hiredate`의 네 번째 문자는 임의 문자입니다.
- `hiredate`의 다섯 번째 문자는 임의 문자입니다.

**2. 문제점:**

`81/%/%` 패턴은 81년도에 입사한 모든 사원을 선택하지만, **81년 이후에 입사한 사원 중 앞 두 자리가 `81`인 경우에도 선택**합니다.

예를 들어, 1982년 1월 1일에 입사한 사원의 `hiredate`는 `'82/01/01'`입니다. 이는 `LIKE '81/%/%'` 패턴에 부합하기 때문에 잘못 선택됩니다.

- 정답

```sql
select ename, hiredate
	from emp
	where hiredate like '81%';
```

![](https://i.imgur.com/X9Gyi7l.png)

문제 35. 이름의 2번째 철자가 M인 사원들의 이름을 출력하시오.

```sql
select ename
	from emp
	where ename like '_M%';
```

![](https://i.imgur.com/yW0zuLc.png)

- 오답노트에서도 정리했듯, like 와 쓸 수 있는 키워드는 2개 입니다.
	- % : 와일드카드 = 이 자리에 뭐가와도 관계 없고, 그 갯수가 몇개가 되던 상관없다는 뜻.
	- _ : 언더바 = 이 자리에 뭐가 와도 관계없는데 자릿수는 한개여야 한다 는 뜻

문제 36. 이름 세번째 철자가 A인 사원들의 이름을 출력하시오.

```sql
select ename
	from emp
	where ename like '__A%';
```

![](https://i.imgur.com/nm9EHiI.png)

## 🤔 오늘의 회고

- 오늘 여러 문제의 쿼리 짜면서 제일 많이 하는 실수는 'where' 뒤에 어떤 기준이 될 컬럼을 입력하지 않는 것이었습니다.
- 그리고 부등호 표시 할때 어떤 기호가 크고 작은 쪽인지 구분을 잘 못해서 헷갈려 했었습니다.

>  ' '>' + 숫자면 (이하) = 숫자를 외면하면 숫자 이하

