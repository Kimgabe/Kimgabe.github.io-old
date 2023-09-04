---
title: "Visualization"
layout: category
taxonomy: "visualization"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/visualization/
highlight : false
---

# 📌Intro
---
> 데이터 시각화는 복잡한 데이터를 이해하기 쉽게 표현하는 중요한 도구입니다. 특히 matplotlib, seaborn, folium 등의 라이브러리를 활용하면 파이썬 환경에서도 직관적이고 아름다운 시각화를 만들어낼 수 있습니다. 이 페이지에서는 위 세 가지 라이브러리를 중심으로 데이터 시각화의 기본적인 개념과 활용 방법을 탐색하며, 제가 공부하며 정리한 내용들을 공유하고자 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if (post.categories contains 'visualization' or post.categories contains 'matplotlib' or post.categories contains 'seaborn' or post.categories contains 'folium') and post.highlight == false %}
    {# 여기에 아무 것도 출력하지 않음 #}
  {% else %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}
