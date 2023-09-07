---
title: "Coding Test Study"
layout: category
taxonomy: "coding-test"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/coding-test/
---

# ?Intro
---
> 이 페이지에서는 프로그래밍의 기초를 다지기 위해 ![Programmers school](https://school.programmers.co.kr/learn/challenges/training?order=acceptance_desc&languages=python3) 과 같은 사이트의 코드들을 학습하며 코딩 테스트에 대해 공부한 내용을 정리하고 있습니다. 가급적 매일 1문제 이상은 풀이하려고 하며, 문제와 풀이 방법을 저만의 방식으로 정리하여 업로드하고 있습니다.
---


{% for post in site.posts %}
  {% if post.categories contains 'coding-test' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

