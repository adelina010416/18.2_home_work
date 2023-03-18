from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.models.directors import DirectorSchema
from dao.models.genres import GenreSchema
from dao.models.movies import MovieSchema
from dao.movie_dao import MovieDAO
from services.director import DirectorService
from services.genre import GenreService
from services.movie import MovieService
from setup_db import db

# подключение к ДАО
movie_dao = MovieDAO(db.session)
genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)

# подключение сервисов
movie_service = MovieService(movie_dao)
genre_service = GenreService(genre_dao)
director_service = DirectorService(director_dao)

# подключение схем для сериализации
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

