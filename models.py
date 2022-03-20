# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)
# Заголовок Location есть в POST на создание сущности

from marshmallow import Schema, fields
from setup_db import db


# 1. модель таблицы с фильмами
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


# 2. сериализация модели
class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


mov_schema = MovieSchema()
mov_schemas = MovieSchema(many=True)


# 1. модель
class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# 2. сериализация модели
class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


dir_schema = DirectorSchema()
dir_schemas = DirectorSchema(many=True)


# 1. модель
class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# 2. сериализация модели
class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


gen_schema = GenreSchema()
gen_schemas = GenreSchema(many=True)
