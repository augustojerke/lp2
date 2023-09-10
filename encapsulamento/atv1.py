class CarrodeCorrida:
    def __init__(self, numCarro, piloto, equipe, vMaxima, vAtual, ligado):
        self.numeroCarro = numCarro
        self.piloto = piloto
        self.equipe = equipe
        self.vMaxima = vMaxima
        self.vAtual = vAtual
        self.ligado = ligado

    def setNumCarro(self, num): self.numeroCarro = num
    def setPiloto(self, piloto): self.piloto = piloto
    def setEquipe(self, equipe): self.numeroCarro = equipe
    def setVeloMaxima(self, v): self.vMaxima = v
    def setVeloAtual(self, v): self.vAtual = v
    def setLigado(self, ligado): self.ligado = ligado

    def getNumCarro(self): return self.numeroCarro
    def getPiloto(self): return self.piloto
    def getEquipe(self): return self.piloto
    def getVeloMaxima(self): return self.vMaxima
    def getVeloAtual(self): return self.vAtual
    def getLigado(self): return self.ligado

    def acelerar(self, acelerar):
        if not self.getLigado(): print("Carro não está ligado")
        elif self.getVeloAtual() >= self.getVeloMaxima(): print("Velocidade Máxima alcançada!")
        elif (acelerar + self.getVeloAtual()) >= self.getVeloMaxima(): self.vAtual = self.vMaxima
        else: self.vAtual += acelerar
    
    def frear(self, valor):
        if self.getVeloAtual() <= 0: print("Carro ja esta parado")
        elif not self.getLigado(): print("Carro parado")
        else:
            valor = 100 - valor
            self.vAtual = self.vAtual * (valor/100)
    
    def parar(self): self.setVeloAtual(0)
    def ligar(self): self.setLigado(True)
    def desligar(self): self.setLigado(False)
