class Musica:
    def __init__(self, nome, categoria, autor):
        self.nome = nome
        self.categoria = categoria
        self.autor = autor
        self.visuailizacoes = 0

#def str para reconhecer mais um metódo próprio Python  
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.autor}'


Musica_1 = Musica('Ela Partiu','Soul','Tim Maia')
Musica_2 = Musica('So os Loucos Sabem','Hip-Hop','Charlie Brown Jr')
# print(vars(Musicas_1))
print(Musica_1)
print(Musica_2)