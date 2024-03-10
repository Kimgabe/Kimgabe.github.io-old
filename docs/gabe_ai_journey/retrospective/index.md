---
title: "Retrospective & Review"
layout: category
taxonomy: "retrospective"
entries_layout: grid
author_profile: true
classes: wide
permalink: gabe_ai_journey/retrospective/
---

# 📌Intro
---
참여했던 다양한 활동에 대한 회고를 작성해 공유합니다. 
---



{% for post in site.posts %}
  {% if post.categories contains 'retrospective' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
