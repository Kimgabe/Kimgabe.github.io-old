---
title: "Pandas"
layout: category
taxonomy: "pandas"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/pandas/
---

# 📌Intro
---
데이터 분석에 주로 사용되는 Python 라이브러리인 Pandas의 핵심적인 기능과 기초내용을 정리합니다. 데이터 프레임의 생성, 기본적인 데이터 조작 방법, 데이터 필터링 및 정렬 방법 등 주요 개념을 정리하였습니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'pandas' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

