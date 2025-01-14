import streamlit as st
import pandas as pd
from src.utils.data import get_full_anime_info, get_anime_data


def initialize_state_variables():
    # initializing session state variables
    st.session_state.animelist_length = 0
    st.session_state.jikan_counter = 0

    st.session_state.anime_data = None
    st.session_state.dashboard_genre_data = pd.DataFrame(columns=['genre', 'count', '_id'])
    st.session_state.dashboard_themes_data = pd.DataFrame(columns=['theme', 'count', '_id'])
    st.session_state.aired_data = pd.DataFrame(columns=['release_date', 'release_year' '_id'])
    
    
class DataStateHandler:
    def __init__(self, *args):
        self.session_state_dfs = {
            'genre': "dashboard_genre_data",
            'theme': "dashboard_themes_data"
        }
    
    def update_anime(self, anime_id):
        """
            Functiont update all dataframes with a new row from jikan api
        """
        # Get the full anime info
        anime = get_full_anime_info(anime_id)
        
        # Get the catergorical data
        data = get_anime_data(anime)
        print(data)
        # update the catergorical state dfs
        self.update_categorical_counter_df(data['genres'], 'genre', anime_id)
        self.update_categorical_counter_df(data['themes'], 'theme', anime_id)
        
    def update_categorical_counter_df(self, data, variable_name, anime_id):
        """
            Updates the state variable dashboard_{variable_name}_data with the given data
        """
        curr_df = st.session_state[self.session_state_dfs[variable_name]]

        for item in data:
            if item in curr_df[variable_name].values:
                curr_df.loc[curr_df[variable_name] == item, 'count'] += 1
            else:
                new_row = {variable_name: item, 'count': 1, '_id': anime_id}
                curr_df = pd.concat([curr_df, pd.DataFrame([new_row])], ignore_index=True)
                
        st.session_state[self.session_state_dfs[variable_name]] = curr_df
        
    def update_dashboard_genre_data(self, data):
        """
            Updates the state variable dashboard_genre_data with the given data
        """
        # given a list of genres update the count of each genre in the bar chart
        curr_df = st.session_state.dashboard_genre_data
        
        for genre in data:
            if genre in curr_df['genre'].values:
                curr_df.loc[curr_df['genre'] == genre, 'count'] += 1
            else:
                new_row = {'genre': genre, 'count': 1}
                curr_df = pd.concat([curr_df, pd.DataFrame([new_row])], ignore_index=True)
    