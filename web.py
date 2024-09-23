# package setting
import streamlit as st

if "chapter" in st.session_state:
    st.session_state.chapter = st.session_state.chapter
if "selection" in st.session_state:
    st.session_state.selection = st.session_state.selection
if "type" in st.session_state:
    st.session_state.type = st.session_state.type
st.header('这里是刷题网站的主页')

chapter = st.selectbox("数学科目选择", ('高数', '线代', '概率论'), key='chapter')
selection = st.slider('章节选择', min_value=1, max_value=36, step=1, key='selection')
type = st.selectbox('题目类型', ['错题', '例题'], key='type')

st.Page("pages/home.py",title="home")