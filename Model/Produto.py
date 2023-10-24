from Model.Venda import Venda
from Model.Compra import Compra

class Produto:

    def __init__(self):
        self.__nome = ""
        self.__qtdeEstoque = 0
        self.__precoUnit = 0.0
        self.__estoqueMinimo = 0
        self.__estoqueMaximo = 0
        self.__historico = []
        self.__compra = []
        self.__venda = []

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

    def addCompra(self, compra):
        self.__compra.append(compra)

    def removerCompra(self, compra):
        self.__compra.remove(compra)

    def listarCompra(self):
        return self.__compra

    def addVenda(self, venda):
        self.__venda.append(venda)

    def removerVenda(self, venda):
        self.__venda.remove(venda)

    def listarVenda(self):
        return self.__venda

    # Metodos da Classe

    def debitarEstoque(self, debitarEstoque):
        self.__qtdeEstoque -= debitarEstoque

    def creditarEstoque(self, creditarEstoque):
        self.__qtdeEstoque += creditarEstoque

    def verificarEstoqueBaixo(self):
        if self.__qtdeEstoque < self.__estoqueMinimo:
            return True
        else:
            return False

    def verificarEstoqueInsuficiente(self, verificarEstoqueInsuficiente):
        if verificarEstoqueInsuficiente > self.__qtdeEstoque:
            return True
        else:
            return False

    def verificarEstoqueExcedente(self, verificarEstoqueExedente):
        if (verificarEstoqueExedente + self.__qtdeEstoque) > self.__estoqueMaximo:
            return True
        else:
            return False

    def calcularValorVenda(self, qtdeVenda):
        valor = self.__precoUnit * qtdeVenda
        return valor

    def calcularValorCompra(self, qtdeCompra):
        for compra in range(len(self.listarCompra())):
            valor = self.__compra[compra].getPrecoUnit() * qtdeCompra
            return valor

    def vender(self, qtdeVenda):
        objeto = Venda()
        if objeto.vender(objeto, qtdeVenda) is True:
            self.registrarHistorico(objeto)

    def comprar(self, qtdeCompra):
        objeto = Compra()
        if objeto.comprar(objeto, qtdeCompra) is True:
            self.registrarHistorico(objeto)

    def registrarHistorico(self, historico):
        self.__historico.append(historico)

    def exibirHistorico(self):
        return self.__historico
