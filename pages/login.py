import streamlit as st
from services.auth_service import login_user, register_user, get_user_full
from utils.session import set_user

def render():
    st.title("Acesso")

    aba = st.radio("Escolha uma opção", ["Login", "Cadastro"])

    # =========================
    # LOGIN
    # =========================
    if aba == "Login":
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            user = login_user(email, senha)

            if user:
                user_full = get_user_full(user)  # 🔥 NOVO
                set_user(user_full)

                st.success("Login realizado!")
                st.rerun()
            else:
                st.error("Email ou senha inválidos")

    # =========================
    # CADASTRO
    # =========================
    else:
        email = st.text_input("Email", key="cad_email")
        senha = st.text_input("Senha", type="password", key="cad_senha")
        nick = st.text_input("Nick", key="cad_nick")

        if st.button("Cadastrar"):
            user = register_user(email, senha, nick)

            if user:
                user_full = get_user_full(user)  # 🔥 NOVO
                set_user(user_full)

                st.success("Cadastro realizado!")
                st.rerun()
            else:
                st.error("Erro ao cadastrar usuário")