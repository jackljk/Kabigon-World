import streamlit as st
from src.utils.sidebar import create_sidebar
from src.utils.state_variables import DataStateHandler, initialize_state_variables
from src.utils.profile_summary_data import _update_data_profile_sum

path = "src/pages/"

# define pages
pages = {
    "": [st.Page(f"{path}home.py", title="Home", icon="🏠")],
    "Tools": [
        st.Page(f"{path}profile_summary.py", title="Profile Summary", icon="📊"),
        st.Page(f"{path}anime_analytics.py", title="Anime Analytics", icon="🎭"),
        st.Page(f"{path}recommender.py", title="Recommender", icon="🔍"),
    ],
    "Resources": [
        st.Page(f"{path}settings.py", title="Settings", icon="⚙️"),
    ],
    " ": [st.Page(f"{path}test.py", title="test")],
}

# Sidebar navigation
pg = st.navigation(pages)


# initialize state variables
if st.session_state.get("state_vars_initialized", False) == False:
    initialize_state_variables()

# init State Handler
state_handler = DataStateHandler()
# save to session state
st.session_state.state_handler = state_handler


# Sidebar data input
st.sidebar.title("Data Input")
create_sidebar()

# Background processes
_update_data_profile_sum()


# Run the app
pg.run()
