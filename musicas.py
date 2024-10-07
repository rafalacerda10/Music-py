class Musica:
    def __init__(self, nome, categoria, autor):
        self.nome = nome
        self.categoria = categoria
        self.autor = autor
        self.visuailizações = 0


Musicas_1 = Musica('Ela Partiu','Soul','Tim Maia')
print(vars(Musicas_1))
