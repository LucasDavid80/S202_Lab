from intefaces.permissao import Permissao


class Sessao:
    def __init__(self, id, data, horario, filme, sala, preco):
        self.id = id
        self.data = data
        self.horario = horario
        self.filme = filme
        self.sala = sala
        self.preco = preco

    def detalhes_sessao(self):
        detalhes = f"Sessão de {self.filme.titulo}"
        detalhes += f"\nData: {self.data} | Horário: {self.horario}"
        detalhes += f"\nSala: {
            self.sala.numero} ({self.sala.capacidade} lugares)"
        detalhes += f"\nPreço do ingresso: R${self.preco:.2f}"
        return detalhes

    def calcular_preco(self, sessao_, idade, cliente=None):
        desconto = 0
        if idade is not None and (idade <= 12 or idade >= 64):
            desconto = 0.05

        if cliente is not None:
            desconto += 0.10
            return sessao_.preco * (1 - desconto)
        else:
            return sessao_.preco

    def atualizar_preco(self, novo_preco, pessoa):
        if Permissao.verificar_permissao(pessoa):
            self.preco = novo_preco
            return f"Preço do ingresso atualizado para R${self.preco:.2f}."
        else:
            return "Você não tem permissão para atualizar o preço do ingresso."
