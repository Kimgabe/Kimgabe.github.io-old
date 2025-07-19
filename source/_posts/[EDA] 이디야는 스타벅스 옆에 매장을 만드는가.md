---
title: "[EDA] 고전 EDA - 이디야는 정말 스타벅스 옆에 포지셔닝하는 전략을 쓰는가?!"
cover: "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1920&h=1080&fit=crop"
date: 2025-07-18
categories:
  - [portfolio]
tags: []
toc: true
---
🚦Summary
- 고전적인 EDA 포폴중 하나인 이디야와 스타벅스 시리즈를 최신데이터로 정리해봤습니다.
- 2023년 11월 크롤링한 데이터를 가지고 분석했습니다.
- 관할구&브랜드별 매장분포, 매장간 평균거리 등을 주요 지표로 하여 분석했습니다.

# 📌Intro. EDA/웹크롤링을 통한 데이터 분석

## 분석 소개

---


이디야커피는가끔 스타벅스 커피매장이 위치하는곳에 매장을 위치시키는것이 아니냐는 의심을 받곤합니다. 공식적인 인터뷰에서 이디야커피회장은 이 사실을부인했습니다.데이터 분석을 통해 이 내용이 사실인지 확인하고자 합니다.

### 상세 분석 요건
1) 웹크롤링을 통해 스타벅스의 '서울시' 매장의 이름, 주소, 구 이름을 pandas data frame으로 정리하기

2) 웹크롤링을 통해 이디야의 '서울시' 매장의 이름, 주소, 구 이름을 pandas data frame으로 정리하기

3) 수집된 데이터를 기반으로 실제로 '이디야 커피는 스타벅스 매장 근처에 존재하는가' 를 검증하기(방식 자율)


# Basic setting

---


- 웹크롤링을 위한 기본 셋팅을 진행합니다.

## 크롬 드라이버 설정

- 크롬 드라이버를 사용하기 위해서는 현재 내가 사용중인 로컬 pc에 설치된 크롬버전에 호환이 되는 드라이브를 설치해야 합니다.

- 하지만 코드의 호환성(여러 로컬에서 사용할경우, 크롬이 업데이트 경우)등을 고려할때 매번 버전에 맞는 드라이버를 설치하는건 번거로운 일입니다. 

- 이를 해결하기 위해 chromedriver_autoinstaller와 edgedriber_autoinstaller를 활용해 버전에 맞는 웹드라이버로 접속하고 크롬에서도 에러가 발생할 경우 edge드라이버로 접속하도록 하였습니다.

```python
# 정적 크롤링 라이브러리
# 웹 페이지 HTML 파싱 라이브러리
from bs4 import BeautifulSoup

# 동적 크롤링 라이브러리
# 웹 브라우저 자동화 라이브러리
from selenium import webdriver
# Chrome 브라우저 옵션 설정 모듈
from selenium.webdriver.chrome.options import Options
# ChromeDriver 서비스 실행 모듈
from selenium.webdriver.chrome.service import Service
# 웹 페이지 요소 선택 방법 정의 모듈
from selenium.webdriver.common.by import By
# 웹 페이지 액션 자동화 모듈
from selenium.webdriver.common.action_chains import ActionChains
# 웹 페이지 특정 요소 로드 대기 모듈
from selenium.webdriver.support.ui import WebDriverWait
# 웹 페이지 특정 조건 확인 모듈
from selenium.webdriver.support import expected_conditions as EC
# 웹 페이지 키보드 특정 키 사용 모듈
from selenium.webdriver.common.keys import Keys
# ChromeDriver 자동 설치 및 관리 라이브러리
import chromedriver_autoinstaller
# EdgeDriver 자동 설치 및 관리 라이브러리 (chrome 버전 이슈 시 사용)
import edgedriver_autoinstaller 
# 웹 브라우징 User-Agent 랜덤 생성 라이브러리
from fake_useragent import UserAgent

# 기타 라이브러리
# 데이터 처리와 분석용 라이브러리
import pandas as pd
# 정규 표현식 사용 라이브러리
import re
# 크롤링 블록 방지용 time.sleep() 사용
import time

import os
```

# [데이터 수집] 스타벅스 매장정보 크롤링하기

---


![](https://i.imgur.com/DK2WVgK.jpg)

---


- 설정한 크롬드라이브를 통해 아래의 과정을 거쳐 '서울시' 전체의 스타벅스 매장에 대한 '매장명', '주소' 와 '구' 정보를 크롤링하여 df로 만고자 합니다.

- 웹페이지를 탐색해보면, 매장검색 기능에서 '서울시' 나 각 '구' 를 선택하는 부분은 selenium으로 접근을 하고, 그 하위 매장정보는 BeautifulSoup을 활용해 수집하는 것이 적절해 보입니다.

- 단계별로 정리하자면 아래와 같습니다.

    - step 1. 스타벅스 홈페이지의 매장찾기 페이지에 접속

    - step 2. Selenium을 활용해 서울시의 각 구별 매장 정보 검색

        - 1) '지역검색' 버튼 선택

        - 2) '서울' 버튼 선택

        - 3) 각 구 버튼 선택해 구별 매장 정보 불러오기

    - step 3. 구 별 스타벅스 매장 정보 크롤링(BeautifulSoup)

    - Step 4. Step 2~3을 반복하며 서울시 전체 매장 정보 수집

        - '구' 정보는 Step 2.에서 수집

        - 매장명, 매장주소 는 Step 3. 에서 수집

    - Step 5. 수집된 정보를 데이터프레임화

---


```python
# 웹 브라우징 시 사용되는 User-Agent를 랜덤으로 생성하는 라이브러리
ua = UserAgent()
user_agent = ua.random

# Chrome 웹 브라우저 옵션 설정
# 이 설정들은 웹 크롤링 시 필요한 기본적인 설정
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(f'user-agent={user_agent}')

# 로컬에 설치된 Chrome 브라우저의 버전을 확인
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    # Chrome 브라우저 드라이버 초기화
    service = Service(f'./{chrome_ver}/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
except:
    try:
        # ChromeDriver 자동 설치 및 초기화
        chromedriver_autoinstaller.install(True)
        service = Service(f'./{chrome_ver}/chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=options)
    except:
        # Edge 브라우저 드라이버 초기화
        edgedriver_autoinstaller.install()  # EdgeDriver 자동 설치
        driver = webdriver.Edge()  # EdgeDriver의 경로를 따로 지정하지 않음

# 'SB_store_info.csv' 파일 유무 확인
import os

if os.path.exists('SB_store_info.csv'):
    sb_df = pd.read_csv('SB_store_info.csv', encoding='utf-8-sig')
else:
    sb_df = pd.DataFrame(columns=['gu', 'store_name', 'store_address'])    

"""
크롤링에 필요한 함수 정의
1) 동적 크롤링 위해 버튼 누르는 함수(지역선택 > 서울 반복)
2) 수집된 주소 전처리 함수 (전화번호, 건물명 삭제 등)
"""
    # 크롤링에 필요한 함수들을 정의
# 1. 서울의 '구'를 선택하기 위한 버튼을 클릭하는 함수 정의
def click_seoul_button(driver):
    # '지역 검색' 버튼을 클릭
    driver.find_element(By.CSS_SELECTOR, "#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search > h3 > a").click()
    time.sleep(1)
    # '서울' 버튼을 클릭
    driver.find_element(By.CSS_SELECTOR, "#container > div > form > fieldset > div > section > article.find_store_cont > article > article > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a").click()
    time.sleep(1)

# 2. 주소지 정보 전처리 하는 함수 정의
import re
def extract_address_pattern(address):
    # 1522-3232 제거
    address = address.replace('1522-3232', '').strip()
    
    # 첫 번째 패턴 시도
    first_pattern = re.compile(r'(\S+(?:시|도)) (\S+(?:구|군)) (\S+(?:로|길) \d+\s*(?:번길|번지)?)')
    matches = first_pattern.search(address)

    # 첫 번째 패턴에서 주소를 찾지 못할 경우 두 번째 패턴 시도
    if matches is None:
        second_pattern = re.compile(r'(\S+(?:시|도)) (\S+(?:구|군)) (\S+(?:로\d+[가-힣]*길)\s*\d*(?:번길|번지)?)')
        matches = second_pattern.search(address)

    if matches:
        full_address = matches.group()
        return full_address
    else:
        return "주소를 찾을 수 없습니다."

"""
크롤링 시작
"""

# 스타벅스 매장 찾기 웹 페이지에 접속
base_url = 'https://www.starbucks.co.kr/store/store_map.do'
driver.get(base_url)
time.sleep(3)  # 페이지 로드를 기다리기 위해 3초 동안 대기

# 위에서 정의한 함수를 호출하여 '서울' 버튼을 클릭
click_seoul_button(driver)

# 현재 웹 페이지의 HTML 내용을 가져옵니다.
page_source = driver.page_source

# BeautifulSoup 객체를 생성하여 HTML을 파싱 준비
soup = BeautifulSoup(page_source, 'html.parser')

# 웹 페이지에서 '구'의 목록을 가져옵니다. ('전체'는 제외)
gu_elements = soup.select("#mCSB_2_container > ul > li > a")
gu_names = [gu.text.strip() for gu in gu_elements]

# 크롤링 대상인 '구'의 이름들을 출력 ('전체' 제외)
print(f'크롤링할 서울시의 구 리스트: {gu_names[1:]}')

# 각 '구'에 대해 반복문을 실행하면서 스타벅스 매장 정보를 크롤링
for index, gu_name in enumerate(gu_names):
    # '전체'는 크롤링 대상에서 제외
    if gu_name == '전체':
        continue
    print(f"현재 {gu_name} 크롤링 중...")

    # 해당 '구'를 선택하기 위한 CSS 선택자를 정의
    gu_selector = f"#mCSB_2_container > ul > li:nth-child({index + 1}) > a"

    # 웹 페이지를 스크롤하여 해당 '구'의 위치까지 이동
    actions = ActionChains(driver)
    element = driver.find_element(By.CSS_SELECTOR, gu_selector)
    actions.move_to_element(element).perform()

    # 해당 '구'의 이름을 클릭
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, gu_selector)))
    element.click()
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 해당 '구'의 스타벅스 매장 개수를 파악
    store_count_text = soup.select_one("#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step3 > div.result_num_wrap > span").text 
    store_count = int(store_count_text) 

    # 해당 '구'의 모든 매장 정보를 크롤링
    store_info = []
    for i in range(1, store_count + 1):
        store_name_selector = f"#mCSB_3_container > ul > li:nth-child({i}) > strong"
        store_address_selector = f"#mCSB_3_container > ul > li:nth-child({i}) > p"

        store_name = soup.select_one(store_name_selector).text.strip() # 매장명 가져오기
        raw_store_address = soup.select_one(store_address_selector).text.strip() # 매장 주소(raw) 가져오기

        # 전처리 함수를 호출하여 store_address 값을 추출
        store_address = extract_address_pattern(raw_store_address)

        # 크롤링한 정보를 딕셔너리 형태로 저장
        collected_info = {
            'gu': gu_name,
            'store_name': store_name,
            'store_address': store_address,
            'raw_store_address': raw_store_address
        }

        # 신규 데이터만 sb_df에 추가하는 로직
        if not ((sb_df['store_name'] == store_name) & (sb_df['store_address'] == store_address)).any():
            store_info.append(collected_info)
            print(f"신규 매장 발견: {store_name} - {store_address}")

    print(f"{gu_name}의 {store_count}개 매장 중 {i}개의 매장정보 크롤링 완료.")
        
    # 중간 저장: 현재까지의 데이터를 DataFrame에 추가
    sb_df = pd.concat([sb_df, pd.DataFrame(store_info)]).reset_index(drop=True)
    
    # 다음 구 정보를 위해 다시 '서울' 버튼을 클릭
    click_seoul_button(driver) 
    time.sleep(2)

# 크롬 드라이버 종료
driver.quit()

# 결과 출력
print('-'*70, '\n')
sb_df.info()

# 크롤링한 데이터를 CSV 파일로 저장
sb_df.to_csv('SB_store_info.csv', encoding='utf-8-sig', index=False)
```


