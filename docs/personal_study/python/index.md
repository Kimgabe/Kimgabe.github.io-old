---
title: "Python"
layout: category
taxonomy: "python"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/python/
---

# 📌Intro
---
> Python 프로그래밍의 기초적인 내용을 집약적으로 정리하여 제공하려고 합니다. 변수의 선언, 데이터 타입, 조건문, 반복문, 함수 생성 방법 등 Python의 핵심적인 기본 구조와 문법을 정리합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'python' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

