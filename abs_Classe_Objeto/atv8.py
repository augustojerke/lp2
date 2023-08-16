class Musica:
    def __init__(self, titulo, artista, duracao, genero, plataforma):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao
        self.genero = genero   
        self.plataforma = plataforma

    def mostrarMusica (self):
        print(f"{self.artista} - {self.titulo}")
    def alterarNone (self, titulo):
        self.titulo = titulo
    def mostraGenero (self):
        print(f"{self.genero}")



