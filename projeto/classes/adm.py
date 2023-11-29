
from classes.pessoa import Pessoa


class Administrador(Pessoa):
    def __init__(self, id, nome, email, telefone):
        super().__init__(id, nome, email, telefone, tipo="administrador")

    def atualizar_contato(self, novo_email, novo_telefone):
        self.email = novo_email
        self.telefone = novo_telefone
        return "Informações de contato atualizadas com sucesso."

    def criar_sala(self, numero, capacidade, tipo_assento):
        from classes.sala import Sala
        nova_sala = Sala(numero, capacidade, tipo_assento)
        # Aqui você pode realizar outras operações se necessário
        return nova_sala

    def adicionar_filme(self, titulo, genero, duracao, classificacao, sinopse):
        from classes.filme import Filme
        novo_filme = Filme(titulo, genero, duracao, classificacao, sinopse)
        # Aqui você pode realizar outras operações se necessário
        return novo_filme

    def criar_sessao(self, horario, filme, sala, preco):
        from classes.sessao import Sessao
        nova_sala = Sessao(horario, filme, sala, preco)
        # Aqui você pode realizar outras operações se necessário
        return nova_sala
