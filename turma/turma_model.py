from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    # Relacionamento com Professor
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)

    # Relacionamento One-to-Many com Aluno
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def __init__(self, descricao, professor_id, ativo=True):
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'professor_id': self.professor_id
        }

class TurmaNaoEncontrada(Exception):
    def __init__(self, id_turma):
        super().__init__(f'Turma com id {id_turma} não encontrada.')

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada(id_turma)
    return turma.to_dict()

def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def adicionar_turma(dados):
    # Validação básica dos dados
    if 'descricao' not in dados or 'professor_id' not in dados:
        raise ValueError('Dados inválidos. Certifique-se de incluir descrição e professor_id.')

    nova_turma = Turma(
        descricao=dados['descricao'],
        professor_id=dados['professor_id'],
        ativo=dados.get('ativo', True)
    )
    db.session.add(nova_turma)
    db.session.commit()

def atualizar_turma(id_turma, novos_dados):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada(id_turma)

    # Validação básica dos dados
    if 'descricao' not in novos_dados or 'professor_id' not in novos_dados:
        raise ValueError('Dados inválidos. Certifique-se de incluir descrição e professor_id.')

    turma.descricao = novos_dados['descricao']
    turma.professor_id = novos_dados['professor_id']
    turma.ativo = novos_dados.get('ativo', True)
    db.session.commit()

def excluir_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada(id_turma)
    db.session.delete(turma)
    db.session.commit()