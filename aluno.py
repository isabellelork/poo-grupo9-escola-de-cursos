
from pessoa import Pessoa


class Aluno(Pessoa):


    def __init__(self, nome, idade, email, matricula, curso):

        super().__init__(nome, idade, email)
        self.__matricula = matricula
        self.__curso = curso

    @property
    def matricula(self):

        return self.__matricula

    @property
    def curso(self):

        return self.__curso

    @curso.setter
    def curso(self, novo_curso):

        if not isinstance(novo_curso, str) or not novo_curso.strip():
            raise ValueError("O curso não pode ficar vazio.")
        self.__curso = novo_curso.strip()

    def estudar(self):

        return f"{self.nome} está estudando {self.curso}."

    def apresentar(self):

        return (
            f"Sou {self.nome}, tenho {self.idade} anos "
            f"e sou aluno do curso de {self.curso}."
        )

    def __str__(self):

        return (
            f"{super().__str__()} | "
            f"Matrícula: {self.matricula} | "
            f"Curso: {self.curso}"
        )
