import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def members_line_plot(data):
    """
    Function to create a line plot of the differences in members data over time.
    """
    st.write("Change in Members Over Time Plot")

    # Ensure timestamp is in datetime format
    data['timestamp'] = pd.to_datetime(data['timestamp'])

    # Calculate the difference in 'statistics.members' for each anime
    data['members_diff'] = data.groupby('title')['statistics.members'].diff()
    
    # sort by timestamp
    data.sort_values(by='timestamp', inplace=True)

    # Create the Plotly line plot
    fig = px.line(
        data,
        x='timestamp',
        y='members_diff',
        color='title',
        title="Change in Members Over Time by Anime",
        labels={
            "timestamp": "Timestamp",
            "members_diff": "Change in Members",
            "title": "Anime Title"
        },
    )

    # Add grid lines and improve interactivity
    fig.update_layout(
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        hovermode="x unified"
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    
    