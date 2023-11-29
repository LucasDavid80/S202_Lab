from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, id, nome, email, telefone, tipo):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.tipo = tipo  # Atributo para distinguir o papel da pessoa

    @abstractmethod
    def atualizar_contato(self, novo_email, novo_telefone):
        pass
