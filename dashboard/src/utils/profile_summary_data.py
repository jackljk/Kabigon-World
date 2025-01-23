import jikanpy
import requests
import streamlit as st
import pandas as pd
import time

JIKAN = jikanpy.Jikan()

MAL_API_BASE_URL = "https://api.myanimelist.net/v2"
MAL_API_SECRET = st.secrets['KEYS']["MAL_API_SECRET"]
MAL_API_ID = st.secrets['KEYS']["MAL_API_ID"]

@st.fragment(run_every=1.5)
def _update_data_profile_sum():
    """
        Function to update all dataframes with a new row from jikan api
    """
    if st.session_state.anime_data is not None and st.session_state.jikan_counter < st.session_state.animelist_length:
        st.session_state.state_handler.update_data_profile_sum(st.session_state.anime_data.iloc[st.session_state.jikan_counter]['id'])
        st.session_state.jikan_counter += 1


def populate_user_data():
    """
        Function to populate the user data
    """
    if st.session_state.mal_username is not None or st.session_state.mal_username != '':
        st.session_state.state_handler.reset_data_profile_sum()
        data = get_user_animelist(st.session_state["mal_username"])
        st.session_state.anime_data = pd.DataFrame(data)
    
        print('New data loaded')
    else:
        print('No username provided')

def get_user_data(mal_id, mal_username):
    jikan = jikanpy.Jikan()
    user_data = jikan.user(username=mal_username, request='profile')
    return user_data

def get_user_animelist(mal_username, limit=1000):
    try:
        req = requests.get(f"{MAL_API_BASE_URL}/users/{mal_username}/animelist?limit={limit}", \
            headers={"X-MAL-CLIENT-ID": MAL_API_ID, "client_secret": MAL_API_SECRET})
        data = req.json()['data']
        data = [x['node'] for x in data]
        st.session_state.animelist_length = len(data)
        return data
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

def get_full_anime_info(anime_id):
    jikan = jikanpy.Jikan()
    anime = jikan.anime(anime_id)['data']
    return anime

def get_anime_data(anime):
    d = {}
    print(anime.keys())
    # genres
    genre_data = anime['genres']
    genre_names = [x['name'] for x in genre_data]
    d['genres'] = genre_names
    
    # themes
    theme_data = anime['themes']
    theme_names = [x['name'] for x in theme_data if x['name'] is not None]
    d['themes'] = theme_names
    
    # aired dates (release date and end date)
    aired_data = anime['aired']
    aired_dict = {}
    aired_dict['aired_date'] = aired_data['from'] # iso format (from datetime import datetime)
    aired_dict['release_year'] = aired_data['prop']['from']['year']
    aired_dict['end'] = aired_data['to'] if aired_data['to'] else "Movie"
    d['release_date'] = aired_dict
    
    
    return d
