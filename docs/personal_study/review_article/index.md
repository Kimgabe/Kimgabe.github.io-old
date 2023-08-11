---
title: "Review Articles"
layout: category
taxonomy: "review_article"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/review_article/
---

# Intro...
---
데이터 분석은 현대 사회에서 중요한 역할을 하는 핵심 기술 중 하나입니다. 수많은 연구자와 전문가들이 이 분야에 대한 다양한 논문과 기사를 발표하거나 자신만의 노하우들을 포스팅하고 있습니다. 이 페이지에서는 데이터 분석 관련해 제가 관심있게 본 논문, Article, Posting, 웨비나 등에 대한 내용을 정리하고 리뷰하는 공간으로 구성하고자 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏
---

{% for post in site.posts %}
  {% if post.categories contains 'review_article' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

