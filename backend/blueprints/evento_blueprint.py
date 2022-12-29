from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.evento import EventoModel
from backend.infrastructure.evento_repository import EventoRepository

evento_blueprint = Blueprint('evento_blueprint', __name__)

repo = EventoRepository()

@evento_blueprint.route('/api/evento/create', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def create_evento():
    print("antes")
    
    #content = repo.create(
    #    id_ponente = 2,
    #    nombre = request.form['evento_nombre'],
    #    detalles = request.form['evento_detalles'],
    #    link = request.form['evento_link'],
    #)
    content = repo.create(request.json['id_ponente'],request.json['nombre'],request.json['detalles'],request.json['link'])
    print(content)
    return jsonify(content)

@evento_blueprint.route('/api/evento/get', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def get_evento():
    content = repo.get(
        int(request.json['id'])
    )    
    return jsonify(content)

@evento_blueprint.route('/api/evento/get_all', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def get_all_evento():
    content = repo.get_all() 
    return jsonify(content)

@evento_blueprint.route('/api/evento/delete', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def delete_evento():
    content = repo.delete(
        int(request.json['id'])
    )    
    return jsonify(content)


#branch diego

@evento_blueprint.route('/api/evento/delete', methods=['POST']) # Ruta accesible por POST
@cross_origin()
def delete_evento():
    content = repo.delete(
        int(request.json['id'])
    )    
    return jsonify(content)
