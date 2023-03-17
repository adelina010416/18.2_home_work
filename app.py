from flask_restx import Api
from config import Config
from flask import Flask
from setup_db import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns


# функция создания основного объекта app
def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    configure_app(application)
    return application


# функция подключения расширений
def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
