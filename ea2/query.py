
class Queries:
    def __init__(self, database):
        self.db = database

# 01)
# a-Busque pelo professor “Teacher” cujo nome seja “Renzo”, retorne o ano_nasc e o CPF.
# MATCH (t:Teacher {name: 'Renzo'})
# RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
    def searchRenzo(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t"
        results = self.db.execute_query(query)
        return [result["t"] for result in results]

# b-Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf.
# MATCH (t:Teacher)
# WHERE t.nome STARTS WITH 'M'
# RETURN t.name AS name, t.cpf AS cpf
    def searchTeacherWithM(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t"
        results = self.db.execute_query(query)
        return [result["t"] for result in results]

# c-Busque pelos nomes de todas as cidades “City” e retorne-os.
# MATCH (c:City)
# RETURN c.name AS cidades
    def searchAllCities(self):
        query = "MATCH (c:City) RETURN c.name AS cidades"
        results = self.db.execute_query(query)
        return [result["cidades"] for result in results]

# d-Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.
# MATCH (e:School)
# WHERE e.number >= 150 AND e.number <= 550
# RETURN e.name AS nome, e.address AS endereço, e.number AS numero
    def searchSchool(self):
        query = "MATCH (e:School) WHERE e.number >= 150 AND e.number <= 550 RETURN e"
        results = self.db.execute_query(query)
        return [result["e"] for result in results]


# 02)
# a-Encontre o ano de nascimento do professor mais jovem e do professor mais velho.
# MATCH (prof:Teacher)
# WITH MIN(prof.ano_nasc) AS mais_jovem, MAX(prof.ano_nasc) AS mais_velho
# RETURN mais_jovem, mais_velho

    def searchMinMaxTeacher(self):
        query = "MATCH (prof:Teacher) WITH MIN(prof.ano_nasc) AS mais_jovem, MAX(prof.ano_nasc) AS mais_velho RETURN mais_jovem, mais_velho"
        results = self.db.execute_query(query)
        return [(result["mais_jovem"], result["mais_velho"]) for result in results]

# b-Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade “population”.
# MATCH (city:City)
# RETURN AVG(city.population) AS media_populacional
    def mediaPopulacional(self):
        query = "MATCH (city:City) RETURN AVG(city.population) AS media_populacional"
        results = self.db.execute_query(query)
        return [result['media_populacional'] for result in results]

# c-Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A” .
# MATCH (city:City {cep: '37540-000'})
# RETURN REPLACE(city.name, 'a', 'A') AS nome_modificado
    def findCityForCep(self):
        query = "MATCH (city:City {cep: '37540-000'}) RETURN REPLACE(city.name, 'a', 'A') AS nome"
        results = self.db.execute_query(query)
        return [result['nome'] for result in results]

# d-Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
# MATCH (prof:Teacher)
# RETURN SUBSTRING(prof.nome, 3, 1) AS terceira_letra
    def returnTeachers(self):
        query = "MATCH (prof:Teacher) RETURN SUBSTRING(prof.name, 3, 1) AS letras"
        results = self.db.execute_query(query)
        return [result['letras'] for result in results]
