from flask import Flask
from flask_cors import CORS
from CoinRepository import CoinRepository
from CoinApi import CoinApi

app = Flask(__name__)
CORS(app)

coinRepository = CoinRepository()
coinApi = CoinApi()


@app.get('/')
def get_coins():
    db_coins = coinRepository.get()
    dict_array = [coin.to_dict() for coin in db_coins]
    return {"items": dict_array, "total": len(dict_array)}


if __name__ == '__main__':
    app.run(debug=True)
