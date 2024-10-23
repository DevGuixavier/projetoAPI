# turma/__init__.py
from flask import Blueprint

turma_bp = Blueprint('turma', __name__)

# Importar as rotas
from .turma_routes import *
