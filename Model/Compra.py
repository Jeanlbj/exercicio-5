from Model.Transacao import Transacao

class Compra(Transacao): # Classe filha

    def __init__(self):
        super().__init__()
        self.__precoUnit = 0
        self.__produto = ""
        self.__fornecedor = ""
        
    def setPrecoUnit(self, precoUnit):
        self.__precoUnit = precoUnit

    def getPrecoUnit(self):
        return self.__precoUnit

    def addFornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    def listarFornecedor(self):
        return self.__fornecedor
