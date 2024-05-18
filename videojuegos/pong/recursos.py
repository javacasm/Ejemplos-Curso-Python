# recursos

from pygame import image, transform
from config import *

v = 1.6

print(f'{__name__} v{v}')

# reescala todos los iconos de la lista al tamaño indicado
def escala_iconos(array_iconos, new_size = ICONOS_SIZE):
    array_iconos_escalados = []
    for icono in array_iconos:
        icono_resize = transform.scale(icono, (new_size, new_size))
        array_iconos_escalados.append(icono_resize)
    return array_iconos_escalados

icono_mute = image.load(CARPETA_IMAGENES + ICONO_MUTE)
icono_sound = image.load(CARPETA_IMAGENES + ICONO_SOUND)

icono_0_jugadores = image.load(CARPETA_IMAGENES + ICONO_0_JUGADORES)
icono_1_jugador = image.load(CARPETA_IMAGENES + ICONO_1_JUGADOR)
icono_2_jugadores = image.load(CARPETA_IMAGENES + ICONO_2_JUGADORES)

iconos_n_jugadores_originales = [icono_0_jugadores, icono_1_jugador, icono_2_jugadores]

# Rescalamos las imágenes a 96x96 https://stackoverflow.com/questions/43046376/how-to-change-an-image-size-in-pygame
iconos_n_jugadores = escala_iconos(iconos_n_jugadores_originales)

icono_raqueta1 = image.load(CARPETA_IMAGENES + ICONO_RAQUETA1)
icono_raqueta2 = image.load(CARPETA_IMAGENES + ICONO_RAQUETA2)

icono_ingles = image.load(CARPETA_IMAGENES + ICONO_EN)
icono_espanol = image.load(CARPETA_IMAGENES + ICONO_ES)
icono_aleman = image.load(CARPETA_IMAGENES + ICONO_DE)

iconos_idiomas = [icono_espanol,icono_ingles,icono_aleman]

icono_dificultad_facil = image.load(CARPETA_IMAGENES + ICONO_NIVEL_FACIL)
icono_dificultad_dificil = image.load(CARPETA_IMAGENES + ICONO_NIVEL_DIFICIL)
icono_dificultad_pesadilla = image.load(CARPETA_IMAGENES + ICONO_NIVEL_PESADILLA)

iconos_dificultad_originales = [icono_dificultad_facil,icono_dificultad_dificil,icono_dificultad_pesadilla]
iconos_dificultad = escala_iconos(iconos_dificultad_originales)

iconos_pelota_original = image.load(CARPETA_IMAGENES + ICONOS_PELOTA)

iconos_pelota = transform.scale(iconos_pelota_original, (ICONO_PELOTA_SIZE, ICONO_PELOTA_SIZE*ICONO_PELOTA_NUMERO_FRAMES))

fondo_original = image.load(CARPETA_IMAGENES + FONDO1)
fondo = transform.scale(fondo_original, (ancho_pantalla, alto_pantalla))
