from models.musicas import  Musica

## Lista de musicas
## Musica a declarar
m1 = Musica('Ela Partiu','Soul','Tim Maia')

m1.receber_comentario('User345', 'Show')


m1.OffOn()
def main():
    Musica.list_musics()

if __name__ == '__main__':
    main()
    
