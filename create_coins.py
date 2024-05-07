from CoinRepository import CoinRepository
from CoinApi import CoinApi
from time import sleep
from datetime import datetime, timedelta
import json

coinRepository = CoinRepository()
coinApi = CoinApi()


def create_coins():
    print("create_coins", datetime.now())
    coins = coinApi.get()
    coin = coins[0]
    last_coin = coinRepository.get_last_update_coin(coin["id"])
    if last_coin:
        last_update = datetime.strptime(
            coin['last_updated'], "%Y-%m-%dT%H:%M:%S.%fZ")
        if (last_coin.is_valid_date(last_update)):
            coinRepository.create_many(coins)
        else:
            print(
                "A data da atualização das moedas não foi alterada ainda")
    sleep(300)  # 5min
    create_coins()


create_coins()
