---
layout : single
title:  "[스터디노트] Day11 파이썬 기초"
categories: [ds19_Bootcamp, Python Programming, Study Note]
tag: 스터디노트
header :
    teaser : "/assets/img/studynote/studynote_day11.png"
---


# 💡공부한 내용

---

- **사용자 Exception 클래스**
- **텍스트 파일 쓰기**
- **텍스트 파일 읽기**
- **텍스트 파일 열기**
- **with ~ as 문**
- **writelines()**
- **readlines(), readline()**

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **사용자 Exception 클래스**: 기존의 예외 클래스로 처리할 수 없는 특정 상황에 대한 예외 처리를 위해 사용자가 직접 정의하는 클래스. 특수한 로직에 맞는 예외를 처리하고자 할 때 유용하다.
    
    ```python
    class MyException(Exception):  # 사용자 정의 예외 클래스 생성
        pass
    
    try:
        raise MyException("이것은 사용자 정의 예외입니다.")
    except MyException as e:
        print(e)  # 사용자가 정의한 예외 메시지 출력
    ```
    
- **텍스트 파일 쓰기**: 파일에 텍스트를 작성하려면 **`'w'`** 모드로 파일을 열어야 한다. 파일이 없으면 새로 만들며, 기존 내용은 덮어쓴다.
    
    ```python
    file = open('file.txt', 'w')  # 'w' 모드로 파일 열기
    file.write('안녕하세요.')      # 파일에 문자열 작성
    file.close()               # 파일 닫기
    ```
    
- **텍스트 파일 읽기**: **`'r'`** 모드로 파일을 열면 텍스트 파일의 내용을 읽을 수 있다. 읽을 파일이 반드시 존재해야 한다.
    
    ```python
    file = open('file.txt', 'r')  # 'r' 모드로 파일 열기
    content = file.read()        # 파일의 모든 내용 읽기
    print(content)               # 출력: 안녕하세요.
    file.close()                 # 파일 닫기
    ```
    
- **with ~ as 문**: 파일을 열 때 발생할 수 있는 오류를 방지하고, 작업 완료 후 파일을 자동으로 닫아주는 구문. 안전한 파일 처리를 위해 권장된다.
    
    ```python
    with open('file.txt', 'r') as file:  # with ~ as로 파일 열기
        content = file.read()            # 파일 읽기
        print(content)                   # 내용 출력
    # with 문을 빠져나가면 파일이 자동으로 닫힌다.
    ```
    
- **writelines()**: 여러 줄의 텍스트를 한 번에 파일에 쓸 수 있는 메소드. 줄바꿈 문자(**`\n`**)를 직접 관리해야 한다.
    
    ```python
    lines = ['첫 번째 줄\n', '두 번째 줄\n']  # 줄바꿈 문자 포함
    with open('file.txt', 'w') as file:
        file.writelines(lines)  # 여러 줄 한 번에 쓰기
    ```
    
- **readlines(), readline()**: **`readlines()`**는 파일의 모든 줄을 리스트 형태로 반환하며, **`readline()`**은 한 줄씩 읽는다.
    
    ```python
    with open('file.txt', 'r') as file:
        lines = file.readlines()  # 파일의 모든 줄을 리스트로 읽기
        line = file.readline()    # 파일에서 한 줄 읽기
    ```
    

# ✍️ 오늘의 혼잣말

---

- 오늘은 파일 처리에 대한 내용을 중점적으로 다뤘다. 사용자 정의 예외 클래스를 통해 보다 세밀한 예외 처리가 가능하다는 것을 되새기게 되었고, 텍스트 파일을 다루는 방법은 실제 프로젝트에서 많이 사용하던 터라 좀 익숙했다.
- 특히 **`with ~ as`** 문을 통해 파일을 안전하게 다루는 방법은 진짜 중요한 포인트 인것 같다. 실제 작업하다 보면 아무 생각없이 불러온 파일에 코드 계속 적용하면서 작성하는 경우가 있는데, 이러다가 원본이 손상되어서 한참 고생했던 기억이 있다.