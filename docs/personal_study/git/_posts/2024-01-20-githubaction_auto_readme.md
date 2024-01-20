---
layout: single
title: '"[Git] Github Action으로 내 README.md 자동화 하기"'
categories:
  - git
toc: true
highlight: false
header:
  teaser: /assets/images/unsplash/git.jpg
  overlay_image: /assets/images/unsplash/git.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/a-close-up-of-a-computer-screen-with-a-bunch-of-words-on-it-EUzk9BIEq6M)"
tags:
  - git
  - README
  - 자동화
  - Github
  - GithubAction
  - 포트폴리오
  - 프로젝트
  - repository
---
## 🚦 Summary
- 개인 포트폴리오로 하나의 레포지토리에 다양한 프로젝트를 관리하곤 합니다.
- 이때, README에 프로젝트를 간결하게 표로 정리하고 각 폴더의 링크를 제공하면 내 프로젝트들을 한눈에 보기 쉽게 제시할 수 있습니다.
- 하지만, 이 README의 표를 프로젝트를 추가할 때마다 매번 작성하는 건 번거로운 일입니다.
- 간단한 Python 코드와 Github Actions를 사용해 이를 자동화 하는 방법을 소개 합니다.
- 더 이상 프로젝트를 추가할 때 마다 표의 내용을 넣거나 링크를 개별적으로 걸어줄 필요없어집니다!
- 이 방법을 응용한다면 다양한 Github의 자동화를 구현할 수 있을 것입니다.
---

##  📌Intro
- 최근에 부트캠프에 참여하면서 퀘스트를 통해 다양한 프로그래밍 코드들을 작성하기도하고, ML이나 DL 관련 사이드 프로젝트 수준의 코드들을 구현해서 하나의 Repository에 업로드 하고 있습니다.
- 처음에는 폴더명으로 구분을 하면 충분하리라 생각했는데, 추가되는 폴더가 10개를 넘어가다 보니 커밋순서에 따라 폴더의 순서가 바뀌기도하는 등 한눈에 작업물을 파악하기가 어려워 지고 있었습니다.
- 다른 포트폴리오를 기록하는 repository들을 찾아보니 README.md에 간단한 표와 링크를 사용해 가독성 좋게 프로젝트들을 정리한 것을 보았습니다.
- 비교적 간단한 형태였기에 매번 프로젝트를 수정하거나 추가할때마다 이 표를 작성하는 것을 자동화하면 좋겠다고 생각했습니다.
- 이 포스팅에서는 간단한 python 코드와 Github Actions를 응용해 나만의 포트폴리오의 README.md 작성을 자동화 하는 방법을 소개합니다.
- 이 방법을 기반으로 다양한 Github의 자동화를 구현할 수 있을 것입니다.

---

> 💡 이런걸 정리합니다.
- 내 메인 Repository 의 README.md 파일의 생성을 자동화 하는 방법
- (Sub) Github Action의 기초 개념


### Target 

