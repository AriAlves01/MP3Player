# progressbar.py

from DetailsSong.Songs import Songs  # Importe a classe Songs ou ajuste conforme sua estrutura de pacotes
import time

class MusicProgressBar:
    def __init__(self, indice):
        self.current_song_index = indice
        self.detail_music = Songs(self.current_song_index)
        self.duration = self.get_duration()  # Obter a duração da música em segundos
        self.start_time = time.time()  # Tempo de início da reprodução da música

    def get_duration(self):
        # Lógica para obter a duração da música (exemplo: retorna um valor fixo)
        return 180  # Exemplo de duração em segundos (3 minutos)

    def get_progress(self):
        # Lógica para obter o progresso atual da música (em segundos)
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        return min(elapsed_time, self.duration)  # Limita o progresso ao máximo da duração

    def update_song(self, indice):
        self.current_song_index = indice
        self.detail_music = Songs(self.current_song_index)
        self.duration = self.get_duration()  # Atualiza a duração para a nova música
        self.start_time = time.time()  # Reinicia o tempo de início da reprodução da música
