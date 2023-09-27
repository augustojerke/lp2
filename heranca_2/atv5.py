class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibeDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibeDados(self):
        super().exibeDados()
        print(f"Departamento: {self.departamento}")


class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def exibeDados(self):
        super().exibeDados()
        print(f"Matrícula: {self.matricula}")


class Tecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus):
        super().__init__(nome, salario, matricula)
        self.bonus = bonus

    def exibeDados(self):
        super().exibeDados()
        print(f"Bônus Salarial: R$ {self.bonus:.2f}")


class Administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno, adicional_noturno):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno

    def exibeDados(self):
        super().exibeDados()
        print(f"Turno: {self.turno}")
        print(f"Adicional Noturno: R$ {self.adicional_noturno:.2f}")


gerente1 = Gerente("João", 5000.0, "Vendas")
gerente1.exibeDados()

tecnico1 = Tecnico("Maria", 2500.0, "T123", 300.0)
tecnico1.exibeDados()

administrativo1 = Administrativo("Pedro", 2200.0, "A456", "Noite", 150.0)
administrativo1.exibeDados()
