---
title: "Personal Study"
layout: category
taxonomy: "Personal_Study"
entries_layout: grid
author_profile: true
classes: wide
---

데이터 분석과 관련해 개인적으로 공부하는 내용들을 정리하고 있습니다. Python 기초부터 전처리, EDA, 모델링, Code shadowing 등을 기록합니다.



## 포스트 목록
{% for post in site.ds17_studynote %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}