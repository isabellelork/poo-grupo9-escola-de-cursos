class Pessoa:


    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email


    @property
    def nome(self):

        return self.nome


    @nome.setter
    def nome(self, novo_nome):

        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self.nome = novo_nome.strip()


    @property
    def idade(self):

        return self.idade


    @idade.setter
    def idade(self, nova_idade):

        if not isinstance(nova_idade, int) or isinstance(nova_idade, bool):
            raise ValueError("A idade deve ser um número inteiro.")
        if nova_idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.idade = nova_idade


    @property
    def email(self):

        return self.email


    @email.setter
    def email(self, novo_email):

        if not isinstance(novo_email, str) or "@" not in novo_email:
            raise ValueError("Informe um e-mail válido.")
        self.email = novo_email.strip()


    def apresentar(self):

        return f"Sou {self.nome} e tenho {self.idade} anos."


    def __str__(self):

        return (
            f"Nome: {self.nome} | "
            f"Idade: {self.idade} | "
            f"E-mail: {self.email}"
        )