import streamlit as st

# .write : 화면에 객체출력
st.write("Hello world 1234")
st.write({"005930": {"name": "삼성전자", "본사": "경기도 수원시"}})

"Terminator 2" # WebPage 출력
title = "Terminator 2"
print(title)   # console 출력

# Button
# 최초값 : False -> Click 을 하면 : True
pressed = st.button("버튼클릭")
if pressed:
    "Run"

pressed2 = st.button("Second Button")
print("Second :", pressed2)
