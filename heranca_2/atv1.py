class Carro:
    def __init__(self):
        self.ligado = False
        self.velocidade = 0
    
    def liga (self):
        self.ligado = True
        print("Carro Ligado")
        