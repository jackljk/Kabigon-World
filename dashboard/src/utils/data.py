import jikanpy

def get_user_data(mal_id, mal_username):
    jikan = jikanpy.Jikan()
    user_data = jikan.user(username=mal_username, request='profile')
    return user_data