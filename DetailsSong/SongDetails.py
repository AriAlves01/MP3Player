
import flet as ft


class SongContent:
    def __init__(self, page, Album, Musica, Artista):
        self.page = page
        self.progressbar = ft.ProgressBar()
        self.Album = Album
        self.Musica = Musica
        self.Artista = Artista
        self.container = ft.Container(
            alignment=ft.alignment.center,
            content=self._build_content()
        )

    def _build_content(self):
        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    image_src=f"{self.Album}",image_fit=ft.ImageFit.CONTAIN,
                    width=250,
                    height=250,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(blur_radius=2, spread_radius=2, color=ft.colors.BLACK)
                ),
                ft.Text(value=f"{self.Musica}", size=30),
                ft.Text(value=f"{self.Artista}")
            ]
        )

    def update_content(self, Album, Musica, Artista):
        self.Album = Album
        self.Musica = Musica
        self.Artista = Artista
        self.container.content = self._build_content()
        self.page.update()

    def build(self):
        return self.container

class SongButtons:
    def __init__(self, page, music_player):
        self.page = page
        self.music_player = music_player
        self.container = ft.Container(
            padding=0,
            alignment=ft.alignment.center,
            content=self._build_buttons()
        )

    def _build_buttons(self):
        return ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.IconButton(
                    col=4,
                    icon=ft.icons.SKIP_PREVIOUS,
                    icon_size=40,
                    icon_color=ft.colors.BLACK,
                    on_click=lambda e: self.music_player.play_previous_song(e)
                ),
                ft.IconButton(
                    col=4,
                    icon=ft.icons.PLAY_ARROW,
                    selected_icon=ft.icons.PAUSE,
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.SELECTED: ft.colors.BLACK,
                            ft.MaterialState.DEFAULT: ft.colors.BLACK
                        }
                    ),
                    selected=True,
                    icon_size=60,
                    on_click=lambda e: self.music_player.toggle_play_pause(e)
                ),
                ft.IconButton(
                    col=4,
                    icon=ft.icons.SKIP_NEXT,
                    icon_size=40,
                    icon_color=ft.colors.BLACK,
                    on_click=lambda e: self.music_player.play_next_song(e)
                )
            ]
        )

    def update_buttons(self):
        self.container.content = self._build_buttons()
        self.page.update()

    def build(self):
        return self.container
