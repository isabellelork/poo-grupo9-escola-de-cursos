"""Módulo com a classe Coordenador do sistema da escola de cursos."""


from pessoa import Pessoa




class Coordenador(Pessoa):
    """Representa um coordenador da escola, que herda de Pessoa.


    Atributos próprios: área coordenada e lista de turmas aprovadas.
    """


    def __init__(self, nome, idade, cpf, area_coordenada):
        """Cria um coordenador.


        Args:
            nome (str): nome completo do coordenador.
            idade (int): idade em anos.
            cpf (str): CPF do coordenador.
            area_coordenada (str): área que ele coordena (não pode ser vazia).
        """
        super().__init__(nome, idade, cpf)
        self.area_coordenada = area_coordenada
        self.__turmas_aprovadas = []


    @property
    def area_coordenada(self):
        """Retorna a área coordenada."""
        return self.__area_coordenada


    @area_coordenada.setter
    def area_coordenada(self, valor):
        """Define a área coordenada.


        Raises:
            ValueError: se a área for vazia.
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("A área coordenada não pode ser vazia.")
        self.__area_coordenada = valor.strip()


    @property
    def turmas_aprovadas(self):
        """Retorna uma cópia da lista de turmas aprovadas."""
        return list(self.__turmas_aprovadas)


    def aprovar_turma(self, turma):
        """Aprova a abertura de uma turma.


        Args:
            turma (str): nome da turma (não pode ser vazio).


        Returns:
            str: mensagem confirmando a aprovação.


        Raises:
            ValueError: se o nome da turma for vazio.
        """
        if not isinstance(turma, str) or not turma.strip():
            raise ValueError("O nome da turma não pode ser vazio.")
        turma = turma.strip()
        if turma not in self.__turmas_aprovadas:
            self.__turmas_aprovadas.append(turma)
        return f"Turma {turma} aprovada pelo coordenador {self.nome}."


    def apresentar_se(self):
        """Apresenta o coordenador (sobrescreve o método de Pessoa)."""
        return (f"Olá, eu sou {self.nome}, coordenador(a) da área de "
                f"{self.area_coordenada}.")


    def __str__(self):
        """Retorna os dados do coordenador em formato legível."""
        turmas = ", ".join(self.__turmas_aprovadas) if self.__turmas_aprovadas else "nenhuma"
        return (f"[Coordenador] {super().__str__()} | Área: "
                f"{self.area_coordenada} | Turmas aprovadas: {turmas}")



