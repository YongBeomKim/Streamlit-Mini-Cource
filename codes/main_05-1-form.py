import streamlit as st
import pandas as pd

st.title('Form 구현하기')

with st.form(key="sample_form"):

    st.subheader('Text 입력')
    name = st.text_input('이름 ...')
    feedback = st.text_area('피드백 상세내용 ...')

    st.subheader('Date & Time 입력')
    _date = st.date_input('생일')
    _time = st.time_input('출생시간')

    st.subheader("선택옵션")
    choice = st.radio('Option 선택', ['Option 1','Option 2','Option 3'])
    gender = st.selectbox("성별", ['남성','여성'])
    slide_bar = st.select_slider("가족수", options=[1,2,3,4,5])

    st.subheader('토클 & 체크박스')
    notification = st.checkbox('내용확인')
    toggle_value = st.checkbox('다크모드?', value=False) # 초기값

    # Submit Button
    submit_button = st.form_submit_button(label="제출하기")

# Form 의 외부영역 처리내용
# `submit_button` 을 클릭한 뒤 변수값이 채워진다
st.subheader('제출하기 클릭 후 반응내용')
if st.button('Click Me'):
    st.write(f'Hello, {name}!')