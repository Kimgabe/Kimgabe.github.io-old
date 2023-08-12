---
title: "SQL"
layout: category
taxonomy: "sql"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/sql/
---

# 📌Intro
---
> SQL(Structured Query Language)은 데이터베이스에서 데이터를 조회, 삽입, 수정, 삭제하는 데 사용되는 표준 프로그래밍 언어입니다. 이 페이지에서는 SELECT, INSERT, UPDATE, DELETE와 같은 기본 쿼리문부터 JOIN, GROUP BY 등의 고급 기능까지 SQL의 핵심 개념과 기본적인 원리를 탐색하며 공부한 내용들을 정리하고자 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'sql' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

