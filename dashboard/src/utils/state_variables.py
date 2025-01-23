import streamlit as st
import pandas as pd
from src.utils.profile_summary_data import get_full_anime_info, get_anime_data
from src.utils.analytics_data import get_analytics_data


def initialize_state_variables():
    # Profile Summary User Data
    st.session_state.mal_username = None
    st.session_state.mal_id = None
    # Profile Summary Counters
    st.session_state.animelist_length = 0
    st.session_state.jikan_counter = 0
    # Profile Summary data
    st.session_state.anime_data = None
    st.session_state.dashboard_genre_data = pd.DataFrame(columns=['genre', 'count', '_id'])
    st.session_state.dashboard_themes_data = pd.DataFrame(columns=['theme', 'count', '_id'])
    st.session_state.aired_data = pd.DataFrame(columns=['release_date', 'release_year' '_id'])
    
    # Anime Analytics data
    st.session_state.analytics_data = {"top_25": None}
    
    # Variable to tell the app that the state variables have been initialized
    st.session_state.state_vars_initialized = True
    print("State variables initialized")
    
    
class DataStateHandler:
    def __init__(self, *args):
        self.session_state_dfs = {
            'genre': "dashboard_genre_data",
            'theme': "dashboard_themes_data",
            "aired": "aired_data",
            "analytics": "analytics_data"
        }
    
    def update_data_profile_sum(self, anime_id):
        """
            Function to update all dataframes with a new row from jikan api
        """
        # Get the full anime info
        anime = get_full_anime_info(anime_id)
        
        # Get the catergorical data
        data = get_anime_data(anime)
        print(data)
        # update the catergorical state dfs
        self._update_state_var_profile_sum(data['genres'], 'genre', anime_id)
        self._update_state_var_profile_sum(data['themes'], 'theme', anime_id)
        
    def reset_data_profile_sum(self):
        """
            Function to reset the profile summary data
        """
        st.session_state[self.session_state_dfs['genre']] = pd.DataFrame(columns=['genre', 'count', '_id'])
        st.session_state[self.session_state_dfs['theme']] = pd.DataFrame(columns=['theme', 'count', '_id'])
        st.session_state[self.session_state_dfs['aired']] = pd.DataFrame(columns=['release_date', 'release_year' '_id'])
        
    def get_data_analytics(self):
        """
            Function to get the analytics data
        """
        data_dict = get_analytics_data()
        
        # update the state variable
        st.session_state[self.session_state_dfs['analytics']]['top_25'] = data_dict['top_25']
        
        
    def _update_state_var_profile_sum(self, data, variable_name, anime_id):
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
    