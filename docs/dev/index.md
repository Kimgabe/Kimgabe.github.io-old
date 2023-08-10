---
title: "Development"
layout: category
taxonomy: "dev"
entries_layout: grid
author_profile: true
classes: wide
---
### 카테고리별 분류
<ul>
{% for category in site.categories %}
  {% assign category_posts = site.posts | where: "category", category[0] %}
  {% if category_posts.size > 0 %}
    <li>
      <a href="#{{ category[0] | slugify }}">{{ category[0] }} ({{ category_posts.size }})</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

{% for category in site.categories %}
  {% assign category_posts = site.posts | where: "category", category[0] %}
  {% if category_posts.size > 0 %}
    <h3 id="{{ category[0] | slugify }}">{{ category[0] }}</h3>
    <ul>
      {% for post in category_posts %}
        {% if post.collection == 'dev' %}
          <li><a href="{{ post.url }}">{{ post.title }}</a></li>
        {% endif %}
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}

### 포스트 목록

{% for post in site.dev %}
  {% include archive-single.html %}
{% endfor %}

개발관련한 경험들을 정리하고 있습니다.