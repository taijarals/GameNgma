import streamlit as st

def set_user(user):
    st.session_state["user"] = user

def get_user():
    return st.session_state.get("user")

def is_logged():
    return "user" in st.session_state

def logout():
    st.session_state.clear()