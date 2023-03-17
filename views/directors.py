from flask_restx import Resource, Namespace

from my_models import Director, DirectorSchema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = Director.query.all()
        result = DirectorSchema(many=True).dump(directors)
        return result, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = Director.query.get(did)
        if not director:
            return 'NotFound', 404
        result = DirectorSchema().dump(director)
        return result, 200
