from config import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100))
    observacoes = db.Column(db.Text)

    # Relacionamento One-to-Many com Turma
    turmas = db.relationship('Turma', backref='professor', lazy=True)

    def __init__(self, nome, idade, materia, observacoes=None):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'observacoes': self.observacoes
        }

class ProfessorNaoEncontrado(Exception):
    def __init__(self, id_professor):
        self.id_professor = id_professor
        super().__init__(f"Professor com ID {id_professor} não encontrado.")

def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado(id_professor)
    return professor.to_dict()

def listar_professores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def adicionar_professor(dados):
    if dados['idade'] < 0:
        raise ValueError("A idade deve ser um número positivo.")
    
    novo_professor = Professor(
        nome=dados['nome'],
        idade=dados['idade'],
        materia=dados['materia'],
        observacoes=dados.get('observacoes')
    )
    
    try:
        db.session.add(novo_professor)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Erro ao adicionar professor: {str(e)}")

def atualizar_professor(id_professor, novos_dados):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado(id_professor)

    if 'nome' in novos_dados:
        professor.nome = novos_dados['nome']
    if 'idade' in novos_dados:
        if novos_dados['idade'] < 0:
            raise ValueError("A idade deve ser um número positivo.")
        professor.idade = novos_dados['idade']
    if 'materia' in novos_dados:
        professor.materia = novos_dados['materia']
    if 'observacoes' in novos_dados:
        professor.observacoes = novos_dados.get('observacoes')

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Erro ao atualizar professor: {str(e)}")

def excluir_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado(id_professor)
    
    try:
        db.session.delete(professor)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Erro ao excluir professor: {str(e)}")
