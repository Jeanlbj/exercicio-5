from Model.Pessoa import Pessoa

class Fornecedor(Pessoa):

    def __init__(self):
        super().__init__()
        self.__cnpj = ""
        self.__compra = ""

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def getCnpf(self):
        return self.__cnpj

    def addCompra(self, compra):
        self.__compra = compra

    def listarCompra(self):
        return self.__compra
