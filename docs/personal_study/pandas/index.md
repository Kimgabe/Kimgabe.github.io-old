---
title: "Personal Study"
layout: category
taxonomy: "pandas"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/pandas/
---

데이터 분석중 Python 기초 프로그래밍에 대해 공부한 내용을 정리하고 있습니다.

{% for post in site.posts %}
  {% if post.categories contains 'pandas' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

