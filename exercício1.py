class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        self.assunto = assunto
        print(f'O professor {self.nome} está ministrando uma aula sobre {self.assunto}.')


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print(f'O aluno {self.nome} está presente.')


class Aula:
    def __init__(self, Professor, assunto):
        self.professor = Professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, Aluno):
        self.alunos.append(Aluno)

    def listar_presenca(self):

        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')

        for i in self.alunos:
            print(f' O aluno {i.nome} está presente.')


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
"""
aluno1.presenca()
aluno2.presenca()
professor.ministrar_aula("Programação Orientada a Objetos")
"""
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()