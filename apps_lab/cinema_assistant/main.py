from loguru import logger
from utils import get_id_movie


movie_name = "The Lord of the Rings The Fellowship of the Ring"
movie_id = get_id_movie(movie_name)
logger.info(f"Movie ID: {movie_id} from Movie Name: {movie_name}")