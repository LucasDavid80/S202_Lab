# sala_cli.py
from classes.sala import Sala


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite um comando: ")
            if command == "sair":
                print("Adeus!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class SalaCLI:
    def __init__(self, sala, pessoa):
        self.sala = sala
        self.pessoa = pessoa
        self.commands = {
            "vender_ingresso": self.vender_ingresso,
            "verificar_lotacao": self.verificar_lotacao,
            "atualizar_assento": self.atualizar_assento,
            "sair": self.quit_cli
        }

    # Em dúvida se vale a pena
    # def vender_ingresso(self):
    #     print()

    def verificar_lotacao(self):
        lotacao = self.sala.verificar_lotacao()
        if lotacao:
            print("Sala está lotada!")
        else:
            print("A sala ainda possui lugares.")

    def atualizar_assento(self):
        assento = input("Qual é o tipo do assento: ")
        self.sala.atualizar_assento(assento, self.pessoa)
        print("atualizar_assento")

    def quit_cli(self):
        print("Adeus!")

    # def run(self):
    #     print("Bem-vindo à CLI da Sala!")
    #     print("Comandos disponíveis: vender_ingresso, verificar_lotacao, atualizar_assento, sair")
    #     while True:
    #         command = input("Digite um comando: ")
    #         if command in self.commands:
    #             self.commands[command]()
    #         else:
    #             print("Comando inválido. Tente novamente.")
