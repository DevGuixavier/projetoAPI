from flask import Blueprint, request, jsonify
from .turma_model import TurmaNaoEncontrada, listar_turmas, turma_por_id, adicionar_turma, atualizar_turma, excluir_turma

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/turmas', methods=['GET'])
def listar_todas_turmas():
    return jsonify(listar_turmas()), 200

@turma_bp.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    try:
        turma = turma_por_id(id)
        return jsonify(turma), 200
    except TurmaNaoEncontrada:
        return jsonify({'error': 'Turma não encontrada'}), 404

@turma_bp.route('/turmas', methods=['POST'])
def adicionar_nova_turma():
    dados = request.get_json()
    
    # Validação básica dos dados
    if not dados or 'descricao' not in dados or 'professor_id' not in dados:
        return jsonify({'error': 'Dados inválidos. Certifique-se de incluir descrição e professor_id.'}), 400

    adicionar_turma(dados)
    return jsonify({'message': 'Turma adicionada com sucesso!'}), 201

@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma_existente(id):
    dados = request.get_json()
    
    # Validação básica dos dados
    if not dados or 'descricao' not in dados or 'professor_id' not in dados:
        return jsonify({'error': 'Dados inválidos. Certifique-se de incluir descrição e professor_id.'}), 400

    try:
        atualizar_turma(id, dados)
        return jsonify({'message': 'Turma atualizada com sucesso!'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'error': 'Turma não encontrada'}), 404

@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
def excluir_turma_existente(id):
    try:
        excluir_turma(id)
        return jsonify({'message': 'Turma excluída com sucesso!'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'error': 'Turma não encontrada'}), 404
