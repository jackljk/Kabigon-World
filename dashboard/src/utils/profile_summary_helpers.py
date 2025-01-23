import streamlit as st
import pandas as pd

def profile_summary_reset():
    """
        Function to reset the profile summary data
    """
    st.session_state['mal_id'] = ''
    st.session_state['mal_username'] = ''
    st.session_state['anime_data'] = None
    st.session_state['animelist_length'] = 0
    st.session_state['jikan_counter'] = 0
    st.session_state['dashboard_genre_data'] = pd.DataFrame(columns=['genre', 'count', '_id'])
    st.session_state['dashboard_themes_data'] = pd.DataFrame(columns=['theme', 'count', '_id'])
    st.session_state['aired_data'] = pd.DataFrame(columns=['release_date', 'release_year' '_id'])
    print('Profile Summary data reset')