from flask import Blueprint, current_app, request, jsonify
from .model import Pais
from .serializer import pais_schema, paises_schema


bp_paises = Blueprint('paises', __name__)


@bp_paises.route('/')
def index():
    return jsonify({"message": "Bem vindo ao PyIses"})


@bp_paises.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.json['nome']
    area = request.json['area']
    populacao = request.json['populacao']

    novo_pais = Pais(nome, area, populacao)

    current_app.db.session.add(novo_pais)
    current_app.db.session.commit()

    return pais_schema.jsonify(novo_pais), 201


@bp_paises.route('/mostrar', methods=['GET'])
def mostrar():
    paises = Pais.query.all()
    return paises_schema.jsonify(paises), 200

@bp_paises.route('/mostrar/<id>', methods=['GET'])
def mostrar_por_id(id):
    pais = Pais.query.get(id)
    return pais_schema.jsonify(pais), 200

@bp_paises.route('/atualizar/<id>', methods=['PUT'])
def atualizar(id):
    pais = Pais.query.get(id)

    nome = request.json['nome']
    area = request.json['area']
    populacao = request.json['populacao']

    pais.nome = nome
    pais.area = area
    pais.populacao = populacao

    current_app.db.session.add(pais)
    current_app.db.session.commit()

    return pais_schema.jsonify(pais), 201

@bp_paises.route('/deletar/<id>', methods=['DELETE'])
def deletar(id):
    pais = Pais.query.get(id)
    current_app.db.session.delete(pais)
    current_app.db.session.commit()
    return pais_schema.jsonify(pais), 200