![](https://i.imgur.com/FQ7gUxT.png)

---

### GitHub Action 의 주요 개념들

<details>
<summary>👉 GitHub Action의 주요 개념 살펴보기</summary>
<br>

1. **GitHub Actions란?**
    - GitHub Actions는 GitHub 저장소에서 직접 CI(Continuous Integration) 및 CD(Continuous Deployment) 워크플로우를 자동화할 수 있는 도구입니다.
      
2. **워크플로우(Workflow)**
    - 워크플로우는 하나 이상의 작업(job)을 정의하고, 이 작업들이 언제 실행될지를 결정하는 자동화된 프로세스입니다.
    - `.yml` 또는 `.yaml` 파일로 작성되며, 저장소의 `.github/workflows` 디렉토리에 위치합니다.
      
3. **이벤트(Event)**
    - 이벤트는 워크플로우를 트리거(시작)하는 활동입니다. 예를 들어, `push`, `pull request`, `issue` 생성 등이 있습니다.
      
4. **작업(Job)**
    - 워크플로우 내에서 실행되는 일련의 단계(step)를 의미합니다.
    - 각 작업은 독립적으로 실행될 수 있으며, 다른 작업과 병렬 또는 순차적으로 실행될 수 있습니다.
      
5. **단계(Step)**
    - 작업 내부에서 실행되는 개별 명령 또는 작업 단위입니다.
    - 스크립트 실행, 명령어 실행, 액션 실행 등이 포함됩니다.
      
6. **액션(Action)**
    - 재사용 가능한 워크플로우의 구성 요소입니다.
    - 공개적으로 공유되어 다른 사용자가 사용할 수 있으며, 커스텀 액션을 만들 수도 있습니다.
      
7. **러너(Runner)**
    - 워크플로우가 실행되는 서버입니다.
    - GitHub에서 호스팅하는 러너를 사용하거나, 자체적으로 호스팅하는 러너를 구성할 수 있습니다.
      
8. **비밀(Secrets)**
    - 중요한 정보(예: 액세스 토큰, 비밀번호)를 안전하게 저장하고 워크플로우에서 사용할 수 있도록 하는 방법입니다.
      
9. **아티팩트(Artifacts)**
    - 워크플로우 실행 동안 생성된 파일을 저장하고, 나중에 다운로드할 수 있게 하는 기능입니다.

</details>


### GitHub Actions 사용 방법

1. **워크플로우 파일 생성**
   - 리포지토리의 `.github/workflows` 디렉토리에 YAML 형식의 워크플로우 파일을 생성합니다.
    
2. **워크플로우 정의**
   - 워크플로우 파일 내에서 실행할 작업을 정의합니다. 이벤트 트리거, 실행할 작업, 필요한 액션 등을 지정합니다.
    
3. **커밋 및 푸시**
   - 워크플로우 파일을 리포지토리에 커밋하고 푸시합니다.
    
4. **워크플로우 실행 및 모니터링**
   - GitHub 리포지토리의 'Actions' 탭에서 워크플로우의 실행 상태를 확인하고 결과를 모니터링합니다.

> GitHub Actions는 이러한 개념들을 기반으로 다양한 자동화 작업을 수행할 수 있습니다.
> 이번 포스팅에서는 이 GitHub Action과 python 코드를 활용해 내 Repository의 README.md에 <font color="#00b050">자동으로</font> <font color="#00b050">표를 만들고 링크를 입력하는 방법을 정리</font>합니다.

---


> 💡 기능 구현을 위해 몇가지 단계를 거쳐야 합니다.
	1. Python 스크립트 작성
	2. GitHub Action 설정
	3. 스크립트 실행 및 확인



### 1. Python 스크립트 작성
- 제가 작성한 코드를 예제코드로 하여 코드별로 상세한 설명을 드리겠습니다.
- 예제 코드의 경우 표를 만들때 몇가지 전제 조건을 설정했습니다.
	- 기존 README.md의 작성 내용 밑에 표를 추가합니다.
	- 추가되는 표는 가장 최신의 repository 정보를 사용해 항상 기존표를 삭제하고 새로 생성한 표를 입력합니다. (중복 생성 방지)
	- 이름이 `.` 으로 시작하는 폴더(GitHub Action의 workflow 가 저장된 폴더) 를 제외한 나머지 폴더만을 표로 정리
	- 폴더명 앞에 붙은 숫자를 기준으로 Ascending하게 Sorting하도록 되어 있습니다.
- 이를 위해 GitHub API를 사용해서 리포지토리의 폴더 목록을 가져오고, 이를 `README.md` 파일에 업데이트하는 Python 코드를 작성했습니다.

> 1. GitHub API를 통한 폴더 목록 가져오기
```python
import requests
import re

def get_folders(repo):

    # GitHub API를 사용하기 위한 URL 생성

    url = f"https://api.github.com/repos/{repo}/contents/"

    response = requests.get(url)

    # API로부터 받은 응답을 JSON 형식으로 파싱하여 저장

    folders = [item for item in response.json() if item['type'] == 'dir' and not item['name'].startswith('.')]

    return folders

```

- `requests`: HTTP 요청을 보내기 위해 사용하는 라이브러리입니다. 여기서는 GitHub API와 통신하는 데 사용됩니다.
- `re`: 정규 표현식을 사용하기 위한 라이브러리입니다. 여기서는 폴더 이름에서 숫자를 추출하는 데 사용됩니다.
- `get_folders` 함수는 GitHub API를 사용하여 지정된 저장소의 모든 폴더 목록을 가져옵니다.
- 숨김 폴더나 특수 폴더(예: `.`으로 시작하는 폴더)는 제외됩니다.
- 결과는 폴더 객체의 리스트로 반환됩니다.

> 2. 폴더 이름에서 숫자 추출

```python
# 폴더 이름에서 숫자를 추출하는 함수

def extract_number(folder_name):

    # 정규 표현식을 사용하여 폴더 이름에서 숫자를 추출

    match = re.search(r'\d+', folder_name)

    if match:

        return int(match.group())

    return float('inf')  # 숫자가 없는 경우 무한대 값을 반환
```

- `extract_number` 함수는 폴더 이름에서 숫자를 추출합니다.
- 폴더 이름에 숫자가 포함되어 있으면 해당 숫자를 반환하고, 없으면 매우 큰 수(`float('inf')`)를 반환합니다.
- 이는 폴더를 숫자 순으로 정렬할 때 사용됩니다.

> 3. README.md 파일 업데이트 로직

```python
def update_readme(repo, folders, original_content):

    # 기존 "## 📑Quest List📑" 섹션과 그 이하 내용을 제거

    start_index = original_content.find("## 📑Quest List📑")

    if start_index != -1:

        original_content = original_content[:start_index]

  

    # 새로운 "## 📑Quest List📑" 섹션 및 테이블을 생성

    new_table = "## 📑Quest List📑\n\n"

    new_table += "| 퀘스트명 | URL |\n"

    new_table += "| --- | --- |\n"

  

    # 폴더를 숫자로 정렬하여 목록을 만듭니다.

    sorted_folders = sorted(folders, key=lambda x: extract_number(x['name']))

    for folder in sorted_folders:

        folder_name = folder['name']

        folder_url = folder['html_url']

        new_table += f"| {folder_name} | [Link]({folder_url}) |\n"

  

    # README.md 파일의 기존 내용 끝에 새로운 테이블을 추가

    updated_content = original_content + new_table

    return updated_content
```

- `update_readme` 함수는 `README.md` 파일을 업데이트합니다.
- 먼저, 기존 내용에서 "## 📑Quest List📑" 섹션을 찾아 해당 섹션 이후의 내용을 제거합니다.
- 새로운 테이블을 생성하여 폴더 목록을 추가합니다.
- `README.md` 파일의 기존 내용 끝에 새로운 테이블을 추가합니다.

> 4. 로직 실행

```python
# GitHub 저장소와 폴더 목록을 설정

repo = "Kimgabe/AIFFEL_Online_Quest"

  

# 기존 README.md 내용을 읽어옵니다.

with open("README.md", "r") as file:

    original_content = file.read()

  

# 저장소에서 폴더 목록을 가져오고 README.md 파일을 업데이트

folders = get_folders(repo)

updated_content = update_readme(repo, folders, original_content)

  

# 업데이트된 내용을 README.md 파일에 업데이트

with open("README.md", "w") as file:

    file.write(updated_content)
```

- 저장소 이름을 설정하고 `README.md` 파일을 읽습니다.
- `get_folders` 함수를 통해 현재 저장소의 폴더 목록을 가져옵니다.
- `update_readme` 함수로 새로운 내용으로 `README.md`를 업데이트합니다.
- 변경된 내용을 다시 `README.md` 파일에 저장합니다.

- 위 코드를 적용할 수 있도록 예제 코드로 만든 전체 코드는 다음과 같습니다.

<details>
<summary>전체 코드 확인하기</summary>

```python
import requests
import re

# GitHub API를 통해 특정 저장소의 폴더 목록을 가져오는 함수
def get_folders(repo):
    # GitHub API를 사용하기 위한 URL 생성
    url = f"https://api.github.com/repos/{repo}/contents/"
    response = requests.get(url)
    # API로부터 받은 응답을 JSON 형식으로 파싱하여 저장
    folders = [item for item in response.json() if item['type'] == 'dir' and not item['name'].startswith('.')]
    return folders

# 폴더 이름에서 숫자를 추출하는 함수
def extract_number(folder_name):
    # 정규 표현식을 사용하여 폴더 이름에서 숫자를 추출
    match = re.search(r'\d+', folder_name)
    if match:
        return int(match.group())
    return float('inf')  # 숫자가 없는 경우 무한대 값을 반환

# README.md 파일을 업데이트하는 함수
def update_readme(repo, folders, original_content):
    # 기존 "## 📑Quest List📑" 섹션과 그 이하 내용을 제거
    start_index = original_content.find("## 📑Quest List📑")
    if start_index != -1:
        original_content = original_content[:start_index]

    # 새로운 "## 📑Quest List📑" 섹션 및 테이블을 생성
    new_table = "## 📑Quest List📑\n\n"
    new_table += "| 퀘스트명 | URL |\n"
    new_table += "| --- | --- |\n"

    # 폴더를 숫자로 정렬하여 목록을 만듭니다.
    sorted_folders = sorted(folders, key=lambda x: extract_number(x['name']))
    for folder in sorted_folders:
        folder_name = folder['name']
        folder_url = folder['html_url']
        new_table += f"| {folder_name} | [Link]({folder_url}) |\n"

    # README.md 파일의 기존 내용 끝에 새로운 테이블을 추가
    updated_content = original_content + new_table
    return updated_content

# 사용자가 자신의 GitHub 리포지토리 이름을 여기에 입력
user_repo = # Enter your GitHub repository (format: username/repository)

# 기존 README.md 내용을 읽어옵니다.
try:
    with open("README.md", "r") as file:
        original_content = file.read()
except FileNotFoundError:
    original_content = ""

# 저장소에서 폴더 목록을 가져오고 README.md 파일을 업데이트
folders = get_folders(user_repo)
updated_content = update_readme(user_repo, folders, original_content)

# 업데이트된 내용을 README.md 파일에 업데이트
with open("README.md", "w") as file:
    file.write(updated_content)

```

</details>

- 제가 사용하는 것과 동일하게 사용하고자 한다면 예제코드에서 본인의 github user명과 적용할 respsitory만 변경하여 사용하면 됩니다.
- `update_readme.py` 로 repository의 가장 main 페이지에 저장하면 됩니다.
- 이후 이 `update_readme.py`를 GitHub Action에서 불러와서 사용하도록 할 예정입니다.


### 2. GitHub Action 설정

- 이제 위에서 설정한 Python 스크립드가 GitHub의 Repository에 새로운 commit이 있을 때 마다 자동으로 실행되도록 GitHub Action을 설정합니다.
  
  
  > 1) GitHub Action 설정 항목 몇 가지를 조정

