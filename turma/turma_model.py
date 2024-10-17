from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    # Relacionamento com Professor
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)

    # Relacionamento One-to-Many com Aluno
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'professor': self.professor.nome if self.professor else None,
            'alunos': [aluno.nome for aluno in self.alunos]
        }
