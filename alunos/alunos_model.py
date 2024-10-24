from config import db
from datetime import date

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    turma = db.Column(db.String(20))
    data_nascimento = db.Column(db.Date)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)

    def __init__(self, nome, idade, turma, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = self.calcular_media_final()

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma': self.turma,
            'data_nascimento': self.data_nascimento.isoformat(),
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final
        }

    def calcular_media_final(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

class AlunoNaoEncontrado(Exception):
    def __init__(self, id_aluno):
        self.id_aluno = id_aluno
        super().__init__(f"Aluno com ID {id_aluno} não encontrado.")

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(id_aluno)
    return aluno.to_dict()

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def adicionar_aluno(aluno_data):
    # Validação de dados
    if aluno_data['idade'] < 0:
        raise ValueError("A idade deve ser um número positivo.")
    if not (0 <= aluno_data['nota_primeiro_semestre'] <= 10):
        raise ValueError("A nota do primeiro semestre deve estar entre 0 e 10.")
    if not (0 <= aluno_data['nota_segundo_semestre'] <= 10):
        raise ValueError("A nota do segundo semestre deve estar entre 0 e 10.")

    data_nascimento = date.fromisoformat(aluno_data['data_nascimento'])

    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        idade=aluno_data['idade'],
        turma=aluno_data['turma'],
        data_nascimento=data_nascimento,
        nota_primeiro_semestre=aluno_data['nota_primeiro_semestre'],
        nota_segundo_semestre=aluno_data['nota_segundo_semestre']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return novo_aluno.to_dict()

def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(id_aluno)

    # Atualização parcial
    if 'nome' in novos_dados:
        aluno.nome = novos_dados['nome']
    if 'idade' in novos_dados:
        aluno.idade = novos_dados['idade']
    if 'turma' in novos_dados:
        aluno.turma = novos_dados['turma']
    if 'data_nascimento' in novos_dados:
        aluno.data_nascimento = date.fromisoformat(novos_dados['data_nascimento'])
    if 'nota_primeiro_semestre' in novos_dados:
        aluno.nota_primeiro_semestre = novos_dados['nota_primeiro_semestre']
    if 'nota_segundo_semestre' in novos_dados:
        aluno.nota_segundo_semestre = novos_dados['nota_segundo_semestre']
    aluno.media_final = aluno.calcular_media_final()

    db.session.commit()
    return aluno.to_dict()

def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(id_aluno)
    db.session.delete(aluno)
    db.session.commit()