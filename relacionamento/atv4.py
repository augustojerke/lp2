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