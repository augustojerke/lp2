class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def exibePreco(self):
        return self.preco


class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def getAdicional(self):
        return self.adicional

    def exibePreco(self):
        return self.preco + self.adicional


class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def getDesconto(self):
        return self.desconto

    def exibePreco(self):
        return self.preco - self.desconto

