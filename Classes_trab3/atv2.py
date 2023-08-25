class Pessoa:
    __nome = None
    __idade = None
    __altura = None

    def setNome(self, valor):
        self.__nome = valor
    def setIdade(self, valor):
        self.__idade = valor
    def setAltura(self, valor):
        self.__altura = valor

    def getNome(self, valor):
        return self.__nome
    def getIdade(self, valor):
        return self.__idade
    def getAltura(self, valor):
        return self.__altura
    
    def listarPessoa(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")
        print(f"Nome: {self.__altura}")