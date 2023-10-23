class Transacao: # Classe pai

    def __init__(self):
        self.__dataTransacao = ""
        self.__qtde = 0
        self.__produto = ""

    def setDataTransacao(self, dataTransacao):
        self.__dataTransacao = dataTransacao

    def getDataTransacao(self):
        return self.__dataTransacao

    def setQtde(self, qtde):
        self.__qtde = qtde

    def getQtde(self):
        return self.__qtde

    def addProduto(self, produto):
        self.__produto = produto

    def listarProduto(self):
        return self.__produto
