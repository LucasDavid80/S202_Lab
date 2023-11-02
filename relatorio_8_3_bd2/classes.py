class Player:
    def __init__(self, id, nome):
        self.id = id  
        self.nome = nome  
        self.matches = []

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}"

class Match:
    def __init__(self, id, resultado):
        self.id = id  
        self.resultado = resultado  
        self.players = []  

    def __str__(self):
        return f"ID: {self.id}, Resultado: {self.resultado}"
    


# Importe as classes Player e Match que você definiu anteriormente
from classes import Player, Match
from database import Database



player1 = Player(1, "Ana")
player2 = Player(2, "Pedro")
player3 = Player(3, "Beatriz")

match1 = Match(101, "Vitória da Alice")
match2 = Match(102, "Empate")
match3 = Match(103, "Vitória da Bea")

match1.players.append(player1)
match1.players.append(player2)
match2.players.append(player1)
match2.players.append(player3)
match3.players.append(player2)
match3.players.append(player3)


# Mostra info
print("Informações sobre jogadores:")
print(player1)
print(player2)
print(player3)
print("\nInformações sobre partidas:")
print(match1)
print(match2)
print(match3)

