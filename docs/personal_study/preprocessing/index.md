---
title: "Pre-processing"
layout: category
taxonomy: "preprocessing"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/preprocessing/
---

# Intro...
---
데이터 전처리(preprocessing)는 머신러닝 및 데이터 분석에서 굉장히 중요한 단계입니다. 원시 데이터는 종종 누락된 값, 이상치, 불필요한 정보 등과 같은 문제점을 가지고 있을 수 있습니다. 따라서, 이러한 문제점들을 수정하고 개선하여 모델의 성능을 최적화하는 작업이 필요합니다. 이 페이지에서는 데이터 전처리의 핵심 단계와 기법, 예를 들어 정규화, 표준화, 인코딩, 결측치 처리 등을 탐색하며, 제가 공부하면서 정리한 내용들을 공유하려고 합니다. 같은 길을 걷는 누군가에게 이 포스팅이 조금이나마 도움이 되길 바랍니다🙏

---

{% for post in site.posts %}
  {% if post.categories contains 'preprocessing' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

