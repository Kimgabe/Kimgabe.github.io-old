---
title: "Code Shadowing"
layout: category
taxonomy: "shadowing"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/shadowing/
---

# Intro...
---
코드 쉐도잉은 다른 사람들의 코드를 분석하고, 이해하며, 그것을 기반으로 자신만의 지식을 확장하는 방법입니다. Kaggle, Dacon 등의 데이터 사이언스 플랫폼에서 우수한 성과를 내고 있는 다양한 프로젝트와 포트폴리오 코드를 직접 살펴보며 그 속의 인사이트를 찾아내는 것은 코딩실력 향상 뿐만 아니라 데이터를 분석하는 다양한 관점을 경험할 수 있는 좋은 학습방법이라 생각합니다. 이 페이지에서는 그러한 코드들을 쉐도잉한 결과와 그 과정에서 제가 학습한 내용들을 정리하여 공유하고자 합니다.

---

{% for post in site.posts %}
  {% if post.categories contains 'shadowing' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

