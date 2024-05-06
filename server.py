from flask import Flask, jsonify
from database import conn
import requests
from tables_model import coins_table
import json
from datetime import datetime, timedelta
from sqlalchemy import desc

app = Flask(__name__)


class CoinsRepository:

    def get(self):
        query = conn.execute(coins_table.select())
        results = query.fetchall()
        coins = []
        for row in results:
            coin = Coin(_id=row[0], coin_id=row[1], current_price=row[2], created_at=row[3])
            coins.append(coin)
        return coins

    def get_last_update_coin(self):
        row = conn.execute(coins_table.select().order_by(desc(coins_table.c.created_at)).limit(1)).fetchone()
        if(row):
            coin = Coin(_id=row[0], coin_id=row[1], current_price=row[2], created_at=row[3])
            return coin


class Coin:

    def __init__(self, _id, coin_id, current_price, created_at):
        self.id = _id
        self.coin_id = coin_id
        self.current_price = current_price
        self.created_at = created_at

    def to_dict(self):
        return {
        'coin_id': self.coin_id,
        'current_price': self.current_price,
        'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'id': self.id,
        }

    def passed_five_minutes(self):
        now = datetime.utcnow()
        return self.created_at < now + timedelta(minutes=10)

    def is_valid_date(self, date):
        return self.created_at < date


coinsRepository = CoinsRepository()


def create_coins(coins):
    for coin in coins:
        query_coins = coins_table.insert().values(
                    coin_id=coin['id'],
                    current_price=coin['current_price'],
                    created_at=coin['last_updated'],
                )
        conn.execute(query_coins)
    conn.commit()
    return coins


def mock_fetch_coins():
    with open('coin.json', 'r') as f:
        # Carregar os dados do arquivo JSON
        dados = json.load(f)
        json_formatado = json.dumps(dados, indent=4)
        return json.loads(json_formatado)
        return jsonify(json.loads(json_formatado))


def fetch_coins():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'brl',
        'ids': 'dogecoin,bitcoin,ethereum',
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


fetch = fetch_coins


@app.get('/')
def get_coins():
    last_coin = coinsRepository.get_last_update_coin()
    if last_coin:
        if(last_coin.passed_five_minutes()):
            coins = fetch()
            coin = coins[0]
            last_update = datetime.strptime(coin['last_updated'], "%Y-%m-%dT%H:%M:%S.%fZ")
            if(last_coin.is_valid_date(last_update)):
                create_coins(coins)  
            else:
                print("A data da atualização das moedas não foi alterada ainda", last_update)      
        else:
            print("Não passou 5 minutos", last_coin.created_at)      
    else:
        coins = fetch()
        create_coins(coins)
        
    db_coins = coinsRepository.get()
    dict_array = []
    for coin in db_coins:
        dict_array.append(coin.to_dict())
    response = {
        "itens": dict_array,
        "total": len(dict_array)
    }
    return response


if __name__ == '__main__':
    app.run(debug=True)
