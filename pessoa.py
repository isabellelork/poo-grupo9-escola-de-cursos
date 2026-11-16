
class Pessoa:

    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    # Getter e Setter do nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome.strip() == "":
            raise ValueError("O nome não pode ficar vazio.")
        self.__nome = novo_nome

    # Getter e Setter da idade
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade <= 0:
            raise ValueError("A idade deve ser maior que zero.")
        self.__idade = nova_idade

    # Getter e Setter do email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if "@" not in novo_email:
            raise ValueError("Email inválido.")
        self.__email = novo_email

    def apresentar_funcao(self):
        return "Faz parte da escola."

    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade} | Email: {self.email}"
