import streamlit as st

# Checkbox 상태값 관리
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False


def toggle_input():
    r"""Checkbox 를 클릭할 때 Callback 함수
    `not` : boolean 값을 변환한다 (True <-> False)"""
    st.session_state.checkbox = not st.session_state.checkbox # False -> True


# CheckBox 상태창
st.checkbox("Input Field 입력값", value=st.session_state.checkbox, on_change=toggle_input)


# CheckBox 상태창이 활성화 되었을 때 -> Input Box 활성화
if st.session_state.checkbox:
    user_input = st.text_input("내용을 입력하세요:")
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get('user_input', '')

st.write(f"User Input: {user_input}")