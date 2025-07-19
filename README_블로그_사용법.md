# 🚀 **ShokaX 블로그 빠른 사용법**

## **⚡ 빠른 시작**

### **새 포스트 작성**
```bash
cd F:\OneDrive\kimgabe\Kimgabe-shokax-blog\Kimgabe-shokax-new
hexo new "포스트 제목"
```

### **로컬 서버 실행**
```bash
hexo clean && hexo server --port 4043
```
→ http://localhost:4043 에서 확인

### **배포용 빌드**
```bash
hexo clean && hexo generate
```

---

## **📝 포스트 메타데이터 템플릿**

```yaml
---
title: "[카테고리] 포스트 제목"
cover: "https://images.unsplash.com/photo-ID?w=1920&h=1080&fit=crop"
date: YYYY-MM-DD
categories:
  - [personal-study, 소분류]
tags:
  - 태그1
  - 태그2
toc: true
---
```

---

## **🎯 카테고리 구조**

- `[personal-study, python]` - Python 학습
- `[personal-study, pandas]` - Pandas 학습  
- `[personal-study, coding-test]` - 코딩 테스트
- `[gabe-ai-journey, reviews]` - AI 과정 리뷰
- `[portfolio]` - 포트폴리오

---

## **📋 체크리스트**

새 포스트 작성 시:
- [ ] 파일명: `YYYY-MM-DD-제목.md`
- [ ] 위치: `source/_posts/`
- [ ] 메타데이터 완성
- [ ] 로컬 테스트 완료

---

**📖 상세 가이드**: `ShokaX_블로그_사용법_가이드.md` 참조 