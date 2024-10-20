import pytest
from unittest.mock import patch
from cinema_assistant.custom_tools import search_movies, get_search_movies_openai_function

@patch('cinema_assistant.custom_tools.tool_movie_search.get_id_movie')
@patch('cinema_assistant.custom_tools.tool_movie_search.get_movie_details')
def test_search_movies(mock_get_movie_details, mock_get_id_movie):
    # Test when movie is found
    mock_get_id_movie.return_value = 123
    mock_get_movie_details.return_value = {"title": "Test Movie", "genres": ["Action", "Adventure"]}
    result = search_movies("Test Movie")
    assert result == {"title": "Test Movie", "genres": ["Action", "Adventure"]}
    
    # Test when movie is not found
    mock_get_id_movie.return_value = None
    result = search_movies("Unknown Movie")
    assert result == {"error": "No movie found"}

def test_get_search_movies_openai_function():
    openai_function = get_search_movies_openai_function()
    assert openai_function['name'] == 'search_movies'
    assert 'description' in openai_function
    assert 'parameters' in openai_function