WARNING:root:Can not find chromedriver for currently installed chrome version.


크롤링할 서울시의 구 리스트: ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']
현재 강남구 크롤링 중...
신규 매장 발견: 청담역 - 서울특별시 강남구 삼성로 709 
강남구의 89개 매장 중 89개의 매장정보 크롤링 완료.
현재 강동구 크롤링 중...
강동구의 17개 매장 중 17개의 매장정보 크롤링 완료.
현재 강북구 크롤링 중...
강북구의 6개 매장 중 6개의 매장정보 크롤링 완료.
현재 강서구 크롤링 중...
신규 매장 발견: 송정역 - 서울특별시 강서구 공항대로 38 
신규 매장 발견: 발산역5번출구 - 서울특별시 강서구 강서로52길 43 
강서구의 27개 매장 중 27개의 매장정보 크롤링 완료.
현재 관악구 크롤링 중...
관악구의 12개 매장 중 12개의 매장정보 크롤링 완료.
현재 광진구 크롤링 중...
광진구의 18개 매장 중 18개의 매장정보 크롤링 완료.
현재 구로구 크롤링 중...
구로구의 14개 매장 중 14개의 매장정보 크롤링 완료.
현재 금천구 크롤링 중...
신규 매장 발견: 가산케이에스 - 서울특별시 금천구 벚꽃로36길 30 
금천구의 13개 매장 중 13개의 매장정보 크롤링 완료.
현재 노원구 크롤링 중...
노원구의 14개 매장 중 14개의 매장정보 크롤링 완료.
현재 도봉구 크롤링 중...
신규 매장 발견: 창동역 - 서울특별시 도봉구 마들로13길 61 
도봉구의 6개 매장 중 6개의 매장정보 크롤링 완료.
현재 동대문구 크롤링 중...
동대문구의 10개 매장 중 10개의 매장정보 크롤링 완료.
현재 동작구 크롤링 중...
동작구의 11개 매장 중 11개의 매장정보 크롤링 완료.
현재 마포구 크롤링 중...
마포구의 36개 매장 중 36개의 매장정보 크롤링 완료.
현재 서대문구 크롤링 중...
서대문구의 22개 매장 중 22개의 매장정보 크롤링 완료.
현재 서초구 크롤링 중...
서초구의 48개 매장 중 48개의 매장정보 크롤링 완료.
현재 성동구 크롤링 중...
성동구의 14개 매장 중 14개의 매장정보 크롤링 완료.
현재 성북구 크롤링 중...
성북구의 15개 매장 중 15개의 매장정보 크롤링 완료.
현재 송파구 크롤링 중...
송파구의 36개 매장 중 36개의 매장정보 크롤링 완료.
현재 양천구 크롤링 중...
신규 매장 발견: 목동SBS - 서울특별시 양천구 목동서로 161 
양천구의 17개 매장 중 17개의 매장정보 크롤링 완료.
현재 영등포구 크롤링 중...
신규 매장 발견: 신풍역 - 서울특별시 영등포구 신풍로 23 
영등포구의 42개 매장 중 42개의 매장정보 크롤링 완료.
현재 용산구 크롤링 중...
용산구의 25개 매장 중 25개의 매장정보 크롤링 완료.
현재 은평구 크롤링 중...
신규 매장 발견: 불광역8번출구 - 서울특별시 은평구 통일로 746 
은평구의 14개 매장 중 14개의 매장정보 크롤링 완료.
현재 종로구 크롤링 중...
종로구의 40개 매장 중 40개의 매장정보 크롤링 완료.
현재 중구 크롤링 중...
신규 매장 발견: 충무로 - 서울특별시 중구 충무로 3 
중구의 54개 매장 중 54개의 매장정보 크롤링 완료.
현재 중랑구 크롤링 중...
중랑구의 8개 매장 중 8개의 매장정보 크롤링 완료.
---------------------------------------------------------------------- 



RangeIndex: 610 entries, 0 to 609
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype 
---  ------             --------------  ----- 


0   gu                 610 non-null    object
 1   store_name         610 non-null    object
 2   store_address      610 non-null    object
 3   raw_store_address  610 non-null    object
dtypes: object(4)
memory usage: 19.2+ KB

# [데이터 수집] 이디야 매장 정보 크롤링 하기

---


