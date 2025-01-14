import pandas as pd
import streamlit as st
import wordcloud
import matplotlib.pyplot as plt


def genre_bar_chart():
    """
    No special barcharts edits for now so returning df
    """
    return st.session_state.dashboard_genre_data.set_index("genre")


def genre_wordcloud():
    df = st.session_state.dashboard_genre_data

    # create text which is all the genres repeated by their count
    text = ""
    
    # Get the current theme's background color
    background_color = st.get_option("theme.backgroundColor")
    print(background_color)

    for index, row in df.iterrows():
        text += (row["genre"] + " ") * row["count"]
    wc = wordcloud.WordCloud(
        width=800, height=400, max_words=500, background_color=background_color, collocations=False, regexp=r'\S+'
    ).generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")

    return fig
