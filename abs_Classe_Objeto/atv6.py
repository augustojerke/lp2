class Time:
    nome = None
    esporte = None
    cidada = None
    pontuacao = None

    def setarPontuacao(self, pts):
        self.pontuacao = pts
    def retornaPontuacao(self):
        return self.pontuacao
    def mudarNomeDoTime(self, nome):
        self.nome = nome
