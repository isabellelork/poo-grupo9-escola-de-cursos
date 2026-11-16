
from pessoa import Pessoa


class Professor(Pessoa):
    """Classe que representa um professor da escola."""

    def __init__(self, nome, idade, email, disciplina, salario):
        """Inicializa os dados do professor."""
        super().__init__(nome, idade, email)
        self.__disciplina = disciplina
        self.__salario = salario

    # Getter e Setter da disciplina
    @property
    def disciplina(self):
        """Retorna a disciplina do professor."""
        return self.__disciplina

    @disciplina.setter
    def disciplina(self, nova_disciplina):
        """Altera a disciplina do professor."""
        if nova_disciplina.strip() == "":
            raise ValueError("A disciplina não pode ficar vazia.")
        self.__disciplina = nova_disciplina

    # Getter e Setter do salário
    @property
    def salario(self):
        """Retorna o salário do professor."""
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        """Altera o salário do professor."""
        if novo_salario <= 0:
            raise ValueError("O salário deve ser maior que zero.")
        self.__salario = novo_salario

    def apresentar_funcao(self):
        """Retorna a função do professor na escola."""
        return "Ministra aulas na escola."

    def dar_aula(self):
        """Representa a atividade de dar aula."""
        return f"{self.nome} está dando aula de {self.disciplina}."

    def __str__(self):
        """Retorna os dados do professor em formato legível."""
        return (
            f"{super().__str__()} | "
            f"Disciplina: {self.disciplina} | "
            f"Salário: R$ {self.salario:.2f}"
        )

