---
title: "Deep Learning"
layout: category
taxonomy: "deep_learning"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/deep_learning/
---

# 📌Intro
---
> 딥러닝은 머신러닝의 하위 분야로, 인공신경망을 기반으로 한 알고리즘과 방법론에 집중합니다. 이 페이지에서는 CNN, RNN, LSTM 등 주요 인공신경망 구조와 함께 딥러닝의 핵심 개념, 기본 원리, 그리고 현대의 다양한 활용 사례를 탐색하며 정리한 내용들을 공유하고자 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'deep_learning' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}