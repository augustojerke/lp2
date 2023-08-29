class Carro:
    def __init__(self, gasolina, dist):
        self.gasolina = gasolina
        self.distPercorrida = dist
    
    def abastecerCarro(self, abastecimento):
        if self.gasolina == 50: print("Tanque Cheio!")
        elif (self.gasolina + abastecimento) < 50: self.gasolina += abastecimento
        else: self.gasolina = 50
    
    def moverCarro(self, dist): self.distPercorrida += dist

    def getGasolina(self): return self.gasolina
    def getDistancia(self): return self.distPercorrida

#Programa

c1 = Carro(20, 200)
c2 = Carro(30, 400)
print(f"Carro 1 -  Distancia: {c1.distPercorrida}km , Gasolina Restante: {c1.distPercorrida/c1.gasolina} ")
print(f"Carro 2 -  Distancia: {c2.distPercorrida}km , Gasolina Restante: {c2.distPercorrida/c2.gasolina} ")