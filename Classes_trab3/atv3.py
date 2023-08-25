class Agenda:
    def __init__(self):
        pessoas = {}
        qtdPessoas = 0
    
    def armazenaPessoa(self, nome, idade, altura):
        if self.qtdPessoas >= 10:
            print("Agenda Cheia!")
        else:
            self.pessoas[self.qtdPessoas] = {'Nome': nome, 'Idade': idade, 'Altura': altura}
            print(f"{nome} registrado!")
    
    def buscaPessoa(self, nome):
        achouPessoa = 0
        for i in self.pessoas:
            if self.pessoas[i]['Nome'] == nome:
                print(f"{nome} na posição {i + 1}")
                achouPessoa = 1
        if achouPessoa == 0:
            print("Nome não encontrado!")
    
    def listarAgenda(self):
        for i in self.pessoas:
            nome = self.pessoas[i]['Nome']
            idade = self.pessoas[i]['Idade']
            altura = self.pessoas[i]['Altura']
            print(f"{i + 1} - Nome: {nome}, Idade: {idade}, Altura: {altura}")
    
    def imprimePessoa(self, i):
        print(f"Pessoa da Posicao {i}: ")
        print(f"Nome: {self.pessoas[i + 1]['Nome']}, Idade: {self.pessoas[i + 1]['Idade']}, Altura: {self.pessoas[i + 1]['Altura']}")
    
#Programa


