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