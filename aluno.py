
from pessoa import Pessoa


class Aluno(Pessoa):
    """Classe que representa um aluno da escola."""

    def __init__(self, nome, idade, email, matricula, curso):
        """Inicializa os dados do aluno."""
        super().__init__(nome, idade, email)
        self.__matricula = matricula
        self.__curso = curso

    # Getter e Setter da matrícula
    @property
    def matricula(self):
        """Retorna a matrícula do aluno."""
        return self.__matricula

    @matricula.setter
    def matricula(self, nova_matricula):
        """Altera a matrícula do aluno."""
        if nova_matricula.strip() == "":
            raise ValueError("A matrícula não pode ficar vazia.")
        self.__matricula = nova_matricula

    # Getter e Setter do curso
    @property
    def curso(self):
        """Retorna o curso do aluno."""
        return self.__curso

    @curso.setter
    def curso(self, novo_curso):
        """Altera o curso do aluno."""
        if novo_curso.strip() == "":
            raise ValueError("O curso não pode ficar vazio.")
        self.__curso = novo_curso

    def apresentar_funcao(self):
        """Retorna a função do aluno na escola."""
        return "Estuda na escola."

    def estudar(self):
        """Representa a atividade de estudar do aluno."""
        return f"{self.nome} está estudando {self.curso}."

    def __str__(self):
        """Retorna os dados do aluno em formato legível."""
        return (
            f"{super().__str__()} | "
            f"Matrícula: {self.matricula} | "
            f"Curso: {self.curso}"
        )
