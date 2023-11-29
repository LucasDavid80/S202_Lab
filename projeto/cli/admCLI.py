

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            print(
                "Comandos disponíveis: atualizar_contato, criar_sala, adicionar_filme, criar_sessao, sair")
            command = input("Digite um comando:")
            if command == "sair":
                print("Adeus!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class AdminCLI(SimpleCLI):
    def __init__(self, admin):
        super().__init__()
        self.admin = admin
        self.add_command("atualizar_contato", self.update_contact)
        self.add_command("criar_sala", self.create_room)
        self.add_command("adicionar_filme", self.add_movie)
        self.add_command("criar_sessao", self.create_session)

    def update_contact(self):
        new_email = input("Digite o novo e-mail: ")
        new_phone = input("Digite o novo número de telefone: ")
        result = self.admin.atualizar_contato(new_email, new_phone)
        print(result)

    def create_room(self):
        number = int(input("Insira o número da sala: "))
        capacity = int(input("Insira a capacidade da sala: "))
        seat_type = input("Insira o tipo de assento: ")
        new_room = self.admin.criar_sala(number, capacity, seat_type)
        print(f"Nova sala criada: {new_room}")

    def add_movie(self):
        title = input("Digite o título do filme: ")
        genre = input("Digite o gênero do filme: ")
        duration = int(input("Insira a duração do filme em minutos: "))
        rating = input("Insira a classificação do filme: ")
        synopsis = input("Entre na sinopse do filme: ")
        new_movie = self.admin.adicionar_filme(
            title, genre, duration, rating, synopsis)
        print(f"Novo filme adicionado: {new_movie}")

    def create_session(self):
        time = input("Insira o horário da sessão (AAAA-MM-DD HH:MM): ")
        movie = input("Insira o filme da sessão: ")
        room = int(input("Digite o número da sala da sessão: "))
        price = float(input("Insira o preço da sessão: "))
        new_session = self.admin.criar_sessao(time, movie, room, price)
        print(f"Nova sessão criada: {new_session}")

    def run(self):
        print(f"Bem-vindo {self.admin.nome} à CLI do administrador!")

        super().run()


# Exemplo de uso:
# Suponha que você já tenha uma instância de Administrador chamada 'admin'
# admin = Administrador(1, "Admin", "admin@email.com", "123456789")
# Crie uma instância de AdminCLI passando essa instância de Administrador

# admin_cli.py


# class AdminCLI:
#     def __init__(self, admin):
#         self.admin = admin
#         self.commands = {
#             "atualizar_contato": self.atualizar_contato,
#             "criar_sala": self.criar_sala,
#             "adicionar_filme": self.adicionar_filme,
#             "criar_sessao": self.criar_sessao,
#             "sair": self.quit_cli
#         }

#     # Métodos para cada comando do CLI
#     # ...

#     def atualizar_contato(self):
#         new_email = input("Digite o novo e-mail: ")
#         new_phone = input("Digite o novo número de telefone: ")
#         result = self.admin.atualizar_contato(new_email, new_phone)
#         print(result)

#     def criar_sala(self):
#         print("Criar sala")

#     def adicionar_filme(self):
#         print("adicionar_filme")

#     def criar_sessao(self):
#         print("criar_sessao")

#     # ...

#     def quit_cli(self):
#         print("Adeus!")

#     def run(self):
#         print("Bem-vindo à CLI do Administrador!")
#         print("Comandos disponíveis: atualizar_contato, criar_sala, adicionar_filme, criar_sessao, sair")
#         while True:
#             command = input("Digite um comando: ")
#             if command in self.commands:
#                 self.commands[command]()
#             else:
#                 print("Comando inválido. Tente novamente.")
