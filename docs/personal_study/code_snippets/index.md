---
title: "Code Snippets"
layout: category
taxonomy: "CodeSnippet"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/code-snippet/
---

# ?Intro
---
> 이 페이지에서는 파이썬에 대해서 배운 다양한 개념들을 활용해서 만든 프로그램코드, 함수 등 별도의 카테고리로 분류하기 힘든 작업물들을 업로드 합니다. 데이터 관련 알바를 하거나, 프로젝트를 하면서 사용했던 유용했던 코드 등 여러가지 내용들을 업로드 하고자 합니다.

---


{% for post in site.posts %}
  {% if post.categories contains 'CodeSnippet' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

