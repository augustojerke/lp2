class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do Ingresso: R$ {self.valor:.2f}")


class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorIngressoVIP(self):
        return self.valor + self.adicional


class Normal(Ingresso):
    def imprimeTipo(self):
        print("Ingresso Normal")


class CamaroteInferior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.localizacao = localizacao

    def acessaLocalizacao(self):
        return self.localizacao

    def imprimeLocalizacao(self):
        print(f"Localização do Ingresso: {self.localizacao}")


class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional):
        super().__init__(valor, adicional)

    def valorIngressoCamaroteSuperior(self):
        return self.valor + self.adicional

