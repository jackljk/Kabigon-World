import streamlit as st
from src.utils.profile_summary_data import populate_user_data

def _clear_mal_data():
    st.session_state['mal_id'] = ''
    st.session_state['mal_username'] = ''
    
def create_sidebar():
    mal_id = st.sidebar.text_input(
        "Enter MAL ID",
        st.session_state.get("mal_id"),
        placeholder="MAL ID",
        key="mal_id",
    )
    mal_username = st.sidebar.text_input(
        "Enter MAL Username",
        st.session_state.get("mal_username"),
        placeholder="MAL Username",
        key="mal_username",
        on_change=populate_user_data
    )
    clear_mal_data = st.sidebar.button("Clear User Data", on_click=_clear_mal_data)