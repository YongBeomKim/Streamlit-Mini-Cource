import os
import streamlit as st

# .write 이외의 기타 화면에 객체출력
st.title("간단한 예시 Site")
st.header("Header 영역")
st.subheader("SubHeader 영역")
st.markdown("""# Title\n## This is Markdown\n _Markdown_""")
st.caption('small text')
st.divider() # Horizon Bar

code_example = """
def test(a:str, b:str) -> str:
    return a + b
"""
st.code(code_example, language='python')
st.divider() # Horizon Bar

st.image(
    os.path.join(os.getcwd(), 'static', 'screen_01.jpg'), 
    width=350
)