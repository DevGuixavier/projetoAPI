from flask import Blueprint, request, jsonify
from .turma_model import TurmaNaoEncontrada, listar_turmas, turma_por_id, adicionar_turma, atualizar_turma, excluir_turma

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('/turmas', methods=['GET'])
def listar_todas_turmas():
    return jsonify(listar_turmas())

@turma_bp.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    try:
        turma = turma_por_id(id)
        return jsonify(turma)
    except TurmaNaoEncontrada:
        return jsonify({'error': 'Turma não encontrada'}), 404

@turma_bp.route('/turmas', methods=['POST'])
def adicionar_nova_turma():
    dados = request.get_json()
    adicionar_turma(dados)
    return jsonify({'message': 'Turma adicionada com sucesso!'}), 201

@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma_existente(id):
    dados = request.get_json()
    try:
        atualizar_turma(id, dados)
        return jsonify({'message': 'Turma atualizada com sucesso!'})
    except TurmaNaoEncontrada:
        return jsonify({'error': 'Turma não encontrada'}), 404

@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
def excluir_turma_existente(id):
    try:
        excluir_turma(id)
        return jsonify({'message': 'Turma excluída com sucesso!'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'error': 'Turma não encontrada'}), 404
