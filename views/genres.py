from flask_restx import Resource, Namespace

from constants import genre_service, genres_schema, genre_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        if not genre:
            return 'NotFound', 404
        return genre_schema.dump(genre), 200
