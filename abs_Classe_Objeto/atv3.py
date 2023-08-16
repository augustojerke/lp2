class LampadaTresEstados:
    brilho = None

    def ajustarLuz(self, luz):
        if luz == 0: self.brilho = 'Apagada'
        elif luz >= 1 and luz <=99 : self.brilho = 'Meia_luz'
        elif luz == 100: self.brilho = 'Acesa'
        else: self.brilho = 'Inválido'
    

luz = int(input("Digite um valor para o brilho da lampada: "))
l = LampadaTresEstados()
l.ajustarLuz(luz)
print(f"Estado da Luz: {l.brilho}")


