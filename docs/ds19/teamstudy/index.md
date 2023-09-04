---
title: "Team Study"
layout: category
taxonomy: "teamstudy"
entries_layout: grid
author_profile: true
classes: wide
permalink: ds19/teamstudy/
---

# 📌Intro
---
Team Study를 위한 주차별 과제를 정리합니다. Team study에서는 직무분석, 채용공고 스크랩, 코드쉐도잉등 다양한 활동을 합니다.
---



{% for post in site.posts %}
  {% if post.categories contains 'teamstudy' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
