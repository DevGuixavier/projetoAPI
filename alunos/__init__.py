from flask import Blueprint

# Criação do Blueprint
alunos_bp = Blueprint('aluno', __name__)

# Importar as rotas
from .alunos_routes import alunos_blueprint

# Registrar o blueprint das rotas no blueprint principal
alunos_bp.register_blueprint(alunos_blueprint)

# Se necessário, você também pode importar os modelos aqui
from .alunos_model import Aluno  # Importando o modelo Aluno