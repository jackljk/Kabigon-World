import streamlit as st


st.title("Home Page")
st.write(st.session_state.mal_id if 'mal_id' in st.session_state else '')
st.write(st.session_state.mal_username if 'mal_username' in st.session_state else '')