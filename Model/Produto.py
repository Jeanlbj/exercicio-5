class Produto:

    def __init__(self):
        self.__nome = ""
        self.__qtdeEstoque = 0
        self.__precoUnit = 0
        self.__estoqueMinimo = 0
        self.__estoqueMaximo = 0
        self.__historico = ""
        self.__transacao = ""

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setQtdeEstoque(self, qtdeEstoque):
        self.__qtdeEstoque = qtdeEstoque

    def getQtdeEstoque(self):
        return self.__qtdeEstoque

    def setPrecoUnit(self, precoUnit):
        self.__precoUnit = precoUnit

    def getPrecoUnit(self):
        return self.__precoUnit

    def setEstoqueMinimo(self, estoqueMinimo):
        self.__estoqueMinimo = estoqueMinimo

    def getEstoqueMinimo(self):
        return self.__estoqueMinimo

    def setEstoqueMaximo(self, estoqueMaximo):
        self.__estoqueMaximo = estoqueMaximo

    def getEstoqueMaximo(self):
        return self.__estoqueMaximo

    def setHistorico(self, historico):
        self.__historico = historico

    def addTransacao(self, transacao):
        self.__transacao = transacao

    def listarTransacao(self):
        return self.__transacao
