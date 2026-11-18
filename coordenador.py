
from pessoa import Pessoa


class Coordenador(Pessoa):

    def __init__(self, nome, idade, email, setor, tempo_experiencia):
        super().__init__(nome, idade, email)
        self.__setor = setor
        self.__tempo_experiencia = tempo_experiencia

    # Getter e Setter do setor
    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, novo_setor):
        if novo_setor.strip() == "":
            raise ValueError("O setor não pode ficar vazio.")
        self.__setor = novo_setor

    # Getter e Setter do tempo de experiência
    @property
    def tempo_experiencia(self):
        return self.__tempo_experiencia

    @tempo_experiencia.setter
    def tempo_experiencia(self, novo_tempo):
        if novo_tempo < 0:
            raise ValueError("O tempo não pode ser negativo.")
        self.__tempo_experiencia = novo_tempo

    def apresentar_funcao(self):
        return "Coordena as atividades da escola."

    def organizar_escola(self):
        return f"{self.nome} está organizando o setor de {self.setor}."

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Setor: {self.setor} | "
            f"Experiência: {self.tempo_experiencia} anos"
        )
