from flask import Blueprint, request, jsonify
from .alunos_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno
from config import db

# Corrigido o nome do blueprint para 'alunos_bp'
alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/', methods=['GET'])  # Ajustado para usar a rota base
def get_alunos():
    return jsonify(listar_alunos())

@alunos_bp.route('/<int:id_aluno>', methods=['GET'])  # Ajustado para usar a rota base
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado as e:
        return jsonify({'message': str(e)}), 404

@alunos_bp.route('/', methods=['POST'])  # Ajustado para usar a rota base
def create_aluno():
    data = request.json
    
    # Validação dos dados recebidos
    required_fields = ['nome', 'idade', 'turma', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Dados inválidos. É necessário fornecer {field}.'}), 400

    if data['idade'] < 0:
        return jsonify({'message': 'A idade deve ser um número positivo.'}), 400
    if not (0 <= data['nota_primeiro_semestre'] <= 10):
        return jsonify({'message': 'A nota do primeiro semestre deve estar entre 0 e 10.'}), 400
    if not (0 <= data['nota_segundo_semestre'] <= 10):
        return jsonify({'message': 'A nota do segundo semestre deve estar entre 0 e 10.'}), 400

    try:
        novo_aluno = adicionar_aluno(data)  # Certifique-se de que essa função retorna o novo aluno
        return jsonify(novo_aluno), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@alunos_bp.route('/<int:id_aluno>', methods=['PUT'])  # Ajustado para usar a rota base
def update_aluno(id_aluno):
    data = request.json
    
    # Validação dos dados recebidos
    if not data:
        return jsonify({'message': 'Dados inválidos. É necessário fornecer dados para atualização.'}), 400

    try:
        atualizar_aluno(id_aluno, data)
        return jsonify(aluno_por_id(id_aluno))
    except AlunoNaoEncontrado as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@alunos_bp.route('/<int:id_aluno>', methods=['DELETE'])  # Ajustado para usar a rota base
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return '', 204
    except AlunoNaoEncontrado as e:
        return jsonify({'message': str(e)}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500