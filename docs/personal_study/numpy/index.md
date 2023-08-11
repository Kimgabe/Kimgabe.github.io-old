---
title: "Numpy"
layout: category
taxonomy: "numpy"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/numpy/
---

# 📌Intro
---
Numpy는 파이썬에서 수치 데이터를 효과적으로 처리하는데 필수적인 라이브러리입니다. 다차원 배열 객체와 이를 활용한 다양한 연산 기능을 제공하며, 수학적 연산을 위한 강력한 도구를 포함하고 있습니다. 이 페이지에서는 Numpy의 기본적인 배열 연산, 함수, 그리고 다양한 데이터 구조에 대해 탐색하며 공부한 내용들을 공유하고자 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'numpy' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

