"fragment : 구성요소들의 묶음"
import streamlit as st

st.title('My Awesome App')

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle('Toggle')
    cols[1].text_area('Text 를 입력하세요')
    # st.rerun(scope='fragment')


@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("필터")
    new_cols[1].file_uploader("이미지 Upload")
    new_cols[2].selectbox("옵션", ['Option 1','Option 2','Option 3'])
    new_cols[3].slider("값 선택", 0, 100, 50)
    new_cols[4].text_input("문자를 입력하세요")


toggle_and_text()
cols = st.columns(2)
cols[0].selectbox('선택', [1,2,3], None)
cols[1].button("업데이트")
filter_and_file()