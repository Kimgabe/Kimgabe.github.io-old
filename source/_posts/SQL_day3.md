---
title: "[SQL] SQL의 기본 비교연산자(IS NULL ~ SQL 함수(LENGTH)"
cover: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1920&h=1080&fit=crop"
date: 2020-10-22
categories:
  - [personal-study, sql]
tags: []
toc: true
---
## 🚦 Summary
- 빅데이터 분석가 과정의 SQL수업을 노트로 정리합니다.
- 약 4주간 467문제를 풀며 SQL의 기본 개념부터 심화 개념까지 학습합니다.
- Day 3 : 지난 시간에 배웠던 내용을 복습하고, SQL의 다양한 비교연산자와, 논리연산자, 그리고 출력 결과물에 대한 처리를 하는 다양한 함수(upper, lower, intcap, substr, length 등) 에 대해 정리합니다.
---


## 강사님의 Tips 

1.	SQL 을 왜 배워야 하는가? 데이터를 검색하는데 파이썬의 판다스를 이용해도 되는데 왜 굳이 SQL을 해야하는가?

👉 회사의 중요한 데이터는 다 database 에 저장되어 있고, 대용량 데이터입니다. 
그리고 그 대용량 데이터에서 데이터를 검색하는데 시간이 오래걸린다.

> 💡 Tip) 아무리 SQL이라 해도, 효율성을 고려하지 않고 작성하면 검색시간이 너무 오래 걸리게 됩니다. 그러므로 항상 검색 시간을 고려해서 SQL을 작성해야 합니다.
 
- 그런데 오라클은 버전이 업그레이드 될수록 점점 인공지능화 되어가고 있어서 SQL을 자체적으로 튜닝을 함(검색을 더 빠르게 잘 할 수 있도록).

> 💡 Tip. 파이썬 시험에서 검색속도를 고려한 코드를 짜는 역량이 더 고평가를 받는다. (SQL도 마찬가지)
 
2.	SQL을 실습위주로 배우는 이유 = 일머리를 배우기 위해서
👉 일머리는 본인이 직접 SQL을 작성해서 데이터를 검색해낼 수 있는 능력을 말합니다.

## 복습

- 어제 배운 것들
### 기본 SELECT문
- select +컬럼명
- from + 테이블명
- where + 검색조건 -> 여기가 많이 중요! (자주 틀리는 부분)
- order by + 정렬할 컬럼명
 
 > 📌 쿼리문 작성 순서와 실제 작동 순서는 다르다!
**💡 SQL 6개 쿼리문의 입력순서와 실행순서**

**코딩 순서:**
`SELECT` 👉 `FROM` 👉 `WHERE` 👉 `GROUP BY` 👉 `HAVING` 👉 `ORDER BY`

**실제 실행 순서:**
`FROM` 👉 `WHERE` 👉 `GROUP BY` 👉 `HAVING` 👉 `SELECT` 👉 `ORDER BY`

**참고:**
- `SELECT` 문은 필수이며, 항상 맨 처음에 작성해야 합니다.
- `FROM` 문은 필수이며, `SELECT` 문 다음에 작성해야 합니다.
- 나머지 쿼리 문들은 선택 사항이며, 위 순서대로 작성해야 합니다.
 
### 연결연산자 : || 
- 문자열로 결과를 도출하는 일이 종종있기 때문에 사용합니다.
- ex) `~님의 통장 잔고는 ~~~입니다.` 라는 식으로 출력하기 위해 사용.
 
### 컬럼별칭 : as 
- 결과로 출력될 컬럼의 이름을 변경하고 싶을때 사용합니다.
- ex) ename 을 '이름' 이라고 출력되게 하고 싶을 때 사용할 수 있습니다.
 ### 그 외의 것들
1.	비교연산자 : >, =, , ^=
2.	기타 비교 연산자 
3.	between ~ and ~
4.	like (까지 어제 배움)
5.	is null (오늘 배울 거)
6.	in (오늘 배울거)

**복습문제!**

문제 37. 이름의 첫번째 철자가 A 로 시작하는 사원들의 이름과 월급을 출력하시오.

```sql
select ename, sal
	from emp
	where ename like 'A%';
```

