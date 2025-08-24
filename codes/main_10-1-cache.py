import streamlit as st
import time

# ttl : 60초 이내에 재 실행시 -> Cache 데이터를 재활용
@st.cache_data(ttl=60)
def fetch_data():
    r"""fetch 작업할 때 Loading 대기시간"""
    time.sleep(3) # 지연시간
    return {'data': 'This is the Cache data'}


st.write('Fetching data ...')
data = fetch_data()
st.write(data)