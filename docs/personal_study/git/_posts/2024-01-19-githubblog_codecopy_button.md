---
layout: single
title: '"[GitHub 블로그] GitHub Blog 코드블록에 복사버튼 추가하기(feat. Minimal-mistakes)"'
categories:
  - git
toc: true
highlight: false
header:
  teaser: /assets/images/unsplash/git.jpg
  overlay_image: /assets/images/unsplash/git.jpg
  overlay_filter: 0.5
  caption: "Photo credit: [**Unsplash**](https://unsplash.com/photos/a-close-up-of-a-computer-screen-with-a-bunch-of-words-on-it-EUzk9BIEq6M)"
tags:
  - git
  - GitHub
  - github_blog
  - 깃허브블로그
  - 복사버튼
---
## 🚦 Summary
- 최근에는 GitHub 블로그를 생성하면 공개된 여러 테마를 그대로 Clone해와서 손쉽게 생성이 가능합니다.
- 다만 코드블록의 복사버튼은 별도로 기능 구현이 필요합니다.
- 이번 포스팅에서는 Minimal-mistake 테마로 만든 GitHub 블로그에서 코드블록의 복사버튼을 만드는 방법을 소개합니다.

---

> 💡 이런걸 정리합니다.
- 내 GitHub 블로그의 코드블록에 복사버튼을 추가하는 방법

## 📑 작업순서 소개
- `_config.yml` 파일 수정
- layout 추가

---

### 1️⃣ config.yml  파일 수정

> 💡 `_config.yml` 이란? 

- `_config.yml` 은 GitHub Pages 혹은 Jekyll을 사용해서 GitHub 블로그를 구성할 때 사용되는 설정파일입니다.
- 이 파일에서 블로그의 기본 설정, 테마, 플러그인, 페이지 제목, 블로그 설명, 사이드바 설정 등 다양한 옵션을 조정할 수 있습니다.

<br>

> 📰 `_config.yml` 파일 수정 하기


- GitHub 블로그를 생성한 Repository의 루트 디렉토리로 이동합니다.
- `_config.yml` 파일을 열고 'plugins' 부분을 찾아서 아래와 같이 `jekyll-remote-theme` 플러그인을 추가합니다.

```yaml
plugins:
  - jekyll-remote-theme
```

- `_config.yml` 파일에서 `remote_theme` 부분을 찾아 Minimal Mistakes 테마를 설정합니다. 아래와 같이 설정합니다
```yaml
remote_theme: "mmistakes/minimal-mistakes"
```


---

###  2️⃣ `_layouts` 과 `default.html` 파일 수정하기

> 💡 `_layouts` 과 `default.html` 파일?


- `_layouts` 디렉토리는 GitHub 블로그의 페이지 레이아웃을 정의하는 곳입니다.
- `default.html` 파일은 블로그의 기본 레이아웃을 정의하며, 모든 페이지에 공통으로 적용됩니다.

<br> 

> 📰 `default.html` 파일 수정 하기


- 만약 `_layouts` 폴더가 없다면 생성하고 `default.html` 을 생성해 줍니다.
- 생성한 `default.html` 파일의 하단에 아래의 코드를 추가합니다.

```html

{% raw %}
<!DOCTYPE html>
<html>
<head>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      const codeBlocks = document.querySelectorAll('pre');
      codeBlocks.forEach(function (codeBlock) {
        const button = document.createElement('button');
        button.className = 'copy-code-button';
        button.textContent = '복사';
        const code = codeBlock.querySelector('code');
        button.addEventListener('click', function () {
          const textArea = document.createElement('textarea');
          textArea.value = code.textContent;
          document.body.appendChild(textArea);
          textArea.select();
          document.execCommand('copy');
          document.body.removeChild(textArea);
          alert('코드가 복사되었습니다.');
        });
        codeBlock.parentNode.insertBefore(button, codeBlock);
      });
    });
  </script>
</head>
<body>
  {{ content }}
</body>
</html>
{% endraw %}
```

---

- 여기까지 진행하면 모든 준비가 완료되었습니다.
- 이제부터 일반적인 마크다운의 코드블록 작성 방식대로 작성을 하면 자동으로 복사버튼이 생성됩니다.
- 위 코드를 적용한 결과 아래와 같이 코드 복사버튼이 생성되고, 복사버튼을 누르면 복사가 되었다는 메시지가 팝업됩니다.

![](https://i.imgur.com/f9zwApM.png)

---

## 🎈Outro.
- 이번 포스팅에서는 GitHub 블로그의 Minimal-mistake 테마에서 코드블록에 복사버튼을 추가하는 방법을 정리했습니다.
- 차후에 시간이 된다면 GitHub 블로그를 생성하는 방법에 대해서도 포스팅을 하다록 하겠습니다.