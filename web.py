import streamlit as st

if "type" not in st.session_state:
    st.session_state.type = None

types = [None, "错题", "例题"]

def login():

    st.header("登录界面")
    role = st.selectbox("你要做啥样的题捏", types, key="type")

    if st.button("登录"):
        st.session_state.type = type
        st.rerun()


def logout():
    st.session_state.type = None
    st.rerun()


type = st.session_state.type

logout_page = st.Page(logout, title="登出")

test = st.Page(
    "pages/test.py",
    title="练习习题",
    default=(type == "例题"),
)
error = st.Page(
    "pages/error.py", title="练习错题"
)

account_pages = [logout_page]
request_pages = [test, error]


st.title("Request manager")

page_dict = {}
if st.session_state.type in ["错题"]:
    page_dict["练习例题"] = test
if st.session_state.role in ["例题"]:
    page_dict["练习错题"] = error


if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()