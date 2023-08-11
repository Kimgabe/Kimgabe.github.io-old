---
title: "Tableau"
layout: category
taxonomy: "tableau"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/tableau/
---

# Intro...
---
Tableau는 세계적으로 널리 알려진 BI(Business Intelligence) 툴로, 복잡한 데이터를 쉽고 빠르게 시각화하고 분석할 수 있게 도와줍니다. 이 페이지에서는 Tableau의 기본 원리부터 다양한 기능, 그리고 실제 비즈니스 환경에서 어떻게 활용될 수 있는지에 대해 공부한 내용들을 정리하고자 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'tableau' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

