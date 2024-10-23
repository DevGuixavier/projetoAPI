import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialização da base de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações da aplicação
    app.config['HOST'] = '0.0.0.0'
    app.config['PORT'] = 8000
    app.config['DEBUG'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados com a aplicação
    db.init_app(app)

    # Importando e registrando os blueprints
    from Alunos.alunos_routes import aluno_bp
    from Professor.professor_routes import professor_bp
    from Turma.turma_routes import turma_bp

    app.register_blueprint(aluno_bp, url_prefix='/api')
    app.register_blueprint(professor_bp, url_prefix='/api')
    app.register_blueprint(turma_bp, url_prefix='/api')

    return app
