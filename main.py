import streamlit as st
import pandas as pd
import numpy as np


def intro():
    r"""안내 메세지"""
    st.title('환영합니다.')
    st.write("""
        소개하는 페이지 입니다. 다양한 기능들을 활용해 보세요
    """)


def plotting_demo():
    r"""chart 구성요소"""
    st.title('Plotting Demo')
    st.write('간단한 simple plot 을 구현해 보겠습니다.')

    # random 데이터
    chart_data = pd.DataFrame(
        np.random.randn(50, 3), 
        columns=["A","B","C"]
    )
    st.line_chart(chart_data)


def mapping_demo():
    r"""지도 데이터 그리기"""
    st.title('지도 데이터 예시')
    st.write('광화문 지역 지도를 그립니다.')
    map_data = pd.DataFrame(
        np.random.rand(100,2)/ [50, 50] + [37.574187,126.976882],
        columns=["lat", "lon"]
    )
    st.map(map_data)


def data_frame_demo():
    df = pd.DataFrame(
        np.random.randn(20, 3,),
        columns=['A', "B", "C"]
    ) # chart_data
    st.dataframe(df)


# Dictionary 를 활용하여 페이지 구성요소 관리
page_names_to_funcs = {
    "-": intro,
    "차트그리기": plotting_demo,
    '지도': mapping_demo,
    '테이블': data_frame_demo
}


# Sidebar 에서 Navigation
selected_page = st.sidebar.selectbox(
    "페이지를 선택하세요",
    options=page_names_to_funcs.keys(),
)

# Selected 페이지 내용을 실행
page_names_to_funcs[selected_page]()