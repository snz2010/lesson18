from flask import request
from flask_restx import Resource, Namespace
from models import Director
from setup_db import db
from models import dir_schemas, dir_schema

dir_ns = Namespace('directors')


@dir_ns.route('/')
class DView(Resource):
    def get(self):
        director = db.session.query(Director).all()
        if director is None:
            return {}, 404
        return dir_schemas.dump(director), 200

    def post(self):
        rj = request.json
        new_note = Director(**rj)
        with db.session.begin():
            db.session.add(new_note)
        return "", 201


# реализаця GET, PUT, DELETE для режиссера c ID
@dir_ns.route('/<int:uid>')
class DirView(Resource):
    def get(self, uid: int):
        director = db.session.query(Director).filter(Director.id == uid).first()
        if director is None:
            return {}, 404
        return dir_schema.dump(director), 200

    # обновление по идентификатору
    def put(self, uid: int):
        note = Director.query.get(uid)
        if note is None:
            return "", 404
        rj = request.json
        if "name" in rj:
            note.name = rj.get("name")
        db.session.add(note)
        db.session.commit()
        return "", 204

    # удалить данные с соответсвующим id
    def delete(self, uid: int):
        note = Director.query.get(uid)
        if not note:
            return "", 404
        db.session.delete(note)
        db.session.commit()
        return "", 204
