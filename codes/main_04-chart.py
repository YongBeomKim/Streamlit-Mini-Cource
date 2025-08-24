import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('차트 그리기')
chart_data = pd.DataFrame(
    np.random.randn(20, 3,),
    columns=['A', "B", "C"]
) # chart_data

# Charts
st.subheader('Area 차트')
st.area_chart(chart_data)

st.subheader('Bar 차트')
st.bar_chart(chart_data)

st.subheader('Line 차트')
st.line_chart(chart_data)

# 산점도 그리기
st.subheader('Scatter 차트')
scatter_data = pd.DataFrame({
    'x': np.random.randn(100,),
    'y': np.random.randn(100),
})
st.scatter_chart(scatter_data)

# 지도 그리기
st.subheader('Map 활용하기')
map_data = pd.DataFrame(
    np.random.rand(100,2)/ [50, 50] + [37.574187,126.976882],
    columns=["lat", "lon"]
)
st.map(map_data)

# matplotlib 엔진을 활용하여 그리기
st.subheader('Pyplot Chart')
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title('Pyplot Line Chart')
ax.legend()
st.pyplot(fig)