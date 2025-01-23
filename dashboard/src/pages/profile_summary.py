import streamlit as st
import time
import random
from src.utils.profile_summary_data import get_user_animelist, get_anime_data, get_full_anime_info
from src.utils.dashboard_visualizations import genre_wordcloud, genre_bar_chart
from src.utils.profile_summary_helpers import profile_summary_reset
import pandas as pd

# Variables
run_every = 1.5

# init State Handler
state_handler = st.session_state.state_handler


st.title("Profile Summary")
placeholder = st.empty()
loader_placeholder = st.empty()
df_placeholder = st.empty()
barchart_genre_container = st.empty()
wordcloud_genre_container = st.empty()
    


# Update visualizations    
@st.fragment(run_every=run_every)
def update_visualizations():    
    if st.session_state.anime_data is not None:
        with df_placeholder.container():
            st.dataframe(st.session_state.anime_data)
        with barchart_genre_container.container():
            st.bar_chart(genre_bar_chart())
            
        with wordcloud_genre_container.container():
            st.pyplot(genre_wordcloud())
        
    
    
    
reset_button = st.button("Reset", on_click=profile_summary_reset)    
    
    
st.write(f"Run every {run_every} seconds")
update_visualizations()