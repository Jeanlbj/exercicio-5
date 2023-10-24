from Model.Transacao import Transacao

class Compra(Transacao): # Classe filha

    def __init__(self):
        super().__init__()
        self.__precoUnit = 0
        self.__produto = []
        self.__fornecedor = ""
        
    def setPrecoUnit(self, precoUnit):
        self.__precoUnit = precoUnit

    def getPrecoUnit(self):
        return self.__precoUnit

    def addFornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    def listarFornecedor(self):
        return self.__fornecedor

    def addProduto(self, produto):
        self.__produto.append(produto)

    def removerProduto(self, produto):
        self.__produto.remove(produto)

    def listarProduto(self):
        return self.__produto

    # Metodos da Classe

    @staticmethod
    def comprar(produto, qtdeCompra):
        if produto.verificarEstoqueExcedente(qtdeCompra) is True:
            print("Estoque excedente")
            return False
        else:
            produto.creditarEstoque(qtdeCompra)
            print(f"Valor Total: R$ {produto.calcularValorCompra(qtdeCompra):.2f}")
            return True

    def toStr(self):
        print(f"Fornecedor: {self.__fornecedor.getNome()}")
        for produto in range(len(self.listarProduto())):
            print(f"Produto: {self.__produto[produto].getNome()}")
            print(f"Valor Unitário: {self.__precoUnit}")