- `settings` 👉 `Actions` 👉 `General` 을 선택해 GitHub Action의 옵션으로 이동합니다.


![](https://i.imgur.com/3VLcF30.png)


- 2가지 옵션을 확인합니다.
	- Actions permisssions
		- `Allow all actions and reusable workflows` 에 체크가 되어야 합니다.
	- `Workflow permissions` 
		- `Read and write permissions` 에 체크가 되어 있어야 합니다.


![](https://i.imgur.com/lEAJB2k.png)



> 2) `.github/workflows` 폴더 생성
- 작업을 적용할 Repository의 root dir에 `.github/workflows` 라는 폴더를 생성합니다.
- 이 폴더는 GitHub Action의 워크플로우 설정 파일들을 저장하는 곳입니다.

> 3) 워크 플로우 설정 파일 생성 및 설정 작성

- `update-readme.yml` 파일을 생성한 뒤 워크플로우 설정을 작성합니다.
- 워크플로우 작성시에는 2가지를 설정해주면 됩니다.
	- 트리거 : 워크플로우가 언제 실행될지 설정
	- 작업설정 : 워크플로우에서 실행할 작업 설정정
- 제가 사용하고 있는 워크플로우 설정은 아래와 같습니다.

```yml
name: Update README

on:
  push:
    branches:
      - main

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: pip install requests

      - name: Update README
        run: python update_readme.py

      - name: Commit and Push
        run: |
          git config --global user.name 'Your Name'
          git config --global user.email 'your-email@example.com'
          git add README.md
          git commit -m "Update README"
          git push
```

