import os
import json
import requests

API_THEMOVIE_BASE_URL = "https://api.themoviedb.org"
API_THEMOVIE_VERSION = "3"
PAGES = 1


def get_id_movie(film_title: str):
    """
    Fetches and returns the ID of a movie from The Movie Database (TMDB).

    :param film_title: The title of the movie.
    :type film_title: str
    :return: The ID of the movie.
    :rtype: int
    """

    parsed_title = film_title.replace(" ", "%20")
    url = f"{API_THEMOVIE_BASE_URL}/{API_THEMOVIE_VERSION}/search/movie?query={parsed_title}&include_adult=false&language=en-US&page={PAGES}"

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
        return int(json.loads(response.text)['results'][0]['id'])
    except IndexError as e:
        return None


def get_movie_details(movie_id: int):
    """
    Fetches and returns details of a movie from The Movie Database (TMDB).

    :param movie_id: The ID of the movie.
    :type movie_id: int
    :return: A dictionary containing the movie details. The keys are 'original_title', 'genres', 'reviews', and 'release_date'.
    :rtype: dict
    """

    url = f"{API_THEMOVIE_BASE_URL}/{API_THEMOVIE_VERSION}/movie/{str(movie_id)}?append_to_response=genre%2Creviews&language=en-US"
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

    response = json.loads(response.text)
    original_title = response['original_title']
    genres = [genre['name'] for genre in response['genres']]
    reviews = [review['content'] for review in response['reviews']['results']]

    return {
        "original_title": original_title,
        "genres": genres,
        "reviews": reviews,
        "release_date": response['release_date']
    }
