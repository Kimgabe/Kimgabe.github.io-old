---
title: "Code Snippets"
layout: category
taxonomy: "CodeSnippet"
entries_layout: grid
author_profile: true
classes: wide
permalink: personal_study/code-snippet/
---

# ?Intro
---
> �� ������������ ���̽㿡 ���ؼ� ��� �پ��� ������� Ȱ���ؼ� ���� ���α׷��ڵ�, �Լ� �� ������ ī�װ��� �з��ϱ� ���� �۾������� ���ε� �մϴ�. ������ ���� �˹ٸ� �ϰų�, ������Ʈ�� �ϸ鼭 ����ߴ� �����ߴ� �ڵ� �� �������� ������� ���ε� �ϰ��� �մϴ�.

---


{% for post in site.posts %}
  {% if post.categories contains 'CodeSnippet' and post.highlight != false %}
    - [{{ post.title }}]({{ post.url }})
  {% endif %}
{% endfor %}

