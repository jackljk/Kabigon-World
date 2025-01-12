import streamlit as st

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


def update_mal_id():
    st.session_state['mal_id'] = st.session_state.mal_id_input

def update_mal_username():
    st.session_state['mal_username'] = st.session_state.mal_username_input

# Initialize session state variables if they don't exist
if 'mal_id' not in st.session_state:
    st.session_state['mal_id'] = ''
if 'mal_username' not in st.session_state:
    st.session_state['mal_username'] = ''

# Sidebar data input
st.sidebar.title("Data Input")
mal_id = st.sidebar.text_input("Enter MAL ID", value=st.session_state['mal_id'], placeholder="MAL ID", key='mal_id_input', on_change=update_mal_id)
mal_username = st.sidebar.text_input("Enter MAL Username", value=st.session_state['mal_username'], placeholder="MAL Username", key='mal_username_input', on_change=update_mal_username)



# Run the app
pg.run()
