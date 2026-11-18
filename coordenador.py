from pessoa import Pessoa




class Coordenador(Pessoa):



    def __init__(self, nome, idade, email, area_responsavel):

        super().__init__(nome, idade, email)
        self.area_responsavel = area_responsavel


    @property
    def area_responsavel(self):

        return self.__area_responsavel


    @area_responsavel.setter
    def area_responsavel(self, nova_area):

        if not isinstance(nova_area, str) or not nova_area.strip():
            raise ValueError("A área responsável não pode ficar vazia.")
        self.__area_responsavel = nova_area.strip()


    def organizar_cursos(self):

        return (
            f"{self.nome} está organizando os cursos "
            f"da área de {self.area_responsavel}."
        )


    def apresentar(self):

        return (
            f"Sou {self.nome}, tenho {self.idade} anos "
            f"e coordeno a área de {self.area_responsavel}."
        )


    def __str__(self):

        return (
            f"{super().__str__()} | "
            f"Área responsável: {self.area_responsavel}"
        )