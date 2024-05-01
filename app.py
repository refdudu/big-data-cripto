from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import requests
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    coins = get_coins()
    return coins


def get_coins():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'brl',
        'ids': 'dogecoin,bitcoin,ethereum',
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

class CoinRepository:
    def __init__(self):
        self.coins = parametro1
    
if __name__ == '__main__':
    app.run(debug=True)