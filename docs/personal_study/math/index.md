---
title: "Math & Statistics"
layout: category
taxonomy: "math"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/math_statistics/
---

# 📌Intro
---
> 데이터 분석에 있어서, 수학과 통계는 핵심적인 역할을 합니다. 이 두 분야는 데이터의 숨겨진 패턴을 발견하고, 예측과 결정을 내릴 때의 기반으로 사용됩니다. 이 페이지에서는 데이터 분석을 위한 기본적인 수학 및 통계의 개념, 원리, 그리고 활용 방법에 대해 탐색하며 공부한 내용들을 체계적으로 정리하고 공유하려 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'math' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}


{% for post in site.posts %}
  {% if post.categories contains 'statistics' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}