from flask import Blueprint, request, jsonify
from .Professor_model import (ProfessorNaoEncontrado, listar_professores as listar_professores_model, professor_por_id, adicionar_professor, atualizar_professor, excluir_professor)

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('/professores', methods=['GET'])
def listar_professores_route():
    professores = listar_professores_model()
    return jsonify(professores), 200

@professor_bp.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    try:
        professor = professor_por_id(id)
        return jsonify(professor), 200
    except ProfessorNaoEncontrado:
        return jsonify({'error': 'Professor não encontrado'}), 404

@professor_bp.route('/professores', methods=['POST'])
def adicionar_novo_professor():
    dados = request.get_json()
    
    # Validação básica dos dados
    if not dados or 'nome' not in dados or 'idade' not in dados or 'materia' not in dados:
        return jsonify({'error': 'Dados inválidos. Certifique-se de incluir nome, idade e matéria.'}), 400

    try:
        adicionar_professor(dados)
        return jsonify({'message': 'Professor adicionado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@professor_bp.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor_existente(id):
    dados = request.get_json()
    
    # Validação básica dos dados
    if not dados:
        return jsonify({'error': 'Dados inválidos. Certifique-se de incluir pelo menos um campo a ser atualizado.'}), 400

    try:
        atualizar_professor(id, dados)
        return jsonify({'message': 'Professor atualizado com sucesso!'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'error': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
def excluir_professor_existente(id):
    try:
        excluir_professor(id)
        return jsonify({'message': 'Professor excluído com sucesso!'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'error': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500