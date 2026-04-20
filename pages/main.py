import streamlit as st
from utils.session import get_user, logout

def render():
    user = get_user()

    st.title(f"Bem-vindo, {user['nome']}")

    if st.button("Logout"):
        logout()
        st.rerun()