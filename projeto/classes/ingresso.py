

class Ingresso:
    def __init__(self, id, sessao, cliente, assento):
        self.id = id
        self.sessao = sessao
        self.cliente = cliente
        self.assento = assento
        self.preco = None

    def calcular_preco(self, idade):
        self.preco = self.sessao.calcular_preco(
            self.sessao, self.cliente, idade)

    def detalhes_ingresso(self):
        if self.preco is None:
            self.calcular_preco(18)

        detalhes = f"Ingresso para '{self.sessao.filme.titulo}' na Sala {
            self.sessao.sala.numero}, assento {self.assento}, preço: R${self.preco:.2f}"
        if self.cliente:
            detalhes += f"\nComprado por: {self.cliente.nome}"

        return detalhes
