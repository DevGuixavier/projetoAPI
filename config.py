import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialização da base de dados
db = SQLAlchemy()

class Config:
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = True  # Mude para False em produção
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.getcwd(), 'banco.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)

    # Configurações da aplicação a partir da classe Config
    app.config.from_object(Config)

    # Inicializa o banco de dados com a aplicação
    db.init_app(app)

    # Importando e registrando os blueprints
    from Alunos.alunos_routes import alunos_bp
    from Professor.professor_routes import professor_bp
    from Turma.turma_routes import turma_bp

    app.register_blueprint(alunos_bp, url_prefix='/api/alunos')
    app.register_blueprint(professor_bp, url_prefix='/api/professores')
    app.register_blueprint(turma_bp, url_prefix='/api/turmas')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
