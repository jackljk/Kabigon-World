import streamlit as st


def update_mal_id():
    st.query_params['mal_id'] = st.session_state.mal_id

def update_mal_username():
    st.query_params['mal_username'] = st.session_state.mal_username
    
def _clear_mal_data():
    st.query_params['mal_id'] = ''
    st.query_params['mal_username'] = ''