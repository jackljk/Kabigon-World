import pandas as pd
import streamlit as st



def update_genre_bar_chart(data):
    # given a list of genres update the count of each genre in the bar chart
    curr_df = st.session_state.dashboard_genre_bar_chart
    
    for genre in data:
        if genre in curr_df['genre'].values:
            curr_df.loc[curr_df['genre'] == genre, 'count'] += 1
        else:
            new_row = {'genre': genre, 'count': 1}
            curr_df = pd.concat([curr_df, pd.DataFrame([new_row])], ignore_index=True)
    
    st.session_state.dashboard_genre_bar_chart = curr_df