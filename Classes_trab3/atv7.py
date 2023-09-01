class Relogio:
    hora = 0
    minuto = 0
    segundo = 0

    def setHora (self):
        self.hora = int(input("Digite a hora"))
        self.minuto = int(input("Digite o minuto"))
        self.segundo = int(input("Digite o segundo"))
    
    def getHora(self, hora_ref, min_ref, seg_ref):
        hora_ref[0] = self.hora
        min_ref[0] = self.minuto
        seg_ref[0] = self.segundo
    
    def avancarHora(self):
        self.segundo += 1
        if self.segundo >= 60:
            self.segundo = 0
            self.minuto += 1
            if self.minuto >= 60:
                self.minuto = 0
                self.hora = (self.hora + 1) % 24
        
    
def mostraMenu():
    print("\n1 - Setar hora")
    print("2 - Avançar Hora")
    print("0 - Sair")

#Programa

r = Relogio()

while True:
    mostraMenu()
    print(f"\nRelogio: {r.hora}:{r.minuto}:{r.segundo}\n")
    opc = int(input("Digite uma opção: "))

    if opc == 1: r.setHora()
    elif opc == 2: r.avancarHora()
    elif opc == 0: break
    else: print("Opção Inválida!")

print("Fim do Programa!")
