from flask_migrate import Migrate
from __init__ import app,db


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()