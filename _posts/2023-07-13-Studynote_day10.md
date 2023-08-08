---
layout : single
title:  "[스터디노트] Day10 파이썬 기초"
categories: [DS17_Bootcamp, Python Programming, Study Note]
tag: 스터디노트
header :
    teaser : "/assets/img/studynote/studynote_day10.png"
---


# 💡공부한 내용

---

- 예외처리 상세
    - try ~ except ~ else
    - finally
    - Exception 클래스

# 📝 오늘의 하이라이트

---

<aside>
💡 복습을 위해 예제 코드는 가급적 강의에서 들은 내용이 아닌 직접 만들어서 작성

</aside>

- **try ~ except ~ else**: 이 구문은 예외가 발생할 가능성이 있는 코드를 실행하고, 예외가 발생하면 except 블록에서 처리하며, 예외가 발생하지 않으면 else 블록을 실행한다.
    
    ```python
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else:
        print("나눗셈 성공:", result)  # 예외가 발생하지 않으면 실행
    ```
    
- **finally**: 예외 발생 여부와 관계 없이 항상 실행되어야 할 코드를 담는다. 주로 리소스의 정리에 사용된다.
    
    ```python
    try:
        file = open("file.txt", "r")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    finally:
        file.close()  # 예외 발생 여부와 관계 없이 항상 실행
    ```
    
- **Exception 클래스**: 파이썬에서 모든 예외의 기본 클래스이며, 사용자 정의 예외를 만들 때 이 클래스를 상속받을 수 있다.
    
    ```python
    class MyException(Exception):  # Exception 클래스 상속
        pass
    
    try:
        raise MyException("내 예외 발생")
    except MyException as e:
        print(e)  # 출력: "내 예외 발생"
    ```
    

# ✍️ 오늘의 혼잣말

---

- 예외 처리는 프로그램을 안정적으로 만드는 중요한 부분이라는 것을 오늘 배운 내용을 통해 다시 한 번 느꼈다. 각 예외 처리 구문의 목적과 사용법을 이해하니 코드의 흐름을 더 잘 제어할 수 있을 것 같다.
- try-except-else-finally의 조합이 얼마나 유용하게 쓰일 수 있는지 알 수 있었다. 특히 사용자 정의 예외를 통해 더 세밀한 예외 처리가 가능함을 깨달았다. 예외 처리를 잘 활용하면 추후 실무에서 더 복잡한 프로그램을 작성할 때 꼭 필요한 기술이 될 것 같다.