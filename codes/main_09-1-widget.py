import streamlit as st

# 같은 내용을 자동으로 동일한 Key 값을 지정한다.
st.button('OK')
st.button('OK', key='btn_2') # 고유 Key 값을 지정한다

# Slider
# : st.slider("Text", min, max, default)
if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("최솟값", 0, 50, 25) # 아랫 Slider 최소값
st.session_state.slider = st.slider('슬라이더', min_value, 50, st.session_state.slider)
