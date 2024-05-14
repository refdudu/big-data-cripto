

class Coin:

    def __init__(self, _id, coin_id, current_price, high24h, low24h, created_at, previous_price):
        self.id = _id
        self.coin_id = coin_id
        self.current_price = current_price
        self.high24h = high24h
        self.low24h = low24h
        self.created_at = created_at
        self.previous_price = previous_price

    @staticmethod
    def RowToCoin(row):
        return Coin(_id=row[0],
                    coin_id=row[1],
                    current_price=row[2],
                    high24h=row[3],
                    low24h=row[4],
                    created_at=row[5])

    def to_dict(self):
        return {
            'coin_id': self.coin_id,
            'current_price': self.current_price,
            'low24h': self.low24h,
            'high24h': self.high24h,
            'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'id': self.id,
            'previous_price': self.previous_price,
            'created_at_formatted': self.created_at.strftime("%H:%M %d/%m")
        }

    def is_valid_date(self, date):
        return self.created_at.replace(microsecond=0) < date.replace(microsecond=0)

    # def passed_five_minutes(self):
    #     now = datetime.utcnow()
    #     return self.created_at < now + timedelta(minutes=10)
