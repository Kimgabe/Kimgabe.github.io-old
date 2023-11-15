---
layout: single
title: '[GitHub] "여러개의 레포지토리를 하나의 레포지토리에서 관리해보자!" (feat.subtree)'
categories: git
toc: true
highlight: false
header: 
   teaser: /assets/images/unsplash/git.jpg   
   overlay_image: /assets/images/unsplash/git.jpg   
   overlay_filter: 0.5   
   caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/a-close-up-of-a-computer-screen-with-a-bunch-of-words-on-it-EUzk9BIEq6M)"
---

---
## 🚦Summary
- 이 과정을 거치면 기존에 보유한 여러 Repository를 하나의 Repository 아래에 두어 정리하고 관리할 수 있습니다.
	- 정확히는 기존 Repository 를 하나의 Repository 로 옮기고, 기존 Repository 를 삭제하는 방식입니다.
	- 그럼에도 불구하고! 과거에 commit한 나의 잔디는 지킬 수 있다는 장점이 있습니다. 😀
	  
- 이 작업은 [GitHub](GitHub.md) 의 Subtree 라는 개념을 사용한 방법 입니다.


## 📌Intro
- 최근 AIFFEL이라는 부트캠프를 시작하면서 여러 퀘스트를 위해 동기들의 레포지토리를 fork 해와서 pull request 하는 작업을 반복하고 있습니다.
  
- [GitHub](GitHub.md) 의 사용법도 익히고, co-work를 하는 방법을 배운다는 점에서 좋기는 하지만 (개인적인) 단점이 있습니다. 매번 여러 동기들의 레포지토리를 fork 해오다보니 개인 레포지토리에 비슷한 이름의 레포지토리가 여러개 생겨나기도하고, 그전부터 무분별하게 fork 해오던 레포지토리들이 그득 해서 이참에 정리를 해야겠다 마음 먹었습니다.
  
- 하나의 레포지 토리 안에 다른 레포지토리들을 넣어서 관리할 수 없을까? (내가 쌓아온 잔디를 잃지 않으면서!) 라는 생각이 들었고, 구글링과 gpt의 힘을 빌어 방법을 찾았고, 기록삼아 포스팅을 해봅니다.

---

