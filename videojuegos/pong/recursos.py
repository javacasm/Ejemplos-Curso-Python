# recursos

from pygame import image, transform
from config import *

v = 1.5

print(f'{__name__} v{v}')

icono_mute = image.load(CARPETA_IMAGENES + ICONO_MUTE)
icono_sound = image.load(CARPETA_IMAGENES + ICONO_SOUND)

icono_0_jugadores = image.load(CARPETA_IMAGENES + ICONO_0_JUGADORES)
icono_1_jugador = image.load(CARPETA_IMAGENES + ICONO_1_JUGADOR)
icono_2_jugadores = image.load(CARPETA_IMAGENES + ICONO_2_JUGADORES)


iconos_n_jugadores_originales = [icono_0_jugadores, icono_1_jugador, icono_2_jugadores]

# Rescalamos las imágenes a 96x96
iconos_n_jugadores = []
for icono in iconos_n_jugadores_originales:
    icono_resize = transform.scale(icono, (ICONOS_SIZE, ICONOS_SIZE))
    iconos_n_jugadores.append(icono_resize)