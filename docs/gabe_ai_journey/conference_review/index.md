---
title: "Conferences & Seminar"
layout: category
taxonomy: "conference_seminar"
entries_layout: grid
author_profile: true
classes: wide
permalink: gabe_ai_journey/conference_seminar/
---

# 📌Intro
---
하루 하루 공부한 내용들을 간략하게 정리하고 있습니다. 공부하며 정리한 주요 핵심내용만 기록하며 상세한 내용들은 [AI Study Notes](https://kimgabe.github.io/personal_study/){: target=_blank}에 카테고리별로 별도로 정리하고 있습니다.

---


{% for post in site.posts %}
  {% if post.categories contains 'conference_seminar' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
