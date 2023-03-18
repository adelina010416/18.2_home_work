from flask import request
from flask_restx import Resource, Namespace

from constants import movie_service, movies_schema, movie_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movies_schema.dump(movie_service.get_all(request.args))
        if not movies:
            return "NotFound", 404
        return movies

    def post(self):
        movie = request.json
        movie_service.create(movie)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_schema.dump(movie_service.get_one(mid))
        if not movie:
            return 'NotFound', 404
        return movie, 200

    def put(self, mid):
        new_data = request.json
        movie_service.update(new_data, mid)
        return "", 200

    def patch(self, mid):
        new_data = request.json
        movie_service.update_partial(new_data, mid)
        return "", 200

    def delete(self, mid):
        movie = movie_service.delete(mid)
        return "", 204
