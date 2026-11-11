
from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from coordenador import Coordenador
from escola import Escola


def cadastrar_pessoa(escola):

    print("\n--- CADASTRAR PESSOA ---")
    print("1 - Aluno")
    print("2 - Professor")
    print("3 - Coordenador")

    tipo = input("Escolha o tipo de cadastro: ")

    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("E-mail: ")

        if tipo == "1":
            matricula = input("Matrícula: ")
            curso = input("Curso: ")
            pessoa = Aluno(nome, idade, email, matricula, curso)

        elif tipo == "2":
            disciplina = input("Disciplina: ")
            pessoa = Professor(nome, idade, email, disciplina)

        elif tipo == "3":
            area = input("Área responsável: ")
            pessoa = Coordenador(nome, idade, email, area)

        else:
            print("Opção inválida!")
            return

        escola.cadastrar_pessoa(pessoa)

    except (ValueError, TypeError) as erro:
        print(f"Erro no cadastro: {erro}")


def buscar_pessoa(escola):

    print("\n--- BUSCAR PESSOA ---")
    nome = input("Digite o nome que deseja buscar: ")

    pessoa = escola.buscar_pessoa(nome)

    if pessoa:
        print("\nPessoa encontrada:")
        print(pessoa)
    else:
        print("Pessoa não encontrada.")


def mostrar_menu():

    print("\n========== ESCOLA DE CURSOS ==========")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Executar apresentações")
    print("5 - Sair")
    print("======================================")


def main():

    escola = Escola("Escola de Cursos")

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa(escola)

        elif opcao == "2":
            escola.listar_pessoas()

        elif opcao == "3":
            buscar_pessoa(escola)

        elif opcao == "4":
            escola.executar_apresentacoes()

        elif opcao == "5":
            print("Obrigado por utilizar o sistema!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
