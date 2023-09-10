class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self): return f"Nome: {self.nome}, Número: {self.numero}"

class Agenda:
    contatos = []

    def incluirContato(self, contato): self.contatos.append(contato)

    def listarContatos(self):
        for i in self.contatos: print(i)
    
#Programa
def mostraMenu():
    print("\n1 - Incluir Contato")
    print("2 - Listar Agenda")
    print("0 - Sair")

a = Agenda()

while True:
    mostraMenu()
    opc =  int(input("Digite uma Opção: "))

    if opc == 1:
        nome = str(input("Digite o Nome: "))
        num = str(input("Digite o Numero: "))
        c = Contato(nome, num)
        a.incluirContato(c)
    elif opc == 2: a.listarContatos()
    elif opc == 0: break
    else: print("Numero Inválido")

print("Fim do Programa!")

