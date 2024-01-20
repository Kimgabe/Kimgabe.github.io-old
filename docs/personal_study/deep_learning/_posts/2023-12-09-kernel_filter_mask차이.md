---
layout: single
title: '"[DL] 제목"'
categories:
  - deep_learning
tags:
  - deep-learning
  - DL
  - 딥러닝
  - filter
  - kernel
  - mask
  - 커널
  - 필터
  - 마스크
  - CNN
  - CV
toc: true
highlight: false
header:
  teaser: /assets/images/review_article/deep_learing_thumbnail.jpg
  overlay_image: /assets/images/review_article/deep_learing_thumbnail.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/ko/%EC%82%AC%EC%A7%84/XJXWbfSo2f0)"
---

## 🚦 Summary


---

## 📌 Intro.
- CNN(Convolution Neural Network) 에 대해 공부를 하며 여러 자료를 찾다보니 하나의 개념임에도 용어가 혼용되서 사용되는 경우가 있었습니다.
- 바로 커널(kernel)과 필터(filter), 그리고 마스크(mask) 였습니다.
- 내용을 보면 같은 내용을 설명하는데도 문서나 블로그등 자료들마다 용어를 혼용해서 사용하고 있었습니다.
- 어떤 것이 더 정확한 표현인가에 대한 궁금증이 생겼고, 왜 혼용되고 있는지에 대한 궁금함도 생겼습니다.
- 이러한 내용들에 대해 정리합니다.

---

> 💡 이런걸 정리합니다.
- 커널 vs 필터 vs 마스크 용어 정리
- 왜 혼용되고 있는가?
- 세 개념의 차이점과 공통점

---

## 1. 커널 vs 필터 vs 마스크 용어 정리
- CNN에서 사용되는 이 3가지 용어의 정확한 뜻에 대해 살펴봅니다.

### 커널(kernel)
- 커널은 이미지나 다차원 데이터에 대해 특정한 수학적 연산을 적용하기 위한 작은 행렬 혹은 배열을 말합니다.
- 이미지 처리에서 커널은 이미지 상의 한 지점의 픽셀 값과 그 주변 픽셀값들의 가중치로 가중합(합성)

## 🎈 Outro.
- 

---

## 📑References
- [볼록티 - Convolution and Pooling](https://data-science-hi.tistory.com/128)
- [커널(kernel), 필터 (filter), 피처 맵 (feature map) 해설, 정리, 요약](https://hyunhp.tistory.com/657)
- 