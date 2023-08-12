---
title: "Machine Learning"
layout: category
taxonomy: "machine_learning"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/machine_learning/
---

# 📌Intro
---
> 머신러닝은 인공지능(AI)의 한 분야로써, 데이터를 통해 학습하고 예측을 수행하는 알고리즘과 기술을 포함합니다. 이 페이지에서는 지도 학습, 비지도 학습, 강화 학습 등의 주요 학습 방법론과 함께 주요 알고리즘과 같은 머신러닝의 주요 개념과 기본적인 원리, 특징 및 활용 사례를 탐색하며 공부한 내용들을 정리하고 소개하고자 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'machine_learning' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

