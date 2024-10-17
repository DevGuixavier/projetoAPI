from flask import Flask
from config import db
from alunos.alunos_routes import alunos_blueprint
from professores.professor_routes import professores_blueprint
from turmas.turma_routes import turmas_blueprint

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

# Registrando os blueprints
app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
