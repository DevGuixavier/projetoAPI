from flask import Flask
from config import create_app
from Alunos.alunos_routes import aluno_bp
from Turma.turma_routes import turma_bp
from Professor.professor_routes import professor_bp

app = create_app()

# Registrando Blueprints
app.register_blueprint(aluno_bp, url_prefix='/alunos')
app.register_blueprint(turma_bp, url_prefix='/turmas')
app.register_blueprint(professor_bp, url_prefix='/professores')

if __name__ == '__main__':
    app.run()
