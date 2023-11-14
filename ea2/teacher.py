class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject


class TeacherCRUD:
    def __init__(self):
        self.teachers = []

    def create_teacher(self, teacher_id, name, subject):
        new_teacher = Teacher(teacher_id, name, subject)
        self.teachers.append(new_teacher)
        return new_teacher

    def get_teacher_by_id(self, teacher_id):
        for teacher in self.teachers:
            if teacher.teacher_id == teacher_id:
                return teacher
        return None

    def update_teacher(self, teacher_id, name=None, subject=None):
        teacher = self.get_teacher_by_id(teacher_id)
        if teacher:
            if name is not None:
                teacher.name = name
            if subject is not None:
                teacher.subject = subject
            return teacher
        return None

    def delete_teacher(self, teacher_id):
        teacher = self.get_teacher_by_id(teacher_id)
        if teacher:
            self.teachers.remove(teacher)
            return teacher
        return None


# Exemplo de uso:
teacher_crud = TeacherCRUD()

# Criar professores
teacher1 = teacher_crud.create_teacher(1, "Professor A", "Matemática")
teacher2 = teacher_crud.create_teacher(2, "Professor B", "História")

# Obter professor por ID
print(teacher_crud.get_teacher_by_id(1).name)  # Saída: Professor A

# Atualizar informações do professor
teacher_crud.update_teacher(1, name="Novo Nome", subject="Nova Matéria")
print(teacher_crud.get_teacher_by_id(1).name)  # Saída: Novo Nome

# Deletar professor
deleted_teacher = teacher_crud.delete_teacher(2)
print(deleted_teacher.name)  # Saída: Professor B
