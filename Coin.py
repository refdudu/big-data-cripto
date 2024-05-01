from app import db

class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    variacao = db.Column(db.Float, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Coin {self.nome}>'