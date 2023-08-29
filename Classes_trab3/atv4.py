class Televisao:
    def __init__(self):
        self.canal = 0
        self.volume = 0

    def aumentarVolume(self):
        self.volume += 1
    def diminuirVolume(self):
        if self.volume == 0: print("\nVolume ja esta no 0!\n")
        else: self.volume -= 1
    def imprimeVolume(self):
        print(f"\nVolume: {self.volume}\n")
    
    def aumentarCanal(self):
        self.canal += 1
    def diminuirCanal(self):
        if self.canal == 0: print("\nCanal ja esta no 0!\n")
        else: self.canal -= 1
    def imprimeCanal(self):
        print(f"\nCanal: {self.canal}\n")
    
def mostraMenu():
    print("1 - Aumentar o Volume")
    print("2 - Diminuir o Volume")
    print("3 - Aumentar o Canal")
    print("4 - Diminuir o Canal") 
    print("5 - Mostrar Volume")
    print("6 - Mostrar Canal")
    print("0 - Sair")

#Programa
t = Televisao()

while True:
    mostraMenu()
    opc = int(input("Digite uma Opção: "))

    if opc == 1: t.aumentarVolume()
    elif opc == 2: t.diminuirVolume()
    elif opc == 3: t.aumentarCanal()
    elif opc == 4: t.diminuirCanal()
    elif opc == 5: t.imprimeVolume()
    elif opc == 6: t.imprimeCanal()
    elif opc == 0: break
    else: print("Numero Inválido!") 

print("Fim do Programa!")