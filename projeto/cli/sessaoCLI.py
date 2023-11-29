from classes.sessao import Sessao


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite um comando:")
            if command == "sair":
                print("Adeus!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class SessaoCLI:
    def __init__(self, sessao, pessoa):
        self.sessao = sessao
        self.pessoa = pessoa
        self.commands = {
            "detalhes_sessao": self.session_details,
            "atualizar_preco": self.update_price,
            "sair": self.quit_cli
        }

    def session_details(self):
        details = self.sessao.detalhes_sessao()
        print(details)

    def update_price(self):
        novo_preco = input("Qual é o novo preço: ")
        self.sessao.atualizar_preco(novo_preco, self.pessoa)

    def quit_cli(self):
        print("Adeus!")

    # def run(self):
    #     print("Bem-vindo à CLI da Sessão!")
    #     print("Comandos disponíveis: detalhes_sessao, atualizar_preco, sair")
    #     while True:
    #         command = input("Digite um comando: ")
    #         if command in self.commands:
    #             self.commands[command]()
    #         else:
    #             print("Comando inválido. Tente novamente.")
