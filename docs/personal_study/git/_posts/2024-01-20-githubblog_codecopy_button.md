---
layout: single
title: '"[GitHub 블로그] GitHub Blog 코드블록에 복사버튼 추가하기(feat. Minimal-mistakes)"'
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
  - GitHub
  - github_blog
  - 깃허브블로그
  - 복사버튼
---
## 🚦 Summary
- 최근에는 GitHub 블로그를 생성하면 공개된 여러 테마를 그대로 Clone해와서 손쉽게 생성이 가능합니다.
- 제가 사용한 Minimal Mistake ㅌ
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