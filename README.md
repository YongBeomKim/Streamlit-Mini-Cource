# Learning Streamlit
[Streamlit Mini Course - Make Websites With ONLY Python](https://www.youtube.com/watch?v=o8p7uQCGD0U) 의 Chapter 단위 실습코드

<iframe width="560" height="315" src="https://www.youtube.com/embed/o8p7uQCGD0U?si=zBRu1o9XV7LZmqTs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Install
[uv / An extremely fast Python package and project manager, written in Rust](https://github.com/astral-sh/uv) 를 먼저 설치하는 방법을 권장합니다. 어려운 분들은 `requirements.txt`를 활용하여 의존선 패키지들을 설치하세요
```bash
$ git clone git@github.com:YongBeomKim/Streamlit-Mini-Cource.git
$ cd Streamlit-Mini-Cource/
$ uv sync
```

## Jupyter -> Streamlit
- React 로 페이지 구현 전단계, 프로토타입 작성용으로, Button 등 반응버튼 & Router 내용 정리하기
- [Streamlit Mini Course - Make Websites With ONLY Python : Youtube](https://www.youtube.com/watch?v=o8p7uQCGD0U)

## Project 시작하기
```bash
uv venv --python python3.13
uv init .
uv pip install streamlit pandas numpy matplotlib
```

## Dev Run
```bash
$ uv run streamlit run ./main.py
```