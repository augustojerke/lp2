class Livro:
    def __init__(self, nome, autor, genero):
        self.nome = nome
        self.autor = autor
        self.genero = genero

class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Emprestimo:
    emprestimos = {}
    dataEntrega = None

def mostraMenu():
    print("1 - Fazer Empréstimo")
    print("2 - Ver Emprestimos")
    print("3 - Sair")

def fazerEmprestimo(pessoa, livro):
    if livro.nome not in Emprestimo.emprestimos:
        Emprestimo.emprestimos[livro.nome] = pessoa.nome
        print(f"O livro '{livro.nome}' foi emprestado para {pessoa.nome}.")
    else:
        print(f"Desculpe, o livro '{livro.nome}' já foi emprestado para {Emprestimo.emprestimos[livro.nome]}.")
    
nome = str(input("Digite seu Nome: "))
email = str(input("Digite seu email: "))
p = Pessoa(nome, email)
l1 = Livro("Harry Potter", "Guto", "Fantasia")
l2 = Livro("Gibi Turma da Monica", "Manu", "Juvenil")
l3 = Livro("A menina que roubava livros", "Nilton", "Drama")

while True:
    mostraMenu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Livros disponíveis para empréstimo:")
        print("1 - Harry Potter")
        print("2 - Gibi Turma da Monica")
        print("3 - A menina que roubava livros")
        escolha = input("Escolha um livro pelo número: ")

        if escolha == "1":
            fazerEmprestimo(p, l1)
        elif escolha == "2":
            fazerEmprestimo(p, l2)
        elif escolha == "3":
            fazerEmprestimo(p, l3)
        else:
            print("Opção inválida!")

    elif opcao == "2":
        print("Livros emprestados:")
        for livro, pessoa in Emprestimo.emprestimos.items():
            print(f"'{livro}' emprestado para {pessoa}")

    elif opcao == "3":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")


