import streamlit as st

if "chapter" in st.session_state:
    st.session_state.chapter = st.session_state.chapter
if "selection" in st.session_state:
    st.session_state.selection = st.session_state.selection
if "type" in st.session_state:
    st.session_state.type = st.session_state.type

st.markdown('**你输入的文字是**')
st.write(st.session_state.selection)





