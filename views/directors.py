from flask_restx import Resource, Namespace

from constants import director_service, directors_schema, director_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_all()), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        if not director:
            return 'NotFound', 404
        return director_schema.dump(director), 200
