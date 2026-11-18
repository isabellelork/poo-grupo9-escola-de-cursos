"""Programa principal da escola de cursos: menu interativo no terminal."""

from aluno import Aluno
from coordenador import Coordenador
from escola import Escola
from professor import Professor


def ler_texto(mensagem):
    """Lê um texto digitado pelo usuário.

    Args:
        mensagem (str): texto exibido ao pedir o dado.

    Returns:
        str: texto digitado, sem espaços nas pontas.
    """
    return input(mensagem).strip()


def ler_inteiro(mensagem):
    """Lê um número inteiro digitado pelo usuário.

    Args:
        mensagem (str): texto exibido ao pedir o dado.

    Returns:
        int: número digitado.

    Raises:
        ValueError: se o texto digitado não for um número inteiro.
    """
    texto = input(mensagem).strip()
    try:
        return int(texto)
    except ValueError:
        raise ValueError("Digite um número inteiro válido.")


def ler_decimal(mensagem):
    """Lê um número decimal digitado pelo usuário (aceita vírgula ou ponto).

    Args:
        mensagem (str): texto exibido ao pedir o dado.

    Returns:
        float: número digitado.

    Raises:
        ValueError: se o texto digitado não for um número.
    """
    texto = input(mensagem).strip().replace(",", ".")
    try:
        return float(texto)
    except ValueError:
        raise ValueError("Digite um número válido.")


def exibir_menu():
    """Exibe as opções do menu principal."""
    print("\n" + "=" * 40)
    print("        ESCOLA DE CURSOS")
    print("=" * 40)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Executar apresentação geral (polimorfismo)")
    print("5 - Registrar nota de um aluno")
    print("6 - Adicionar curso a um professor")
    print("7 - Aprovar turma (coordenador)")
    print("0 - Sair")
    print("-" * 40)


def cadastrar_pessoa(escola):
    """Pede os dados ao usuário e cadastra um aluno, professor ou coordenador.

    Args:
        escola (Escola): escola onde a pessoa será cadastrada.
    """
    print("\n--- Cadastro ---")
    print("1 - Aluno")
    print("2 - Professor")
    print("3 - Coordenador")
    tipo = ler_texto("Tipo de pessoa: ")

    if tipo not in ("1", "2", "3"):
        print("Tipo inválido.")
        return

    try:
        nome = ler_texto("Nome: ")
        idade = ler_inteiro("Idade: ")
        cpf = ler_texto("CPF: ")

        if tipo == "1":
            matricula = ler_texto("Matrícula: ")
            curso = ler_texto("Curso: ")
            pessoa = Aluno(nome, idade, cpf, matricula, curso)
        elif tipo == "2":
            especialidade = ler_texto("Especialidade: ")
            salario = ler_decimal("Salário: R$ ")
            pessoa = Professor(nome, idade, cpf, especialidade, salario)
        else:
            area = ler_texto("Área coordenada: ")
            pessoa = Coordenador(nome, idade, cpf, area)

        escola.cadastrar(pessoa)
        print(f"\n{pessoa.nome} cadastrado(a) com sucesso!")
    except ValueError as erro:
        print(f"\nErro no cadastro: {erro}")


def listar_pessoas(escola):
    """Exibe todas as pessoas cadastradas na escola.

    Args:
        escola (Escola): escola cujas pessoas serão listadas.
    """
    print("\n--- Pessoas cadastradas ---")
    pessoas = escola.listar()
    if not pessoas:
        print("Nenhuma pessoa cadastrada ainda.")
        return
    for numero, pessoa in enumerate(pessoas, start=1):
        print(f"{numero}. {pessoa}")


def buscar_pessoa(escola):
    """Busca pessoas pelo nome e exibe os resultados.

    Args:
        escola (Escola): escola onde a busca será feita.
    """
    print("\n--- Buscar pessoa ---")
    termo = ler_texto("Digite o nome (ou parte dele): ")
    if not termo:
        print("Digite pelo menos uma letra para buscar.")
        return
    resultados = escola.buscar_por_nome(termo)
    if not resultados:
        print("Nenhuma pessoa encontrada.")
        return
    print(f"{len(resultados)} resultado(s):")
    for pessoa in resultados:
        print(f"- {pessoa}")


