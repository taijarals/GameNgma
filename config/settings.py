import streamlit as st

class Settings:
    SUPABASE_URL = st.secrets["SUPABASE_URL"].replace("/rest/v1", "")
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

settings = Settings()