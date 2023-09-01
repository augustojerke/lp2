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