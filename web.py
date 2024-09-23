# package setting
import streamlit as st



def logout():
    st.header('选择你自己需要刷的题目')
    chapter = st.selectbox("数学科目选择", ('高数', '线代', '概率论'), key='chapter')
    selection = st.slider('章节选择', min_value=1, max_value=36, step=1, key='selection',)
    type = st.selectbox('题目类型', ['错题', '例题'], key='type')
    if st.button("提交选择"):
        st.session_state.chapter = chapter
        st.session_state.selection = selection
        st.session_state.type = type
        st.rerun()

def login():
    st.session_state.chapter = None
    st.session_state.selection = 1
    st.session_state.type = None
    st.rerun()

if "chapter" in st.session_state:
    st.session_state.chapter = st.session_state.chapter
if "selection" in st.session_state:
    st.session_state.selection = st.session_state.selection
if "type" in st.session_state:
    st.session_state.type = st.session_state.type


logout_page = st.Page(login, title="Log out", icon=":material/logout:")
home = st.Page(
    "pages/home.py",
    title="home",
    icon=":material/help:",
    default=(type == '错题')
)
test = st.Page("pages/test.py",
    title='test',
    icon=":material/help:"
)
account_pages = [logout_page]
# 导航页面
st.title("Request manager")
page_dict = {}
if st.session_state.type == '错题':
    page_dict["Request"] = home
if st.session_state.type == '例题':
    page_dict["Respond"] = test

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)

else:
    pg = st.navigation([st.Page(login)])

pg.run()