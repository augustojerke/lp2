class Carro:
    def __init__(self, gasolina, dist):
        self.gasolina = gasolina
        self.distPercorrida = dist
    
    def abastecerCarro(self, abastecimento):
        if self.gasolina == 50:
            print("Tanque Cheio!")
        elif (self.gasolina + abastecimento) < 50:
            self.gasolina += abastecimento
        else:
            self.gasolina = 50
    
    def moverCarro(self, dist):
        self.distPercorrida += dist

    def getGasolina(self):
        return self.gasolina
    
    def getDistancia(self):
        return self.distPercorrida

# Programa

c1 = Carro(20, 200)
c2 = Carro(30, 400)
gasolina_restante_c1 = c1.getGasolina() - (c1.getDistancia() / 15)
gasolina_restante_c2 = c2.getGasolina() - (c2.getDistancia() / 15)
print(f"Carro 1 - Distancia: {c1.getDistancia()} km, Gasolina Restante: {gasolina_restante_c1:.2f} litros")
print(f"Carro 2 - Distancia: {c2.getDistancia()} km, Gasolina Restante: {gasolina_restante_c2:.2f} litros")
