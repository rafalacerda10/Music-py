class Musica:
    musics = [] # List of music
    def __init__(self, nome, categoria, autor):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self.autor = autor
        self._visualizacoes = ''

#def str para reconhecer mais um metódo próprio Python  
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.autor}'
    
    def list_music():
        print(f'{'Name Music'.ljust(25)} | {'Category Music'.ljust(25)} | {'Author Music'.ljust(25)} | {'Visualization Music'.ljust(25)}')
        for music in Musica.musics:
            print(f'{music.nome.ljust(25)} | {music.categoria.ljust(25)} | {music.autor.ljust(25)} | {music.visualizacoes.ljust(25)}')
    
    @property
    def _visualizacoes(self):
        return 'Offline'
    
    def alternate_offline(self):
        self._visualizacoes = self._visualizacoes

 

Musica_1 = Musica('Ela Partiu','Soul','Tim Maia')
Musica_1.alternate_offline()    
Musica_2 = Musica('So os Loucos Sabem','Hip-Hop','Charlie Brown Jr')
Musica_3 = Musica('Onda','Soul','Cassiano')
# print(vars(Musicas_1))
#print(Musica_1)
#print(Musica_2)]

Musica.musics.append(Musica_1)
Musica.musics.append(Musica_2)
Musica.musics.append(Musica_3)

Musica.list_music()