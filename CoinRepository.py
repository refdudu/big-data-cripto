from tables_model import coins_table
from database import conn
from sqlalchemy import desc
from Coin import Coin


class CoinRepository:

    def create_many(self, coins):
        for coin in coins:
            query_coins = coins_table.insert().values(
                coin_id=coin['id'],
                current_price=coin['current_price'],
                created_at=coin['last_updated'],
            )
            conn.execute(query_coins)
        conn.commit()
        return coins

    def get(self):
        query = conn.execute(coins_table.select())
        results = query.fetchall()
        coins = []
        for row in results:
            coin = Coin(_id=row[0], coin_id=row[1],
                        current_price=row[2], created_at=row[3])
            coins.append(coin)
        return coins

    def get_last_update_coin(self, coin_id):
        query = (coins_table.select()
                            .where(coins_table.c.coin_id==coin_id)
                            .order_by(desc(coins_table.c.created_at))
                            .limit(1))
        row = conn.execute(query).fetchone()
        if (row):
            coin = Coin(_id=row[0], coin_id=row[1],
                        current_price=row[2], created_at=row[3])
            return coin
