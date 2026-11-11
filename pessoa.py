class Pessoa:
    """Representa uma pessoa cadastrada na escola de cursos."""


    def __init__(self, nome, idade, email):
        """Inicializa os dados básicos de uma pessoa."""
        self.__nome = nome
        self.__idade = idade
        self.__email = email


    @property
    def nome(self):
        """Retorna o nome da pessoa."""
        return self.__nome


    @nome.setter
    def nome(self, novo_nome):
        """Altera o nome, impedindo que fique vazio."""
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self.__nome = novo_nome.strip()


    @property
    def idade(self):
        """Retorna a idade da pessoa."""
        return self.__idade


    @idade.setter
    def idade(self, nova_idade):
        """Altera a idade, impedindo valores inválidos."""
        if not isinstance(nova_idade, int) or isinstance(nova_idade, bool):
            raise ValueError("A idade deve ser um número inteiro.")
        if nova_idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.__idade = nova_idade


    @property
    def email(self):
        """Retorna o e-mail da pessoa."""
        return self.__email


    @email.setter
    def email(self, novo_email):
        """Altera o e-mail da pessoa."""
        if not isinstance(novo_email, str) or "@" not in novo_email:
            raise ValueError("Informe um e-mail válido.")
        self.__email = novo_email.strip()


    def apresentar(self):
        """Retorna uma apresentação genérica da pessoa."""
        return f"Sou {self.nome} e tenho {self.idade} anos."


    def __str__(self):
        """Retorna os dados da pessoa em formato legível."""
        return (
            f"Nome: {self.nome} | "
            f"Idade: {self.idade} | "
            f"E-mail: {self.email}"
        )