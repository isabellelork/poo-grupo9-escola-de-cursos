"""Módulo com a classe base Pessoa do sistema da escola de cursos."""


class Pessoa:
    """Representa uma pessoa da escola (classe base de Aluno, Professor e Coordenador).

    Os atributos são privados e só podem ser acessados por meio de
    propriedades (@property), que validam os valores recebidos.
    """

    def __init__(self, nome, idade, cpf):
        """Cria uma pessoa.

        Args:
            nome (str): nome completo da pessoa (não pode ser vazio).
            idade (int): idade em anos (não pode ser negativa).
            cpf (str): CPF da pessoa (não pode ser vazio).
        """
        # Usa os setters para que a validação já aconteça na criação do objeto
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    @property
    def nome(self):
        """Retorna o nome da pessoa."""
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Define o nome da pessoa.

        Raises:
            ValueError: se o nome for vazio ou conter só espaços.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def idade(self):
        """Retorna a idade da pessoa."""
        return self.__idade

    @idade.setter
    def idade(self, valor):
        """Define a idade da pessoa.

        Raises:
            ValueError: se a idade não for um número inteiro maior ou igual a zero.
        """
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("A idade deve ser um número inteiro maior ou igual a zero.")
        self.__idade = valor

    @property
    def cpf(self):
        """Retorna o CPF da pessoa."""
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        """Define o CPF da pessoa.

        Raises:
            ValueError: se o CPF for vazio.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O CPF não pode ser vazio.")
        self.__cpf = valor.strip()

    def apresentar_se(self):
        """Retorna uma apresentação da pessoa.

        Este método será sobrescrito nas classes filhas (polimorfismo).
        """
        return f"Olá, eu sou {self.nome} e faço parte da escola."

    def __str__(self):
        """Retorna os dados da pessoa em formato legível."""
        return f"Nome: {self.nome} | Idade: {self.idade} | CPF: {self.cpf}"


