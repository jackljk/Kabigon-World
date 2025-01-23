import streamlit as st
from src.utils.analytics_visualizations import members_line_plot

# state_handler = DataStateHandler()

st.title("Anime Analytics!")
dropdown_container = st.empty()
data_container = st.empty()
graph_container = st.empty()


def handle_data_type():
    """
    Function to handle the data type selection.
    """
    data_type = st.session_state.analytics_display_data
    if data_type == "Top 25 Animes":
        print(st.session_state.analytics_data)
        if not st.session_state.analytics_data['top_25']:
            print('getting data')
            st.session_state.state_handler.get_data_analytics()
            
        with data_container.container():
            st.write(st.session_state.analytics_data["top_25"])
            
        with graph_container.container():
            members_line_plot(st.session_state.analytics_data['top_25'][['timestamp', 'title', 'statistics.members']])
            
        print(st.session_state.analytics_data)
    elif data_type == "Top 25 Mangas":
        with data_container.container():
            st.write("Top 25 Mangas coming soon!")
    else:
        st.error("Invalid data type selected.")



with dropdown_container.container():
    st.selectbox(
        "Select the type of data to display",
        ["Top 25 Animes", "Top 25 Mangas"],
        index=None,  # Default index
        key="analytics_display_data",
    )
handle_data_type()