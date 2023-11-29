from intefaces.permissao import Permissao


class Filme:
    def __init__(self, id, titulo, genero, duracao, classificacao, sinopse):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.classificacao = classificacao
        self.sinopse = sinopse

    def exibir_informacoes(self):
        info = f"Título: {self.titulo}\nGênero: {self.genero}\nDuração: {
            self.duracao}\nClassificação: {self.classificacao}\nSinopse: {self.sinopse}"
        return info

    def atualizar_sinopse(self, nova_sinopse, pessoa):
        if Permissao.verificar_permissao(pessoa):
            self.sinopse = nova_sinopse
            return f"Sinopse atualizada com sucesso para:\n{self.sinopse}"
        else:
            return "Você não tem permissão para atualizar a sinopse do filme."
