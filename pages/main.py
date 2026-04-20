import streamlit as st
from utils.session import get_user, logout

def render():
    user = get_user()

    if not user:
        st.error("Usuário não encontrado")
        return

    nick = user.get("nick", "Usuário")

    st.title(f"Bem-vindo, {nick}")

    if st.button("Logout"):
        logout()
        st.rerun()