
from pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, nome, idade, email, disciplina, salario):
        super().__init__(nome, idade, email)
        self.__disciplina = disciplina
        self.__salario = salario

    # Getter e Setter da disciplina
    @property
    def disciplina(self):
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, nova_disciplina):
        if nova_disciplina.strip() == "":
            raise ValueError("A disciplina não pode ficar vazia.")
        self.__disciplina = nova_disciplina

    # Getter e Setter do salário
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario <= 0:
            raise ValueError("O salário deve ser maior que zero.")
        self.__salario = novo_salario

    def apresentar_funcao(self):
        return "Ministra aulas na escola."

    def dar_aula(self):
        return f"{self.nome} está dando aula de {self.disciplina}."

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Disciplina: {self.disciplina} | "
            f"Salário: R$ {self.salario:.2f}"
        )