![](https://i.imgur.com/IWUcFTh.png)

- If, `where ename = 'A%';` 로 썼다면, 와일드 카드가 아닌 문자 그대로 A%라고 적힌 데이터를 찾았을 것
- %가 특수문자로서가 아닌 '와일드 카드'로서 사용되려면 '기타 비교연산자' 중 하나인 like를 반드시 사용해야 합니다.
- 'like' 연산자의 키워드 2가지 를 반드시 기억해야 합니다!
	- %(와일드카드=whatever)와 \_(언더바=1개의 자리수를 나타냄)

> So, like 와 같이 쓰이지 않는 와일드카드% 와 언더바(\_) 는 그저 특수문자일 뿐입니다.

- 예를 들어
	- `where ename = '_A%'` 라고만 작성했다면, 이는 조건을 설정하는 것이 아니라 그저 특수문자인 언더바와 %로서 취급될 뿐입니다.
	- 즉, ename중에 `_A%` 라고 입력된 ename을 찾으라는 뜻 밖에 되지 않습니다.

```sql
select ename, sal
	from emp
	where ename = '_A%';
```
---


![](https://i.imgur.com/QQDZEaK.png)

문제 38. 이름이 SCOTT 인 사원의 이름과 월급과 직업을 출력하시오.

```sql
select ename, sal, job
	from emp
	where ename ='SCOTT';
```

![](https://i.imgur.com/xPVoGDH.png)

문제 39. 이름의 끝에서 두번째 철자가 T인 사원들의 이름과 월급을 출력하시오.

```sql
select ename, sal
	from emp
	where ename like '%T_';
```

![](https://i.imgur.com/G6FhY3N.png)

## 013 비교 연산자 배우기 4(IS NULL)

- NULL 값을 조회할 때 사용하는 연산자가 is null 입니다.
- null 값이란, data가 없는 상태 혹은 알 수 없는 값(unkown-> oracle 메뉴얼에서만 표현 -> 의미가 더 명확화됨) 이라는 의미 입니다.

문제 40. 이름과 월급과 커미션을 출력하세요. (1).  커미션이 null 인 사원들의 이름과 커미션을 출력하시오.(2)

- (1)
```sql
select ename, sal, comm
	from emp;
```

![](https://i.imgur.com/FjbIVMU.png)

- 결과값에서 `null` 로 나오는 사람들이 커미션(comm)이 없는 사람들을 의미합니다.

- (2)
```sql
select ename, comm
	from emp
	where comm is null;
```

![](https://i.imgur.com/NlY7PXu.png)

- 만약 수식을 `is null`이 아닌 `where comm = null` 이라고 작성하면 오류가 납니다.
- 왜냐하면 `null` 은 말그대로 알 수 없는 값 이므로 비교연산자인 = 로는 조회할 수 없기 때문입니다.
- 즉, `null` 값을 테이블에서 조회하기 위해서는 `기타 비교연산자` 인 `is null` 을 반드시 사용해야 합니다.

![](https://i.imgur.com/RUzlJn9.png)

문제 41. 커미션이 'null 이 아닌' 사원들의 이름과 커미션을 출력하시오.

```sql
selece ename, comm
	from emp
	where comm is not null;
```

![](https://i.imgur.com/XSEWDYp.png)

문제 42. mgr(관리자의 사원번호) 이 null 인 사원의 이름과 직업을 출력하시오.

```sql
select ename, job
	from emp
	where mgr is null;
```
![](https://i.imgur.com/2LlU30o.png)

- 참고로, 사장(PRESIDENT) 은 관리자 번호(mgr)가 없습니다. (총 책임자이므로)

문제 43. 사원번호, 이름, 관리자 번호를 출력하시오.

```sql
select empno, ename, mgr
	from emp;
```

![](https://i.imgur.com/Wfq0yLY.png)

## 014 비교 연산자 배우기 5(IN)

- where 절의 검색 조건에서 여러개의 행을 비교할때는 in 을 사용해야 합니다.

i.e) 사원번호가 7788, 7902 인 사원들의 사원번호와 이름을 조회하시오.

```sql
select empno, ename
	from emp
	where emptno in (7788, 7902);
```

![](https://i.imgur.com/xOuWBny.png)

- = (equal) 연산자는 하나의 값만 비교할 수 있습니다. 
- 따라서 여러개의 값을 비교할 때는 in 을 사용해야 합니다.

![](https://i.imgur.com/YK0myF8.png)

문제 44. 직업이 SALESMAN, ANALYST 인 사원들의 이름과 직업을 출력하시오.

```sql
select ename, job
	from emp
	where job in ('SALESMAN', 'ANALYST');
```

![](https://i.imgur.com/dwIy6Wu.png)

- 여러개를 비교하는 것이니까 'in'을 써야 하고, 괄호 로 묶어 줘야 합니다.
- ename 은 검은색인데, job 은 파란색인 이유? -> job 이 오라클의 명령어중 하나여서 그렇습니다.
- 이러한 이유로 보통 회사에서 데이터 스키마를 작성할때는 job이라고 잘 사용하지 않습니다.

문제 45. 직업이 SALESMAN, ANALYST 가 아닌 사원들의 이름과 직업을 출력하세요.

```sql
select ename, job
	from emp
	where job not in ('SALESMAN', 'ANALYST);
```

![](https://i.imgur.com/cTIwztI.png)

```sql
select ename, job
	from emp
	where not job in ('SALESMAN', 'ANALYST ');
```

- 위와 같이 작성해도 같은 결과값을 확인할 수 는 있습니다.
💡하지만 이것은 오라클이 자동으로 문법을 수정해준 것이므로, 오라클 사용시에는 이런식으로 무조건 작동한다고 해서 맹신하면 안됩니다.



문제 46. 직업이 SALESMAN 이 아닌 사원들의 이름과 월급과 직업을 출력하시오.

```sql
select ename, job, sal
	from emp
	where job !='SALESMAN';
```

![](https://i.imgur.com/4lkCmeo.png)

문제 47. 위의 결과를 다시 출력하는데 월급이 높은 사원부터 출력하시오.

```sql
select ename, sal, job
	from emp
	where job != 'SALESMAN'
	order by sal desc;
```

![](https://i.imgur.com/4cPfXQu.png)

> ✔️ 이후 노트부터 같은 수업을 듣는 동기들의 인적사항으로 만든 테이블을 사용해서 문제를 풉니다.

문제 48. 우리반 테이블에서 이름과 나이를 출력하는데 나이가 높은 학생부터 출력하시오.

```sql
select ename, age
	from emp12
	order by age desc;
```

![](https://i.imgur.com/k5pLCTl.png)

문제 49. 이름과 나이와 주소를 출력하는데, 30살 이상인 학생들만 출력하시오.

```sql
select ename, age
	from emp12
	where age >=30;
```

![](https://i.imgur.com/x9COOCp.png)

문제 50. 성씨가 '김씨' 인 학생들의 이름과 통신사를 출력하시오.

```sql
select ename, telecom
	from emp12
	where ename like '김%';
```

![](https://i.imgur.com/EsnqkFo.png)

문제 51. 전공에 통계를 포함하고 있는 학생들의 이름과  전공을 출력하시오.

```sql
select ename , major
	from emp12
	where major like '%통계%';
```

![](https://i.imgur.com/wBCyuC4.png)

- like 연산자를 사용할 때 특정 단어를 포함하고 있는 데이터를 검색하려면 '%단어%' (양쪽에 와일드카드) 라고 하면 됩니다.

문제 52. 우리반에 gmail 사용하는 학생들의 이름과 메일을 출력하시오.

```sql
select ename, email
	from emp12
	where email like '%@gmail%';
```

![](https://i.imgur.com/DvGxKlq.png)

- `@` 는 쓰지 않았어도 같은 결과를 얻을 수는 있었지만, 좀 더 확실한 결과를 위해 사용했습니다.

문제 53. 우리반에 나이가 27에서 34사이인 학생들의 이름과 나이를 출력하시오.

```sql
select ename, age
	from emp12
	where age between 27 and 34;
```

![](https://i.imgur.com/2S5roaq.png)

문제 54. 우리반에서 나이가 27에서 34 사이가 아닌 학생들의 이름과 나이를 출력하시오.

```sql
select ename, age
	from emp12
	where age not between 27 and 34;
```

![](https://i.imgur.com/InFHTLv.png)

문제 55. 주소가 경기도인 학생들의 이름과 나이와 주소를 출력하시오.

```sql
select ename, age , address
	from emp12
	where address like '%경기도%';
```

![](https://i.imgur.com/60LxQjr.png)

문제 56. 통신사가 sk, lg 인 학생들의 이름과 통신사를 출력하시오.

```sql
select ename, telecom
	from emp12
	where telecom in ('sk', 'lg');
```

![](https://i.imgur.com/BjW0Mbp.png)

- 다만 현실적으로 생각해보면 데이터에 Sk, skt, U+, LG 등도 있어서 실무에선 올바르게 짠 코딩이 아닐 수도있습니다.
- 조금 더 현실성을 고려해 개선된 쿼리를 작성해 보자면 아래와 같습니다.

```sql
 select ename, telecom
	from emp12
	where UPPER(telecom) in ('SK', 'SKT', 'U+', 'LG');
```

- telecom 테이블의 값들에 upper 적용해 모두 대문자로 변형한 뒤에 sk혹은 lg 통신사로 입력할 수 있는 다양한 경우의 수를 포함 시켜 봤습니다.

문제 57. 서울에서 사는 학생들의 이름과 나이와 전공을 출력하는데 나이가 높은학생부터 출력하시오.

```sql
select ename, age, major
	from emp12
	where address like '%서울%'
	order by age desc;
```

![](https://i.imgur.com/fnvLu9r.png)

문제 58. 이메일이 gmail이 아닌 학생들의 이름과 이메일을 출력하시오.

```sql
select ename, email
	from emp12
	where email not like '%gmail%';
```

![](https://i.imgur.com/rn4pW9N.png)

문제 59. 아래와 같이 결과가 출력되도록 하시오.

- 김** 학생의 나이는 44세 입니다. ), 작거나 같음(=), 같지 않음(!= 또는 <>) 등이 있습니다. 추가로 BETWEEN, IN, LIKE 등의 비교 연산자도 사용됩니다.
    
3. **논리 연산자**: 여러 조건을 결합하여 논리적인 결과를 반환하는 데 사용됩니다. 주요 논리 연산자로는 AND, OR, NOT이 있습니다. AND 연산자는 모든 조건이 참일 때 참을 반환하고, OR 연산자는 하나 이상의 조건이 참일 때 참을 반환하며, NOT 연산자는 조건의 부정을 반환합니다.
    
4. **집합 연산자**: 두 개 이상의 결과 집합을 결합하거나 비교하는 데 사용됩니다. 주요 집합 연산자로는 UNION, INTERSECT, EXCEPT 등이 있습니다. UNION 연산자는 결과 집합을 결합하고 중복된 행을 제거하며, INTERSECT 연산자는 공통된 행만 반환하며, EXCEPT 연산자는 첫 번째 결과 집합에만 있는 행을 반환합니다.
    
5. **기타 연산자**: SQL에서는 기타 다양한 연산자도 사용됩니다. 이러한 연산자에는 비트 연산자, 문자열 연산자, 날짜 및 시간 연산자 등이 있습니다.

- 이중 논리연산자에 대해 정리합니다.

예제 문제 
직업이 SALESMAN 이고 월급이 1200 이상인 사원들의 이름과 월급과 직업을 출력하시오.

```sql
select ename, sal, job
	from emp   
	 where job = 'SALESMAN' and sal>=1200;
```

![](https://i.imgur.com/YCHDWIu.png)

- `and` 의 양 옆 조건이 모두 true이기 때문에 값이 조회되어 출력됩니다.
- true and true =  true 이기 때문입니다.

![](https://i.imgur.com/reeuF0o.png)

- 반대로 'and' 양옆의 조건 중 하나가 false 이면 나머지 하나가 true 여도 false 가 됩니다.
- false and true = false 여서 결과가 출력이 안되는 것 입니다.

> What if, 두번째 예시에서 and가 아닌 or 라면?
>  👉false or true = true 가 되어 결과물이 나옵니다.

![](https://i.imgur.com/2u6dgT7.png)

- SALESMAN 은 해당되지 않아도 sal 이 1200 이상인 조건들이 모두 나온 것입니다.
- 그러므로 'or' 명령어를 쓸때는 매우 주의 해야 합니다! 
- 조건 하나가 false 여도 값은 나오기 때문입니다.

문제 60. 직업이 SALESMAN 이거나 ANALYST 인  사원들의 이름과 월급과 직업을 출력하시오.

- 내가 생각 했던 답

```sql
select ename, sal, job
	from emp 
	where job = 'SALESMAN' or 'ANALYST';
```

- 위는 잘못된 구문입니다. 'or' 연산자 뒤에 오는 조건이 올바르지 않습니다. 
- 이는 'ANALYST' 조건만으로 해석되어 모든 행을 반환하게 되어 오답이 됩니다.

- 정답(1)
```sql
select ename, sal, job
	from emp
	where job = 'SALESMAN' or job = 'ANALYST';
```

- 올바른 구문입니다. 'or' 연산자 뒤에 오는 각각의 조건은 개별적으로 비교되어야 하며, 위 구문대로면 'SALESMAN' 또는 'ANALYST'인 사원을 찾아 결괄르 반환합니다.

- 정답(2)
```sql
select ename, sal, job
	from emp
	where job in ('SALESMAN' , 'ANALYST');
```

- 올바른 구문입니다. 'in' 연산자를 사용하여 한 번에 여러 값을 비교할 수 있습니다. 
- 이 경우 'SALESMAN'이나 'ANALYST'인 사원을 찾는데 사용됩니다.

문제 61. 성씨가 김씨, 이씨가 아닌 학생들의 이름을 출력하시오.

```sql
select ename
	from emp12
	where ename not like '%김%' and ename not like '%이%';
```

![](https://i.imgur.com/Dwu5MzW.png)

- 두개의 조건을 연결 해주는 거니까 하나 명령어 뒤에 (and, or ) 두번째 조건에 또다시  명령어를 입력해주는게 포인트!

문제 62. 이메일이 gmail 과 naver 이 아닌 학생들의 이름과 이메일을 출력하시오.

```sql

select ename, email
	from emp12
	where email not like '%@gmail%' and email not like '%naver%';
```

![](https://i.imgur.com/37e5Q2W.png)

# PART 2「초급」 SQL 기초 다지기

## 016 대소문자 변환 함수 배우기(UPPER, LOWER, INITCAP)
- 함수는 특정 기능을 구현하는 코드 집합입니다. 특정 입력 값이 함수에 입력되면 항상 특정 출력 값이 나타납니다. 
- 함수를 사용하는 이유는 더 복잡한 데이터를 조사할 수 있기 때문입니다.

### 함수의 유형
**단일 행 함수(Single-row functions)**: 
- 하나의 입력 값에 대해 하나의 결과를 반환하는 함수입니다. 
- 각 입력 행에 대해 독립적으로 작동하며, 결과는 입력 행마다 다를 수 있습니다. 
- 예를 들어, LENGTH(), UPPER(), LOWER()와 같은 문자열 함수, ROUND(), ABS()와 같은 수학 함수 등이 있습니다.

**다중 행 함수(Multi-row functions):** 
- 여러 행의 데이터를 그룹으로 취급하여 단일 결과를 반환하는 함수입니다. 
- 이러한 함수는 여러 행에 걸쳐 계산을 수행하며, 그룹 함수나 집계 함수라고도 불립니다. 
- 예를 들어, SUM(), AVG(), COUNT(), MAX(), MIN()와 같은 함수가 있습니다.

**문자열 함수:**
- UPPER: 대문자로 변환하는 함수
- LOWER: 소문자로 변환하는 함수
- INITCAP: 첫 글자는 대문자로 나머지는 소문자로 변환하는 함수

단일행 함수 중 문자함수의 예시

- `upper(ename)`: `ename` 열의 값을 모두 대문자로 변환합니다.
- `lower(ename)`: `ename` 열의 값을 모두 소문자로 변환합니다.
- `initcap(ename)`: `ename` 열의 각 단어의 첫 문자를 대문자로, 나머지 문자를 소문자로 변환합니다.

 👉결과적으로, 각 행에 대해 `ename`의 원래 값이 대문자로 변환된 값, 소문자로 변환된 값, 그리고 단어의 첫 문자만 대문자로 변환된 값이 순서대로 표시됩니다.
```sql
select upper(ename), lower(ename), initcap(ename)
	from emp;
```

![](https://i.imgur.com/rkkF1nr.png)

- 즉, 이러한 함수들은 특정 조건을 찾는 것이 아니라, 데이터를 내가 원하는 조건으로 적용 시켜 주는 함수입니다.
- 설령 데이터가 대/소문자가 섞여 있어도 내가 원하는 방식으로 정제할 수가 있습니다.

문제 63. 우리반 테이블에서 통신사가 sk 와 관련된 통신사이면 그 학생의 이름과 통신사를 출력하시오. 정확하게 데이터가 출력되게 끔 SQL 을 작성하시오!

```sql
select ename, upper(telecom)
	form emp12
	where upper(telecom) like '%SK%';
```

![](https://i.imgur.com/oHbwjAB.png)

- 이 코드가 효율적이면서 잘 작성된 코드가 되는 주요 부분은 `where upper(telecom)` 이 부분 덕분입니다.

- **대소문자 무시**: `upper` 함수를 사용함으로써, `telecom` 열의 데이터가 대문자든 소문자든, 혹은 혼합되어 있든 간에 상관없이 검색 조건을 만족하는 모든 데이터를 찾을 수 있습니다. 즉, 데이터베이스에 저장된 통신사 이름이 'SK', 'sk', 'Sk', 'sK' 등으로 다양하게 기록되어 있어도 모두 'SK'로 인식하여 검색할 수 있습니다.
    
- **포괄적 검색**: `LIKE '%SK%'` 조건을 사용함으로써, 'SK'라는 문자열이 어디에 위치하든 간에 해당하는 모든 행을 찾아낼 수 있습니다. 예를 들어, 'SKTelecom', 'HelloSK', 'SKMobile' 등 통신사 이름에 'SK'가 포함되어 있는 모든 경우를 포함시킬 수 있습니다.
    
- 이렇게 `upper` 함수와 `LIKE` 연산자를 조합함으로써, 데이터의 일관성이나 입력 방식의 차이로 인한 검색의 누락 없이, 관련된 모든 데이터를 정확하고 효율적으로 검색할 수 있습니다.

---


## 017 문자에서 특정 철자 추출하기(SUBSTR)

- SQL에서 `SUBSTR` 함수는 문자열의 특정 부분을 추출하는 데 사용됩니다. `SUBSTR` 함수의 기본 구문은 다음과 같습니다

```sql
SUBSTR(문자열, 시작 위치, [길이])
```

- **`문자열`**: 부분 문자열을 추출할 원본 문자열입니다.
- **`시작 위치`**: 추출을 시작할 위치를 나타냅니다. 이 값은 1부터 시작하며, 문자열의 첫 번째 문자를 가리킵니다. 음수 값을 사용할 경우 문자열의 끝에서부터 위치를 셉니다.
- **`길이`** (선택적): 추출할 문자의 수를 지정합니다. 이 매개변수를 생략하면 시작 위치에서부터 문자열의 끝까지의 모든 문자가 추출됩니다.

![](https://i.imgur.com/emFzbKZ.png)

- 이름이 3글자 김.승.순 이면 김 은 1번째 혹은 -3, 승 은 2번째, 혹은 -2, 순 은 3번째 자리를 의미
- substr(ename, 2,2) 면 이름 데이터에서 2번째 글자부터 2개를 읽어라 라는 의미!
    👉승 (2번째 글자) 부터 2글자 인 '승순'으로 읽게 되는 것.
- substr(ename, -3,2) 면 이름 이터에서 뒤에서 3번째인 글자 (김) 부터 2글자를 읽으라는의미
  👉 김승 이라고 나오게 됩니다.

예제문제
성씨가 '이'씨인 학생들의 이름을 출력하시오. like 쓰지 않고, in 과 substr 만을 써서 나타내시오.

```sql
select ename, substr(eame, 1,1)
	from emp12
	where substr(ename,1,1) in '이';
```

- 조건이 하나여서 사실 in 대신 =을 써도 되긴 합니다.
- `SELECT ename, SUBSTR(ename, 1, 1)`: `emp12` 테이블에서 `ename` 열의 데이터와 `ename`의 첫 글자를 선택합니다.
- `WHERE SUBSTR(ename, 1, 1) IN ('이')`: `WHERE` 절에서는 조건을 명시합니다. 여기서 `SUBSTR(ename, 1, 1)`은 `ename` 열의 첫 번째 문자를 추출하는데, 이 문자가 '이'인 행만을 선택하도록 조건을 설정합니다. `IN`은 주어진 리스트 안의 값과 일치하는 데이터를 찾는 연산자인데, 이 경우 리스트 안에는 '이'만 포함되어 있습니다.

![](https://i.imgur.com/oGEricr.png)

문제 64. 성씨가 김, 이, 유씨인 학생들의 이름과 나이를 출력하는데 like 를 쓰지 말고 in 과 substr 을 써서 출력하시오.

```sql
select ename, age
	from emp12
	where substr(ename, 1,1) in ('김','이','유');
```

![](https://i.imgur.com/lT0c2G3.png)

---


## 018 문자열의 길이를 출력하기(LENGTH)

- SQL에서 문자열의 길이를 구하는 함수는 `LENGTH`입니다. `LENGTH` 함수는 주어진 문자열의 길이를 숫자로 반환합니다. 이 함수는 문자열 내의 문자 개수를 계산하여 그 수를 반환합니다.

```sql
select length(문자열)
	from 테이블명;
```

![](https://i.imgur.com/IFHw2he.png)

문제 65. 우리반 테이블에서 이메일과 이메일 철자의 길이를 출력하는데, 이메일 철자의 길이가 긴 것부터 출력되도록 하시오.

```sql
select ename, email, length(email)
	from emp12
	order by length(email) desc;
```

![](https://i.imgur.com/Bfcx6Qn.png)

응용문제
위 코드의 결과에서 이메일을 글자순으로 나열하고, 이름을 가나다순으로 나열해보기

```sql
select ename, email, length(email)
	from emp12
	order by length(email) desc, ename desc;
```

- 다른 조건 명령어들은 and 나 not 등을 붙여서 처음엔 `order by length(email) desc and ename desc;` 요렇게 했는데 오류가 발생했었습니다.
- order by 는 전치사 없이 조건 추가할때 콤마로 구분만 하면 되는데 그 부분을 헷갈려 했던 것 같습니다.

문제 66. EMP 테이블에서 ename 을 출력하고 그 옆에 ename 의 첫번째 철자를 출력하시오.

```sql
select ename, substr(ename, 1,1)
	from emp;
```

![](https://i.imgur.com/stcqL1Z.png)

문제 67. 위의 결과를 다시 출력하는데 이름의 첫번째 철자로 출력되는 부분은 소문자로 출력하시오.

- 내가 푼 방식

![](https://i.imgur.com/xVCdWHE.png)

```sql
select ename, lower(substr(ename, 1,1))
	from emp;
```

- 이 방식에서는 `SUBSTR(ename, 1, 1)`을 사용하여 `ename`의 첫 번째 글자를 추출한 후, `LOWER` 함수를 사용하여 이 글자를 소문자로 변환합니다.
- `LOWER` 함수가 `SUBSTR` 함수의 결과에 적용되기 때문에, 첫 글자만 소문자로 변환되어 출력됩니다.

- 정답
```sql
select ename, substr(lower(ename),1,1)
	from emp;
```
- 이 방식에서는 먼저 `LOWER(ename)`을 사용하여 `ename` 열의 모든 문자를 소문자로 변환한 후, `SUBSTR` 함수를 사용하여 변환된 문자열의 첫 번째 글자를 추출합니다.
- `LOWER` 함수가 `ename` 전체에 먼저 적용되고 그 결과에서 첫 글자를 추출하기 때문에, 결과적으로 첫 글자가 소문자로 출력됩니다.

**차이점:**
- **적용 순서의 차이**: A 방식은 첫 글자를 추출한 후 그 글자를 소문자로 변환하는 반면, B 방식은 먼저 전체 이름을 소문자로 변환한 후 첫 글자를 추출합니다.
- **결과에 미치는 영향**: 이 경우, 두 방법 모두 최종 결과에서 `ename`의 첫 글자만 소문자로 출력됩니다. 그러나, 만약 작업의 목적이나 처리 과정에서 전체 문자열을 소문자로 변환해야 하는 상황이라면 B 방식이 더 적합할 수 있습니다. 예를 들어, 후에 추가적인 문자열 처리를 위해 전체 이름을 소문자로 사용해야 하는 경우가 이에 해당합니다.

문제 68. (오늘의 마지막 문제) 
아래의 결과를 initcap 쓰지 말고, upper, lower, substr, || (연결연산자) 사용해서 출력하시오!

```sql
select initcap(ename)
	from emp;
```

![](https://i.imgur.com/5xQ8ApZ.png)

- 내가 푼 방식

```sql
select substr(upper(ename),1,1)||substr(lower(ename),2,5) as "INITCAP(ENAME)"
    from emp;
```

- 이 방식에서는 `ename`의 첫 글자를 대문자로 변환한 후(`UPPER(ename), 1, 1`), 나머지 글자들(2번째 글자부터 5개 글자)을 소문자로 변환합니다(`LOWER(ename), 2, 5`).
- 이 방식의 한계는 `ename`의 길이가 6글자를 초과하는 경우, 나머지 글자들이 잘리게 되므로, 모든 이름에 대해 올바르게 작동하지 않을 수 있습니다.

- 다른 사람이 푼 방식 (1)
```sql
select substr(upper(ename),1,1)||substr(lower(ename),2,length(ename)-1)
    from emp;
```

- 이 방식은 `ename`의 첫 글자를 대문자로 변환하고, 나머지 글자들을 소문자로 변환합니다. 여기서 `LENGTH(ename) - 1`을 사용하여 두 번째 글자부터 문자열의 끝까지를 소문자로 변환합니다.
- 이 방법은 `ename`의 길이에 상관없이 모든 문자열에 대해 올바르게 작동합니다.

- 다른 사람이 푼 방식 (2)

```sql
select upper(substr(ename,1,1))||lower(substr(ename,2))
	from emp;
```

- 마지막 방식은 `ename`의 첫 글자만 대문자로 변환하고(`UPPER(SUBSTR(ename, 1, 1))`), 나머지 부분을 전부 소문자로 변환합니다(`LOWER(SUBSTR(ename, 2))`).
- 이 방법도 모든 `ename`에 대해 올바르게 작동하며, `B` 방식과 유사한 결과를 제공하지만, 코드의 구성이 조금 더 간결합니다.

> 이러한 다른 사람들의 코드를 보면서 "emp 테이블로 부터 substr 을 쓸때 데이터를 고를 컬럼을 선택하고 콤마/숫자/괄호(끝날 순번 지정하지 않음) 하면 해당 숫자부터 끝까지 별도의 지정 없이 다 선택이 되는 것이구나! 꼭 substr(컬럼, 숫자,숫자) 이런 식으로 입력할 필요 없구나!" 라는 걸 배웠습니다.

응용문제
 Q. 68번의 결과 + job 을 출력하는데 initcap 쓰지 말고, upper, lower, substr, || (연결연산자) 사용해서 출력하시오!  (아래 그림 처럼 만들)

![](https://i.imgur.com/4MmowrP.png)

```sql
select upper(substr(ename,1,1)) || lower(substr(ename,2)) as "INITCAP ENAME", upper(substr(job,1,1)) || lower(substr(job,2)) as "INITCAP JOB"
	from emp;
```

![](https://i.imgur.com/aHUluHO.png)

- `UPPER(SUBSTR(ename, 1, 1))`: `ename`의 첫 번째 문자를 추출한 후, 그 문자를 대문자로 변환합니다.
- `LOWER(SUBSTR(ename, 2))`: `ename`의 두 번째 문자부터 끝까지를 추출한 후, 그 문자열을 소문자로 변환합니다.
- `||`: 문자열 연결 연산자를 사용하여 두 문자열을 연결합니다.
- `"INITCAP ENAME"`: 결과 칼럼의 별칭을 설정하여, `ename`에 대해 적용한 결과가 `"INITCAP ENAME"`으로 출력됩니다.
- 같은 방식으로 `job`에 대해서도 첫 글자는 대문자로, 나머지는 소문자로 변환하여 `"INITCAP JOB"`이라는 별칭의 칼럼으로 결과를 출력합니다.

## 🤔 오늘의 회고
- 어제 배운 기본적인 6개의 SQL 쿼리문을 비롯해 다양한 연산자들에 대해 학습했습니다.
- 연산자의 논리 자체는 어려울 것이 없지만, 함수에 접근하면서 부터 출력형태를 다양하게 변형 시키는 부분에서 애를 많이 먹은 것 같습니다.
- 그래도 특정 형태의 결과물을 위해 다양한 함수를 사용해 여러 방법으로 시도해보면서 그러한 것을 숙달하고 이해할 수 있었던 것 같습니다.

