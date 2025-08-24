import streamlit as st
import pandas as pd

st.title("Streamlit Element Demo")

# DataFrame 활용하기
st.subheader("DataFrame 일반")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 37, 42, 32],
    'Occupation':['엔지니어', '의사', '예술가','요리사']
})
st.dataframe(df)

# Static Table 영역
st.subheader('Static Table : 정적인 테이블')
st.table(df)

# DataFrame 편집영역
st.subheader("Data 수정가능")
editable_df = st.data_editor(df)

# Metrics 영역 : 결과값 출력
st.subheader('Metrics')
st.metric(label="총합", value=len(df))
st.metric(label="평균", value=round(df['Age'].mean(), 1))

# JSON and Dict Section
st.subheader('JSON 과 Dictionary')
sample_dict = {
    'name': 'Alice',
    'age': 24,
    'skill': ['Python', 'Nginx', 'ML']
}
st.json(sample_dict)
sample_dict
st.write("Dictionary 데이터 :", sample_dict)