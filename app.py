# основной файл приложения.
# здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.

from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import dir_ns
from views.genres import gen_ns
from views.movies import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(dir_ns)
    api.add_namespace(gen_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
