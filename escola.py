
from pessoa import Pessoa


class Escola:


    def __init__(self, nome):

        self.__nome = nome
        self.__pessoas = []

    @property
    def nome(self):

        return self.__nome

    def cadastrar_pessoa(self, pessoa):

        if not isinstance(pessoa, Pessoa):
            raise TypeError("O cadastro deve ser uma pessoa válida.")

        self.__pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")

    def listar_pessoas(self):

        if not self.__pessoas:
            print("Nenhuma pessoa cadastrada.")
            return

        print(f"\nPessoas cadastradas na {self.nome}:")
        for pessoa in self.__pessoas:
            print(pessoa)

    def buscar_pessoa(self, nome):

        for pessoa in self.__pessoas:
            if pessoa.nome.lower() == nome.lower():
                return pessoa

        return None

    def executar_apresentacoes(self):

        if not self.__pessoas:
            print("Não existem pessoas para apresentar.")
            return

        print("\nApresentação das pessoas cadastradas:")
        for pessoa in self.__pessoas:
            print(pessoa.apresentar())

    def __str__(self):

        return (
            f"Escola: {self.nome} | "
            f"Total de pessoas cadastradas: {len(self.__pessoas)}"
        )
