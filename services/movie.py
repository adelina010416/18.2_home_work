from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, data):
        director_id = data.get('director_id')
        genre_id = data.get('genre_id')
        year = data.get('year')

        if director_id:
            return self.dao.get_all_by_director(director_id)
        if genre_id:
            return self.dao.get_all_by_genre(genre_id)
        if year:
            return self.dao.get_all_by_year(year)

        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def update(self, data, mid):
        movie = self.get_one(mid)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        self.dao.update(movie)
        return movie

    def update_partial(self, data, mid):
        movie = self.get_one(mid)
        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.update(movie)
        return movie

    def delete(self, mid):
        return self.dao.delete(mid)
