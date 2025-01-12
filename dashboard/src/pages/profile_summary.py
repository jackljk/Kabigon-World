import streamlit as st
import time
import random

# Cached function to fetch data
@st.cache_data(ttl=5)  # Cache expires after 5 seconds
def fetch_data():
    time.sleep(2)  # Simulate a delay (e.g., fetching from API)
    return random.randint(1, 100)

st.title("Profile Summary")
placeholder = st.empty()

# while True:
#     # Fetch the cached data
#     data = fetch_data()
#     with placeholder.container():
#         st.write(f"Data: {data}")

#     # Sleep for the refresh interval
#     time.sleep(5)

