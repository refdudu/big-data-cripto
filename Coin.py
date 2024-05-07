
class Coin:

    def __init__(self, _id, coin_id, current_price, created_at):
        self.id = _id
        self.coin_id = coin_id
        self.current_price = current_price
        self.created_at = created_at
        # self.created_at_formatted = created_at.strftime("%H:%M %d/%m")

    def to_dict(self):
        return {
            'coin_id': self.coin_id,
            'current_price': self.current_price,
            'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'id': self.id,
            'created_at_formatted': self.created_at.strftime("%H:%M %d/%m")
        }

    def is_valid_date(self, date):
        return self.created_at.replace(microsecond=0) < date.replace(microsecond=0)

    # def passed_five_minutes(self):
    #     now = datetime.utcnow()
    #     return self.created_at < now + timedelta(minutes=10)
