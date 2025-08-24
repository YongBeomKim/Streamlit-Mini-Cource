import streamlit as st

file_path = 'example.txt'


# 내용의 일 부분만 추가/ 삭제 활용될 때
@st.cache_resource
def get_file_handler(file_path:str):
    file = open(file_path, "a+")
    return file


# Cache file handler 를 사용한다
file_handler = get_file_handler(file_path)

# Cached handler 를 활용하여 문장을 file 에 추가한다 
if st.button("File 에 문장 추가하기"):
    file_handler.write('새롭게 추가할 Text\n')
    file_handler.flush()
    st.success("새로운 Line 의 문장이 추가 되었습니다.")

# File 의 내용을 출력
if st.button(f"{file_path} 내용보기"):
    file_handler.seek(0)
    content = file_handler.read()
    st.text(content)

# File 내용 닫기
st.button('File 닫기', on_click=file_handler.close)