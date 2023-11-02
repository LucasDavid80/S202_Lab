from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.195.44.94:7687", "neo4j", "seam-axis-meats")
db.drop_all()

game_db = GameDatabase(db)

# Criando alguns jogadores
game_db.create_player(1, "Ana")
game_db.create_player(2, "Pedro")
game_db.create_player(3, "Beatriz")

# Criando algumas partidas e suas relações
game_db.create_match(101, "Vitória da Alice")
game_db.create_match(102, "Empate")
game_db.create_match(103, "Vitória da Beatriz")

# Criando as relações entre partidas e usuários
game_db.insert_player_match(1,101)
game_db.insert_player_match(2,101)
game_db.insert_player_match(1,102)
game_db.insert_player_match(3,102)
game_db.insert_player_match(2,103)
game_db.insert_player_match(3,103)


# Imprimindo todas as informações do banco de dados
print("Informações sobre jogadores:")
print(game_db.get_players())
print("Informações sobre partidas:")
print(game_db.get_matches())

# Fechando a conexão com o banco de dados
db.close()