- 각 내용에 대한 설명은 아래와 같습니다.

1. **워크플로우 이름 설정 (`name`)**:
    - `Update README`: 이 워크플로우의 이름입니다. GitHub Actions 탭에서 이 이름으로 워크플로우를 찾을 수 있습니다.
      
2. **트리거 설정 (`on`)**:
    - `push`: 이 워크플로우는 `push` 이벤트에 의해 트리거됩니다.
    - `- main`: `main` 브랜치에 대한 `push` 이벤트가 발생할 때마다 이 워크플로우가 실행됩니다.
      
3. **작업 설정 (`jobs`)**:
    - `update-readme`: 이 작업의 ID입니다. 여기서는 'README 파일을 업데이트하는 작업'이라는 의미입니다.
    - `runs-on: ubuntu-latest`: 이 작업은 최신 버전의 Ubuntu 가상 환경에서 실행됩니다.
      
4. **작업 단계 (`steps`)**:
    - **Checkout**: 현재 리포지토리를 체크아웃합니다. 이를 통해 리포지토리의 파일에 접근할 수 있습니다.
    - **Set up Python**: Python 환경을 설정합니다. `python-version: '3.8'`을 통해 Python 3.8 버전을 사용하도록 설정합니다.
    - **Install dependencies**: 필요한 Python 패키지를 설치합니다. 여기서는 `requests` 모듈을 설치합니다.
    - **Update README**: `update_readme.py`라는 Python 스크립트를 실행합니다. 이 스크립트는 `README.md` 파일을 업데이트하는 로직을 포함하고 있습니다.
    - **Commit and Push**: 변경된 `README.md` 파일을 깃허브 리포지토리에 커밋하고 푸시합니다. 사용자 이름과 이메일 주소를 설정한 후, `git add`, `git commit`, `git push` 명령을 사용합니다.

