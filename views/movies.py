# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace
from models import Movie
from setup_db import db
from models import mov_schemas, mov_schema

movie_ns = Namespace('movies')


# Сlass based view (CBV) для обработки запроса:
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        the_query = db.session.query(Movie)  # Movie.query.all()
        # получим аргументы
        args = request.args
        director_id = args.get('director_id')
        if director_id is not None:  # используем их в фильтрах
            the_query = the_query.filter(Movie.director_id == director_id)
        genre_id = args.get('genre_id')
        if genre_id is not None:
            the_query = the_query.filter(Movie.genre_id == genre_id)
        year = args.get('year')
        if year is not None:
            the_query = the_query.filter(Movie.year == year)
        # возвращ. фильмы с определенным условием
        all_movies = the_query.all()  # выполняем запрос типа /movies/?director_id=2&genre_id=4
        return mov_schemas.dump(all_movies), 200

    def post(self):
        the_movie = mov_schema.load(request.json)
        db.session.add(Movie(**the_movie))
        db.session.commit()
        return None, 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        movie = Movie.query.get(uid)
        if movie is None:
            return "", 404
        return mov_schema.dump(movie), 200

    # удалить данные с соответсвующим id
    def delete(self, uid: int):
        note = Movie.query.get(uid)
        if note is None:
            return "", 404
        db.session.delete(note)
        db.session.commit()
        return "", 204

    # обновление по идентификатору
    def put(self, uid: int):
        m = Movie.query.get(uid)
        if m is None:
            return "", 404
        rj = request.json
        if "title" in rj:
            m.title = rj.get("title")
        if "description" in rj:
            m.description = rj.get("description")
        if "trailer" in rj:
            m.trailer = rj.get("trailer")
        if "year" in rj:
            m.year = rj.get("year")
        if "rating" in rj:
            m.rating = rj.get("rating")
        if "genre_id" in rj:
            m.genre_id = rj.get("genre_id")
        if "director_id" in rj:
            m.director_id = rj.get("director_id")
        db.session.add(m)
        db.session.commit()
        return "", 204
