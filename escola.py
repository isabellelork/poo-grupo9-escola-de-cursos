
from aluno import Aluno
from professor import Professor
from coordenador import Coordenador



class Escola:
    """Classe responsável por gerenciar as pessoas da escola."""

    def __init__(self):
        """Inicializa as listas de pessoas da escola."""
        self.__alunos = []
        self.__professores = []
        self.__coordenadores = []

    # Cadastro de pessoas
    def cadastrar_aluno(self, aluno):
        """Adiciona um aluno à lista."""
        self.__alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    def cadastrar_professor(self, professor):
        """Adiciona um professor à lista."""
        self.__professores.append(professor)
        print("Professor cadastrado com sucesso!")

    def cadastrar_coordenador(self, coordenador):
        """Adiciona um coordenador à lista."""
        self.__coordenadores.append(coordenador)
        print("Coordenador cadastrado com sucesso!")

    # Listagem de pessoas
    def listar_pessoas(self):
        """Exibe todos os alunos, professores e coordenadores."""

        print("\n--- ALUNOS ---")
        for aluno in self.__alunos:
            print(aluno)

        print("\n--- PROFESSORES ---")
        for professor in self.__professores:
            print(professor)

        print("\n--- COORDENADORES ---")
        for coordenador in self.__coordenadores:
            print(coordenador)

    # Busca de pessoas
    def buscar_pessoa(self, nome):
        """Busca uma pessoa pelo nome."""

        pessoas = (
            self.__alunos
            + self.__professores
            + self.__coordenadores
        )

        for pessoa in pessoas:
            if pessoa.nome.lower() == nome.lower():
                return pessoa

        return None

    # Polimorfismo
    def executar_funcoes(self):
        """Executa a função de cada pessoa usando polimorfismo."""

        pessoas = (
            self.__alunos
            + self.__professores
            + self.__coordenadores
        )

        for pessoa in pessoas:
            print(pessoa.apresentar_funcao())

