import streamlit as st

if "chapter" in st.session_state:
    st.session_state.chapter = None
if "selection" in st.session_state:
    st.session_state.selection = st.session_state.selection
if "type" in st.session_state:
    st.session_state.type = st.session_state.type

st.markdown('**你输入的文字是**')






