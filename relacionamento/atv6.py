class Funcionario:
    def __init__(self, nome, setor):
        self.nome = nome
        self.setor = setor
    
    def setSetor(self, setor): self.setor = setor

    def __str__(self): 
        return f"Nome: {self.nome} | Setor: {self.setor.nome}"

class Setor: 
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
    
s1 = Setor(1, "Programadores")
s2 = Setor(2, "RH")
s3 = Setor(3, "Diretoria")

funcionarios = []

funcionarios.append(Funcionario("Augusto", s1))
funcionarios.append(Funcionario("Neymar", s1))
funcionarios.append(Funcionario("Messi", s2))
funcionarios.append(Funcionario("Cr7", s2))
funcionarios.append(Funcionario("Luan", s3))

for i in funcionarios: print(i)
