from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicialização do banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa a extensão do banco de dados com a aplicação
    db.init_app(app)

    # Importa e registra o blueprint de professores
    from .professor_routes import professor_bp
    app.register_blueprint(professor_bp)

    # Criação do banco de dados (opcional)
    with app.app_context():
        db.create_all()

    return app