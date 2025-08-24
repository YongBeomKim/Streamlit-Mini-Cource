import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

def go_to_step_02(name):
    r"""2 Step 페이지 실행 전 Callback 함수
    Callback : 다음단계 실행 직전에 미리실행 - 상태관리"""
    st.session_state.info['name'] = name
    st.session_state.step = 2

def go_to_step_01():
    r"""1 Step 페이지 실행 복귀시 Callback 함수
    :: 단계만 이동 - session 값은 그대로 보관"""
    st.session_state.step = 1


# 첫번째 단계
if st.session_state.step == 1:
    st.header("Part 1: Info")
    name = st.text_input('이름', 
        value=st.session_state.info.get("name", "")
    )
    st.button('다음',on_click=go_to_step_02, args=(name,))


# 두번째 단계
if st.session_state.step == 2:
    st.header("Part 2: 리뷰")

    st.subheader("입력값 확인:")
    st.write(f"**이름**: {st.session_state.info.get('name', '')}")

    if st.button("확인"):
        st.success("검토완료")
        st.balloons()
        st.session_state.info = {}
    
    st.button('이전', on_click=go_to_step_01)

st.session_state