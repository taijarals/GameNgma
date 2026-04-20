import streamlit as st
from services.auth_service import login_user
from utils.session import set_user

def render():
    st.title("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        user = login_user(email, senha)

        if user:
            set_user(user)
            st.rerun()  # recarrega e vai pro main
        else:
            st.error("Credenciais inválidas")