def executar_polimorfismo(escola):
    """Chama apresentar_se() de todas as pessoas, mostrando o polimorfismo.

    Args:
        escola (Escola): escola cujas pessoas se apresentarão.
    """
    print("\n--- Apresentação geral ---")
    apresentacoes = escola.executar_apresentacao_geral()
    if not apresentacoes:
        print("Nenhuma pessoa cadastrada ainda.")
        return
    for texto in apresentacoes:
        print(f"- {texto}")


def buscar_do_tipo(escola, tipo, nome_tipo):
    """Pede o CPF e devolve a pessoa encontrada, se for do tipo esperado.

    Args:
        escola (Escola): escola onde a pessoa será procurada.
        tipo (type): classe esperada (Aluno, Professor ou Coordenador).
        nome_tipo (str): nome do tipo para exibir nas mensagens.

    Returns:
        Pessoa | None: a pessoa encontrada ou None se não existir ou for de outro tipo.
    """
    cpf = ler_texto(f"CPF do {nome_tipo}: ")
    pessoa = escola.buscar_por_cpf(cpf)
    if pessoa is None:
        print("Nenhuma pessoa encontrada com este CPF.")
        return None
    if not isinstance(pessoa, tipo):
        print(f"Essa pessoa não é {nome_tipo}.")
        return None
    return pessoa


def registrar_nota(escola):
    """Registra uma nota para um aluno, localizado pelo CPF.

    Args:
        escola (Escola): escola onde o aluno está cadastrado.
    """
    print("\n--- Registrar nota ---")
    aluno = buscar_do_tipo(escola, Aluno, "aluno")
    if aluno is None:
        return
    try:
        nota = ler_decimal("Nota (0 a 10): ")
        aluno.adicionar_nota(nota)
        print(f"\nNota registrada! Média atual de {aluno.nome}: "
              f"{aluno.calcular_media():.1f}")
    except ValueError as erro:
        print(f"\nErro ao registrar nota: {erro}")


def adicionar_curso_professor(escola):
    """Adiciona um curso à lista de cursos de um professor, localizado pelo CPF.

    Args:
        escola (Escola): escola onde o professor está cadastrado.
    """
    print("\n--- Adicionar curso a um professor ---")
    professor = buscar_do_tipo(escola, Professor, "professor")
    if professor is None:
        return
    try:
        curso = ler_texto("Nome do curso: ")
        professor.adicionar_curso(curso)
        print(f"\nCurso adicionado! {professor.ministrar_aula(curso)}")
    except ValueError as erro:
        print(f"\nErro ao adicionar curso: {erro}")


def aprovar_turma_coordenador(escola):
    """Aprova uma turma por meio de um coordenador, localizado pelo CPF.

    Args:
        escola (Escola): escola onde o coordenador está cadastrado.
    """
    print("\n--- Aprovar turma ---")
    coordenador = buscar_do_tipo(escola, Coordenador, "coordenador")
    if coordenador is None:
        return
    try:
        turma = ler_texto("Nome da turma: ")
        print(f"\n{coordenador.aprovar_turma(turma)}")
    except ValueError as erro:
        print(f"\nErro ao aprovar turma: {erro}")


def main():
    """Executa o menu principal até o usuário escolher sair."""
    escola = Escola("Escola de Cursos")

    while True:
        exibir_menu()
        opcao = ler_texto("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa(escola)
        elif opcao == "2":
            listar_pessoas(escola)
        elif opcao == "3":
            buscar_pessoa(escola)
        elif opcao == "4":
            executar_polimorfismo(escola)
        elif opcao == "5":
            registrar_nota(escola)
        elif opcao == "6":
            adicionar_curso_professor(escola)
        elif opcao == "7":
            aprovar_turma_coordenador(escola)
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()