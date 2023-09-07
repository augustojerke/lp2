class CadastroEmpregado:
    nome = None
    idade = None
    funcao = None
    datanasc = None
    telefone = None
    peso = None
    altura = None
    salario = None

    def getNome(self): return self.nome
    def getIdade(self): return self.idade
    def getFuncao(self): return self.funcao
    def getDataNasc(self): return self.datanasc
    def getTelefone(self): return self.telefone
    def getPeso(self): return self.peso
    def getAltura(self): return self.altura
    def getSalario(self): return self.salario

    def setNome(self, nome): self.nome = nome
    def setIdade(self, idade): self.idade = idade
    def setFuncao(self, funcao): self.funcao = funcao
    def setDataNasc(self, datanasc): self.datanasc = datanasc
    def setTelefone(self, telefone): self.telefone = telefone
    def setPeso(self, peso): self.peso = peso
    def setAltura(self, altura): self.altura = altura
    def setSalario(self, salario): self.salario = salario

    def incluirEmpregado(self):
        self.setNome(str(input("Digite o Nome: ")))
        self.setIdade(int(input("Digite a idade: ")))
        self.setFuncao(str(input("Digite a função: ")))
        self.setDataNasc(str(input("Digite a data de nascimento: ")))
        self.setTelefone(str(input("Digite o telefone: ")))
        self.setPeso(float(input("Digite o peso: ")))
        self.setAltura(float(input("Digite a altura: ")))
        self.setSalario(float(input("Digite o salario")))
    
    def mostrarEmpregado(self):
        print(f"Nome: {self.getNome()}")
        print(f"Idade: {self.getIdade()}")
        print(f"Função: {self.getFuncao()}")
        print(f"Nascimento: {self.getDataNasc()}")
        print(f"Telefone: {self.getTelefone()}")
        print(f"Peso: {self.getPeso()}")
        print(f"Altura: {self.getAltura()}")
        print(f"Salario: {self.getSalario()}")

#Programa

e = CadastroEmpregado()

while True:
    print("1 - Cadastrar Empregado")
    print("2 - Ver Empregado")
    print("0 - Sair")
    opc = int(input("Digite uma opção"))

    if opc == 1: e.incluirEmpregado()
    elif opc == 2: e.mostrarEmpregado()
    elif opc == 0: break
    else: print("Número Inválido!")

print("Fim do Programa")