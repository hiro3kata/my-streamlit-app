import streamlit as st

st.title("はじめてのStreamlitアプリ")
st.write("こんにちは！これはアクアと一緒に作ったStreamlitアプリだよ💧")

name = st.text_input("お名前を入力してね")
if name:
    st.success(f"{name}さん、ようこそ！")
