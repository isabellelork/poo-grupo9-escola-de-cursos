"""Módulo com a classe Aluno do sistema da escola de cursos."""

from pessoa import Pessoa


class Aluno(Pessoa):
    """Representa um aluno da escola, que herda de Pessoa.

    Atributos próprios: matrícula, curso e lista de notas.
    """

    def __init__(self, nome, idade, cpf, matricula, curso):
        """Cria um aluno.

        Args:
            nome (str): nome completo do aluno.
            idade (int): idade em anos.
            cpf (str): CPF do aluno.
            matricula (str): número de matrícula (não pode ser vazio).
            curso (str): curso em que o aluno está matriculado (não pode ser vazio).
        """
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self.curso = curso
        self.__notas = []

    @property
    def matricula(self):
        """Retorna a matrícula do aluno."""
        return self.__matricula

    @matricula.setter
    def matricula(self, valor):
        """Define a matrícula do aluno.

        Raises:
            ValueError: se a matrícula for vazia.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("A matrícula não pode ser vazia.")
        self.__matricula = valor.strip()

    @property
    def curso(self):
        """Retorna o curso do aluno."""
        return self.__curso

    @curso.setter
    def curso(self, valor):
        """Define o curso do aluno.

        Raises:
            ValueError: se o nome do curso for vazio.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O curso não pode ser vazio.")
        self.__curso = valor.strip()

    @property
    def notas(self):
        """Retorna uma cópia da lista de notas do aluno."""
        return list(self.__notas)

    def adicionar_nota(self, nota):
        """Adiciona uma nota à lista de notas do aluno.

        Args:
            nota (float): nota entre 0 e 10.

        Raises:
            ValueError: se a nota não estiver entre 0 e 10.
        """
        if not isinstance(nota, (int, float)) or not 0 <= nota <= 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        self.__notas.append(float(nota))

    def calcular_media(self):
        """Calcula a média das notas do aluno.

        Returns:
            float: média das notas, ou 0.0 se ainda não houver notas.
        """
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def apresentar_se(self):
        """Apresenta o aluno (sobrescreve o método de Pessoa)."""
        return (f"Olá, eu sou {self.nome}, aluno(a) do curso de {self.curso} "
                f"(matrícula {self.matricula}).")

    def __str__(self):
        """Retorna os dados do aluno em formato legível."""
        return (f"[Aluno] {super().__str__()} | Matrícula: {self.matricula} | "
                f"Curso: {self.curso} | Média: {self.calcular_media():.1f}")


