from database import db_connect
from tables_model import metadata

metadata.drop_all(db_connect)
metadata.create_all(db_connect)