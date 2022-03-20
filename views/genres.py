from flask import request
from flask_restx import Resource, Namespace
from models import Genre
from setup_db import db
from models import gen_schemas, gen_schema

gen_ns = Namespace('genres')


@gen_ns.route('/')
class GView(Resource):
    def get(self):
        genre = db.session.query(Genre).all()
        if genre is None:
            return {}, 404
        return gen_schemas.dump(genre), 200

    def post(self):
        rj = request.json
        new_note = Genre(**rj)
        with db.session.begin():
            db.session.add(new_note)
        return "", 201


# Реализация методов GET, PUT, DELETE для жанра c ID
@gen_ns.route('/<int:uid>')
class GenView(Resource):
    def get(self, uid: int):
        genre = db.session.query(Genre).filter(Genre.id == uid).first()
        if genre is None:
            return {}, 404
        return gen_schema.dump(genre), 200

    # обновление по идентификатору
    def put(self, uid: int):
        note = Genre.query.get(uid)
        if not note:
            return "", 404
        rj = request.json
        if "name" in rj:
            note.name = rj.get("name")
        db.session.add(note)
        db.session.commit()
        return "", 204

    # удалить данные с соответсвующим id
    def delete(self, uid: int):
        note = Genre.query.get(uid)
        if not note:
            return "", 404
        db.session.delete(note)
        db.session.commit()
        return "", 204
