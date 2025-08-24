import streamlit as st


# sidebar Layout
st.sidebar.title("사이드 Menu")
st.sidebar.write('Button / Text in Here')
sidebar_input = st.sidebar.text_input('아무거나 입력가능')


# Tab Layout
tab1, tab2, tab3 = st.tabs(['Tab1','Tab2','Tab3'])

with tab1:
    st.write('# 탭1 화면 입니다.')

with tab2:
    st.write('# 탭2 화면 입니다.')

with tab3:
    st.write('# 탭3 화면 입니다.')


# Columns Layout
col1, col2, col3 = st.columns(3)
with col1:
    st.header('컬럼 1')
    st.write('Content of 컬럼 1')

with col2:
    st.header('컬럼 2')
    st.write('Content of 컬럼 2')

with col3:
    st.header('컬럼 3')
    st.write('Content of 컬럼 3')


# container 예제
with st.container(border=True):
    st.write('Container 내부의 내용 입니다.')
    st.write('구성요소들을 Grouping 하는데 유용합니다.')


# Empty placeholder
placeholder = st.empty()
placeholder.write('여기는 빈 공백공간 입니다.')

if st.button('placeholder 내용 갱신'):
    placeholder.write('content 가 update 되었습니다.')


# Expander
with st.expander('Expand for more details'):
    st.write('default 는 숨김상태 이지만, 추가정보를 노출한다')


# Pop-over (Tool tip)
st.write("tool tip 기능을 구현 합니다.")
st.button('툴팁 기능이 가능합니다', help="툴팁으로 보여줄 내용 입니다.")


# Sidebar Input 다루기
if sidebar_input:
    st.write(f'사이드바에 내용을 입력한 내용 입니다.')
    st.write(f': {sidebar_input}')