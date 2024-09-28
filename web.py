import streamlit as st

if "type" not in st.session_state:
    st.session_state.type = None

types = [None, "错题", "例题"]


def login():
    st.header("登录界面")
    type = st.selectbox("你要做啥样的题捏", types)

    if st.button("登录"):
        st.session_state.type = type
        st.rerun()


def logout():
    st.session_state.type = None
    st.rerun()


type = st.session_state.type

logout_page = st.Page(logout, title="登出")

test_pages = st.Page(
    "test_pages/test_pages.py",
    title="例题习题",
    default=(type == "例题"),
)
test_random = st.Page(
    "test_pages/test_random.py",
    title="随机练习"
)


error_pages = st.Page(
    "error_pages/error_pages.py",
    title="错题习题",
    default=(type == "错题"),
)
error_random = st.Page(
    "error_pages/error_random.py",
    title="随机错题练习",
)


account_pages = [logout_page]
request_pages = [test_pages, test_random]
respond_pages = [error_pages, error_random]

st.title("刷题网站")

page_dict = {}
if st.session_state.type == "例题":
    page_dict["练习例题"] = request_pages
if st.session_state.type == "错题":
    page_dict["练习错题"] = respond_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
