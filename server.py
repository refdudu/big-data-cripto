from flask import Flask, jsonify
from flask_cors import CORS
import json
from CoinRepository import CoinRepository
from CoinApi import CoinApi

app = Flask(__name__)
CORS(app)

coinRepository = CoinRepository()
coinApi = CoinApi()

@app.get('/')
def get_coins():
    db_coins = coinRepository.get()
    dict_array = []
    for coin in db_coins:
        dict_array.append(coin.to_dict())
    response = {
        "items": dict_array,
        "total": len(dict_array)
    }
    return response


if __name__ == '__main__':
    app.run(debug=True)
