from Model.Cliente import Cliente
from Model.Compra import Compra
from Model.Fornecedor import Fornecedor
from Model.Produto import Produto
from Model.Venda import Venda

if __name__ == "__main__":

    # Criando Produto

    produto1 = Produto()
    produto1.setNome("Caneta")
    produto1.setQtdeEstoque(1000)
    produto1.setPrecoUnit(2.50)
    produto1.setEstoqueMinimo(100)
    produto1.setEstoqueMaximo(2000)
    produto1.registrarHistorico("Data: 20/10/23; Código: 001; Entrada de 500 unidades no estoque.")

    produto2 = Produto()
    produto2.setNome("Caderno")
    produto2.setQtdeEstoque(950)
    produto2.setPrecoUnit(18.80)
    produto2.setEstoqueMinimo(50)
    produto2.setEstoqueMaximo(1500)
    produto2.registrarHistorico("Data: 21/10/23; Código: 002; Entrada de 950 unidades")

    produto3 = Produto()
    produto3.setNome("Lapiseira")
    produto3.setQtdeEstoque(1200)
    produto3.setPrecoUnit(8.50)
    produto3.setEstoqueMinimo(100)
    produto3.setEstoqueMaximo(1800)
    produto3.registrarHistorico("Data: 22/10/23; Código: 003; Entrada de 1200 unidades")

    produto4 = Produto()
    produto4.setNome("Borracha")
    produto4.setQtdeEstoque(500)
    produto4.setPrecoUnit(1.50)
    produto4.setEstoqueMinimo(80)
    produto4.setEstoqueMaximo(900)
    produto4.registrarHistorico("Data: 23/10/23; Código: 004; Entrada de 500 unidades")

    # Criando Cliente

    cliente1 = Cliente()
    cliente1.setNome("João")
    cliente1.setCpf("764.234.890-43")

    cliente2 = Cliente()
    cliente2.setNome("Jean")
    cliente2.setCpf("151.324.877-65")

    cliente3 = Cliente()
    cliente3.setNome("Lucas")
    cliente3.setCpf("645.451.956-23")

    # Criando Fornecedor

    fornecedor1 = Fornecedor()
    fornecedor1.setNome("Giacopo")
    fornecedor1.setCnpj("12.345.678/0001-90")

    fornecedor2 = Fornecedor()
    fornecedor2.setNome("Murilo")
    fornecedor2.setCnpj(" 98.765.432/0001-21")

    # Criando Venda

    venda1 = Venda()
    venda1.setDataTransacao("24/10/23")
    venda1.setQtde(1)

    venda2 = Venda()
    venda1.setDataTransacao("24/10/23")
    venda1.setQtde(1)

    venda3 = Venda()
    venda3.setDataTransacao("24/10/23")
    venda3.setQtde(1)

    venda4 = Venda()
    venda4.setDataTransacao("24/10/23")
    venda4.setQtde(1)

    # Criando Compra

    compra1 = Compra()
    compra1.setDataTransacao("24/10/23")
    compra1.setQtde(600)
    compra1.setPrecoUnit(1.80)

    compra2 = Compra()
    compra2.setDataTransacao("24/10/23")
    compra2.setQtde(400)
    compra2.setPrecoUnit(16.70)

    compra3 = Compra()
    compra3.setDataTransacao("24/10/23")
    compra3.setQtde(700)
    compra3.setPrecoUnit(6.80)

    compra4 = Compra()
    compra4.setDataTransacao("25/10/23")
    compra4.setQtde(100)
    compra4.setPrecoUnit(1.00)

    # Criando a amarração entre Produto/venda

    produto1.addVenda(venda1)
    produto2.addVenda(venda2)
    produto3.addVenda(venda3)
    produto4.addVenda(venda3)

    venda1.addProduto(produto1)
    venda2.addProduto(produto2)
    venda3.addProduto(produto3)
    venda4.addProduto(produto4)

    # Criando a amarração entre Produto/Compra

    produto1.addCompra(compra1)
    produto2.addCompra(compra2)
    produto3.addCompra(compra3)
    produto4.addCompra(compra4)

    compra1.addProduto(produto1)
    compra2.addProduto(produto2)
    compra3.addProduto(produto3)
    compra4.addProduto(produto4)

    # Criando a amarração entre Venda/Cliente

    cliente1.addVenda(venda1)
    cliente1.addVenda(venda2)
    cliente2.addVenda(venda3)
    cliente3.addVenda(venda4)

    venda1.addCliente(cliente1)
    venda2.addCliente(cliente1)
    venda3.addCliente(cliente2)
    venda4.addCliente(cliente3)

    # Criando a amarração entre Compra/Fornecedor

    compra1.addFornecedor(fornecedor1)
    compra2.addFornecedor(fornecedor1)
    compra3.addFornecedor(fornecedor2)
    compra4.addFornecedor(fornecedor2)

    fornecedor1.addCompra(compra1)
    fornecedor1.addCompra(compra2)
    fornecedor2.addCompra(compra3)
    fornecedor2.addCompra(compra4)

    # Efetuando vendas

    print("Venda 1:")
    venda1.toStr()
    venda1.vender(produto1, 10)

    print()

    print("Venda 2:")
    venda2.toStr()
    venda2.vender(produto2, 2)

    print()

    print("Venda 3:")
    venda3.toStr()
    venda3.vender(produto3, 5)

    print()

    print("Venda 4:")
    venda4.toStr()
    venda4.vender(produto4, 5)

    print()

    # Efetuando compra

    print("Compra 1:")
    compra1.toStr()
    compra1.comprar(produto1, 800)

    print()

    print("Compra 2:")
    compra2.toStr()
    compra2.comprar(produto2, 400)

    print()

    print("Compra 3:")
    compra3.toStr()
    compra3.comprar(produto3, 700)

    print()

    print("Compra 4:")
    compra4.toStr()
    compra4.comprar(produto4, 120)
