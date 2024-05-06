from sqlalchemy import create_engine

# db_connect = create_engine('sqlite:///database.db')
db_connect= create_engine('mysql://root:@localhost/big_data')
conn = db_connect.connect()
