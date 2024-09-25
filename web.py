import streamlit as st

if "type" not in st.session_state:
    st.session_state.type = None

types = [None, "错题", "例题"]

def login():
    st.header("登录界面")
    type = st.selectbox("你要做啥样的题捏", types, key="type")

    if st.button("登录"):
        st.session_state.type = type
        st.rerun()


def logout():
    st.session_state.type = None
    st.rerun()


type = st.session_state.type

logout_page = st.Page(logout, title="登出")

highmath_test = st.Page(
    "test_pages/highmath.py",
    title="高数例题习题",
    default=(type == "例题"),
)
mertic_test = st.Page(
    "test_pages/metric.py",
    title="线代例题习题",
    default=(type == "例题"),
)
probability_theory_test = st.Page(
"test_pages/probability_theory.py",
    title="概率论例题习题",
    default=(type == "例题"),
)

highmath_error = st.Page(
    "error_pages/highmath.py",
    title="高数错题习题",
    default=(type == "错题"),
)
mertic_error = st.Page(
    "error_pages/highmath.py",
    title="线代错题习题",
    default=(type == "错题"),
)
probability_theory_error = st.Page(
    "error_pages/highmath.py",
    title="概率论错题习题",
    default=(type == "错题"),
)
account_pages = [logout_page]
request_pages = [highmath_test, mertic_test, probability_theory_test]
respond_pages = [highmath_error, mertic_error, probability_theory_error]

st.title("宝贝的刷题网站")

page_dict = {}
if st.session_state.type in ["例题"]:
    page_dict["练习例题"] = request_pages
if st.session_state.type in ["错题"]:
    page_dict["练习错题"] = respond_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()