import streamlit as st

# 定义登出页面功能
def logout():
    st.header('选择你需要刷的题目')
    chapter = st.selectbox("数学科目选择", ('高数', '线代', '概率论'), key='chapter')
    selection = st.slider('章节选择', min_value=1, max_value=36, step=1, key='selection')
    question_type = st.selectbox('题目类型', ['错题', '例题'], key='type')
    if st.button("提交选择"):
        st.session_state.chapter = chapter
        st.session_state.selection = selection
        st.session_state.type = question_type
        st.experimental_rerun()

# 定义登录页面功能
def login():
    st.session_state.chapter = None
    st.session_state.selection = 1
    st.session_state.type = '错题'
    st.experimental_rerun()

# 初始化 session_state
if "chapter" not in st.session_state:
    st.session_state.chapter = None
if "selection" not in st.session_state:
    st.session_state.selection = 1
if "type" not in st.session_state:
    st.session_state.type = "错题"

# 导航页面
def home_page():
    st.title("错题页面")
    st.write(f"当前选择的科目: {st.session_state.chapter}")
    st.write(f"当前选择的章节: {st.session_state.selection}")
    st.write(f"当前题目类型: {st.session_state.type}")

def example_page():
    st.title("例题页面")
    st.write(f"当前选择的科目: {st.session_state.chapter}")
    st.write(f"当前选择的章节: {st.session_state.selection}")
    st.write(f"当前题目类型: {st.session_state.type}")

# 页面导航逻辑
st.title("Request Manager")

# 根据 session_state.type 决定显示哪个页面
if st.session_state.type == '错题':
    home_page()
elif st.session_state.type == '例题':
    example_page()

# 添加一个退出登录的按钮
if st.button("退出登录"):
    login()

