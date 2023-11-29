from intefaces.permissao import Permissao


class Sala:
    def __init__(self, id, numero, capacidade, tipo_assento):
        self.id = id
        self.numero = numero
        self.capacidade = capacidade
        self.tipo_assento = tipo_assento
        self.ingresso_vendidos = []

    def vender_ingresso(self, ingresso):
        self.ingressos_vendidos.append(ingresso)

    def verificar_lotacao(self):
        return len(self.ingressos_vendidos) >= self.capacidade

    def atualizar_assento(self, novo_assento, pessoa):
        if Permissao.verificar_permissao(pessoa):
            self.tipo_assento = novo_assento
            return f"Tipo de assento atualizado para '{self.tipo_assento}'."
        else:
            return "Você não tem permissão para atualizar o tipo de assento."
