import streamlit as st
from datetime import datetime


min_date = datetime(2020,1,1)
max_date = datetime.now()

st.title = "사용자 정보입력"

with st.form(key='user_info_form', clear_on_submit=True):
    name1 = st.text_input('First name: ')
    name2 = st.text_input('Last name: ')
    birth_date = st.date_input("생일",
        max_value=max_date,
        min_value=min_date
    )

    if birth_date:
        age = max_date.year - birth_date.year
        # 생일이 지났는지 확인
        if (birth_date.month > max_date.month) or (
            birth_date.month == max_date.month and birth_date.day > max_date.day):
            age -= 1
        st.write(f"당신의 나이는 {age} 세 입니다.")

    submit_button1 = st.form_submit_button(label='제출하기')

    if submit_button1:
        # 이름, 생년월일 입력이 없을 때
        if not name1 or not birth_date:
            st.warning('모든 form 을 채워주세요')

        else:
            st.success(f"{name1} 님의 나이는 {age} 세 입니다.")
            st.balloons()
