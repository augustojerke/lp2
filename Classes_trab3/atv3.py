class Agenda:
    pessoas = {}
    qtdPessoas = 0
    
    def armazenaPessoa(self, nome, idade, altura):
        if self.qtdPessoas >= 10:
            print("Agenda Cheia!")
        else:
            self.pessoas[self.qtdPessoas] = {'Nome': nome, 'Idade': idade, 'Altura': altura}
            print(f"\n{nome} registrado!\n")
            self.qtdPessoas += 1
    
    def buscaPessoa(self, nome):
        achouPessoa = 0
        for i in self.pessoas:
            if self.pessoas[i]['Nome'] == nome:
                print(f"{nome} na posição {i + 1}\n")
                achouPessoa = 1
        if achouPessoa == 0:
            print("Nome não encontrado!\n")
    
    def listarAgenda(self):
        print("\n")
        for i in self.pessoas:
            nome = self.pessoas[i]['Nome']
            idade = self.pessoas[i]['Idade']
            altura = self.pessoas[i]['Altura']
            print(f"{i + 1} - Nome: {nome}, Idade: {idade}, Altura: {altura}")
        print("\n")
    
    def imprimePessoa(self, i):
        print(f"Pessoa da Posicao {i}: ")
        print(f"Nome: {self.pessoas[i - 1]['Nome']}, Idade: {self.pessoas[i - 1]['Idade']}, Altura: {self.pessoas[i - 1]['Altura']}\n")
    

def mostraMenu():
    print("1 - Armazenar Pessoa")
    print("2 - Imprime Pessoa por Nome")
    print("3 - Listar Agenda")
    print("4 - Imprime Pessoa por Posição")
    print("0 - Sair")


#Programa

a = Agenda()

while True:
    mostraMenu()
    opc = int(input("Digite a Opção: "))

    if opc == 1:
        nome = str(input("Digite o Nome: "))
        idade = int(input("Digite a Idade: "))
        altura = float(input("Digite a Altura: "))
        a.armazenaPessoa(nome, idade, altura)
    elif opc == 2:
        nome = str(input("Digite o Nome: "))
        a.buscaPessoa(nome)
    elif opc == 3:
        a.listarAgenda()
    elif opc == 4:
        i = int(input("Digite uma posição da agenda: "))
        a.imprimePessoa(i)
    elif opc == 0:
        break
    else:
        print("Numero Invalido!")

print("Fim do Programa!")


