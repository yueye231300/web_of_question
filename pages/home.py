import streamlit as st

st.header('这里是刷题网站的主页')
chapter = st.selectbox("数学科目选择", ('高数', '线代', '概率论'))
if chapter == '高数':
    selection = st.selectbox('章节选择', ('第一节', '第二节'))
    st.write(f'你选择的科目是{chapter},选择的章节是{selection}')
if chapter == '线代':
    selection = st.selectbox('章节选择', ('第一节', '第二节'))
    st.write(f'你选择的科目是{chapter},选择的章节是{selection}')
if chapter == '概率论':
    selection = st.selectbox('章节选择', ('第一节', '第二节'))
    st.write(f'你选择的科目是{chapter},选择的章节是{selection}')







