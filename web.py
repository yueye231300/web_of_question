# package setting
import streamlit as st

st.header('这里是刷题网站的主页')
with st.form('数学章节选择'):
    st.subheader('**选择你的数学科目和章节**')

    # Input widgets
    chapter = st.selectbox("数学科目选择", ('高数', '线代', '概率论'), key='chapter')
    selection = st.slider('章节选择', min_value=1, max_value=36, step=1, key='selection')
    type = st.selectbox('题目类型', ['错题', '例题'], key='type')
    # Every form must have a submit button
    submitted = st.form_submit_button('提交你的选择')

if submitted:
    st.markdown(f'''
        你选择的题目类型是
        - 课程类型: `{chapter}`
        - 章节: `{selection}`
        - 类型: `{type}`
        你的刷题网页在下方可以找到
        ''')
    # if chapter == '高数':
    #     chapter = 'math'
    # if chapter == '线代':
    #     chapter = 'metric'
    # if chapter == '概率论':
    #     chapter = 'probability'
    st.page_link('pages/home.py')
else:
    st.write('☝️ Place your order!')
