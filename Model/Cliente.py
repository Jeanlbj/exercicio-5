from Model.Pessoa import Pessoa
class Cliente(Pessoa): # Classe filha

    def __init__(self):
        super().__init__()
        self.__cpf = ""
        self.__venda = []

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf

    def addVenda(self, venda):
        self.__venda.append(venda)

    def removerVenda(self, venda):
        self.__venda.remove(venda)

    def listarVenda(self):
        return self.__venda
