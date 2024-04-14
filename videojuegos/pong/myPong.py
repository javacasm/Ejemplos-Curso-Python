# Name: Pong by JLCQL
from pygame import *
# TODO: optimizar carga del modulo

from config import *
from menu import show_menu
from game import play_game
v = 1.5

print(f'{__name__} v{v}')

init() # inicializamos pygame

pantalla = display.set_mode( (ancho_pantalla, alto_pantalla) )

display.set_caption('Mi primer juego - Pong')

clock = time.Clock()

# Sonido
mixer.init()

configuracion = show_menu(pantalla, clock)

play_game(pantalla, clock, configuracion[CONFIG_N_JUGADORES],configuracion[CONFIG_MUTE])
    
quit() # cerramos pygame
print('Adiós')