---
title: "[SQL] 코테 BASIC SELCT문 - 3월에 태어난 여성 회원 목록 출력하기"
cover: "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1920&h=1080&fit=crop"
date: 2024-06-20
categories:
  - [personal-study, sql]
tags: []
toc: true
---
## 🚦 Summary
- SQL의 SELECT 관련 기초 코테 문제를 풀이 합니다.
- 특정 월을 추출하는 2가지 방법을 활용해 문제를 풀어봤습니다.
- 날짜 관련 데이터 추출에 사용되는 다양한 SQL 함수도 함께 공부 했습니다.

---


## 💡 문제 설명
### 기본 정보
- 다음은 식당 리뷰 사이트의 회원 정보를 담은 `MEMBER_PROFILE` 테이블입니다. `MEMBER_PROFILE` 테이블은 다음과 같으며 `MEMBER_ID`, `MEMBER_NAME`, `TLNO`, `GENDER`, `DATE_OF_BIRTH`는 회원 ID, 회원 이름, 회원 연락처, 성별, 생년월일을 의미합니다.

| Column name   | Type         | Nullable |
| ------------- | ------------ | -------- |
| MEMBER_ID     | VARCHAR(100) | FALSE    |
| MEMBER_NAME   | VARCHAR(50)  | FALSE    |
| TLNO          | VARCHAR(50)  | TRUE     |
| GENDER        | VARCHAR(1)   | TRUE     |
| DATE_OF_BIRTH | DATE         | TRUE     |

### 문제
- `MEMBER_PROFILE` 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요. 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 결과는 회원ID를 기준으로 오름차순 정렬해주세요.

### 예시
- `MEMBER_PROFILE` 테이블이 다음과 같을 때

|MEMBER_ID|MEMBER_NAME|TLNO|GENDER|DATE_OF_BIRTH|
|---|---|---|---|---|
|[jiho92@naver.com](mailto:jiho92@naver.com)|이지호|01076432111|W|1992-02-12|
|[jiyoon22@hotmail.com](mailto:jiyoon22@hotmail.com)|김지윤|01032324117|W|1992-02-22|
|[jihoon93@hanmail.net](mailto:jihoon93@hanmail.net)|김지훈|01023258688|M|1993-02-23|
|[seoyeons@naver.com](mailto:seoyeons@naver.com)|박서연|01076482209|W|1993-03-16|
|[yoonsy94@gmail.com](mailto:yoonsy94@gmail.com)|윤서연|NULL|W|1994-03-19|

- SQL을 실행하면 다음과 같이 출력되어야 합니다.

| MEMBER_ID                                       | MEMBER_NAME | GENDER | DATE_OF_BIRTH |
| ----------------------------------------------- | ----------- | ------ | ------------- |
| [seoyeons@naver.com](mailto:seoyeons@naver.com) | 박서연         | W      | 1993-03-16    |

### 주의 사항
- `DATE_OF_BIRTH` 의 데이트 포맷이 예시와 동일해야 정답처리 됩니다
---


## 문제 풀이 과정
- 문제 요구사항이 Oracle 기준 풀이 였습니다.
- 프로그래머스 SQL 코딩 테스트 문제는 주로 Oracle 이나 Mysql 쿼리로 풀이 됩니다.

### 조건 정리
- 문제에서 요구하는 조건을 정리하면 다음과 같습니다.

- 성별이 여성 (`GENDER = 'W'`)
- 전화번호가 NULL이 아닌 경우 (`TLNO IS NOT NULL`)
- 생일이 3월 (`EXTRACT(MONTH FROM DATE_OF_BIRTH) = 3` 또는 `TRUNC(DATE_OF_BIRTH, 'MM') = TRUNC(DATE 'YYYY-MM-DD', 'MM')`)
- 결과를 회원ID 기준 오름차순 정렬 (`ORDER BY MEMBER_ID ASC`)

### 문제 풀이
#### EXTRACT 함수를 사용한 쿼리
- EXTRACT 함수는 날짜에서 특정 부분(연, 월, 일 등)을 추출하는 데 사용됩니다. 이를 활용하여 생일의 월이 3월인 회원을 필터링 할 수 있습니다.

```sql
SELECT MEMBER_ID, MEMBER_NAME, GENDER, TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER = 'W'
  AND TLNO IS NOT NULL
  AND EXTRACT(MONTH FROM DATE_OF_BIRTH) = 3
ORDER BY MEMBER_ID ASC;
```

