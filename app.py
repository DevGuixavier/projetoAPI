from flask import Flask
from config import config, create_app
from Alunos.alunos_routes import alunos_bp
from Turma.turma_routes import turma_bp
from Professor.professor_routes import professor_bp

# Criação da aplicação Flask
app = create_app()

# Registrando Blueprints
app.register_blueprint(alunos_bp, url_prefix='/alunos')
app.register_blueprint(turma_bp, url_prefix='/turmas')
app.register_blueprint(professor_bp, url_prefix='/professores')

@app.errorhandler(404)
def not_found(error):
    return {'error': 'Recurso não encontrado'}, 404

@app.errorhandler(500)
def internal_error(error):
    return {'error': 'Erro interno do servidor'}, 500

if __name__ == '__main__':
    # Executa a aplicação em modo de depuração se for o ambiente de desenvolvimento
    app.run(debug=config.DEBUG)