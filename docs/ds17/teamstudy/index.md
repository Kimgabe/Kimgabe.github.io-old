---
title: "Team Study"
layout: category
taxonomy: "teamstudy"
entries_layout: grid
author_profile: true
classes: wide
permalink: ds17/teamstudy/
---

Team Study를 위한 주차별 과제를 정리합니다. Team study에서는 직무분석, 채용공고 스크랩, 코드쉐도잉등 다양한 활동을 합니다. 차후 내용들이 좀 더 누적되면 별도의 페이지를 만들어서 카테고리화 하려 합니다.

{% for post in site.posts %}
  {% if post.categories contains 'teamstudy' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
