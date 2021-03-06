from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    area = db.Column(db.Float)
    populacao = db.Column(db.Float)

    def __init__(self, nome, area, populacao):
        self.nome = nome
        self.area = area
        self.populacao = populacao