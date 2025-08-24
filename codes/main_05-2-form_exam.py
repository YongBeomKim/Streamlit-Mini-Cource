import streamlit as st
from datetime import datetime


min_date = datetime(2020,1,1)
max_date = datetime.now()

st.title = "사용자 정보입력"
form_value = {
    'name': None,
    'height':None,
    'gender':None,
    'birth':None,
}

with st.form(key='user_info_form'):
    form_value['name'] = st.text_input('이름: ')
    form_value['height'] = st.number_input("키: ")
    form_value['gender'] = st.selectbox("성별: ",['남성','여성'])
    form_value['birth'] = st.date_input("생일",
        max_value=max_date,
        min_value=min_date
    )

    submit_button = st.form_submit_button(label="입력") # 초기값 False
    print("입력 - 버튼 클릭 후 실행")
    if submit_button:
        if not all(form_value.values()):
            st.warning('모든내용을 입력하세요')
        else:
            st.balloons() # 풍선 Animation
            st.write('### 알림')
            for (key, value) in form_value.items():
                st.write(f"{key}: {value}")