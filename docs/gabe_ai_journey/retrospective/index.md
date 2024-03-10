---
title: "Retrospective & Review"
layout: category
taxonomy: "retrospective"
entries_layout: grid
author_profile: true
classes: wide
permalink: Gabe's AI Journey/retrospective/
---

# 📌Intro
---
AIFFEL에서 공부하면서 경험하는 다양한 일상(공부, 세미나, 프로젝트, etc.) 등에 대한 경험을 공유합니다. 차후에는 KPT(Keep, Problem, Try) 기반의 회고에 대해서도 공유해볼까 합니다.

---



{% for post in site.posts %}
  {% if post.categories contains 'retrospective' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