>  실행 결과

| member_id          | member_name | gender | date_of_birth |
|--------------------|-------------|--------|---------------|
| seoyeons@naver.com | 박서연         | W      | 1992-03-16    |

#### TRUNC 함수를 사용한 쿼리
- TRUNC 함수는 날짜를 특정 단위로 자르는 데 사용됩니다. 이를 활용하여 날짜를 월 단위로 잘라서 비교할 수 있습니다.

```sql
SELECT MEMBER_ID, MEMBER_NAME, GENDER, TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER = 'W'
  AND TLNO IS NOT NULL
  AND TRUNC(DATE_OF_BIRTH, 'MM') = TRUNC(DATE '2023-03-01', 'MM')
ORDER BY MEMBER_ID ASC;
```

>  실행 결과

| member_id          | member_name | gender | date_of_birth |
|--------------------|-------------|--------|---------------|
| seoyeons@naver.com | 박서연         | W      | 1992-03-16    |

---


## 날짜 관련 추출함수 정리
### EXTRACT 함수
> **EXTRACT 함수**: 특정 날짜 부분(연, 월, 일 등)을 추출합니다.

```sql
SELECT EXTRACT(YEAR FROM DATE '2023-06-20') AS year_part FROM DUAL;
SELECT EXTRACT(MONTH FROM DATE '2023-06-20') AS month_part FROM DUAL;
SELECT EXTRACT(DAY FROM DATE '2023-06-20') AS day_part FROM DUAL;
```

- DATE 데이터 유형에서 연도(YEAR), 월(MONTH), 일(DAY) 등을 추출할 수 있습니다.

### TO_CHAR 함수
> **TO_CHAR 함수**: 날짜를 특정 형식으로 변환합니다.

```sql
SELECT TO_CHAR(DATE '2023-06-20', 'YYYY') AS year_part FROM DUAL;
SELECT TO_CHAR(DATE '2023-06-20', 'MM') AS month_part FROM DUAL;
SELECT TO_CHAR(DATE '2023-06-20', 'DD') AS day_part FROM DUAL;
```

- 포맷 문자열을 사용해 다양한 형식으로 날짜를 변환할 수 있습니다.
### TRUNC 함수
> **TRUNC 함수**: 날짜를 특정 단위로 잘라냅니다.

```sql
SELECT TRUNC(DATE '2023-06-20', 'YEAR') AS trunc_year FROM DUAL;
SELECT TRUNC(DATE '2023-06-20', 'MONTH') AS trunc_month FROM DUAL;
SELECT TRUNC(DATE '2023-06-20', 'DAY') AS trunc_day FROM DUAL;
```

- YEAR, MONTH, DAY 등의 단위를 사용해 날짜를 자를 수 있습니다.
### LAST_DAY 함수
> **LAST_DAY 함수**: 주어진 날짜의 해당 월의 마지막 날을 반환합니다.

```sql
SELECT LAST_DAY(DATE '2023-06-20') AS last_day_of_month FROM DUAL;
```

### NEXT_DAY 함수
> **NEXT_DAY 함수**: 주어진 날짜 이후의 특정 요일의 날짜를 반환합니다.

```sql
SELECT NEXT_DAY(DATE '2023-06-20', 'MONDAY') AS next_monday FROM DUAL;
```

- 특정 요일을 기준으로 다음 날짜를 구할 때 유용합니다.
### ADD_MONTHS 함수
> **ADD_MONTHS 함수**: 주어진 날짜에 특정 개월 수를 더하거나 뺍니다.

```sql
SELECT ADD_MONTHS(DATE '2023-06-20', 1) AS next_month FROM DUAL;
SELECT ADD_MONTHS(DATE '2023-06-20', -1) AS previous_month FROM DUAL;
```

- 날짜 계산에 유용하며, 개월 단위로 더하거나 뺄 수 있습니다.

## 🎈 Outro.
- 날짜관련 함수들에서는 사소한 실수로 코테 실수가 정말 많이 발생하는 문제 유형 같습니다.
- 특히 코테에서 요구하는 날짜 포맷이 있다면 샘플로 날짜 데이터를 추출하여 어떤 포맷인지 확인을 하고 쿼리를 문제 요구사항에 맞게 작성하는게 중요 합니다.
