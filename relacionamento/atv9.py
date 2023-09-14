class Produto:
    def __init__(self, preco, tamanho):
        self.preco = preco
        self.tamanho = tamanho

    def vendido(self):
        print("Produto vendido")

class Vendedor:
    def __init__(self, comissao):
        self.comissao = comissao

    def vende(self):
        print("Vendedor realizou uma venda")

class Comprador:
    def __init__(self, verba):
        self.verba = verba

    def compra(self):
        print("Comprador realizou uma compra")

class Venda:
    def __init__(self, produto, vendedor, comprador):
        self.produto = produto
        self.vendedor = vendedor
        self.comprador = comprador

    def concretizaVenda(self):
        print("Venda concretizada")

    def cancelaVenda(self):
        print("Venda cancelada")
