
import flet as ft
from DetailsSong.Songs import Songs
from DetailsSong.SongDetails import  SongContent, SongButtons
from time import sleep
import asyncio
class FunctionSongs:
    def __init__(self, page, indice):
        self.page = page
        self.current_song_index = indice

        self.update_song_info()
        self.audio = ft.Audio(
            src=self.audio_url,
            autoplay=True,
            volume=1,
            balance=0,
            on_position_changed=self.progressbaradd,
        )
        self.page.add(self.audio)
        self.song_content = SongContent(
            page=self.page,
            Album=self.album_atual,
            Musica=self.musica_atual,
            Artista=self.artista_atual
        )
        self.total_minutos = ft.Text(color='black')
        self.minutoscorridos = ft.Text(color='black')
        self.song_buttons = SongButtons(page=self.page, music_player=self)
        self.progressbar = ft.Slider(on_change=self.avancar)
        self.container = ft.Column(spacing=0,controls=[self.song_content.build(), self.song_buttons.build(),ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,controls=[self.minutoscorridos,self.total_minutos]),self.progressbar])

        self.page.add(self.container)

    def format_duration(self,milliseconds):
        # Converter milissegundos para segundos
        total_seconds = milliseconds / 1000

        # Calcular horas, minutos e segundos
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Formatar e retornar como uma string no formato "hh:mm:ss"
        return f"{int(minutes):02}:{int(seconds):02}"

    def avancar(self,e):
        self.audio.seek(int(self.progressbar.value))

    def progressbaradd(self,e):
        self.minutoscorridos.value = self.format_duration(self.audio.get_current_position())
        self.total_minutos.value = self.format_duration(self.audio.get_duration())
        self.minutoscorridos.update()
        self.total_minutos.update()
        self.progressbar.max = int(self.audio.get_duration())
        self.progressbar.value = int(self.audio.get_current_position())
        self.progressbar.update()


    def play_next_song(self, e):
        self.current_song_index += 1
        self.update_song_info()
        self.update_audio()
        self.update_song_content()

    def play_previous_song(self, e):
        self.current_song_index -= 1
        self.update_song_info()
        self.update_audio()
        self.update_song_content()

    def toggle_play_pause(self,e):
        if e.control.selected == True:
            self.audio.pause()
            e.control.selected = False
        else:
            self.audio.resume()
            e.control.selected = True
        e.control.update()


    def update_song_info(self):
        self.detail_music = Songs(self.current_song_index)
        self.audio_url = self.detail_music.url_atual()
        self.album_atual = self.detail_music.album_atual()
        self.musica_atual = self.detail_music.musica_atual()
        self.artista_atual = self.detail_music.artista_atual()

    def update_audio(self):
        self.audio.src = self.audio_url
        self.page.update()

    def update_song_content(self):

        self.song_content.update_content(
            Album=self.album_atual,
            Musica=self.musica_atual,
            Artista=self.artista_atual
        )

        self.song_buttons.update_buttons()