![](https://i.imgur.com/qdQJCIC.png)

- 이디야의 경우 접근방법이 다소 달라집니다.

- 스타벅스 처럼 특정 구를 선택하면 모든 매장정보가 뜨는 구조가 아닙니다.

- 주소에 서울시의 각 관할구를 입력하고, 그 결과로 뜨는 매장들의 리스트를 확보한 뒤

- 그 리스트에서 매장명과 주소를 수집해야 합니다.

- 주소에 입력할 관할구는 스타벅스에서 수집한 데이터를 활용하였습니다.

```python
# 로컬에 설치된 Chrome 브라우저의 버전을 확인
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    # Chrome 브라우저 드라이버 초기화
    service = Service(f'./{chrome_ver}/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
except:
    try:
        # ChromeDriver 자동 설치 및 초기화
        chromedriver_autoinstaller.install(True)
        service = Service(f'./{chrome_ver}/chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=options)
    except:
        # Edge 브라우저 드라이버 초기화
        edgedriver_autoinstaller.install()  # EdgeDriver 자동 설치
        driver = webdriver.Edge()  # EdgeDriver의 경로를 따로 지정하지 않음

# 주소 전처리 함수 정의
def extract_address_pattern2(address):
    
    # 첫 번째 패턴 시도
    first_pattern = re.compile(r'(\S+(?:시|도)) (\S+(?:구|군)) (\S+(?:로|길) \d+\s*(?:번길|번지)?)')
    matches = first_pattern.search(address)

    # 첫 번째 패턴에서 주소를 찾지 못할 경우 두 번째 패턴 시도
    if matches is None:
        second_pattern = re.compile(r'(\S+(?:시|도)) (\S+(?:구|군)) (\S+(?:로\d+[가-힣]*길)\s*\d*(?:번길|번지)?)')
        matches = second_pattern.search(address)

    if matches:
        full_address = matches.group()
        return full_address
    else:
        return "주소를 찾을 수 없습니다."

# 기존 크롤링 결과 불러오기 및 확인(EDIYA_store_info.csv 파일 유무 확인)
if os.path.exists('EDIYA_store_info.csv'):
    ed_df = pd.read_csv('EDIYA_store_info.csv', encoding='utf-8-sig')
else:
    ed_df = pd.DataFrame(columns=['gu', 'store_name', 'store_address'])

# sb_df의 'gu' 컬럼에서 unique한 값 가져오기 (검색에 입력할 구의 이름 가져오기)
gu_list = sb_df['gu'].unique().tolist()

for idx, gu in enumerate(gu_list):
    print(f"[{idx+1}/{len(gu_list)}] 현재 수집 중인 구: {gu}")  # 1. 현재 수집중인 구 출력

    driver.get('https://ediya.com/contents/find_store.html')
    
    # 주소 검색 버튼 클릭
    search_button = driver.find_element(By.CSS_SELECTOR, '#contentWrap > div.contents > div > div.store_search_pop > ul > li:nth-child(2) > a')
    search_button.click()
    
    # '구'명 입력
    search_input_selector = '#keyword'
    search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_input_selector)))
    search_input.send_keys(f'서울 {gu}')
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)
    
    # 검색 결과가 나올 때까지 대기
    result_list_selector = '#contentWrap > div.contents > div > div.store_search_pop > div > div.result_list'
    result_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, result_list_selector)))
    
    current_gu_count = 0  # 현재 '구'에서 크롤링한 데이터 개수를 저장할 변수

    # 결과 크롤링
    stores = result_list.find_elements(By.CSS_SELECTOR, 'li > a > dl')
    for store in stores:
        store_name = store.find_element(By.CSS_SELECTOR, 'dt').text
        raw_store_address = store.find_element(By.CSS_SELECTOR, 'dd').text
        if '서울' in raw_store_address:
            raw_store_address = raw_store_address.replace('서울', '서울특별시')
        store_address = extract_address_pattern2(raw_store_address)
        
        #store_address = '서울특별시 ' + store_address

        new_data = {
            'gu': gu,
            'store_name': store_name,
            'store_address': store_address
        }

        # 중복 체크 후 ed_df에 추가
        if not ((ed_df['store_name'] == store_name) & (ed_df['store_address'] == store_address)).any():
            print(f"신규 매장 발견: {store_name} - {store_address}")  # 2. 신규 수집된 주소 정보 출력

            new_df = pd.DataFrame([new_data])
            ed_df = pd.concat([ed_df, new_df]).reset_index(drop=True)
            current_gu_count += 1

    print(f"{gu}에서 총 {current_gu_count}개의 매장을 크롤링했습니다.")  # 3. 각 구의 크롤링이 끝난 후 총 수집된 매장 수 출력

    time.sleep(2)

    # 중간 저장
    ed_df.to_csv('EDIYA_store_info_temp.csv', encoding='utf-8-sig', index=False)

# WebDriver 종료
driver.quit()    

# 임시 저장 파일 삭제
if os.path.exists('EDIYA_store_info_temp.csv'):
    os.remove('EDIYA_store_info_temp.csv')

# 결과 출력
print('-'*70, '\n')
ed_df.info()

# 크롤링한 데이터를 CSV 파일로 저장
ed_df.to_csv('EDIYA_store_info.csv', encoding='utf-8-sig', index=False)
```


WARNING:root:Can not find chromedriver for currently installed chrome version.


[1/25] 현재 수집 중인 구: 강남구
강남구에서 총 0개의 매장을 크롤링했습니다.
[2/25] 현재 수집 중인 구: 강동구
강동구에서 총 0개의 매장을 크롤링했습니다.
[3/25] 현재 수집 중인 구: 강북구
강북구에서 총 0개의 매장을 크롤링했습니다.
[4/25] 현재 수집 중인 구: 강서구
강서구에서 총 0개의 매장을 크롤링했습니다.
[5/25] 현재 수집 중인 구: 관악구
신규 매장 발견: 신림문화교점 - 서울특별시 관악구 신림로46길 1 
관악구에서 총 1개의 매장을 크롤링했습니다.
[6/25] 현재 수집 중인 구: 광진구
광진구에서 총 0개의 매장을 크롤링했습니다.
[7/25] 현재 수집 중인 구: 구로구
구로구에서 총 0개의 매장을 크롤링했습니다.
[8/25] 현재 수집 중인 구: 금천구
금천구에서 총 0개의 매장을 크롤링했습니다.
[9/25] 현재 수집 중인 구: 노원구
노원구에서 총 0개의 매장을 크롤링했습니다.
[10/25] 현재 수집 중인 구: 도봉구
도봉구에서 총 0개의 매장을 크롤링했습니다.
[11/25] 현재 수집 중인 구: 동대문구
동대문구에서 총 0개의 매장을 크롤링했습니다.
[12/25] 현재 수집 중인 구: 동작구
동작구에서 총 0개의 매장을 크롤링했습니다.
[13/25] 현재 수집 중인 구: 마포구
마포구에서 총 0개의 매장을 크롤링했습니다.
[14/25] 현재 수집 중인 구: 서대문구
신규 매장 발견: 연희홍연길점 - 서울특별시 서대문구 홍제천로 146
서대문구에서 총 1개의 매장을 크롤링했습니다.
[15/25] 현재 수집 중인 구: 서초구
서초구에서 총 0개의 매장을 크롤링했습니다.
[16/25] 현재 수집 중인 구: 성동구
성동구에서 총 0개의 매장을 크롤링했습니다.
[17/25] 현재 수집 중인 구: 성북구
성북구에서 총 0개의 매장을 크롤링했습니다.
[18/25] 현재 수집 중인 구: 송파구
송파구에서 총 0개의 매장을 크롤링했습니다.
[19/25] 현재 수집 중인 구: 양천구
양천구에서 총 0개의 매장을 크롤링했습니다.
[20/25] 현재 수집 중인 구: 영등포구
영등포구에서 총 0개의 매장을 크롤링했습니다.
[21/25] 현재 수집 중인 구: 용산구
용산구에서 총 0개의 매장을 크롤링했습니다.
[22/25] 현재 수집 중인 구: 은평구
신규 매장 발견: 서광교회점 - 서울특별시 은평구 통일로 951 
은평구에서 총 1개의 매장을 크롤링했습니다.
[23/25] 현재 수집 중인 구: 종로구
종로구에서 총 0개의 매장을 크롤링했습니다.
[24/25] 현재 수집 중인 구: 중구
신규 매장 발견: 동대문팀204점 - 서울특별시 중구 마장로 30 
신규 매장 발견: 을지로중앙점 - 서울특별시 중구 마른내로 49 
중구에서 총 2개의 매장을 크롤링했습니다.
[25/25] 현재 수집 중인 구: 중랑구
중랑구에서 총 0개의 매장을 크롤링했습니다.
---------------------------------------------------------------------- 



RangeIndex: 649 entries, 0 to 648
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 


0   gu             649 non-null    object
 1   store_name     649 non-null    object
 2   store_address  649 non-null    object
dtypes: object(3)
memory usage: 15.3+ KB

---


# [분석] 이디야 커피는 정말로 스타벅스 매장 근처에 있는가?

# 3. EDA

- 스타벅스 매장과 이디야 매장의 위치 및 주소, 소속된 구를 수집한 데이터를 간단하게 EDA하며 데이터 파악합니다.

### 통합 데이터 만들기 및 클리닝

```python
# SB_store_info.csv 파일 유무 확인
if os.path.exists('SB_store_info.csv'):
    df1 = pd.read_csv('SB_store_info.csv', encoding='utf-8-sig')
    df1['brand'] = 'STARBUCKS'
    print("SB_store_info.csv 파일을 불러왔습니다.")
else:
    df1 = sb_df.copy()
    df1['brand'] = 'STARBUCKS'
    print("SB_store_info.csv 파일이 없어서 sb_df를 복사했습니다.")

# EDIYA_store_info.csv 파일 유무 확인
if os.path.exists('EDIYA_store_info.csv'):
    df2 = pd.read_csv('EDIYA_store_info.csv', encoding='utf-8-sig')
    df2['brand'] = 'EDIYA'
    print("EDIYA_store_info.csv 파일을 불러왔습니다.")
else:
    df2 = ed_df.copy()
    df2['brand'] = 'EDIYA'
    print("EDIYA_store_info.csv 파일이 없어서 ed_df를 복사했습니다.")

# sb_df에서 'raw_store_address' 컬럼 삭제 (만약 존재한다면)
if 'raw_store_address' in df1.columns:
    df1 = df1.drop('raw_store_address', axis=1)

# 두 DataFrame 합치기
merged_df = pd.concat([df1, df2], ignore_index=True)

# 컬럼 순서 조정
merged_df = merged_df[['brand', 'gu', 'store_name', 'store_address']]

print(merged_df.info())
merged_df.head()
```


SB_store_info.csv 파일을 불러왔습니다.
EDIYA_store_info.csv 파일을 불러왔습니다.

RangeIndex: 1259 entries, 0 to 1258
Data columns (total 4 columns):
 #   Column         Non-Null Count  Dtype 
---  ------         --------------  ----- 


0   brand          1259 non-null   object
 1   gu             1259 non-null   object
 2   store_name     1259 non-null   object
 3   store_address  1259 non-null   object
dtypes: object(4)
memory usage: 39.5+ KB
None





### [전처리] 주소를 기반으로 좌표정보 구하기(feat. Google Maps)

- 이디야 매장찾기에서 상세 주소를 제공하지 않는 데이터들이 있습니다.(주로 관할구까지만 입력된 경우들입니다.)

- googlemaps를 활용해서 매장명을 입력해 주소를 가져오고 가져온 주소를 기존 전처리 함수에 적용하여 획일화합니다.

```python
# 주소처리용 라이브러리 불러오기
import googlemaps
import os
import re
from tqdm import tqdm
tqdm.pandas()

# .env 파일로부터 API 키 불러오기 (API키 보안용)
from dotenv import load_dotenv
load_dotenv()
GMaps_API_KEY = os.getenv('GMaps_API_KEY')

# Google Maps 클라이언트 초기화
gmaps = googlemaps.Client(key=GMaps_API_KEY)

# 주소를 좌표값으로 변환하는 함수 정의
def get_coordinates(address, current_lat=None, current_lon=None):
    try:
        # current_lat와 current_lon 값이 None이 아니면, 이미 좌표값이 있으므로 해당 값을 그대로 반환
        if current_lat is not None and current_lon is not None:
            return current_lat, current_lon
        
        # 크롤링한 매장 주소를 기반으로 Google Maps API를 사용하여 좌표값을 요청
        geocode_result = gmaps.geocode(address)
        
        # API의 응답이 없을 경우 (예: 주소가 잘못되었거나 결과가 없는 경우)
        if not geocode_result:
            print(f"'{address}'에 대한 결과가 없습니다.")
            return None, None
        
        # API 응답에서 위도와 경도 값을 추출
        lat = geocode_result[0]['geometry']['location']['lat']
        lon = geocode_result[0]['geometry']['location']['lng']
        
        return lat, lon
    except Exception as e:
        # API 요청 중 오류가 발생하면 오류 메시지를 출력하고 None 값을 반환
        print(f"'{address}' 처리 중 오류 발생: {e}")
        return None, None

# DataFrame에 적용
merged_df['lat'], merged_df['lon'] = zip(*merged_df['store_address'].progress_apply(get_coordinates))

merged_df.info()
```


 49%|██████████████████████████████████████▍                                        | 613/1259 [01:49

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 50%|███████████████████████████████████████▏                                       | 624/1259 [01:51

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 60%|███████████████████████████████████████████████▌                               | 758/1259 [02:15

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 64%|██████████████████████████████████████████████████▊                            | 809/1259 [02:24

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 66%|████████████████████████████████████████████████████                           | 829/1259 [02:28

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 70%|███████████████████████████████████████████████████████▋                       | 887/1259 [02:38

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 75%|███████████████████████████████████████████████████████████                    | 941/1259 [02:48

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 75%|███████████████████████████████████████████████████████████▏                   | 944/1259 [02:48

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 76%|███████████████████████████████████████████████████████████▊                   | 953/1259 [02:50

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 76%|████████████████████████████████████████████████████████████▏                  | 960/1259 [02:51

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 76%|████████████████████████████████████████████████████████████▎                  | 962/1259 [02:51

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 77%|████████████████████████████████████████████████████████████▋                  | 967/1259 [02:52

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 77%|████████████████████████████████████████████████████████████▊                  | 969/1259 [02:53

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 78%|█████████████████████████████████████████████████████████████▍                 | 980/1259 [02:55

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 93%|████████████████████████████████████████████████████████████████████████▋     | 1173/1259 [03:30

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 94%|█████████████████████████████████████████████████████████████████████████▏    | 1182/1259 [03:32

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 95%|█████████████████████████████████████████████████████████████████████████▋    | 1190/1259 [03:33

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


 95%|██████████████████████████████████████████████████████████████████████████    | 1195/1259 [03:34

'주소를 찾을 수 없습니다.'에 대한 결과가 없습니다.


100%|██████████████████████████████████████████████████████████████████████████████| 1259/1259 [03:46


RangeIndex: 1259 entries, 0 to 1258
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  


0   brand          1259 non-null   object 
 1   gu             1259 non-null   object 
 2   store_name     1259 non-null   object 
 3   store_address  1259 non-null   object 
 4   lat            1241 non-null   float64
 5   lon            1241 non-null   float64
dtypes: float64(2), object(4)
memory usage: 59.1+ KB




- 보통은 google api로 직접 주소나, 매장명을 입력하여 검색하면 결과가 잘 나오는데, 컬럼에서 추출한 단어를 입력하면 결과가 나오지 않는 매장들이 존재합니다.

- 이런 경우 보통 구글지도에 등록되지 않은 주소이거나, 이디야 홈페이지에 등록된 매장명과 구글 지도에 등록된 매장명이 일치하지 않아서 발생합니다.

- 일단 어떤 매장들이 주소가 없는지 확인하고, 추가 처리를 통해 주소를 입력하고 좌표를 도출해야 합니다.

### [전처리] 주소정보가 없는 결과 추출용 함수

```python
# 주소입력용 함수 생성
def update_address(row):
    if row['store_address'] == '주소를 찾을 수 없습니다.':
        search_query = ""
        if row['brand'] == 'EDIYA':
            search_query = "이디아 " + row['store_name']
            print(search_query)
        elif row['brand'] == 'STARBUCKS':
            search_query = "스타벅스 " + row['store_name']
            print(search_query)
        
        # 설정된 검색어를 이용하여 Google Maps API로 주소 검색
        address_result = gmaps.geocode(search_query, language='ko')
        # 검색 결과가 있을 경우
        if address_result:
            formatted_address = address_result[0]['formatted_address']  # 정형화된 주소 가져오기
            refined_address = extract_address_pattern2(formatted_address)  # 주소 전처리
            print(refined_address)  # 전처리된 주소 출력
            return refined_address  # 전처리된 주소 반환
        else:
            return '주소를 찾을 수 없습니다.'  # 검색 결과가 없을 경우 반환
    else:
        return row['store_address']  # 'store_address'가 이미 있는 경우 그대로 반환
```

### 주소검색결과가 없는 rows 추출

```python
# DataFrame에 적용
merged_df2 = merged_df.copy()

merged_df2['store_address'] = merged_df2.apply(update_address, axis=1)

# 주소추출이 안된 매장 확인
merged_df2[merged_df2['store_address'].str.contains('주소')]
```


이디아 강남YMCA점
서울특별시 강남구 학동로 338
이디아 도산사거리점
주소를 찾을 수 없습니다.
이디아 동서울터미널점
이디아 시흥동점
주소를 찾을 수 없습니다.
이디아 월계초교점
이디아 노량진역사점
주소를 찾을 수 없습니다.
이디아 무악재역점
이디아 서대문점
주소를 찾을 수 없습니다.
이디아 홍제역점
이디아 남부터미널점
주소를 찾을 수 없습니다.
이디아 반포지하상가점
주소를 찾을 수 없습니다.
이디아 서울교대점
주소를 찾을 수 없습니다.
이디아 서초역점
주소를 찾을 수 없습니다.
이디아 청계산입구역점
주소를 찾을 수 없습니다.
이디아 낙원동점
주소를 찾을 수 없습니다.
이디아 상명대점
이디아 종로구청점
이디아 탑골공원점
서울특별시 종로구 종로 117





### [전처리] 주소 업데이트를 위한 함수 생성 및 주소 입력

```python
def search_address_in_google_maps(query):
    # Google Maps API를 사용하여 주어진 쿼리에 해당하는 주소를 검색합니다.
    try:
        # geocode 메서드를 사용하여 주어진 쿼리로 주소를 검색합니다.
        # 여기서 language="ko"는 결과를 한국어로 반환하도록 설정합니다.
        result = gmaps.geocode(query, language="ko")

        # 검색 결과가 없는 경우
        if not result:
            print(f"'{query}'에 대한 결과가 없습니다.")
            return None

        # 검색 결과에서 'formatted_address' 값을 가져옵니다.
        address = result[0]['formatted_address']
        
        # 검색된 주소를 반환합니다.
        return address
    except Exception as e:
        # 검색 중 발생한 오류를 출력합니다.
        print(f"'{query}' 검색 중 오류 발생: {e}")
        return None

def update_store_addresses():
    # '주소를 찾을 수 없습니다.'를 포함하는 행들을 선택
    missing_address_rows = merged_df2[merged_df2['store_address'].str.contains('주소를 찾을 수 없습니다.')]
    display(missing_address_rows)
    
    for _, row in missing_address_rows.iterrows():
        # 해당 행의 매장명 및 브랜드 출력
        print(f"브랜드: {row['brand']}, 매장명: {row['store_name']}")
        
        # 브랜드에 따라서 예시 텍스트를 다르게 설정
        example_text = "스타벅스 도산" if row['brand'] == "STARBUCKS" else "이디야 도산"
        
        # 검색어 입력
        query = input(f"해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '{example_text}'): ")

        # 주소 검색
        address = search_address_in_google_maps(query)
        if address:
            # 주소에 '대한민국 ' 문자열이 포함되어 있으면 제거
            if '대한민국 ' in address:
                address = address.replace('대한민국 ', '')
            print(f"검색된 주소: {address}")
            
            # 주소 업데이트
            merged_df2.loc[row.name, 'store_address'] = address
            
            # 업데이트 된 정보 출력
            print(f"{row['brand']}의 '{row['store_name']}' 매장의 주소가 '{address}'로 업데이트되었습니다.\n")

# 함수 실행
update_store_addresses()
```






브랜드: EDIYA, 매장명: 도산사거리점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야 도산사거리점
검색된 주소: 서울특별시 강남구 논현동 98-12
EDIYA의 '도산사거리점' 매장의 주소가 '서울특별시 강남구 논현동 98-12'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 동서울터미널점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야커피 동서울터미널점
'이디야커피 동서울터미널점'에 대한 결과가 없습니다.
브랜드: EDIYA, 매장명: 시흥동점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야커피 시흥동점
'이디야커피 시흥동점'에 대한 결과가 없습니다.
브랜드: EDIYA, 매장명: 월계초교점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야월계초교점
'이디야월계초교점'에 대한 결과가 없습니다.
브랜드: EDIYA, 매장명: 노량진역사점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야커피 노량진역사점
검색된 주소: 서울특별시 동작구 노량진동 60-11 노량진역 지하 1층
EDIYA의 '노량진역사점' 매장의 주소가 '서울특별시 동작구 노량진동 60-11 노량진역 지하 1층'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 무악재역점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야커피무악재역점
검색된 주소: 서울특별시 서대문구 통일로 369
EDIYA의 '무악재역점' 매장의 주소가 '서울특별시 서대문구 통일로 369'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 서대문점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야서대문점
검색된 주소: 서울특별시 서대문구 통일로 141
EDIYA의 '서대문점' 매장의 주소가 '서울특별시 서대문구 통일로 141'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 홍제역점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야 홍제점
'이디야 홍제점'에 대한 결과가 없습니다.
브랜드: EDIYA, 매장명: 남부터미널점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야 남부터미널점
검색된 주소: 서울특별시 서초구 서초동 1444-2
EDIYA의 '남부터미널점' 매장의 주소가 '서울특별시 서초구 서초동 1444-2'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 반포지하상가점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야반포지하상가
검색된 주소: 서울특별시 서초구 반포동
EDIYA의 '반포지하상가점' 매장의 주소가 '서울특별시 서초구 반포동'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 서울교대점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야 커피서울교대점
검색된 주소: 서울특별시 서초구 서초3동 서초중앙로 89
EDIYA의 '서울교대점' 매장의 주소가 '서울특별시 서초구 서초3동 서초중앙로 89'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 서초역점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야 서초역점
검색된 주소: 서울특별시 서초구 서초동 1510-2
EDIYA의 '서초역점' 매장의 주소가 '서울특별시 서초구 서초동 1510-2'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 청계산입구역점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야커피 청계산입구역점
검색된 주소: 서울특별시 신원동 271-23번지 1층 107호 서초구 서울특별시 KR
EDIYA의 '청계산입구역점' 매장의 주소가 '서울특별시 신원동 271-23번지 1층 107호 서초구 서울특별시 KR'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 낙원동점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야커피 낙원동점
검색된 주소: 서울특별시 종로구 삼일대로 436-1
EDIYA의 '낙원동점' 매장의 주소가 '서울특별시 종로구 삼일대로 436-1'로 업데이트되었습니다.

브랜드: EDIYA, 매장명: 상명대점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야 상명대점
'이디야 상명대점'에 대한 결과가 없습니다.
브랜드: EDIYA, 매장명: 종로구청점
해당 매장의 정확한 이름 또는 키워드를 입력하세요 (예: '이디야 도산'): 이디야 종로구청점
검색된 주소: 서울특별시 종로구 수송동 58
EDIYA의 '종로구청점' 매장의 주소가 '서울특별시 종로구 수송동 58'로 업데이트되었습니다.


- 최대한 정보를 찾아서 입력하려 했으나 일부 주소지는 서울시가 아니거나 상세 주소가 불명확한 경우가 또 발생합니다.

- 카카오API를 쓰는 방법도 있겠으나, nulL인 자료가 몇개 되지 않으므로, 이디야 홈페이지와 지도앱의 검색을 교차 검증하여 주소를 확인후 수기로 업데이트를 진행했습니다.

- 매 항목을 판다스 코드로 업데이트하기엔 손이 많이 가서 간단한 함수를 생성하여 업데이트 과정을 간소화 했습니다.

```python
def update_address_with_option(df):
    while True:
        # 메뉴 출력
        print("\n1: 주소 업데이트")
        print("2: 종료")
        
        choice = input("원하는 옵션을 선택하세요 (1 or 2): ")

        if choice == '1':
            # 주소를 수정할 매장명 키워드 입력받기
            keyword = input("주소를 업데이트할 매장의 이름을 입력하세요: ")

            # 해당 키워드를 포함하는 매장명을 가진 행들을 필터링
            matched_rows = df[df['store_name'].str.contains(keyword, case=False)]
            print("\n검색 결과:")
            print(matched_rows[['brand', 'store_name']])
            
            # 고유한 브랜드 목록 출력
            unique_brands = matched_rows['brand'].unique()
            print("\n브랜드 목록:")
            for idx, brand in enumerate(unique_brands, start=1):
                print(f"{idx}: {brand}")
            
            brand_choice = int(input("업데이트할 브랜드의 번호를 선택하세요: "))
            chosen_brand = unique_brands[brand_choice-1]

            # 선택한 브랜드의 매장들에 대해 주소 업데이트
            brand_rows = matched_rows[matched_rows['brand'] == chosen_brand]
            for idx, row in brand_rows.iterrows():
                print(f"\n현재 매장명: {row['store_name']}, 주소: {row['store_address']}")
                new_address = input("새로운 주소를 입력하세요 (아무것도 입력하지 않고 엔터를 누르면 패스): ")

                if new_address:  # 주소를 입력했을 경우에만 업데이트
                    df.loc[idx, 'store_address'] = new_address
                    print(f"'{row['store_name']}'의 주소가 '{new_address}'로 업데이트되었습니다.")

        elif choice == '2':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

update_address_with_option(merged_df2)
```



1: 주소 업데이트
2: 종료
원하는 옵션을 선택하세요 (1 or 2): 1
주소를 업데이트할 매장의 이름을 입력하세요: 동서울터미널

검색 결과:
     brand store_name
755  EDIYA    동서울터미널점

브랜드 목록:
1: EDIYA
업데이트할 브랜드의 번호를 선택하세요: 1

현재 매장명: 동서울터미널점, 주소: 주소를 찾을 수 없습니다.
새로운 주소를 입력하세요 (아무것도 입력하지 않고 엔터를 누르면 패스): 서울특별시 광진구 구의동 547
'동서울터미널점'의 주소가 '서울특별시 광진구 구의동 547'로 업데이트되었습니다.

1: 주소 업데이트
2: 종료
원하는 옵션을 선택하세요 (1 or 2): 1
주소를 업데이트할 매장의 이름을 입력하세요: 시흥동

검색 결과:
     brand store_name
806  EDIYA       시흥동점

브랜드 목록:
1: EDIYA
업데이트할 브랜드의 번호를 선택하세요: 1

현재 매장명: 시흥동점, 주소: 주소를 찾을 수 없습니다.
새로운 주소를 입력하세요 (아무것도 입력하지 않고 엔터를 누르면 패스): 서울특별시 금천구 시흥동 890-10
'시흥동점'의 주소가 '서울특별시 금천구 시흥동 890-10'로 업데이트되었습니다.

1: 주소 업데이트
2: 종료
원하는 옵션을 선택하세요 (1 or 2): 1
주소를 업데이트할 매장의 이름을 입력하세요: 홍제역

검색 결과:
         brand store_name
284  STARBUCKS        홍제역
950      EDIYA       홍제역점

브랜드 목록:
1: STARBUCKS
2: EDIYA
업데이트할 브랜드의 번호를 선택하세요: 2

현재 매장명: 홍제역점, 주소: 주소를 찾을 수 없습니다.
새로운 주소를 입력하세요 (아무것도 입력하지 않고 엔터를 누르면 패스): 서울특별시 서대문구 홍은홍 464
'홍제역점'의 주소가 '서울특별시 서대문구 홍은홍 464'로 업데이트되었습니다.

1: 주소 업데이트
2: 종료
원하는 옵션을 선택하세요 (1 or 2): 1
주소를 업데이트할 매장의 이름을 입력하세요: 반포지하

검색 결과:
     brand store_name
959  EDIYA    반포지하상가점

브랜드 목록:
1: EDIYA
업데이트할 브랜드의 번호를 선택하세요: 1

현재 매장명: 반포지하상가점, 주소: 서울특별시 서초구 반포동
새로운 주소를 입력하세요 (아무것도 입력하지 않고 엔터를 누르면 패스): 서울특별시 서초구 반포동 128-2
'반포지하상가점'의 주소가 '서울특별시 서초구 반포동 128-2'로 업데이트되었습니다.

1: 주소 업데이트
2: 종료
원하는 옵션을 선택하세요 (1 or 2): 1
주소를 업데이트할 매장의 이름을 입력하세요: 상명대

검색 결과:
      brand store_name
1179  EDIYA       상명대점

브랜드 목록:
1: EDIYA
업데이트할 브랜드의 번호를 선택하세요: 1

현재 매장명: 상명대점, 주소: 주소를 찾을 수 없습니다.
새로운 주소를 입력하세요 (아무것도 입력하지 않고 엔터를 누르면 패스): 서울특별시 종로구 홍지동 60-2
'상명대점'의 주소가 '서울특별시 종로구 홍지동 60-2'로 업데이트되었습니다.

1: 주소 업데이트
2: 종료
원하는 옵션을 선택하세요 (1 or 2): 1
주소를 업데이트할 매장의 이름을 입력하세요: 종로구청

검색 결과:
          brand store_name
529   STARBUCKS       종로구청
1187      EDIYA      종로구청점

브랜드 목록:
1: STARBUCKS
2: EDIYA
업데이트할 브랜드의 번호를 선택하세요: 2

현재 매장명: 종로구청점, 주소: 서울특별시 종로구 수송동 58
새로운 주소를 입력하세요 (아무것도 입력하지 않고 엔터를 누르면 패스): 서울특별시 종로구 수송동 58
'종로구청점'의 주소가 '서울특별시 종로구 수송동 58'로 업데이트되었습니다.

1: 주소 업데이트
2: 종료
원하는 옵션을 선택하세요 (1 or 2): 2
프로그램을 종료합니다.


```python
# 결과 확인(서울이 아닌 주소를 가진 것 확인)
merged_df2[~merged_df2['store_address'].str.contains('서울')]
```





- 상세 주소를 찾을 수 없는 매장이므로 drop 합니다.

```python
merged_df2 = merged_df2[merged_df2['store_address'].str.contains('서울')]
```

```python
# 주소정보 기반 좌표 추출 2차시도
merged_df2['lat'], merged_df2['lon'] = zip(*merged_df2['store_address'].progress_apply(get_coordinates))

merged_df2.info()
```


100%|██████████████████████████████████████████████████████████████████████████████| 1258/1258 [03:13


Int64Index: 1258 entries, 0 to 1258
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  


0   brand          1258 non-null   object 
 1   gu             1258 non-null   object 
 2   store_name     1258 non-null   object 
 3   store_address  1258 non-null   object 
 4   lat            1258 non-null   float64
 5   lon            1258 non-null   float64
dtypes: float64(2), object(4)
memory usage: 68.8+ KB





```python
# 결과 확인(좌표값이 빈 컬럼 확인)
merged_df2[merged_df2['lat'].isna() | merged_df2['lon'].isna()]
```





## 분석 1) 어느 브랜드의 매장이 더 많을까?

```python
# 시각화를 위한 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

# 불필요 경고 제거
import warnings
warnings.filterwarnings('ignore')
```

```python
# 브랜드별 매장 수 계산
brand_counts = merged_df['brand'].value_counts()

# seaborn을 사용한 시각화
plt.figure(figsize=(10, 6))
colors = ['#102566' if brand == 'EDIYA' else '#036635' for brand in brand_counts.index]
ax = sns.barplot(x=brand_counts.index, y=brand_counts.values, palette=colors)

# 각 막대에 중간에 수치 표현
for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{int(height)}',
                xy=(p.get_x() + p.get_width() / 2., height/2), # 중간에 위치시키기 위해 height/2 사용
                ha='center',
                va='center',
                color='white',
                weight='bold') # 텍스트 색상과 굵기 조절

# 부등호 그리기
if len(brand_counts) == 2: # 브랜드가 두 개인 경우만 실행
    ediya_count, starbucks_count = brand_counts.values
    if ediya_count > starbucks_count:
        symbol = '>'
    elif ediya_count 

- 2023년 11월 기준 매장의 수는 EDIYA가 스타벅스 매장 보다 33개 매장이 더 많습니다.

- 점포의 수가 비슷하다는 점에서 우리의 가설(**'이디야커피는 스타벅스 커피매장이 위치하는곳에 매장을 위치시킨다?!'**)이 성립이 될 수도 있어 보입니다.

- 다만, 단순 매장의 개수만으로는 가설을 검증할 수 없으니 이런 사실만을 염두해 두어야 합니다.

- 조금 더 공간적인 개념을 적용해서 각 구마다 있는 두 브랜드의 매장수를 비교해 보면 어떨까요?

## 분석 2) 가장 많은 매장이 있는 구는 어디일까? (TOP 5)

---


```python
# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 브랜드와 구('gu') 별로 그룹화하여 매장 수를 계산
grouped = merged_df.groupby(['brand', 'gu']).size().reset_index(name='store_count')

# EDIYA의 매장 수 상위 5개 구 선택
top5_ediya = grouped[grouped['brand'] == 'EDIYA'].nlargest(5, 'store_count')

# STARBUCKS의 매장 수 상위 5개 구 선택
top5_starbucks = grouped[grouped['brand'] == 'STARBUCKS'].nlargest(5, 'store_count')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 8)) # 1행 2열로 axes 생성

# EDIYA 시각화
sns.barplot(data=top5_ediya, x='store_count', y='gu', palette=['#102566'], ax=ax1)
ax1.set_title('이디야 매장이 가장 많은 구 Top 5', fontsize=24, fontweight='bold')
ax1.set_xlabel('매장 수', fontsize=18)
ax1.set_ylabel('구', fontsize=18)
ax1.tick_params(axis='y', labelsize=18)  # y축 라벨 크기 조절
for p in ax1.patches:
    ax1.annotate(f"{int(p.get_width())}개", 
                 (p.get_width() - (p.get_width() - 5), p.get_y() + p.get_height() / 2),
                 ha='center', va='center', 
                 color='white', 
                 fontweight='bold', 
                 fontsize=16)

# STARBUCKS 시각화
sns.barplot(data=top5_starbucks, x='store_count', y='gu', palette=['#036635'], ax=ax2)
ax2.set_title('스타벅스 매장이 가장 많은 구 Top 5', fontsize=24, fontweight='bold')
ax2.set_xlabel('매장 수', fontsize=18)
ax2.set_ylabel('구', fontsize=18)
ax2.tick_params(axis='y', labelsize=18)  # y축 라벨 크기 조절
for p in ax2.patches:
    ax2.annotate(f"{int(p.get_width())}개", 
                 (20, p.get_y() + p.get_height() / 2),
                 ha='center', va='center', 
                 color='white', 
                 fontweight='bold', 
                 fontsize=16)

plt.tight_layout()
plt.show()
```



- 서울시 유동인구 통계, 통계청 인구 데이터등을 기반으로 공개된 2021년 기준 서울시 유동인구 TOP5는 '강남구', '송파구', '서초구', '영등포구', '관악구' 입니다.

- 정확하게 일치하지는 않으나 대체로 두 브랜드 모두 유동인구가 많은 지역에 집중해서 매장이 위치하고 있음을 알 수 있습니다.

- 하지만 두 브랜드의 TOP5가 일치하지는 않기 때문에 우리의 가설이 성립되기는 다소 어려워 보입니다.

- 그럼에도 불구하고 몇몇 구(강남구, 영등포구 등)에서는 매장의 순위나 개수가 유사한 점이 있어 아직 가설이 성립될 여지가 있어 보입니다.

- 더 상세한 정보를 확인하기 위해 각 자치구별 매장의 수 트렌드를 살펴볼 필요가 있습니다.

## 분석 3) 각 구별로 매장의 수는 비슷할까?

---


### 자치구별 스타벅스 & 이디야 매장수 비교

```python
# 구별, 브랜드별 매장 수 집계
grouped = merged_df.groupby(['gu', 'brand']).size().unstack().fillna(0)

# 각 구의 전체 매장 수
grouped['total'] = grouped.sum(axis=1)

# 각 브랜드의 비율 계산
grouped['EDIYA_ratio'] = grouped['EDIYA'] / grouped['total'] * 100
grouped['STARBUCKS_ratio'] = grouped['STARBUCKS'] / grouped['total'] * 100

plt.figure(figsize=(12, 10))

# 누적 막대 그래프 그리기
bar1 = plt.barh(grouped.index, grouped['EDIYA_ratio'], color='#102566', label='이디야')
bar2 = plt.barh(grouped.index, grouped['STARBUCKS_ratio'], left=grouped['EDIYA_ratio'], color='#036635', label='스타벅스')

# 각 막대에 비율 및 매장 수 표시
for i in range(len(grouped)):
    plt.text(grouped['EDIYA_ratio'][i] / 2, i, 
             f"{grouped['EDIYA_ratio'][i]:.1f}% ({int(grouped['EDIYA'][i])}개)", 
             ha='center', va='center', color='white', weight='bold')
    plt.text(grouped['EDIYA_ratio'][i] + grouped['STARBUCKS_ratio'][i] / 2, i, 
             f"{grouped['STARBUCKS_ratio'][i]:.1f}% ({int(grouped['STARBUCKS'][i])}개)", 
             ha='center', va='center', color='white', weight='bold')

plt.xlabel('브랜드별 매장 비율 (%)')
plt.ylabel('구')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1)) # 범례 위치 조정
plt.title('서울특별시 구별 스타벅스와 이디야 매장 비율')
plt.tight_layout()  # 그래프 밖 범례 표시를 위한 레이아웃 조정
plt.show()
```



- 위 그래프는 각 구별로 두 브랜드의 매장수가 각 구별로 어느정도의 비중을 차지하는지 시각화한 결과입니다.

- 괄호 안에는 실제 매장의수를 표기했으며, 전체 매장의 수를 정렬하여 내림차순으로 정렬하였습니다.

- 각 구별로 전반적으로 매장의 수는 이디야가 더 많은 편이며, 두 브랜드의 매장수가 비슷한 지역보다는 매장수의 차이가 나는 지역이 더 많습니다.

- 점점 더 **'이디야커피는 스타벅스 커피매장이 위치하는곳에 매장을 위치시킨다?!'** 는 가설은 기각될 가능성이 높아 보입니다.

- 위 그래프를 조금더 상세하게 확인해보고 싶습니다. 그래서 위 그래프를 재구성하여 이디야 매장수를 기준으로 각 구별로 스타벅스 매장수와의 점유율 차이를 시각화하고자 했습니다.

---


### 자치구별 이디야 & 스타벅스 점유율 비교(기준 : 이디야 커피 매장수)

```python
grouped = merged_df.groupby(['gu', 'brand']).size().unstack().fillna(0)

# 스타벅스와 이디야의 매장 수 차이 계산
grouped['difference'] = grouped['EDIYA'] - grouped['STARBUCKS']

# 점유율 차이 계산
grouped['difference_ratio'] = (grouped['difference'] / (grouped['STARBUCKS'] + grouped['EDIYA'])) * 100

# positive와 negative로 구별
grouped_sort_positive = grouped[grouped['difference'] > 0].sort_values(by='difference_ratio', ascending=True)
grouped_sort_negative = grouped[grouped['difference']  스타벅스')

# 빨간색 막대 그래프 (스타벅스가 이디야보다 많을 때)
bar2 = plt.barh(grouped_sort_negative.index, grouped_sort_negative['difference_ratio'], 
               color='#b22222', label='스타벅스 > 이디야')

# 막대 위에 점유율 차이 및 매장 수 차이 표시
for i, gu in enumerate(grouped_sort_positive.index):
    position = -5  # 그래프 반대편에 표기하기 위한 위치 조정
    plt.text(position, i, 
             f"{grouped_sort_positive['difference_ratio'][gu]:.1f}% (+{int(grouped_sort_positive['EDIYA'][gu] - grouped_sort_positive['STARBUCKS'][gu])}개)", 
             ha='right', va='center', color='black')

for i, gu in enumerate(grouped_sort_negative.index):
    position = 5  # 그래프 반대편에 표기하기 위한 위치 조정
    plt.text(position, i + len(grouped_sort_positive), 
             f"{grouped_sort_negative['difference_ratio'][gu]:.1f}% ({int(grouped_sort_negative['EDIYA'][gu] - grouped_sort_negative['STARBUCKS'][gu])}개)", 
             ha='left', va='center', color='black')

plt.axvline(x=0, color='grey', linestyle='--') # 0 기준선 추가
plt.xlabel('이디야와 스타벅스의 매장 점유율 차이 (%)')
plt.ylabel('구')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.title('서울특별시 구별 이디야와 스타벅스 매장 점유율 차이')
plt.tight_layout()
plt.show()
```



- 먼저 앞서 살펴본 브랜드별 매장수 기준 TOP5 구 중에서 서로 일치하지 않았던 지역의 매장수를 비교해보면 아래와 같습니다.

- 1) 이디야의 나머지 TOP5인 송파구, 마포구, 강서구를 스타벅스의 매장수와 비교

    - 송파구 : 이디야 37개 / 스타벅스 36개로 TOP5에 들지는 못했으나 이디야 매장수와 거의 차이가 나지 않는다. (1.4%)

    - 마포구 : 이디야 32개 / 스타벅스 36개로 TOP5에 들지는 못했으나 이디야 매장수보다 더 많은 매장이 위치한다. (-5.8%)

    - 강서구 : 이디야 31개 / 스타벅스 25개로 매장의수는 다소 적으나 큰 차이는 없다. (10.8%)

- 2) 스타벅스의 나머지 TOP5인 중구, 서초구, 종로구를 이디야의 매장수와 비교

    - 중구 : 스타벅스 53개 / 이디야 30개로 상당히 큰 격차를 보인다. (-27.8%)

    - 서초구 : 스타벅스 49개 / 이디야 29개로 마찬가지로 상당히 큰 격차를 보인다. (-25.6%)

    - 종로구 : 스타벅스 40개 / 이디야 29개로 어느정도 격차가 있다. (-16%) 

- 해당 지역들이 아니어도 서울시 전체 25개 자치구중에 두 브랜드간 매장수 차이가 10%이상인 곳이 20곳이나 됩니다.

    - 상세하게는 10%를 기준으로 이디야 매장이 더 많은 지역이 15곳이며, 스타벅스 매장이 더 많은 지역은 5곳입니다.

- 현재까지 데이터를 살펴보았을때는 우리의 가설(**'이디야커피는 스타벅스 커피매장이 위치하는곳에 매장을 위치시킨다?!'**)는 잘못된 가설일 가능성이 높아 보입니다.

- 하지만 아직 마지막 단계가 남아있습니다. 실제로 매장의 개수는 차이가 날 수 있지만, 지리적으로 인접해 있는 경우들이 있다면 우리의 가설이 유효할 가능성이 있습니다.

- 이디야의 상대적으로 저렴한 브랜딩 전략을 고려한다면 이디야의 매장수가 스타벅스보다 많은 것은 그리 이상한 일이 아니라고 해석할 수 있기 때문입니다.

- 즉, 이디야의 매장수가 다소 많다고 해도, 스타벅스 매장을 중심으로 주변에 여러개의 이디야 매장이 존재한다면 오히려 가설이 성립된다고 판단할 수 있는 요인이 될 수 있습니다.

- 따라서, **folium을 통해 실제 매장의 분포를 살펴보며 시각적으로 확인을 해야 더 정확한 분석이 가능**할 것 같습니다.

## 분석 4) 스타벅스와 이디야 매장위치 시각화

```python
import folium
import geopandas as gpd
from shapely.geometry import Point

# 'lat'와 'lon' 열을 사용하여 Point 객체를 생성
geometry = [Point(xy) for xy in zip(merged_df2['lon'], merged_df2['lat'])]

# GeoDataFrame을 생성
gdf = gpd.GeoDataFrame(merged_df2, geometry=geometry)

# 행정구역의 CRS가 None인 경우 WGS 84로 설정
if gdf.crs is None:
    gdf.set_crs(epsg=4326, inplace=True)

# 서울시의 중심으로 지도 시작점을 설정
map_seoul = folium.Map(location=[37.56, 126.97], zoom_start=11)

# 스타벅스와 이디야의 위치를 지도에 추가
for idx, row in merged_df2.iterrows():
    if row['brand'] == 'STARBUCKS':
        marker_color = 'green'
    else:
        marker_color = 'blue'
    
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        color=marker_color,
        fill=True,
        fill_opacity=0.7,
        radius=5
    ).add_to(map_seoul)

# 지도를 출력
map_seoul
```

Make this Notebook Trusted to load map: File -> Trust Notebook

- 위 지도는 초록색은 스타벅스, 파란색은 이디야 매장으로 두 매장의 위치를 시각화 한 것입니다.

- 절대적으로 스타벅스 매장인근에 이디야 매장이 인접해 있는 것은 아니지만 전반적으로 매장이 밀집된 곳일수록 두 매장이 상당히 인접하여 위치하고 있음을 알 수 있습니다.

---


- 더욱 상세한 파악을 위해 자치구별로 매장의 분포가 비슷한지를 파악해볼 필요가 있습니다.

- 이를 위해 각 자치구별/브랜드별 매장의 위치에 대한 heatmap과 circlemarker를 통해 매장위치를 다른 방법으로 시각화해서 확인해보겠습니다.

## 분석 5) 매장위치 Heatmap 및 구별 위치 CircleMarker 구현

- hetmap : 두 브랜드의 지역별 분포 농도를 색상별로 비교

- CircleMarker : 각 구의 중심점을 기준으로 브랜드별 매장 위치를 원의 크기로 시각화

```python
import folium
from folium.plugins import HeatMap

# 스타벅스와 이디야 데이터 분리
starbucks_df = merged_df2[merged_df2['brand'] == 'STARBUCKS']
ediya_df = merged_df2[merged_df2['brand'] == 'EDIYA']

# 지도 생성
map_seoul = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 스타벅스와 이디야 데이터 병합
brand_locations = starbucks_df[['lat', 'lon']].values.tolist() + ediya_df[['lat', 'lon']].values.tolist()

# 스타벅스 히트맵 (검은색)
starbucks_heatmap = HeatMap(
    data=starbucks_df[['lat', 'lon']].values.tolist(),
    gradient={0: 'black', 1: 'black'},
    max_val=1.0,
    radius=15,
    blur=10,
    max_zoom=18,
)

# 이디야 히트맵 (빨간색)
ediya_heatmap = HeatMap(
    data=ediya_df[['lat', 'lon']].values.tolist(),
    gradient={0: 'red', 1: 'red'},
    max_val=1.0,
    radius=15,
    blur=10,
    max_zoom=18,
)

# 히트맵 추가
starbucks_heatmap.add_to(map_seoul)
ediya_heatmap.add_to(map_seoul)

# 구별 매장 수 계산
gu_store_counts = merged_df2.groupby('gu')['store_name'].count()

# 구별 중심 좌표 계산
gu_center_coords = merged_df2.groupby('gu')[['lat', 'lon']].mean()

# 스타벅스 매장 Circlemarker (코드색: #036635), 초록
for gu, group in starbucks_df.groupby('gu'):
    count = group.shape[0]
    folium.CircleMarker(
        location=[gu_center_coords.loc[gu, 'lat'], gu_center_coords.loc[gu, 'lon']],
        radius=count * 0.3,
        color='#036635',
        fill=True,
        fill_color='#036635',
        fill_opacity=0.5,
        popup=f"스타벅스: {count}개 매장"
    ).add_to(map_seoul)

# 이디야 매장 Circlemarker (코드색: #102566), 파랑
for gu, group in ediya_df.groupby('gu'):
    count = group.shape[0]
    folium.CircleMarker(
        location=[gu_center_coords.loc[gu, 'lat'], gu_center_coords.loc[gu, 'lon']],
        radius=count * 0.3,
        color='#102566',
        fill=True,
        fill_color='#102566',
        fill_opacity=0.5,
        popup=f"이디야: {count}개 매장"
    ).add_to(map_seoul)

# 지도 출력
map_seoul
```

Make this Notebook Trusted to load map: File -> Trust Notebook

[heatmap]

- 각 매장의 분포 개수를 시각화 한 것으로 붉은 색은 이디야, 검은색은 스타벅스로 표현했습니다.

- 이디야 매장의 수가 대체로 더 많기에 전체적으로 보면 붉은색이나 확대하여 보면 결과가 조금 다름을 알 수 있습니다.

- 일부지역은 차이가 있으나 대체로 붉은색 히트맵 주변에 검은색 히트맵도 있어 두 매장의 분포가 유사함을 알 수 있습니다.

---


[circlemarker]

- 각 구별 매장개수를 시각화 한 결과이빈다.

- 각 자치구의 중심점을 구한뒤, 구별 매장 개수를 원의 크기로 표현 했습니다.

- 일부 지역(특히 강남 등)은 스타벅스 매장수가 더 많으나 대체로 두 브랜드의 매장수가 각 자치구별로 비슷하게 분포하고 있음을 알 수 있습니다.

---


- 이로서 우리의 가설이 일정부분 일치하고 있음을 확인할 수 있습니다.

- 다만, **지도상의 위치를 눈으로 확인하였다고 해도, 실제로 인접한것인지 확정짓기 어려우므로 실제 인접한 매장간의 거리를 확인하면 더욱 명확해질 것입니다.**

## 분석 6) 두 브랜드 매장간 거리(Histogram)

### 스타벅스 매장별 가까운 이디야 매장 거리 계산

- 전체 스타벅스 매장에 대해 가장 가까운 이디야 매장과의 평균거리(구 상관없이 계산)

```python
# 거리계산 함수

import math

def haversine(lat1, lon1, lat2, lon2):
    # 위도와 경도를 라디안으로 변환
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # haversine 공식
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    r = 6371  # 지구의 반경 (km)
    return c * r
```

```python
# # 스타벅스와 이디야 데이터 분리
# starbucks_df = merged_df2[merged_df2['brand'] == 'STARBUCKS']
# ediya_df = merged_df2[merged_df2['brand'] == 'EDIYA']

# 각 스타벅스 위치에 대해 가장 가까운 이디야와의 거리를 저장할 리스트
closest_ediya_distances = []

# tqdm을 사용하여 진행률을 표시
for s_idx, s_row in tqdm(starbucks_df.iterrows(), total=starbucks_df.shape[0], desc="Processing Distances"):
    min_distance = float('inf')  # 초기값을 무한대로 설정
    for e_idx, e_row in ediya_df.iterrows():
        distance = haversine(s_row['lat'], s_row['lon'], e_row['lat'], e_row['lon'])
        if distance 
Processing Distances: 100%|██████████████████████████████████████████████████████████| 610/610 [00:25

스타벅스와 가장 가까운 이디야와의 평균 거리: 0.26 km




- 전반적으로 스타벅스와 이디야의 매장간 평균거리가 약 260m로 매우 가까운 거리에 위치하는 경우가 대부분임을 알 수 있습니다.

- 이는 평균 거리이므로, 각 거리별로 매장의 수가 몇개가 되는지 histogram을 통해 확인해보겠습니다.

```python
# Seaborn 환경 설정
sns.set_style("whitegrid")
sns.set_palette("pastel")

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 히스토그램 그리기
plt.figure(figsize=(10, 6))
sns.histplot(closest_ediya_distances, bins=30, kde=True, color='skyblue', edgecolor='black')

plt.title('스타벅스와 가장 가까운 이디야와의 거리 분포')
plt.xlabel('거리 (km)')
plt.ylabel('스타벅스 매장 수')
plt.show()
```



- histogram상으로는 대부분의 이디야 매장이 스타벅스 매장의 인근 3~500m 내에 위치하고 있는 것을 알 수 있습니다.

- 해당 결과로 볼때 우리의 가설인 **'이디야커피는 스타벅스 커피매장이 위치하는곳에 매장을 위치시킨다?!'** 가 어느정도 근거가 있는 주장임을 알수가 있습니다.

- 다만, 이는 확실한 상관관계를 명시하는 것은 아니고 가설이 성립될 수 있는 근거데이터가 될 수 있음을 의미합니다.

- 명확환 확인을 위해 스타벅스 매장을 기준으로 인근에 이디야 매장이 어느정도 거리에 위치해 있는지 지도상의 거리를 확인해볼 필요가 있습니다.

## 분석 7) 두 매장간의 거리에 대한 Box plot

```python
plt.figure(figsize=(10, 6))  # Set the figure size
plt.boxplot(closest_ediya_distances)
plt.title('스타벅스와 가장 가까운 이디야와의 거리 분포 (Box Plot)')
plt.ylabel('거리 (km)')
plt.show()
```



- histogram에서 확인한 바와 마찬가지로 box plot의 결과로도 대부분의 이디야 매장은 스타벅스의 인근에 위치하고 있음을 알 수 있습니다.

    - median(주황색 선) 으로 볼때 대부분의 이디야 매장은 스타벅스 인근 0.25km내에 위치

    - IQR : 이디야 매장은 대체로 스타벅스 매장에서 0.15km ~ 0.35km 내에 위치

    - 이상치 : 몇몇 이디야 매장은 가장 가까운 스타벅스 매장까지 0.5km 이상 떨어진 곳에 위치

- 대부분의 이디야 매장은 스타벅스 매장인근에 위치하고 있으나 아닌 경우들도 상당수 존재하기때문에 이를 파악해볼 필요가 있습니다.

## 분석 8) Q3이상 거리인 이디야 매장 위치 확인하기

```python
# 계산된 거리를 신규 컬럼으로 추가
starbucks_df2 = starbucks_df.copy()
starbucks_df2['closest_ediya_distance'] = closest_ediya_distances

# IQR 계산
Q1 = starbucks_df2['closest_ediya_distance'].quantile(0.25)
Q3 = starbucks_df2['closest_ediya_distance'].quantile(0.75)
IQR = Q3 - Q1

# 상위 이상치 경계값
upper_bound = Q3 + 1.5 * IQR

# 상위 이상치를 가진 스타벅스 매장들 필터링
outliers_df = starbucks_df2[starbucks_df2['closest_ediya_distance'] > upper_bound]

# 지역별로 이상치 매장들 집계
outliers_count_by_gu = outliers_df['gu'].value_counts()

print(outliers_count_by_gu)
```


강남구     7
서초구     5
서대문구    3
은평구     3
강서구     2
동작구     2
성북구     2
용산구     2
종로구     2
광진구     1
구로구     1
노원구     1
마포구     1
성동구     1
송파구     1
양천구     1
Name: gu, dtype: int64

- 분석 결과를 보면 강남구와 서초구에는 이상치로 분류되는 매장이 많이 위치하고 있음을 알 수 있습니다.

- 이는 해당 지역에서 스타벅스 매장이 이디야 매장으로 부터 상대적으로 먼 곳에 위치하고 있음을 의미합니다.

- 전체 매장이 이디야 633개, 스타벅스 601개인점을 감안할때 이상치의 개수가 매우적고 강남, 서초구에 몰려있음을 알 수 있습니다.

- 즉, 두 매장간 거리가 먼 경우는 매우 소수이고, 대부분 평균값인 0.26 km 내외의 거리를 가지고 있음을 알 수 있습니다.

## 분석 9) 각 구별 스타벅스와 이디야의 평균거리 및 분포 시각화

- 분석 2,3에서 각 구별로 매장의 수를 비교하였고, 데이터의 분석 결과 일부가 가설이 옳음을 뒷받침할 수 있는 가능성이 있음을 확인하였습니다.

- 좀 더 정확한 검증을 위해 각 자치구별로 매장의 위치와 집중도 등을 시각화 하여 매장의 개수만 구별로 비슷한 것인지, 아니면 매장의 분포도 가까운 거리에 위치하는지를 확인해볼 필요가 있습니다.

```python
# 각 구별로 스타벅스와 가장 가까운 이디야와의 평균 거리 계산
# 각 구(gu)에 대한 스타벅스와 이디야의 평균 거리를 저장할 딕셔너리
gu_avg_distances = {}

# merged_df2에서 유일한 'gu' 값들을 순회
for gu in tqdm(merged_df2['gu'].unique(), desc = '구별 진행률'):
    # 해당 구에 위치한 스타벅스 정보만 추출
    gu_starbucks = starbucks_df[starbucks_df['gu'] == gu]
    
    # 해당 구 내 스타벅스와 가장 가까운 이디야 간의 거리를 저장할 리스트
    gu_distances = []
    
    # 각 스타벅스 매장에 대한 정보를 순회
    for s_idx, s_row in (gu_starbucks.iterrows()):
        # 가장 가까운 이디야까지의 거리를 저장할 변수. 초기값은 무한대로 설정.
        min_distance = float('inf')
        
        # 모든 이디야 매장에 대한 정보를 순회
        for e_idx, e_row in ediya_df.iterrows():
            # haversine 함수를 이용하여 스타벅스와 이디야 간의 거리 계산
            distance = haversine(s_row['lat'], s_row['lon'], e_row['lat'], e_row['lon'])
            
            # 거리가 현재까지 찾은 최소 거리보다 작으면 업데이트
            if distance 
구별 진행률: 100%|█████████████████████████████████████████████████████████████████████| 25/25 [00:25
### 각 구별 평균거리 시각화

```python
# 각 구별 평균 거리 데이터 프레임 생성
gu_distance_df = pd.DataFrame(list(gu_avg_distances.items()), columns=['gu', 'avg_distance'])

# 바 그래프 시각화
plt.figure(figsize=(15, 10))
sns.barplot(x='avg_distance', y='gu', data=gu_distance_df.sort_values(by='avg_distance', ascending=False))
plt.title('구별 스타벅스와 가장 가까운 이디야와의 평균 거리')
plt.xlabel('평균 거리 (km)')
plt.ylabel('구')
plt.show()
```



- **거리가 상대적으로 먼 구**

    - 은평구, 용산구, 서초구, 강남구 등으로 상대적으로 이디야 매장이 스타벅스와 먼 곳에 위치하고 있음을 알 수 있습니다.

- **거리가 상대적으로 가까운 구**

    - 중구, 관악구, 동대문구, 중랑구 등으로 상대적으로 이디야 매장이 스타벅스와 가까운 곳에 위치하고 있음을 알 수 있습니다.

- 은평구, 용산구, 서초구, 강남구등 일부 몇몇 지역을 제외하고는 대체로 매장간 거리가 매우 가까운 편임을 확인할 수 있음을 알 수 있습니다.  

- 지금까지의 분석 결과로 볼때 두 매장의 분포가 대부분 동일한 지역에 비슷한 분포수준을 보이고 있음을 확인할 수 있습니다.

## 분석 10) 스타벅스 매장과 가장 가까운 이디야 매장 TOP3

```python
import folium
from folium import plugins
from geopy.distance import geodesic

# 지도 생성
map_seoul = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 스타벅스 매장 Circlemarker (코드색: #036635)
for idx, row in starbucks_df.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=5,
        color='#036635',
        fill=True,
        fill_color='#036635',
        fill_opacity=0.5,
        popup=row['store_name']
    ).add_to(map_seoul)

# 이디야 매장 Circlemarker (코드색: #102566)
for idx, row in ediya_df.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=5,
        color='#102566',
        fill=True,
        fill_color='#102566',
        fill_opacity=0.5,
        popup=row['store_name']
    ).add_to(map_seoul)

# 스타벅스와 가장 가까운 이디야 매장 top 2을 선으로 연결하여 표시
for s_idx, s_row in starbucks_df.iterrows():
    distances = []  # 거리를 저장하는 리스트 초기화
    ediya_coords = []  # 이디야 좌표를 저장하는 리스트 초기화
    for e_idx, e_row in ediya_df.iterrows():
        distance = geodesic((s_row['lat'], s_row['lon']), (e_row['lat'], e_row['lon'])).meters  # 거리를 미터 단위로 변경
        distances.append(distance)
        ediya_coords.append((e_row['lat'], e_row['lon']))
    
    # 거리가 가장 짧은 상위 2개의 이디야 매장 선택
    closest_ediya_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:2]
    
    colors = ['#FF5733', '#337DFF']  # 대비되는 2개의 색상 설정
    special_color = '#FFFF33'  # 추가한 3번째 색상
    
    for rank, e_idx in enumerate(closest_ediya_indices):
        distance_to_ediya = distances[e_idx]
        if distance_to_ediya Make this Notebook Trusted to load map: File -> Trust Notebook

- 해당 시각화는 스타벅스 매장을 기준으로 가까운 이디야 매장 TOP3를 시각화 한것입니다.

- 주황색이 1순위, 파란색이 2순위이며 특히 400m내에 매장이 위치하는 경우 노란색으로 표시하도록 하였습니다.

- 스타벅스 매장은 초록색 원, 이디야 매장은 파란색 원으로 표현했습니다.

- 몇몇 관할구에는 특정 브랜드만 집약된 경우가 종종 있으나, 대체로 노란색이 빈번하게 보여 실제 매장간 거리가 매우 가깝다는 것을 알 수 있습니다.

---


# 결론

---


## 소결

---


- 지금까지 다양한 분석 방법을 통해 우리의 가설인 **'이디야커피는 스타벅스 커피매장이 위치하는곳에 매장을 위치시킨다?!'** 를 검증하고자 했습니다.

- 기초적인 데이터인 각 구별 스타벅스 매장의 수와, 이디야 매장의수, 각 매장의 위치등으로 분석한 결과 완벽하진 않지만, **가설이 옳을 가능성이 높음** 을 확인할 수 있었습니다.

- 그 판단 근거는 다음과 같다.

- 1) 두 브랜드의 매장수는 큰 차이가 없음(이디야가 조금 더 많음)

- 2) 일부 지역별로는 매장분포수에 차이가 있지만, 대체로 매장 분포의 수가 각 구별로 비슷하거나 차이가 크지 않습니다.

- 3) 스타벅스와 이디야의 매장 위치를 지도로 시각화 하면 대부분의 매장이 인근에 위치하고 있습니다.

- 4) 두 매장간 거리를 구한뒤 Histogram으로 보면 스타벅스 매장과 이디야 매장간 평균거리는 0.26km이고, 대부분의 매장들이 0.4km 내외의 거리에 존재하고 있습니다.

- 5) box plot으로 확인한 Q3이상인 (매장간 거리가 500m 이상)경우의 매장들은 전체 매장수로 보았을때 일부 매장을 제외하고 대체로 스타벅스 매장 인근에 이디야 매장이 있음을 확인할 수 있었습니다.

- 6) 분석 범위를 좁혀 각 구별로 한정지어 두 브랜드의 매장간 거리를 계산해 보아도 두 브랜드별 매장간 거리는 가까운 편이빈다.

- 7) 해당 결과를 Heatmap과 CircleMarker로 구현하여도 각 구별로 매장의 분포 히트맵의 농도 등이 유사한 경향을 보이고 있습니다.

- 8) 마지막으로 스타벅스 매장과 가장 가까운 이디야 매장을 선으로 연결하고 해당 매장중 400m이내의 매장인 경우 노란색 선으로 연결하도록 하였고, 그 결과 대부분의 매장이 노란색으로 연결되어 두 브랜드 매장간 거리가 상당히 가까움을 확인할 수 있었습니다.

---


- 전체 데이터를 탐색하며 살펴본 결과 스타벅스 매장의 인근(400m내)에 대부분의 이디야 매장이 존재하고 있으며, 각 관할구역별로 매장의 분포 개수도 유사한 것을 확인할 수 있었습니다. 

    - 이는 **'이디야커피는 스타벅스 커피매장이 위치하는곳에 매장을 위치시킨다?!'** 는 가설이 어느정도 성립할 수 있는 근거가 된다고 판단 됩니다.

- 지속적으로 해당 분석의 결과를 확정적으로 말하지 않고, 가능성이 높음만을 언급하는 이유는 아래의 한계점들 때문입니다.

---


## 한계점

---


1) 데이터 한계: 이 분석에서 사용된 데이터는 스타벅스와 이디야의 매장 위치와 수만을 고려하였습니다. 그러나 실제 매장 입지 결정에는 더 많은 변수들이 영향을 줄 수 있습니다.(경쟁 업체, 지역적 특성, 임대료, 소비자 인구 등). 그러나 이를 고려할만한 데이터를 확보하여 분석하지 못했습니다. 

    - 가령, 위 변수 중 평균적으로 입지선정에 핵심적인 요소(예를 들어 임대료)가 나쁜수치임에도 이디야가 스타벅스 인근에 입점을 했다면 우리의 가설이 성립한다고 할 수 있으나 이러한 정확한 분석을 하기에는 데이터가 부족합니다.

2) 시계열 데이터의 부족 : 실제로 가설을 검증하기 위해서는 시간대별로 **'스타벅스가 먼저 입점한 뒤에 이디야가 스타벅스 매장 인근에 입점하는지'** 를 확인해야 합니다. 그러나 현재 데이터로는 이러한 점을 확인할 수 없습니다. 또한, 지금 확보한 데이터만으로는 가설과 같은 전략을 실제 이디야가 사용했는지 단정 짓기 어렵습니다. 사업 초기와 달리 이디야의 인지도가 높아짐에 따라 사업전략을 바꿔 신규 매장의 경우 스타벅스 인근이 아닌 자신만의 기준에 따른 입지를 했을 수 도 있습니다. 이와 같이 단순히 위치만을 가지고 이것을 단정적으로 단언하기에는 무리가 있습니다.

3) 신뢰성: 데이터의 정확성과 충분한 양의 데이터를 사용하는 것이 중요합니다. 데이터 수집과 전처리 과정에서 오류가 발생하거나 누락된 정보가 있다면 분석 결과에 영향을 미칠 수 있습니다. 이번 분석에서도 주소지의 누락이나, 관련된 데이터의 부족현상으로 인해 신뢰성있는 분석을 설계하지 못했습니다.

4) 데이터의 현실성 반영 여부 : 단순 수치로만 본다면 분명 이디야 매장은 스타벅스 매장과 가까운 곳에 입점하고 있습니다. 그러나 서울이라는 도시와 상권의 특성상 주요 상권에 대부분의 프렌차이즈 매장이 집중되어 있는점, 커피라는 동일 카테고리의 제품을 판매하기에 입지 선정 요인의 대부분이 일치할 가능성이 높은 점 등을 고려한다면 두 매장의 위치가 가까운 것이 무조건 가설이 성립하는 증거라 보기는 어렵습니다.

---


## 최종 결론

따라서, 이러한 고려사항을 감안한다면 "**이 가설이 옳음을 확정하기는 어려우나, 현재 확보한 데이터와 표면적으로 도출된 결과를 볼때 가설이 어느정도 상관관계가 있음"** 을 시사합니다.

# 추가 분석 가능성

- 한계점으로 언급한 요소의 대부분은 일반인 입장에서는 구하기 어려운 데이터 일 수 있습니다.

- 그러나 4번 사항의 경우는 데이터 확보 및 검증이 가능합니다.

    - 다른 프렌차이즈 커피 매장의 데이터를 추가로 크롤링 하여 기존 분석방법을 적용해 본다면 이디야만 스타벅스 매장인근에 있는 것인지, 다른 프렌차이즈도 인접하게 위치해 있는지 등을 통해 더욱 확실한 검증이 가능할 것입니다.

