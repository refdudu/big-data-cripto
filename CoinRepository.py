from tables_model import coins_table
from database import conn
from sqlalchemy import desc
from Coin import Coin


class CoinRepository:

    def create_many(self, coins):
        for coin in coins:
            # query_coins = coins_table.insert().values(coin)

            query_coins = coins_table.insert().values(
                coin_id=coin['id'],
                current_price=coin['current_price'],
                created_at=coin['last_updated'],
                high_24h=coin['high_24h'],
                low_24h=coin['low_24h']
            )
            conn.execute(query_coins)
        conn.commit()
        return coins

    def get(self):
        query = conn.execute(coins_table.select())
        results = query.fetchall()
        conn.commit()

        coins = []
        for row in results:
            coin = Coin.RowToCoin(row)
            coins.append(coin)
        return coins    

    def get_last_update_coin(self, coin_id):
        query = (coins_table.select()
                            .where(coins_table.c.coin_id == coin_id)
                            .order_by(desc(coins_table.c.created_at))
                            .limit(1))
        row = conn.execute(query).fetchone()
        conn.commit()
        if row:
            return Coin.RowToCoin(row)              
