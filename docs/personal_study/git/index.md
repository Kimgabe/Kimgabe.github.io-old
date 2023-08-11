---
title: "Git"
layout: category
taxonomy: "git"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/git/
---

# Intro...
---
Git은 분산 버전 관리 시스템으로, 여러 개발자들이 동시에 소스 코드의 변경 이력을 효과적으로 관리할 수 있게 도와주는 도구입니다. 이 페이지에서는 Git의 기본적인 원리부터 시작해 commit, branch, merge와 같은 핵심적인 명령어와 기능 개인적으로 학습하면서 정리한 내용들 그리고 이 Github Blog를 구축한 과정을 공유하고자 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'git' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}


