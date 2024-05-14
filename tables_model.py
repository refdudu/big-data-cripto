from sqlalchemy import Table, Column, Integer, Float, String, DateTime, MetaData, ForeignKeyConstraint
metadata = MetaData()
coins_table = Table(
    'coin_prices',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('coin_id', String(25)),
    Column('current_price', Float),
    Column('high_24h', Float),
    Column('low_24h', Float),
    Column('created_at', DateTime),
)
