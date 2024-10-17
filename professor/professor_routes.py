from flask import Blueprint, jsonify, request
from .professor_model import Professor
from config import db

professores_blueprint = Blueprint('professores', __name__)

# Listar todos os professores
@professores_blueprint.route('/professores', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professores])

# Buscar professor por ID
@professores_blueprint.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404
    return jsonify(professor.to_dict())

# Criar novo professor
@professores_blueprint.route('/professores', methods=['POST'])
def criar_professor():
    data = request.json
    novo_professor = Professor(
        nome=data['nome'],
        idade=data['idade'],
        materia=data['materia'],
        observacoes=data.get('observacoes')
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify(novo_professor.to_dict()), 201

# Atualizar professor
@professores_blueprint.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404
    
    data = request.json
    professor.nome = data.get('nome', professor.nome)
    professor.idade = data.get('idade', professor.idade)
    professor.materia = data.get('materia', professor.materia)
    professor.observacoes = data.get('observacoes', professor.observacoes)

    db.session.commit()
    return jsonify(professor.to_dict())

# Deletar professor
@professores_blueprint.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 404
    
    db.session.delete(professor)
    db.session.commit()
    return jsonify({'message': 'Professor excluído com sucesso'})
