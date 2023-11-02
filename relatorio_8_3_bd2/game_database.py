class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, id, name):
        query = "CREATE (:player {id: $id, name: $name})"
        parameters = {"name": name, "id": id}
        self.db.execute_query(query, parameters)

    def create_match(self, id, resultado):
        query = "CREATE (:match {id: $id, resultado: $resultado})"
        parameters = {"id": id, "resultado": resultado}
        self.db.execute_query(query, parameters)

    # Pegando informações dos players
    def get_players(self):
        query = "MATCH (a:player) RETURN a.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    # Pegando informacao das partidas
    def get_matches(self):
        query = "MATCH (a:match)<-[:JOGA]-(p:player) RETURN a.name AS name, p.name AS player_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["player_name"]) for result in results]

    def update_player(self, old_name, new_name):
        query = "MATCH (a:player {name: $old_name}) SET a.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
        
    def insert_player_match(self, player_id, match_id):
        query = "MATCH (a:player {id: $player_id}) MATCH (b:match {id: $match_id}) CREATE (a)-[:JOGA]->(b)"
        parameters = {"player_id": player_id, "match_id": match_id}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (a:player {name: $name}) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def delete_match(self, name, match_name):
        query = "MATCH (a:player {name: $player_name}) MATCH (b:match {name: $match_name}) DETACH DELETE a"
        parameters = {"name": name, "match_name": match_name}
        self.db.execute_query(query, parameters)