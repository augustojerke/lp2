class Empregado:
    def __init__ (self, nome, departamento, horasTrabalhadasNoMes, salarioPorHora):
        self.nome = nome
        self.departamento = departamento
        self.horasTrabalhadasNoMes = horasTrabalhadasNoMes
        self.salarioPorHora = salarioPorHora

    def listarTudo(self):
        print(f"Nome: {self.nome}\nDepartameto: {self.departamento}")
        print(f"Horas Trabalhadas por Mes: {self.horasTrabalhadasNoMes}\nSalario por Hora: {self.salarioPorHora}")

    def salarioMensal (self):
        return self.horasTrabalhadasNoMes * self.salarioPorHora
    

nome = str(input("Digite o nome do Funcionario: "))
departamento = str(input("Digite o nome do departamento: "))
horasTrab = int(input("Digite as horas trabalhadas no mes: "))
salarioHora = int(input("Digite o salario por hora: "))

e = Empregado(nome, departamento, horasTrab, salarioHora)
e.listarTudo()
print(f"Salario: {e.salarioMensal()}")


