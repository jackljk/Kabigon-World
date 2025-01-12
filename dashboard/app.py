import streamlit as st
from src.utils.sidebar import update_mal_id, update_mal_username, _clear_mal_data

path = 'src/pages/'

# define pages 
pages = {
     "": [st.Page(f"{path}home.py", title="Home", icon="🏠")],
     "Tools": [
          st.Page(f"{path}profile_summary.py", title="Profile Summary", icon="📊"),
          st.Page(f"{path}recommender.py", title="Recommender", icon="🔍"),
     ],
     "Resources": [
          st.Page(f"{path}settings.py", title="Settings", icon="⚙️"),
     ]
}

# Sidebar navigation
pg = st.navigation(pages)





# Sidebar data input
st.sidebar.title("Data Input")
mal_id = st.sidebar.text_input("Enter MAL ID", st.query_params.get('mal_id'), placeholder="MAL ID", key='mal_id', on_change=update_mal_id)
mal_username = st.sidebar.text_input("Enter MAL Username", st.query_params.get('mal_username'), placeholder="MAL Username", key='mal_username', on_change=update_mal_username)
clear_mal_data = st.sidebar.button("Clear User Data", on_click=_clear_mal_data)


# Run the app
pg.run()
