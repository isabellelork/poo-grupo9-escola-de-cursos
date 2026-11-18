"""Módulo com a classe Professor do sistema da escola de cursos."""

from pessoa import Pessoa


class Professor(Pessoa):
    """Representa um professor da escola, que herda de Pessoa.

    Atributos próprios: especialidade, salário e lista de cursos ministrados.
    """

    def __init__(self, nome, idade, cpf, especialidade, salario):
        """Cria um professor.

        Args:
            nome (str): nome completo do professor.
            idade (int): idade em anos.
            cpf (str): CPF do professor.
            especialidade (str): área de atuação (não pode ser vazia).
            salario (float): salário mensal (deve ser maior que zero).
        """
        super().__init__(nome, idade, cpf)
        self.especialidade = especialidade
        self.salario = salario
        self.__cursos = []

    @property
    def especialidade(self):
        """Retorna a especialidade do professor."""
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, valor):
        """Define a especialidade do professor.

        Raises:
            ValueError: se a especialidade for vazia.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("A especialidade não pode ser vazia.")
        self.__especialidade = valor.strip()

    @property
    def salario(self):
        """Retorna o salário do professor."""
        return self.__salario

    @salario.setter
    def salario(self, valor):
        """Define o salário do professor.

        Raises:
            ValueError: se o salário não for um número maior que zero.
        """
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O salário deve ser maior que zero.")
        self.__salario = float(valor)

    @property
    def cursos(self):
        """Retorna uma cópia da lista de cursos ministrados pelo professor."""
        return list(self.__cursos)

    def adicionar_curso(self, curso):
        """Adiciona um curso à lista de cursos ministrados.

        Args:
            curso (str): nome do curso.

        Raises:
            ValueError: se o nome do curso for vazio.
        """
        if not isinstance(curso, str) or not curso.strip():
            raise ValueError("O nome do curso não pode ser vazio.")
        if curso.strip() not in self.__cursos:
            self.__cursos.append(curso.strip())

    def ministrar_aula(self, curso):
        """Retorna uma mensagem informando que o professor está dando aula.

        Args:
            curso (str): curso em que a aula está sendo dada.
        """
        return f"Prof. {self.nome} está ministrando uma aula de {curso}."

    def apresentar_se(self):
        """Apresenta o professor (sobrescreve o método de Pessoa)."""
        return (f"Olá, eu sou o professor {self.nome} e minha especialidade "
                f"é {self.especialidade}.")

    def __str__(self):
        """Retorna os dados do professor em formato legível."""
        cursos = ", ".join(self.__cursos) if self.__cursos else "nenhum"
        return (f"[Professor] {super().__str__()} | Especialidade: "
                f"{self.especialidade} | Salário: R$ {self.salario:.2f} | "
                f"Cursos: {cursos}")

