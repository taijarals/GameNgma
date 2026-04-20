import streamlit as st
from utils.session import is_logged
from pages import login, main

st.set_page_config(page_title="Enigma Game")

def run():
    if not is_logged():
        login.render()
    else:
        main.render()

if __name__ == "__main__":
    run()