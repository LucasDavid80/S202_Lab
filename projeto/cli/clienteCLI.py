# cliente_cli.py
from classes.cliente import Cliente
from classes.ingresso import Ingresso


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


class ClienteCLI(SimpleCLI):
    def __init__(self, cliente):
        super().__init__()
        self.cliente = cliente
        self.commands = {
            "atualizar_contato": self.update_contact,
            "comprar_ingresso": self.buy_ticket,
            "listar_ingressos_comprados": self.list_tickets_purchased,
            "sair": self.quit_cli
        }

    def update_contact(self):
        new_email = input("Digite o novo e-mail: ")
        new_phone = input("Digite o novo número de telefone: ")
        result = self.cliente.atualizar_contato(new_email, new_phone)
        print(result)

    def buy_ticket(self):
        # Primeiro verificar se existe alguma sessão
        # Se não bloqueia
        sessao = input("Digite uma sessão: ")
        cliente = input("Cliente: ")
        assento = input("Número do assento: ")

        ingresso = Ingresso(sessao, cliente, assento)
        self.cliente.comprar_ingresso(ingresso)

    def list_tickets_purchased(self):
        ingressos = self.cliente.listar_ingressos_comprados()
        print(ingressos)

    def quit_cli(self):
        print("Adeus!")

    def run(self):
        print(f"Bem-vindo cliente {self.cliente.nome}")
        print("Escolha uma das opções: atualizar_contato, comprar_ingresso, listar_ingressos_comprados, sair")
        super().run()

    # def add_command(self, name, function):
    #     self.commands[name] = function

    # def run(self):
    #     print("Bem-vindo à CLI do Cliente!")
    #     print("Comandos disponíveis: atualizar_contato, comprar_ingresso, listar_ingressos_comprados, sair")
    #     while True:
    #         command = input("Digite um comando:")
    #         if command == "sair":
    #             print("Adeus!")
    #             break
    #         elif command in self.commands:
    #             self.commands[command]()
    #         else:
    #             print("Comando inválido. Tente novamente.")
