class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.quantidade = qtd

class Pedido:
    def __init__(self):
        self.items = {}
        self.pagamento = ""
        self.valorTotal = 0
    
    def cadastrarItens(self, prod, qtd):
        if qtd > prod.quantidade: print("Faltou Estoque!")
        else:
            self.items[len(self.items)] = {'Nome': prod.nome, 'Valor': prod.preco, 'Quantidade': qtd}
            self.valorTotal += prod.preco * qtd

    def setPagamento(self, pag): self.pagamento = pag

def mostraMenu():
    print("Faça seu Pedido: ")
    print("1 - Coca-Cola -   R$ 5,00")
    print("2 - Fandangos -   R$ 3,50")
    print("3 - Trident -     R$ 2,50")
    print("0 - Concluir")

#Programa

p1 = Produto('Coca-Cola', 5, 10)
p2 = Produto('Fandangos', 3.50, 6)
p3 = Produto('Trident', 2.50, 20)
ped = Pedido()

while True:
    mostraMenu()
    opc = int(input("Digite um Pedido: "))
    if opc == 0: break
    qtd = int(input("Digite a quantidade: "))
    if opc == 1: ped.cadastrarItens(p1, qtd)
    elif opc == 2: ped.cadastrarItens(p2, qtd)
    elif opc == 3: ped.cadastrarItens(p3, qtd)
    else: print("Numero Inválido")

ped.setPagamento(str(input("Digite o pagamento em dinheiro, cartão ou cheque: ")))

print("Pedido Fechado!")
print("Items: \n")
for i in ped.items: print(f"Produto: {ped.items[i]['Nome']} - Quantidade: {ped.items[i]['Quantidade']}")
print(f"\nForma de Pagamento: {ped.pagamento}")
print(f"Total: {ped.valorTotal}")




