---
title: "Team Study"
layout: category
taxonomy: "teamstudy"
entries_layout: grid
author_profile: true
classes: wide
permalink: AIFFEL_7th/teamstudy/
---

# 📌Intro
---
Team Study로 하게 되는 다양한 과제들을 정리합니다.(예정)

---



{% for post in site.posts %}
  {% if post.categories contains 'teamstudy' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
