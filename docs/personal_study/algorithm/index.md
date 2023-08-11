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
알고리즘은 문제를 해결하기 위한 명확한 절차나 방법을 의미합니다. 특히 데이터 분석을 진행하면서 자주 접하게 되는 여러 가지 기본 알고리즘들이 있습니다. 이 페이지에서는 데이터 분석의 기반을 이루는 버블 정렬, 이진 검색과 같은 기초적인 알고리즘들에 대해 간단하게 소개하려고 합니다. 이러한 기초 알고리즘들의 이해는 데이터의 구조화, 검색, 정렬 등의 작업에서 꼭 필요하며, 더 복잡한 알고리즘을 이해하는 데도 큰 도움이 됩니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏
---


{% for post in site.posts %}
  {% if post.categories contains 'algorithms' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

