import streamlit as st

# # 일반상태 조건문
# # 조건문 실행시 - 바로 App 재실행
# counter = 0
# st.write(f'카운팅 숫자: {counter}')

# if st.button('증가'):
#     counter += 1
#     st.write(f"카운트 숫자의 증가")
# else:
#     st.write(f"카운트 stays at {counter}")

# Session상태 조건문
if "counter" not in st.session_state:
    st.session_state.counter = 0

# 조건문의 실행내용 앞/ 뒤에 위치한 변수값 다르게 표현된다.
# st.session_state.counter += 1 : 코드 이전의 내용을
# "증가" 버튼을 최초 1회 누르면 여기값은 `0` 을 그대로 유지 
# 이후 추가로 "증가" 버튼을 누르면 전체가 재실행 되어서 `1`로 증가
st.write(f"Counter value: {st.session_state.counter}")

if st.button("증가"):
    st.session_state.counter += 1
    st.write(f"Counter 증가 {st.session_state.counter}")

if st.button("리셋"):
    st.session_state.counter = 0
# else:
#     st.write(f"Count 가 리셋되지 않았습니다.")

st.write(f"Counter 값 : {st.session_state.counter}")