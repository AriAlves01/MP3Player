import flet as ft
from DetailsSong.Songs import Songs
from DetailsSong.FunctionSongs import FunctionSongs
from DetailsSong.SongDetails import SongContent, SongButtons

class MP3:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.window_center()
        self.page.window_width = 400
        self.page.window_height = 550
        self.current_song_index = 0
        self.functions = FunctionSongs(page=self.page, indice=self.current_song_index)
        self.song_content = SongContent(
            page=self.page,
            Album=self.functions.album_atual,
            Musica=self.functions.musica_atual,
            Artista=self.functions.artista_atual
        )
        self.song_buttons = SongButtons(page=self.page, music_player=self.functions)

ft.app(MP3, assets_dir="assets")