### 기존의 나의 Repository 들..
![](https://i.imgur.com/3zrXqfc.png)

- 동일한 이름에 동기들의 username으로 구분을 했지만, 왠지 보기에 Repository 가 조잡해보입니다.
- 이러면 정리하고 싶은 욕구가 마구 샘솟습니다. 자주 쓰지도 않을 건데 메인 폴더에 안쓰는 폴더들이 넘쳐나는 기분입니다.
- 하지만 언제 또 이 동료들과 협업을 할지 모르니 fork한 것들을 지우고 싶지는 않습니다. 
- 자료관리의 기본은 역시 동일 카테고리로 묶는 것인데 깃허브에서는 각각의 Repository 가 하나의 프로그램을 이루는 경우가 많다보니 이것이 쉽지 않습니다.
- 하지만 Git의 Subtree 개념을 사용한다면 이 작업이 어느정도 구현 가능합니다.


✔️ 제 목표는 
- 제가 <span style="background:#ff4d4f">AIFFEL을 들으면서 Quest를 하는 `AIFFEL_Online_Quest` repository 안에 fork 해온 동료들의 Repository 를 옮기는 것</span>입니다.
- 하지만, 이전에 동료들과 했던 소중한 제 <span style="background:#ff4d4f">잔디를 지우고싶지는 않습니다.</span>
- 이걸 가능하게 해주는게 Git의 subtree라는 개념입니다. subtree의 개념에 대해서는 포스팅 맨 마지막에 정리하도록 하겠습니다.

---

### 필요 사항
- 로컬 pc(개인 컴퓨터)에 git이 설치가 되어 있어야 합니다.
- 그리고 git의 명령어를 어느정도 사용할 줄 알아야 합니다. (하지만 필요한 명령어는 모두 여기에서 알려드립니다!)
- 왕초보인 저도 하나씩 따라하다보니 가능했습니다. 모두가 가능할거라 생각합니다 😀

---


### 🔭전체 과정 미리보기
1. 잡다한 repository를 관리할 repository를 새로 만든다.
   - 정리할 폴더가 이미 있다면 이 단계를 스킵하고 2번 부터 진행하시면 됩니다.
     
2. 해당 repository를 내 로컬 pc에 clone한다.
   
3.  clone한 repository에 git commit을 한다.
   
4. 이후 subtree 명령어를 사용해 관리하고 싶은 repository들을 하나의 repository로 이동시킨다.
   - 엄밀히는 해당 'repository의 subtree를 관리할 repository에 생성시킨다.'  가 더 맞는 표현이긴 합니다.
     
5. 기존의 repository를 삭제한다.

- 변경된 Repository 의 구조는 아래 이미지와 같습니다.
  
![](https://i.imgur.com/qD66ri7.png)



---
### Repository 합치기 (1) - 여러 Repository를 저장할 Repository를 생성
> 💡 물론 기존의 Repository에 여러 Repository를 저장하는 것도 가능합니다.
>  기존에 보유한 Repository에 바로 여러 Repository를 옮기는 것은 Repository 합치기(2) 부터 작업하시면 됩니다.


- Git 설치가 필요하다면 아래의 링크를 통해 다운받을 수 있습니다. 👉 [Git 다운로드](https://git-scm.com/download/win)
---

#### 1) 새로운 Repository 생성
- 개별 Github의 프로필에서 우측의 이미지 선택후 <span style="background:#ff4d4f">Your Repositories </span> 또는 좌측 상단에 있는 <font color="#8064a2">Repositories</font>를 클릭해 개인 Repository 로 이동 후 <span style="background:#ff4d4f">New</span> 를 눌러 새로운 Repository 를 생성합니다.
![](https://i.imgur.com/TFc9ZQa.png)


- 이제 적절한 Repository 이름을 만들고 적당히 설명도 작성해줍니다. 저는 분류하기 애매한 잡다한 코드들을 모아두는 곳이란 의미로 "MiscellaneousRepos" 라고 이름지어봤습니다.
  
- 기존에 공부하기 위해 fork했던 repository 나, 굳이 메인에 보일 필요 없는 모든 repository 들을 이곳에 옮길 생각입니다.
  
![](https://i.imgur.com/mvcvqls.png)

- 다음으로는 생성한 Repository를 <span style="background:#ff4d4f">내 Local로 Clone</span> 합니다.
  
- 일단 간단하게 README.md 파일 하나 생성해준 뒤, Clone할 Repository 의 주소를 복사합니다.
  
  💡다음 단계의 로컬 git에서 첫번째로 할 작업이 commit 인데, 이를위해 미리 README.md를 하나 만들어 두는게 편합니다.
  별도의 수정없이 `git add .` 한 후에 commit을 해도 되지만, 종종 '변동사항이 없어 commit이 불가능하다'고 뜨는 경우가 있어서 미리 생성하는게 더 편리합니다.

![](https://i.imgur.com/19wUB1e.png)

#### 2) 내 Local에 생성한 Repository Clone 및 Commit하기
- 저 같은 경우 github desktop을 사용하고 있어 바로 프로그램을 통해 폴더를 지정하고 clone을 했습니다.
  (github desktop에 대한 사용법은 차후 기회가 되면 정리해서 포스팅 하겠습니다.)
  
- git 만 컴퓨터에 설치한 상태라면 다음의 단계를 따라 작업합니다.
  
1) Clone할 레포지토리를 저장할 폴더로 이동 또는 생성한다.
   
2) 해당 폴더를 우클릭해 <span style="background:#ff4d4f">Open Git Bash here 를 클릭</span>해 해당 폴더를 경로로 하는 git command 창을 엽니다.

   ![](https://i.imgur.com/XazNTEa.png)

3) 그럼 아래의 이미지와 같이 git command 창이 열리며 해당 경로로 접속된 걸 확인할 수 있습니다.
   
   ![](https://i.imgur.com/KQCbixv.png)

4) 이제 아래의 코드를 각각 입력해 줍니다.
   
   ![](https://i.imgur.com/j66yyLI.png)
- git init으로 저장소를 생성해줍니다. (저의 경우 해당 폴더에 이미 다른 레포지토리를 클론 해둔 상태라 `Reinitialized existing Git repository in~` 이란 메시지가 뜹니다. 
  
- 이후 `git clone + 복사한 repository 주소.git` 를 입력해 clone합니다.
  
- 정상적으로 clone이 되었다면 위의 이미지와 같은 메시지들이 출력 됩니다.
  
5)  이제 clone된 repository에 에 수정작업을 하고 commit을 해줍니다.
   - clone한 repository에 아무작업 없이 다른 repository를 합치는 작업을 하면 git은 변동사항이 없다고 판단합니다.
     
   - 이 경우 `Working tree has modification. Cannot add` 라는 에러가 발생합니다.
     
   - 이를 방지하기 위해 적어도 1번 이상의 commit을 해야 합니다.
     
   - 미리 생성해둔 README.md를 열어서 문구를 조금 수정해도 되고, 아무런 작업을 하지 않고도 아래의 코드를 입력해서 commit을 할 수 있습니다. (commit 불가하다고 나오면 README를 간단하게 수정하고 다시 시도해주세요🫡)
   ```
   $ git add .
   $ git commit -m "message"
```

### Repository 합치기(2) - 생성한 Repository 에 기존 Repository 옮기기

- 아까 `git bash`로 열어둔 터미널에서 이어서 작업 합니다.
- 해당 터미널에서 아래의 명령어를 입력합니다.
```bash
$ git subtree add --prefix=옮길repo이름 옮길repo주소 옮길_repo의_branch명
```
- 현재 Repository에 합치고자 하는 모든 repository에 대해 위 코드를 사용해 1줄씩 입력해주면 됩니다.
  
  > 💡이때, 옮기려고 하는 repository 의 branch가 main 또는 master 경우에 따라서는 user가 지정한 별도의 이름일 수도 있으니 이를 잘 확인해야 합니다.
	- 저같은 경우 SQL용으로 연동해놓은 repository의 경우 branch이름이 2개의 branch가 있었고 이중 하나는 SQL이었습니다.
	  
	  ![](https://i.imgur.com/MBgtzpb.png)

- 정상적으로 subtree가 생성되었다면 아래와 같은 메시지가 출력되어야 합니다.
  
  ![](https://i.imgur.com/YMoHXg5.png)

### Repository 합치기 (3) - Subtree로 옮긴 Repository에 push하기
- 이제 Repository를 합치기 위한 최종 작업입니다.
  
- 이 작업까지 완료를 해야 정상적으로 Repository 합치기 작업이 완료 됩니다.
  
- (1)~(2) 까지는 여러 Repository를 옮기기 위한 공간을 만들고, 그 공간안에 옮기는 작업을 했습니다.
  
- 이제는 원격저장소(GitHub)에 push를 함으로써 <span style="background:#ff4d4f">git에서 subtree로 여러 repository를 옮긴 것들을 push해서 업데이트</span> 해줘야 합니다.
  
- `git push origin HEAD:main --force` 코드를 git command 창에 입력해주면 됩니다.
	- 아래와 같은 결과가 뜬다면 성공적으로 작업이 완료된 것입니다.
	  
	  ![](https://i.imgur.com/Zk5hl4u.png)
	  
- 이후 실제 저의 [GitHub](GitHub.md) 으로 이동해서 subtree를 생성한 Repository에 가보면 아래와 같이 Repository들이 성공적으로 옮겨진 것을 알 수 있습니다.
  
![](https://i.imgur.com/T3arQo8.png)

### Repository 합치기 (4) - 옮긴 Repository 원본 삭제하기
- <span style="background:#ff4d4f">이제 Subtree로 특정 Repository 에 옮기고난 원본 repository 를 삭제할 수 있습니다.</span>
  
- 이미 해당 repository 에 대한 모든 정보가 subtree로 옮겨졌기 때문에 기존 <span style="background:#ff4d4f">repository 를 삭제해도, 과거의 모든 commit을 유지</span>할 수 있습니다.

---
<br>
## 🤔 어떻게 이런 작업이 가능한가? (feat. subtree)
- 이제 모든 작업이 잘 이뤄지고 원하는대로 구현이 되었으니, 원리를 살펴봅니다.
  
- 위 작업에는 git의 subtree라는 개념이 사용되었습니다. 
  
- 이 subtree라는 것이 무엇인지, 어떻게 위와 같은 작업이 이뤄지는지, 왜 기존 commit이 유지되는 지를 정리합니다.

### subtree란?

- subtre는 Git에서 사용하는 개념으로, <span style="background:#ff4d4f">한 repository 안에서 다른 repository로 sub-directory 형태로 통합할 수 있게 해주는 기능</span>입니다.
  
- 이는 여러 프로젝트나 라이브러리를 하나의 repository 에서 관리할 수 있게 하고, sub-directory 는 독립적인 repository 로써 본연의 특징을 그대로 유지하는 특성을 가지고 있습니다.

### 원래 subtree는 어떨때 쓰는걸까?
1) 분리된 프로젝트 관리
   - 서로 다른 프로젝트를 하나의 repository 에서 관리할 수 있기 때문에 각 프로젝트 간 의존성 관리 및 코드 공유가 용이합니다.

2) 독립적인 개발 가능
   - 각 sub-directory 는 독립적인 개발 흐름을 유지할 수 있으므로, 큰 프로젝트 내에서 작은 부분들을 개별적으로 관리할 수 있게 해줍니다.

✔️ [git 공식문서](https://git-memo.readthedocs.io/en/latest/subtree.html) 의 내용을 보면 subtree에 대해 더 다양한 정보를 확인할 수 있습니다.

### subtree로 옮긴후 기존 repository 를 삭제해도 기록이 남는 이유?
- subtree 를 할때 기존 repository 의 commit 내역들도 모두 함께 복사가 됩니다.
  
- 따라서 원본 repository 를 삭제해도 통합된 repository 에 남아있는 commit 기록으로 인해 과거의 기록이 유지됩니다.
  
- 또한 이렇게 생성된 subtree는 자체적으로 '독립된 repository ' 이기 때문에 원본 repository 의 삭제나 commit등에 영향을 받지 않습니다.

### 그렇다면 branch를 새로 만들어서 작업하는것과 subtree는 뭐가 다른가?!
- 개념적으로 branch를 새로만드는 것과 기존 repository 를 subtree로 작업하는 것은 다르며 그 목적도 다릅니다.

1) Branch 
   - branch는 동일한 repository 안에서 다른 개발 흐름을 만들기 위한게 목적입니다.
     
   - 주로 기능개발, 버그 수정, 실험 등을 메인 라인과 분리하여 관리하고자 할때 사용합니다.
     
   - branch는 같은 코드 베이스를 공유하며, 다른 branch로 부터 분기하거나 다시 병합되는 것이 가능합니다.

2) Subtree
   - subtree는 완전히 다른 repository 를 현재 repository 의 sub-repository로서 통합하는데 사용합니다.
     
   - 서로 다른 프로젝트, repository 를 하나의 repository 안에서 관리하는 것이 주 목적입니다.
     
   - subtree를 사용하면, 통합된 repository는 원본 repository 의 commit 내역과 독립성을 유지합니다. (= 영향을 받지 않는다.)
     
   - 또한 기존 repository 와 subtree한 repository 는 별도의 개발 흐름을 가질 수 있습니다.

- 즉, branch는 동일한 repository  내에서 다양한 개발 라인을 관리하는 데 사용되며, subtree는 서로 다른 repository 들을 하나의 repository  안에서 관리하는 데 사용됩니다.
