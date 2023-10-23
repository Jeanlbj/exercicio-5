from Model.Transacao import Transacao

class Venda(Transacao):

    def __init__(self):
        super().__init__()
        self.__cliente = ""

    def addCliente(self, cliente):
        self.__cliente = cliente

    def listarCliente(self):
        return self.__cliente
