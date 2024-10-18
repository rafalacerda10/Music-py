from models.musicas import  Musica

## Musicas a declarar
m1 = Musica('Ela Partiu', 'Soul', 'Tim Maia')

def main():
    Musica.list_musics()

if __name__ == '__main__':
    main()
    print('O programa foi executado.')