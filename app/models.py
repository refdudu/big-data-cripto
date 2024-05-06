# from app import db
# import datetime

# class Coin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(100), nullable=False)
#     variations = db.relationship('CoinVariation', backref='coin', lazy=True)

#     def __repr__(self):
#         return f'<Coin {self.nome}>'

# class CoinVariation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     coin_id = db.Column(db.Integer, db.ForeignKey('coin.id'), nullable=False)
#     variacao = db.Column(db.Float, nullable=False)
#     preco = db.Column(db.Float, nullable=False)
#     data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
#     def __repr__(self):
#         return f'<CoinVariation {self.variacao}>'
from __init__ import db



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title