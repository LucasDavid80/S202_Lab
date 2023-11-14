from database import Database
from query import Queries

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.205.8.115:7687", "neo4j", "isolation-mess-speech")
# db.drop_all()

queries_db = Queries(db)

# 1
results = queries_db.searchRenzo()
if results:
    first_result = results[0]
    print('Buscando pelo professor cujo nome seja “Renzo”')
    print('Ano de nascimento: ', first_result['ano_nasc'],
          ', CPF:', first_result['cpf'])
    print()

results = queries_db.searchTeacherWithM()
if results:
    print('Buscando pelos professores cujo nome comece com a letra “M”')
    qtd_teacher = len(results)
    print("Quantidade de professores:", qtd_teacher)
    for elemento in results:
        print('Nome: ', elemento['name'],
              ', CPF:', elemento['cpf'])
    print()


results = queries_db.searchAllCities()
if results:
    print('Buscando pelos nomes de todas as cidades')
    qtd_cities = len(results)
    print("Quantidade de professores:", qtd_cities)
    for elemento in results:
        print('Nome: ', elemento)
    print()


results = queries_db.searchSchool()
if results:
    print('Buscando pelas escolas, onde o number seja maior ou igual a 150 e menor ou igual a 550')
    qtd_cities = len(results)
    print("Quantidade de professores:", qtd_cities)
    for elemento in results:
        print('Nome: ', elemento['name'],
              ', Endereço:', elemento['address'],
              ', Número: ', elemento['number'])
    print()


################################################################
# 2

results = queries_db.searchMinMaxTeacher()
if results:
    print('Ano de nascimento do professor mais jovem e do professor mais velho.')
    for elemento in results:
        print('Mais velho: ', elemento[0],
              ', Mais novo:', elemento[1])
    print()


results = queries_db.mediaPopulacional()
if results:
    print('média aritmética para os habitantes de todas as cidades.')
    print('Média: ', "{:.2f}".format(results[0]), ' pessoas.')
    print()


results = queries_db.findCityForCep()
if results:
    print('cidade cujo CEP seja igual a “37540-000”.')
    print("Nome: ", results[0])
    print()

results = queries_db.returnTeachers()

if results:
    print('Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.')
    for elemento in results:
        print('Letras: ', elemento)
    print()
