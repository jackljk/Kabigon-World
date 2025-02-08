import requests

def get_top_data(**kwargs):
    url = "https://api.jikan.moe/v4/top/anime"
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Return the JSON content (a dict) instead of the response object.
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching data from Jikan API: {str(e)}")
