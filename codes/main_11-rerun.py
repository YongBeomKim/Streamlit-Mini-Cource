import streamlit as st

st.title('Counter 예제를 즉시 재실행 하기')

if "count" not in st.session_state:
    st.session_state.count = 0


def increase_and_return():
    st.session_state.count += 1
    st.rerun()


# Count 값이 먼저 화면에 노출 후, increase_and_return() 실행
# : 최초 1회 실행시, 뒤에 있는 함수값은 화면에 영향을 안준다
# : 이처럼 불가피하게 실행함수가 뒤에 있을 땐, `st.rerun()` 으로
# : 강제 재실행 명령을 
st.write(f'Current Count: {st.session_state.count}')

if st.button("숫자의 증가와 즉시 Update"):
    increase_and_return()