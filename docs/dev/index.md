---
title: "Development"
layout: category
taxonomy: "dev"
entries_layout: grid
author_profile: true
classes: wide
---

### 카테고리별 분류

{% for category in site.categories %}
  <h3>{{ category[0] }}</h3>
  <ul>
    {% for post in category[1] %}
      {% if post.collection == 'dev' %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endif %}
    {% endfor %}
  </ul>
{% endfor %}

### 포스트 목록

{% for post in site.dev %}
  {% include archive-single.html %}
{% endfor %}

개발관련한 경험들을 정리하고 있습니다.