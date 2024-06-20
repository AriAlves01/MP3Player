import flet as ft
from os import getcwd
from assets.Songs import script_dir
class Songs:
    def __init__(self,indice):
        super().__init__()
        self.indice = indice
        self.musicas = self.ListaMusicas()

    def ListaMusicas(self):
        return [
            {
                "titulomusica": "She Wolf",
                "Artista": "David Guetta",
                "music": f"{script_dir}\\David Guetta She Wolf.mp3",
                "album": r"https://upload.wikimedia.org/wikipedia/pt/4/40/David_Guetta_-_She_Wolf_%28Falling_to_Pieces%29.jpeg"
            },
            {
                "titulomusica": "Sweet Nothing",
                "Artista": "Calvin Harris",
                "music": f"{script_dir}\\Calvin Harris  Sweet Nothing.mp3",
                "album": r"https://upload.wikimedia.org/wikipedia/pt/5/5f/Calvin_Harris_-_Sweet_Nothing_cover.jpg"
            },
            {
                "titulomusica": "Ocean",
                "Artista": "Alok ft Zeeba",
                "music": f"{script_dir}\\Alok Ocean.mp3",
                "album": r"https://i.scdn.co/image/ab67616d0000b273d593b27368a31b28ac5c9d1f"
            },
            {
                "titulomusica": 'Genius',
                "Artista": "LSD ft Sia,Diplo,Labrinth",
                "music": f"{script_dir}\\LSD Genius.mp3",
                "album": r"https://i.scdn.co/image/ab67616d0000b2733f159ae07dd556323f39f47b"
            },
            {
                "titulomusica": "Little Bad Girl",
                "Artista": "David Guetta",
                "music": f"{script_dir}\\Little Bad Girl.mp3",
                "album": r"https://i1.sndcdn.com/artworks-000312367929-8qpvv3-t500x500.jpg"
            },
            {
                "titulomusica": "In The Name Of Love",
                "Artista": "Martin Garrix ft Bebe Rexha",
                "music": f"{script_dir}\\Martin Garrix & Bebe Rexha - In The Name Of Love.mp3",
                "album": r"https://upload.wikimedia.org/wikipedia/pt/thumb/6/66/In_the_Name_of_Love_Cover_Art_by_Bebe_Rexha_and_Martin_Garrix.jpeg/220px-In_the_Name_of_Love_Cover_Art_by_Bebe_Rexha_and_Martin_Garrix.jpeg"
            },

        ]
        return musicas
    def url_atual(self):
        return self.musicas[self.indice]["music"]

    def musica_atual(self):
        return self.musicas[self.indice]["titulomusica"]

    def artista_atual(self):
        return self.musicas[self.indice]["Artista"]

    def album_atual(self):
        return self.musicas[self.indice]["album"]