class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"{self.marca} {self.modelo} ligado como carro")

class Barco:
    def __init__(self, nome):
        self.nome = nome

    def ligar(self):
        print(f"{self.nome} ligado como barco")

class CarroAnfibio(Carro, Barco):
    def liga(self):
        super().ligar()

carro_anfibio = CarroAnfibio("CarroBarco", "Anfibio")

carro_anfibio.liga()
