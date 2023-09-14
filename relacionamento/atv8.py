class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.pneus = []
        self.motor = None

    def adicionar_pneu(self, pneu):
        if len(self.pneus) < 4:
            self.pneus.append(pneu)
            pneu.carro = self
        else:
            print("O carro já possui 4 pneus. Não é possível adicionar mais.")

    def adicionar_motor(self, motor):
        if self.motor is None:
            self.motor = motor
            motor.carro = self
        else:
            print("O carro já possui um motor.")

class Pneu:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho
        self.carro = None

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
        self.carro = None
