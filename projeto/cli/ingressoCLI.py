

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


class IngressoCLI:
    def __init__(self, ingresso):
        self.ingresso = ingresso
        self.commands = {
            "detalhes_ingresso": self.ticket_details,
            "sair": self.quit_cli
        }

    def ticket_details(self):
        details = self.ingresso.detalhes_ingresso()
        print(details)

    def quit_cli(self):
        print("Adeus!")

    # def run(self):
    #     print("Bem-vindo à CLI de Ingresso!")
    #     print("Comandos disponíveis: detalhes_ingresso, sair")
    #     while True:
    #         command = input("Digite um comando: ")
    #         if command in self.commands:
    #             self.commands[command]()
    #         else:
    #             print("Comando inválido. Tente novamente.")
