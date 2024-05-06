from datetime import datetime

from peewee import SqliteDatabase

# define a conexão com o banco de dados
db = SqliteDatabase("database.db")

# define a classe do modelo
class User(Model):
    id = IntegerField(primary_key=True)
    name = TextField()
    created_on = DateTimeField(default=datetime.now)

    class Meta:
        database = db


# cria a tabela
db.create_tables([User])
# cria um novo usuário
user = User(name="John Doe")
user.save()
# busca um usuário pelo id
user = User.get(User.id == 1)
print(user.name)
# atualiza o nome do usuário
user.name = "Jane Doe"
user.save()
# deleta o usuário
user.delete_instance()