import streamlit as st
import pandas as pd


def initialize_state_variables():
    # initializing session state variables
    st.session_state.animelist_length = 0
    st.session_state.jikan_counter = 0

    st.session_state.anime_data = None
    st.session_state.dashboard_genre_bar_chart = pd.DataFrame(columns=['genre', 'count'])