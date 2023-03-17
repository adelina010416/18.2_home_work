from flask_restx import Resource, Namespace

from my_models import Genre, GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        directors = Genre.query.all()
        result = GenreSchema(many=True).dump(directors)
        return result, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = Genre.query.get(gid)
        if not genre:
            return 'NotFound', 404
        result = GenreSchema().dump(genre)
        return result, 200