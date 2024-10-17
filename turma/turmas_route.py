from flask import Blueprint, jsonify, request
from .turma_model import Turma
from config import db

turmas_blueprint = Blueprint('turmas', __name__)

# Listar todas as turmas
@turmas_blueprint.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([turma.to_dict() for turma in turmas])

# Buscar turma por ID
@turmas_blueprint.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({'message': 'Turma não encontrada'}), 404
    return jsonify(turma.to_dict())

# Criar nova turma
@turmas_blueprint.route('/turmas', methods=['POST'])
def criar_turma():
    data = request.json
    nova_turma = Turma(
        descricao=data['descricao'],
        professor_id=data['professor_id']
    )
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify(nova_turma.to_dict()), 201

# Atualizar turma
@turmas_blueprint.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({'message': 'Turma não encontrada'}), 404
    
    data = request.json
    turma.descricao = data.get('descricao', turma.descricao)
    turma.professor_id = data.get('professor_id', turma.professor_id)
    
    db.session.commit()
    return jsonify(turma.to_dict())

# Deletar turma
@turmas_blueprint.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({'message': 'Turma não encontrada'}), 404
    
    db.session.delete(turma)
    db.session.commit()
    return jsonify({'message': 'Turma excluída com sucesso'})
