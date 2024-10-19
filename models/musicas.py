from models.comentario import Comentario

class Musica:
    musics = [] # List of music
    def __init__(self, nome, categoria, autor):

        self._nome = nome.title() # Indica titulo da Musica
        self._categoria = categoria # Indica categoria da Musica
        self._autor = autor # Indica nome do Autor
        self._online = False  # Indica se a música está online ou não.
        self._comentario = [] # Lista de comentarios da musica.
        Musica.musics.append(self)  # Adiciona a música à lista de músicas.
        

#def str para reconhecer mais um metódo próprio Python  
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._autor}'
    
    @classmethod
    def list_musics(self):
        print(f'{'Name Music'.ljust(10)} | {'Category Music'.ljust(10)} | {'Author Music'.ljust(10)} | {'Online'.ljust(10)} | {'comentario'.ljust(10)}')
        for music in Musica.musics:
            print(f'{music._nome.ljust(10)} | {music._categoria.ljust(10)} | {music._autor.ljust(15)}| {music._online} | {music._comentario}')

    @property
    def online(self):
        return 'Yes' if self._online else 'No'
    

    def OffOn(self):
        self._online = not self._online
        print(f'Music {self._nome} is now {"Online" if self._online else "Offline"}')
   
   #Comentario
    def receber_comentario(self, usuario, comentario):
        comentarios =  Comentario(usuario, comentario)
        self._comentario.append(comentario)

    #Mostrando comentarios
    def mostrar_comentarios(self):
        if self._comentario == None:
            print('Nenhum comentario cadastrado.')
        else:
            for comentario in self._comentario:
                print(f'Usuario: {comentario._usuario}, Comentario: {comentario._comentario}')
    



