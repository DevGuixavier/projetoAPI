from flask import Blueprint, request, jsonify
from .Professor_model import ProfessorNaoEncontrado, listar_professores, professor_por_id, adicionar_professor, atualizar_professor, excluir_professor

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(listar_professores())

@professor_bp.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    try:
        professor = professor_por_id(id)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'error': 'Professor não encontrado'}), 404

@professor_bp.route('/professores', methods=['POST'])
def adicionar_novo_professor():
    dados = request.get_json()
    adicionar_professor(dados)
    return jsonify({'message': 'Professor adicionado com sucesso!'}), 201

@professor_bp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor_existente(id):
    dados = request.get_json()
    try:
        atualizar_professor(id, dados)
        return jsonify({'message': 'Professor atualizado com sucesso!'})
    except ProfessorNaoEncontrado:
        return jsonify({'error': 'Professor não encontrado'}), 404

@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
def excluir_professor_existente(id):
    try:
        excluir_professor(id)
        return jsonify({'message': 'Professor excluído com sucesso!'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'error': 'Professor não encontrado'}), 404
