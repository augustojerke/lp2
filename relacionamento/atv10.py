class ContaCorrente:
    def __init__(self, saldo, chequeEspecial):
        self.saldo = saldo
        self.chequeEspecial = chequeEspecial
    
    def deposita(self, valor):
        self.saldo += valor
    
    def extrato(self):
        return f"Saldo: {self.saldo}, Cheque Especial: {self.chequeEspecial}"

class Poupanca:
    def __init__(self, saldo):
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.contas_corrente = []
        self.contas_poupanca = []

    def abreContam(self, saldo, chequeEspecial):
        conta = ContaCorrente(saldo, chequeEspecial)
        self.contas_corrente.append(conta)

    def abrePoupanca(self, saldo):
        conta = Poupanca(saldo)
        self.contas_poupanca.append(conta)

    def falencia(self):
        self.contas_corrente = []
        self.contas_poupanca = []
