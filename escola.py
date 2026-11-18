"""Módulo com a classe gerenciadora Escola do sistema da escola de cursos."""


from pessoa import Pessoa




class Escola:
    """Gerencia a lista de pessoas (alunos, professores e coordenadores) da escola."""


    def __init__(self, nome):
        """Cria uma escola com a lista de pessoas vazia.


        Args:
            nome (str): nome da escola (não pode ser vazio).
        """
        self.nome = nome
        self.__pessoas = []


    @property
    def nome(self):
        """Retorna o nome da escola."""
        return self.__nome


    @nome.setter
    def nome(self, valor):
        """Define o nome da escola.


        Raises:
            ValueError: se o nome for vazio.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome da escola não pode ser vazio.")
        self.__nome = valor.strip()


    @property
    def pessoas(self):
        """Retorna uma cópia da lista de pessoas cadastradas."""
        return list(self.__pessoas)


    def cadastrar(self, pessoa):
        """Cadastra uma pessoa na escola.


        Args:
            pessoa (Pessoa): objeto Pessoa, Aluno, Professor ou Coordenador.


        Raises:
            TypeError: se o objeto não for uma Pessoa.
            ValueError: se já existir uma pessoa cadastrada com o mesmo CPF.
        """
        if not isinstance(pessoa, Pessoa):
            raise TypeError("Só é possível cadastrar objetos do tipo Pessoa.")
        if self.buscar_por_cpf(pessoa.cpf) is not None:
            raise ValueError("Já existe uma pessoa cadastrada com este CPF.")
        self.__pessoas.append(pessoa)


    def listar(self):
        """Retorna a lista de todas as pessoas cadastradas."""
        return list(self.__pessoas)


    def buscar_por_nome(self, termo):
        """Busca pessoas cujo nome contenha o termo informado.


        Args:
            termo (str): parte do nome (não diferencia maiúsculas de minúsculas).


        Returns:
            list: pessoas encontradas (lista vazia se não houver nenhuma).
        """
        termo = termo.strip().lower()
        return [p for p in self.__pessoas if termo in p.nome.lower()]


    def buscar_por_cpf(self, cpf):
        """Busca uma pessoa pelo CPF.


        Args:
            cpf (str): CPF da pessoa.


        Returns:
            Pessoa | None: a pessoa encontrada ou None se não existir.
        """
        cpf = cpf.strip()
        for pessoa in self.__pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None


    def executar_apresentacao_geral(self):
        """Executa a ação polimórfica: chama apresentar_se() de cada pessoa.


        Cada objeto (Aluno, Professor ou Coordenador) responde de um jeito.


        Returns:
            list: lista com a apresentação de cada pessoa cadastrada.
        """
        return [pessoa.apresentar_se() for pessoa in self.__pessoas]


    def __str__(self):
        """Retorna um resumo da escola em formato legível."""
        return f"Escola: {self.nome} | Pessoas cadastradas: {len(self.__pessoas)}"



