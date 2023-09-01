class Elevador:
    def __init__(self, andares, cap):
        self.andarAtual = 0
        self.andares = andares
        self.capacidade = cap
        self.pesPresentes = 0

    def adicionarPessoa(self):
        if self.capacidade == self.pesPresentes: print("Ta cheio!")
        else: self.pesPresentes += 1
    def tirarPessoa(self):
        if self.pesPresentes > 0: self.pesPresentes -= 1
        else: print("Elevador ja esta vazio")
    
    def subirAndar(self):
        if self.andarAtual == self.andares: print("Ja esta no topo!")
        else: self.andarAtual += 1
    def descerAndar(self):
        if self.andarAtual > 0: self.andarAtual -= 1
        else: print("Elevador ja esta no terreo")
    
    def getAndarAtual(self): return self.andarAtual
    def getAndares(self): return self.andares
    def getCapacidade(self): return self.capacidade
    def getPessoasPresentes(self): return self.pesPresentes
    


                                                    
    

        