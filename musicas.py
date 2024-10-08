class Musica:
    musics = [] # List of music
    def __init__(self, nome, categoria, autor):
        self.nome = nome
        self.categoria = categoria
        self.autor = autor
        self.visuailizacoes = 0

#def str para reconhecer mais um metódo próprio Python  
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.autor}'
    
    def list_music():
        for music in Musica.musics:
            print(f'{music.nome} | {music.categoria} | {music.autor}')


Musica_1 = Musica('Ela Partiu','Soul','Tim Maia')
Musica_2 = Musica('So os Loucos Sabem','Hip-Hop','Charlie Brown Jr')
Musica_3 = Musica('Onda','Soul','Cassiano')
# print(vars(Musicas_1))
#print(Musica_1)
#print(Musica_2)]

Musica.musics.append(Musica_1)
Musica.musics.append(Musica_2)
Musica.musics.append(Musica_3)

Musica.list_music()