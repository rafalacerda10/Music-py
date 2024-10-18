
class Musica:
    musics = [] # List of music
    def __init__(self, nome, categoria, autor):

        self._nome = nome.title() # Indica titulo da Musica
        self._categoria = categoria # Indica categoria da Musica
        self._autor = autor # Indica nome do Autor
        self._online = False  # Indica se a música está online ou não.
        Musica.musics.append(self)  # Adiciona a música à lista de músicas.
        

#def str para reconhecer mais um metódo próprio Python  
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._autor}'
    
    @classmethod
    def list_musics(self):
        print(f'{'Name Music'.ljust(25)} | {'Category Music'.ljust(25)} | {'Author Music'.ljust(25)} | {'Online'.ljust(25)}')
        for music in Musica.musics:
            print(f'{music._nome.ljust(25)} | {music._categoria.ljust(25)} | {music._autor.ljust(25)} | {music._online}')

    @property
    def online(self):
        return 'Yes' if self._online else 'No'
    

    def OffOn(self):
        self._online = not self._online
        print(f'Music {self._nome} is now {"Online" if self._online else "Offline"}')
   

 



