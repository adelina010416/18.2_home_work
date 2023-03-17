from flask import request
from flask_restx import Resource, Namespace

from my_models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        movies = Movie.query
        if director_id:
            movies = movies.filter(Movie.director_id == director_id)
        if genre_id:
            movies = movies.filter(Movie.genre_id == genre_id)
        if year:
            movies = movies.filter(Movie.year == year)

        result = MovieSchema(many=True).dump(movies.all())
        if not result:
            return "NotFound", 404
        return result

    def post(self):
        movie = request.json
        result = Movie(**movie)
        db.session.add(result)
        db.session.commit()
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = Movie.query.get(mid)
        if not movie:
            return 'NotFound', 404
        result = MovieSchema().dump(movie)
        return result, 200

    def put(self, mid):
        movie = Movie.query.get(mid)
        new_data = request.json
        if not movie:
            return 'NotFound', 404

        movie.title = new_data['title']
        movie.description = new_data['description']
        movie.trailer = new_data['trailer']
        movie.year = new_data['year']
        movie.rating = new_data['rating']
        movie.genre_id = new_data['genre_id']
        movie.director_id = new_data['director_id']

        db.session.add(movie)
        db.session.commit()
        return "", 200

    def delete(self, mid):
        movie = Movie.query.get(mid)
        if not movie:
            return 'NotFound', 404
        db.session.delete(movie)
        db.session.commit()
        return "", 204
