from flask import Flask, jsonify
from flask_migrate import Migrate
from .model import db, configure as config_db
from .serializer import configure as config_ma
import os

# criando factory
def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))

    #configuração sqlalchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pyises.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .paises import bp_paises
    app.register_blueprint(bp_paises)

    return app
