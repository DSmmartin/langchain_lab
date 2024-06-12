""" This module contains functions to fetch movie details from The Movie Database (TMDB).
"""
import os
import sys
import json
import requests
from loguru import logger

API_THEMOVIE_BASE_URL = "https://api.themoviedb.org"
API_THEMOVIE_VERSION = "3"
THEMOVIE_VERSION_URL = f"{API_THEMOVIE_BASE_URL}/{API_THEMOVIE_VERSION}"
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
    url = f"{THEMOVIE_VERSION_URL}/search/movie?" + \
        f"query={parsed_title}" + \
        "&include_adult=false" + \
        "&language=en-US" \
        f"&page={PAGES}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('TMDB_BEARER_TOKEN')}"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.RequestException as e:
        sys.exit(f"Error: {e}")

    if response.status_code != 200:
        sys.exit(f"Error: {response.status_code}")
    try:
        return int(json.loads(response.text)['results'][0]['id'])
    except IndexError as e:
        logger.error(f"Error: {e}")
        return None


def get_movie_details(movie_id: int):
    """
    Fetches and returns details of a movie from The Movie Database (TMDB).

    :param movie_id: The ID of the movie.
    :type movie_id: int
    :return: A dictionary containing the movie details.
    :rtype: dict
    """

    url = f"{THEMOVIE_VERSION_URL}/movie/{str(movie_id)}" + \
        "?append_to_response=genre%2Creviews" + \
        "&language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ.get('TMDB_BEARER_TOKEN', timeout=5)}"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.RequestException as e:
        sys.exit(f"Error: {e}")

    if response.status_code != 200:
        sys.exit(f"Error: {response.status_code}")

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
