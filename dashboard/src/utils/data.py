import jikanpy
import requests
import streamlit as st
import pandas as pd

JIKAN = jikanpy.Jikan()

MAL_API_BASE_URL = "https://api.myanimelist.net/v2"
MAL_API_SECRET = st.secrets['KEYS']["MAL_API_SECRET"]
MAL_API_ID = st.secrets['KEYS']["MAL_API_ID"]

def get_user_data(mal_id, mal_username):
    jikan = jikanpy.Jikan()
    user_data = jikan.user(username=mal_username, request='profile')
    return user_data

def get_user_animelist(mal_username, limit=1000):
    req = requests.get(f"{MAL_API_BASE_URL}/users/{mal_username}/animelist?limit={limit}", \
        headers={"X-MAL-CLIENT-ID": MAL_API_ID, "client_secret": MAL_API_SECRET})
    data = req.json()['data']
    data = [x['node'] for x in data]
    st.session_state.animelist_length = len(data)
    return data

def get_full_anime_info(anime_id):
    jikan = jikanpy.Jikan()
    anime = jikan.anime(anime_id)['data']
    return anime

def get_anime_data(anime):
    d = {}
    
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
    aired_dict['aired'] = aired_data['from'] # iso format (from datetime import datetime)
    aired_dict['release_year'] = aired_data['from']['prop']['from']['year']
    aired_dict['end'] = aired_data['to'] if aired_data['to'] else "Movie"
    d['release_date'] = aired_dict
    
    
    return d

# @st.cache_data
# def load_data():
#     # Simulate an expensive computation
#     url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
#     return pd.read_csv(url)