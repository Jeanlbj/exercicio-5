from Model.Transacao import Transacao

class Venda(Transacao):

    def __init__(self):
        super().__init__()
        self.__cliente = ""
        self.__produto = []

    def addCliente(self, cliente):
        self.__cliente = cliente

    def listarCliente(self):
        return self.__cliente

    def addProduto(self, produto):
        self.__produto.append(produto)

    def removerProduto(self, produto):
        self.__produto.remove(produto)

    def listarProduto(self):
        return self.__produto

    # Metodos da Classe

    @staticmethod
    def vender(produto, qtdeVenda):
        if produto.verificarEstoqueInsuficiente(qtdeVenda) is True:
            print("Estoque insuficiente")
            return False
        else:
            produto.debitarEstoque(qtdeVenda)
            print(f"Valor da venda: {produto.calcularValorVenda(qtdeVenda)}")
            if produto.verificarEstoqueBaixo() is True:
                print("Estoque baixo")
            return True
