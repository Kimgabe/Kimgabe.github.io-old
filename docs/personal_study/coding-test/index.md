---
title: "Coding Test Study"
layout: category
taxonomy: "coding-test"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/coding-test/
---

# ?Intro
---
> �� ������������ ���α׷����� ���ʸ� ������ ���� ![Programmers school](https://school.programmers.co.kr/learn/challenges/training?order=acceptance_desc&languages=python3) �� ���� ����Ʈ�� �ڵ���� �н��ϸ� �ڵ� �׽�Ʈ�� ���� ������ ������ �����ϰ� �ֽ��ϴ�. ������ ���� 1���� �̻��� Ǯ���Ϸ��� �ϸ�, ������ Ǯ�� ����� ������ ������� �����Ͽ� ���ε��ϰ� �ֽ��ϴ�.
---


{% for post in site.posts %}
  {% if post.categories contains 'coding-test' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

