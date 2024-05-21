from loguru import logger
from utils import get_id_movie, get_movie_details


movie_name = "The Lord of the Rings The Fellowship of the Ring"
movie_id = get_id_movie(movie_name)
logger.info(f"Movie ID: {movie_id} from Movie Name: {movie_name}")

logger.info(f"Getting movie details for movie ID: {movie_id}")
movie_details = get_movie_details(movie_id)
print(movie_details)

logger.info("End of the program.")
