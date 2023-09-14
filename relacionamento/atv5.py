class Pessoa:
    def __init__(self, nome, idade, pai = None, mae = None):
        self.nome = nome
        self.idade = idade
        self.pai = pai
        self.mae = mae
        self.numero = len(familia)

    def __str__(self):
        pai = self.pai.nome if self.pai else ""
        mae = self.mae.nome if self.mae else ""  
        return f"{self.numero} - Nome: {self.nome} | Idade: {self.idade} | Pai: {pai} | Mãe: {mae}"
    
    def setPai(self, p) : self.pai = p
    def setMae(self, m) : self.mae = m
    
familia = []

def listarFamilia():
    for f in familia: print(f)

def criarPessoa():
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    p = Pessoa(nome, idade)
    familia.append(p)

def setarPaiMae(paimae):
    filho = int(input("Digite o numero do filho: "))
    parente = int(input("Digite o numero do parente: "))
    if paimae == "pai": familia[filho].setPai(familia[parente])
    else: familia[filho].setMae(familia[parente])

def mostraMenu():
    print("\n1 - Criar Pessoa")
    print("2 - Setar Pai")
    print("3 - Setar Mãe")
    print("4 - Ver Lista")
    print("0 - Sair")

#Programa

while True:
    mostraMenu()
    opc = int(input("Digite uma Opção: "))

    if opc == 1: criarPessoa()
    elif opc == 2: setarPaiMae("pai")
    elif opc == 3: setarPaiMae("mae")
    elif opc == 4: listarFamilia()
    elif opc == 0: break
    else: print("Numero Inválido!")

print("Fim do Programa!")






