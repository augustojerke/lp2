class Produto:
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item_pedido):
        self.itens.append(item_pedido)

    def obter_total(self):
        total = 0
        for item in self.itens:
            total += item.produto.valor * item.quantidade
        return total
