class Circulo :
    def __init__(self, raio, x, y):
        self.raio = raio
        self.centrox = x
        self.centroy = y

    def __calculaArea(self):
        return 3.14 * self.raio ** 2
    
    def __calculaCircunferencia(self):
        return 2 * 3.14 * self.raio
    
    def setRaio(self, raio):
        self.raio = raio

    def aumentarRaio(self, porcentagem):
        self.raio =  self.raio * (1 + porcentagem / 100)
    
    def setCentro(self, x, y):
        self.centrox = x
        self.centroy = y

    def mostraRaio(self):
        print(f"Raio: {self.raio}")
    
    def mostraCentro(self):
        print(f"Centro: x = {self.centrox}, y = {self.centroy}")
    
    def mostraArea(self):
        print(f"Area: {self.__calculaArea()}")

def mostraMenu():
    print("\n")
    print("1 - Setar valor do raio")
    print("2 - Aumentar o raio em porcentagem")
    print("3 - Setar Centro do circulo")
    print("4 - Mostrar Raio")
    print("5 - Mostrar Centro")
    print("6 - Mostrar Area")
    print("0 - Sair")

#Programa

raio = float(input("Digite o raio: "))
x = float(input("Digite o x do centro: "))
y = float(input("Digite o y do centro: "))
c = Circulo(raio, x, y)

while True:
    mostraMenu()
    opc = int(input("\nDigite uma Opção: "))

    if opc == 1: c.setRaio(float(input("Digite o novo valor do Raio: ")))
    elif opc == 2: c.aumentarRaio(float(input("Digite o valor em % para aumentar o Raio: ")))
    elif opc == 3:
        x = float(input("Digite o x do centro: "))
        y = float(input("Digite o y do centro: "))
        c.setCentro(x, y)
    elif opc == 4: c.mostraRaio()
    elif opc == 5: c.mostraCentro()
    elif opc == 6: c.mostraArea()
    elif opc == 0: break
    else: print("Numero invalido!")
        
print("Fim do Programa!")