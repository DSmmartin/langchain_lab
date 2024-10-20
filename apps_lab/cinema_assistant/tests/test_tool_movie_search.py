import pytest
from unittest.mock import patch
from cinema_assistant.custom_tools.tool_movie_search import search_movies, get_search_movies_openai_function

@pytest.fixture
def mock_get_id_movie():
    with patch('cinema_assistant.themovie_api.get_id_movie') as mock:
        yield mock

@pytest.fixture
def mock_get_movie_details():
    with patch('cinema_assistant.themovie_api.get_movie_details') as mock:
        yield mock

def test_search_movies_success(mock_get_id_movie, mock_get_movie_details):
    mock_get_id_movie.return_value = 123
    mock_get_movie_details.return_value = {
        "original_title": "The Lord of the Rings: The Fellowship of the Ring",
        "genres": ["Adventure", "Fantasy", "Action"],
        "reviews": ["Great movie!", "A masterpiece."],
        "release_date": "2001-12-19"
    }

    result = search_movies("The Lord of the Rings")
    assert result == {
        "original_title": "The Lord of the Rings: The Fellowship of the Ring",
        "genres": ["Adventure", "Fantasy", "Action"],
        "reviews": ["Great movie!", "A masterpiece."],
        "release_date": "2001-12-19"
    }

def test_search_movies_no_movie_found(mock_get_id_movie):
    mock_get_id_movie.return_value = None

    result = search_movies("Nonexistent Movie")
    assert result == {"error": "No movie found"}

def test_get_search_movies_openai_function():
    openai_function = get_search_movies_openai_function()
    assert openai_function['name'] == 'search_movies'
    assert openai_function['description'] == 'This is a search tool that allows you to search properties of a movie (release date, genres and some reviews).'
    assert 'parameters' in openai_function
    assert 'query' in openai_function['parameters']['properties']
    assert openai_function['parameters']['properties']['query']['description'] == 'The movie you want to search for'
