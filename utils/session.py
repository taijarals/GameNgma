import streamlit as st

def set_user(user):
    st.session_state["user"] = user

def get_user():
    return st.session_state.get("user")

def is_logged():
    return st.session_state.get("user") is not None

def logout():
    if "user" in st.session_state:
        del st.session_state["user"]