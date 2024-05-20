import os
import json
import requests

API_THEMOVIE_BASE_URL = "https://api.themoviedb.org"
PAGES = 1

def get_id_movie(film_title: str):
    parsed_title = film_title.replace(" ", "%20")
    url = f"{API_THEMOVIE_BASE_URL}/3/search/movie?query={parsed_title}&include_adult=false&language=en-US&page={PAGES}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('TMDB_BEARER_TOKEN')}"
    }
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        exit(f"Error: {e}")

    if response.status_code != 200:
        exit(f"Error: {response.status_code}")
    try:
        return json.loads(response.text)['results'][0]['id']
    except IndexError as e:
        return None
