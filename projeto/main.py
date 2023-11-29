from datetime import date, time
import random

from classes.cliente import Cliente
from classes.adm import Administrador
from classes.filme import Filme
from classes.ingresso import Ingresso
from classes.sala import Sala
from classes.sessao import Sessao
from cli.clienteCLI import ClienteCLI
from cli.admCLI import AdminCLI
from cli.ingressoCLI import IngressoCLI
from Dao.clienteDao import ClienteModel
from database import Database

# Criando instâncias
# FILME
filme1 = Filme(1, "Inception", "Ficção científica", time(2, 28, 0), "PG-13",
               "Em um mundo onde é possível entrar na mente humana, um ladrão especializado em roubar segredos corporativos enfrenta um desafio final: implantar uma ideia na mente de um CEO.")
filme2 = Filme(2, "The Shawshank Redemption", "Drama", time(2, 22, 0), "R",
               "Condenado injustamente, um banqueiro é enviado para Shawshank, onde faz amizade com outros prisioneiros e planeja sua fuga.")
filme3 = Filme(3, "The Godfather", "Crime/Drama", time(2, 55, 0), "R",
               "Uma família mafiosa luta pelo controle da máfia em Nova York enquanto o líder envelhecido passa o controle para seu filho relutante.")

# SALA
sala1 = Sala(1, 101, 100, "Padrão")
sala2 = Sala(2, 102, 80, "VIP")
sala3 = Sala(3, 103, 120, "Premium")

# SESSÃO
sessao1 = Sessao(1, date(2023, 11, 25), time(15, 30), filme1, sala1, 15.0)
sessao2 = Sessao(2, date(2023, 11, 26), time(18, 0), filme3, sala2, 20.0)
sessao3 = Sessao(3, date(2023, 11, 27), time(20, 15), filme1, sala3, 18.5)
sessao4 = Sessao(4, date(2023, 11, 28), time(14, 45), filme2, sala1, 16.0)
sessao5 = Sessao(5, date(2023, 11, 29), time(21, 0), filme3, sala2, 22.0)

# CLIENTE
cliente1 = Cliente(1, "João Silva", "joao@email.com", "123456789")
cliente2 = Cliente(2, "Maria Santos", "maria@email.com", "987654321")
cliente3 = Cliente(3, "Pedro Oliveira", "pedro@email.com", "111223344")
cliente4 = Cliente(4, "Ana Souza", "ana@email.com", "555666777")

# ADM
admin1 = Administrador(1, "Carlos Oliveira", "carlos@email.com", "111222333")
admin2 = Administrador(2, "Amanda Rodrigues", "amanda@email.com", "444555666")
admin3 = Administrador(1, "Rafael Oliveira", "rafael@email.com", "123456789")
admin4 = Administrador(1, "Lucas", "lucas@email.com", "")

# # INGRESSO
ingressos = []

filmes = [filme1, filme2, filme3]
salas = [sala1, sala2, sala3]
sessoes = [sessao1, sessao2, sessao3, sessao4, sessao5]
clientes = [cliente1, cliente2, cliente3, cliente4]
admins = [admin1, admin2, admin3, admin4]


print("Bem-vindo ao menu do Cinema!!")
aux = input("Digite seu nome: ")

for adm in admins:
    if adm.nome == aux:
        admCLI = AdminCLI(adm)
        admCLI.run()

flag = True
while flag:
    cliente_existente = None

    for cliente in clientes:
        if cliente.nome == aux:
            cliente_existente = cliente

    if cliente_existente:
        db = Database(database="CinemaDB", collection="Cliente")
        clientemodel = ClienteModel(database=db)
        clienteCLI = ClienteCLI(clientemodel)
        clienteCLI.run()

    else:
        aux2 = input(
            "Você não possui cadastro, deseja se cadastrar (ou 'sair' para encerrar)? ")

        if aux2.lower() == "sim":
            # Criar um novo cliente

            new_name = input("Qual é o seu nome: ")
            new_email = input("Qual é o seu email: ")
            new_number = input("Qual é o seu número: ")

            cliente5 = Cliente(
                (clientes[-1].id+1), new_name, new_email, new_number)

            clientes.append(cliente5)

        elif aux2.lower() == "não":
            while True:
                print("Opções de sessões disponíveis:")
                for i, session in enumerate(sessoes, start=1):
                    print(
                        f"{i} - {session.filme.titulo} - Preço: R${session.preco}")

                escolha = input(
                    "Escolha o número da sessão desejada (ou 'sair' para encerrar): ")

                if escolha.lower() == "sair":
                    print("Encerrando a venda de ingressos.")
                    break

                try:
                    indice_sessao = int(escolha) - 1
                    if 0 <= indice_sessao < len(sessoes):
                        sessao_escolhida = sessoes[indice_sessao]
                        novo_ingresso = Ingresso(i, sessao_escolhida, None, f"A{
                            random.randint(1, sessao_escolhida.sala.capacidade)}")

                        idade = int(input("Qual é a sua idade? "))
                        if 12 <= idade <= 64:
                            desconto = 0
                        elif idade < 12 or idade >= 65:
                            desconto = 0.05
                        else:
                            print("Idade inválida para desconto.")

                        preco_final = sessao_escolhida.preco * \
                            (1 - desconto)

                        aux = novo_ingresso.calcular_preco(int(idade))
                        print(aux)

                        print(f"Preço do ingresso: R${preco_final:.2f}")

                        confirmacao = input(
                            "Deseja confirmar a compra? (sim/não) ")
                        if confirmacao.lower() == "sim":
                            ingressos.append(novo_ingresso)
                            print("Ingresso comprado com sucesso!")

                    else:
                        print("Número de sessão inválido.")
                except ValueError:
                    print("Por favor, insira um número válido.")

        if aux2.lower() == "sair":
            print("Encerrando a venda de ingressos.")
            break
