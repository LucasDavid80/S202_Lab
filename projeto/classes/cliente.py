from classes.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, id, nome, email, telefone):
        super().__init__(id, nome, email, telefone, tipo="cliente")
        self.ingressos_comprados = []

    def atualizar_contato(self, novo_email, novo_telefone):
        self.email = novo_email
        self.telefone = novo_telefone
        return "Informações de contato atualizadas com sucesso."

    def comprar_ingresso(self, ingresso):
        self.ingressos_comprados.append(ingresso)
        return f"Ingresso para a sessão de {ingresso.sessao.filme.titulo} na Sala {ingresso.sessao.sala.numero}, dia {ingresso.sessao.data}, às {ingresso.sessao.horario}, assento {ingresso.assento} comprado com sucesso!"

    def listar_ingressos_comprados(self):
        if self.ingressos_comprados:
            return "\n".join([f"Sessão: {sessao.filme.titulo}, Sala {sessao.sala.numero}, Dia: {sessao.data}, Horário: {sessao.horario}, Assento: {assento}" for sessao, assento in self.ingressos_comprados])
        else:
            return "Nenhum ingresso comprado ainda."
