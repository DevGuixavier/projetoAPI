from flask import Blueprint, request, jsonify
from .alunos_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno

aluno_bp = Blueprint('alunos', __name__)

@aluno_bp.route('/alunos', methods=['GET'])
def listar_todos_alunos():
    return jsonify(listar_alunos())

@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    try:
        aluno = aluno_por_id(id)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404

@aluno_bp.route('/alunos', methods=['POST'])
def adicionar_novo_aluno():
    dados = request.get_json()
    adicionar_aluno(dados)
    return jsonify({'message': 'Aluno adicionado com sucesso!'}), 201

@aluno_bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno_existente(id):
    dados = request.get_json()
    try:
        atualizar_aluno(id, dados)
        return jsonify({'message': 'Aluno atualizado com sucesso!'})
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404

@aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])
def excluir_aluno_existente(id):
    try:
        excluir_aluno(id)
        return jsonify({'message': 'Aluno excluído com sucesso!'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404
