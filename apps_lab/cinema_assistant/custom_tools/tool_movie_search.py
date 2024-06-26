"""Tools for searching movies using the TheMovieDB API.
"""
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.agents import tool
from langchain.tools.render import format_tool_to_openai_function
from cinema_assistant.themovie_api import get_id_movie, get_movie_details


class MovieSearch(BaseModel):
    """This is a search tool that allows you to search properties of a movie (release date, genres and some reviews)."""
    query: str = Field(description="The movie you want to search for")


@tool(args_schema=MovieSearch)
def search_movies(query: str):
    """This is a search tool that allows you to search properties of a movie (release date, genres and some reviews)."""
    movie_id = get_id_movie(query)
    return get_movie_details(movie_id) if movie_id else {"error": "No movie found"}


def get_search_movies_openai_function():
    """This function is used to format the search_movies tool to be used in OpenAI API."""
    return format_tool_to_openai_function(search_movies)