---


### 3. 스크립트 실행 및 확인
- 이제 생성한 워크플로우 파일을 저장한 뒤 실제 스크립트가 잘 작동하는지 확인합니다.
- 새로운 폴더를 추가하거나 기존 폴더 이름을 변경해 `README.md`의 파일이 올바르게 업데이트 되는지 확인합니다.
- 올바르게 작성이 되었다면 아래의 이미지처럼 기존 README.md의 내용을 유지하면서 repository에 포함된 폴더명을 기반으로 표를 만들고 링크가 작성되어 있을 것입니다.

![](https://i.imgur.com/FQ7gUxT.png)

---

## 😀 Outro.
- 이번 포스팅에서는 GitHub Action과 파이썬을 활용해 내 GitHub의 Repository의 목록을 자동으로 업데이트하는 방법에 대해 살펴봤습니다.
- 이 방법을 적용해 프로젝트 관리를 수월하게 할 수 있고, 외부인에게 해당 Repository의 내용을 좀 더 높은 가독성과 접근성을 제공할 수 있습니다.
- 또한 이 과정을 통해 기본적인 GitHub Action의 작동 방식을 이해함으로서 다른 자동화 방법을 발굴 및 적용할 수 있을 것입니다.

---
### References
- [Github Actions](https://docs.github.com/ko/enterprise-cloud@latest/actions)
- [Python 빌드 및 테스트](https://docs.github.com/ko/enterprise-cloud@latest/actions/automating-builds-and-tests/building-and-testing-python)


