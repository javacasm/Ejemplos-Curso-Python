# fichero utiles
from pygame import *

from config import *

v = 1.5

print(f'{__name__} v{v}')


def draw_text(surface, text, size, x, y, color, font_name):
    fuente = font.Font(CARPETA_FUENTES + font_name, size)
    text_surface = fuente.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)
    
def reproducir_sonido(sonido,mute=False):
    if not mute: 
        mixer.music.load(CARPETA_SONIDO + sonido)
        mixer.music.play()
        