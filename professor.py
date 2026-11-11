
from pessoa import Pessoa


class Professor(Pessoa):


    def __init__(self, nome, idade, email, disciplina):

        super().__init__(nome, idade, email)
        self.disciplina = disciplina

    @property
    def disciplina(self):

        return self.__disciplina

    @disciplina.setter
    def disciplina(self, nova_disciplina):

        if not isinstance(nova_disciplina, str) or not nova_disciplina.strip():
            raise ValueError("A disciplina não pode ficar vazia.")
        self.__disciplina = nova_disciplina.strip()

    def ministrar_aula(self):

        return (
            f"{self.nome} está ministrando uma aula "
            f"de {self.disciplina}."
        )

    def apresentar(self):

        return (
            f"Sou {self.nome}, tenho {self.idade} anos "
            f"e sou professor de {self.disciplina}."
        )

    def __str__(self):

        return (
            f"{super().__str__()} | "
            f"Disciplina: {self.disciplina}"
        )
