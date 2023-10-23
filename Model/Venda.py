from Model.Transacao import Transacao

class Venda(Transacao):

    def __init__(self):
        super().__init__()
        self.__cliente = ""

    def addCliente(self, cliente):
        self.__cliente = cliente

    def listarCliente(self):
        return self.__cliente

    # Metodos da Classe

    @staticmethod
    def vender(produto, qtdeVenda):
        if produto.verificarEstoqueInsuficiente(qtdeVenda) is True:
            print("Estoque insuficiente")
            return False
        else:
            produto.debitarEstoque(qtdeVenda)
            print(produto.calcularValorVenda(qtdeVenda))
            if produto.verificarEstoqueBaixo() is True:
                print("Estoque baixo")
            return True
