---
title: "Algorithms"
layout: category
taxonomy: "algorithms"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/algorithms/
---

# Intro...
---
이 페이지에서는 프로그래밍의 기초를 다지기 위한 필수 알고리즘들을 공부하고 정리합니다. 버블 정렬, 선택 정렬, 삽입 정렬과 같은 기본 정렬 방식부터 선형 검색, 이진 검색과 같은 검색 방법, 그리고 팩토리얼 계산, 피보나치 수열 같은 재귀 알고리즘까지 다양한 기초 알고리즘들을 정리하고자 합니다. 이러한 알고리즘들은 복잡한 문제를 해결하는 데 있어 기본적인 토대를 제공합니다. 기초 알고리즘들의 이해는 데이터의 구조화, 검색, 정렬 등의 작업에서 꼭 필요하며, 더 복잡한 알고리즘을 이해하는 데도 큰 도움이 됩니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---


{% for post in site.posts %}
  {% if post.categories contains 'algorithms' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

