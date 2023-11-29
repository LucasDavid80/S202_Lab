from classes.filme import Filme


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


class FilmeCLI:
    def __init__(self, filme, pessoa):
        self.filme = filme
        self.pessoa = pessoa
        self.commands = {
            "exibir_informacoes": self.display_information,
            "atualizar_sinopse": self.update_synopsis,
            "sair": self.quit_cli
        }

    def display_information(self):
        info = self.filme.exibir_informacoes()
        print(info)

    def update_synopsis(self):
        nova_sinopse = input("Qual é a nova sinopse: ")
        response = self.filme.atualizar_sinopse(nova_sinopse, self.pessoa)
        print(response)

    def quit_cli(self):
        print("Adeus!")

    # def run(self):
    #     print("Bem-vindo à CLI do Filme!")
    #     print("Comandos disponíveis: exibir_informacoes, atualizar_sinopse, sair")
    #     while True:
    #         command = input("Digite um comando: ")
    #         if command in self.commands:
    #             self.commands[command]()
    #         else:
    #             print("Comando inválido. Tente novamente.")
