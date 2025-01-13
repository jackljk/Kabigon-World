import streamlit as st
import time
import random
from src.utils.data import get_user_animelist, get_anime_genre_data, get_full_anime_info
from src.utils.dashboard_visualizations import update_genre_bar_chart
import pandas as pd

st.title("Profile Summary")
placeholder = st.empty()
loader_placeholder = st.empty()
chart_container = st.empty()

# Fetch and display data if a username is entered
if "mal_username" in st.session_state and st.session_state["mal_username"]:
    with placeholder.container():
        with st.spinner("Fetching data..."):
            time.sleep(1)
            data = get_user_animelist(st.session_state["mal_username"])
        try:
            df = pd.DataFrame(data)

            # Display the results
            st.write(f"Displaying data for {st.session_state['mal_username']}")
            st.write(f"Total entries: {st.session_state.animelist_length}")
            st.dataframe(df)
            st.session_state.anime_data = df
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a valid MAL username to see the profile summary.")
    

    
if st.session_state.jikan_counter > 10 or st.session_state.animelist_length < st.session_state.jikan_counter: # number variables to be changed
    run_every = None
else:
    run_every = 1.5
    
# Update visualizations    
@st.fragment(run_every=run_every)
def update_visualizations():    
    # get new data
    anime = get_full_anime_info(st.session_state.anime_data.iloc[st.session_state.jikan_counter]['id'])
    genre_data = get_anime_genre_data(anime)
    
    with chart_container.container():
        update_genre_bar_chart(genre_data)
        st.bar_chart(st.session_state.dashboard_genre_bar_chart.set_index('genre'))
        
        
    st.session_state.jikan_counter += 1

st.write(f"Run every {run_every} seconds")
update_visualizations()