# Name: Pong by JLCQL
from pygame import *
# TODO: optimizar carga del modulo

from config import *
from menu import show_menu
import game 

v = 1.7

print(f'{__name__} v{v}')

init() # inicializamos pygame

pantalla = display.set_mode( (ancho_pantalla, alto_pantalla) )

display.set_caption('myPong v{v}')

clock = time.Clock()

# Sonido
mixer.init()

configuracion = show_menu(pantalla, clock)

game.numero_jugadores = configuracion[CONFIG_N_JUGADORES]
game.mute = configuracion[CONFIG_MUTE]
game.dificultad = configuracion[CONFIG_LEVEL]
game.idioma = configuracion[CONFIG_LANGUAGE]

game.play_game(pantalla, clock)
    
quit() # cerramos pygame
print('Adiós')