# Sistema de menús para pygame
from pygame import *

from config import *
from utiles import draw_text, reproducir_sonido
from recursos import *

v = 1.7

print(f'{__name__} v{v}')

opciones = {CONFIG_MUTE:False, CONFIG_N_JUGADORES:0, CONFIG_LANGUAGE:0, CONFIG_LEVEL:0}

num_opciones_visuales = 0

opcion_seleccionada = 0

bMenu = True

def dibuja_menu_simple(pantalla):
    # dibujando menú

    pantalla.fill(COLOR_FONDO_MENU)  # rellenamos el fondo de la pantalla de negro

    altura_opcion = alto_pantalla//(num_opciones_visuales+1)
    
    indice = 0
    for grupo_opciones in opciones_visuales[opciones[CONFIG_LANGUAGE]]:
        for texto_opcion in grupo_opciones:
            draw_text(pantalla, texto_opcion,
                      altura_opcion//2, 200, 50 + indice*altura_opcion,
                      COLOR_OPCION_SELECCIONADA if indice == opcion_seleccionada else COLOR_OPCION,
                      FUENTE_MENU)
            indice += 1

    pantalla.blit(icono_mute if opciones[CONFIG_MUTE] else icono_sound, (ancho_pantalla-ICONOS_SIZE-5, alto_pantalla-ICONOS_SIZE))
    pantalla.blit(iconos_n_jugadores[opciones[CONFIG_N_JUGADORES]], ( 5, alto_pantalla-ICONOS_SIZE-5))
    pantalla.blit(iconos_idiomas[opciones[CONFIG_LANGUAGE]], (ancho_pantalla*3//4, alto_pantalla-ICONOS_SIZE+22))
    pantalla.blit(iconos_dificultad[opciones[CONFIG_LEVEL]], (ancho_pantalla*4//7, alto_pantalla-ICONOS_SIZE-5))

    display.flip()
    

    
def gestiona_eventos():
    global bMenu
    global opciones_visuales
    global opcion_seleccionada
    
    for evento in event.get():
        if evento.type == QUIT:
            bMenu = False
            quit() # pygame quit
            exit()                
            # Pulso la tecla ESC bJugando = False
        elif evento.type == KEYDOWN:
            if evento.key == K_DOWN:
                opcion_seleccionada += 1
                if opcion_seleccionada >= num_opciones_visuales:
                    opcion_seleccionada = 0
                reproducir_sonido(SONIDO_MENU,opciones[CONFIG_MUTE])
            elif evento.key == K_UP:
                opcion_seleccionada -= 1
                if opcion_seleccionada < 0:
                    opcion_seleccionada = num_opciones_visuales - 1
                reproducir_sonido(SONIDO_MENU,opciones[CONFIG_MUTE])
            elif evento.key in ( K_RETURN, K_SPACE):
                reproducir_sonido(SONIDO_MENU_SELECCION,opciones[CONFIG_MUTE])                    
                if opcion_seleccionada == OPCION_SONIDO_ON:
                    opciones[CONFIG_MUTE] = False
                elif opcion_seleccionada == OPCION_SONIDO_OFF:
                    opciones[CONFIG_MUTE] = True
                elif opcion_seleccionada == OPCION_N_0_JUGADORES:
                    opciones[CONFIG_N_JUGADORES] = 0
                elif opcion_seleccionada == OPCION_N_1_JUGADORES:
                    opciones[CONFIG_N_JUGADORES] = 1
                elif opcion_seleccionada == OPCION_N_2_JUGADORES:
                    opciones[CONFIG_N_JUGADORES] = 2
                elif opcion_seleccionada == OPCION_ESPANOL:
                    opciones[CONFIG_LANGUAGE] = 0
                elif opcion_seleccionada == OPCION_INGLES:
                    opciones[CONFIG_LANGUAGE] = 1
                elif opcion_seleccionada == OPCION_ALEMAN:
                    opciones[CONFIG_LANGUAGE] = 2
                elif opcion_seleccionada == OPCION_FACIL:
                    opciones[CONFIG_LEVEL] = 0
                elif opcion_seleccionada == OPCION_DIFICIL:
                    opciones[CONFIG_LEVEL] = 1
                elif opcion_seleccionada == OPCION_PESADILLA:
                    opciones[CONFIG_LEVEL] = 2                           
                elif opcion_seleccionada == OPCION_JUGAR:
                    bMenu=False # Jugamos
                elif opcion_seleccionada == OPCION_SALIR:
                    quit() # pygame quit
                    exit()

def show_menu(pantalla, clock):
    global  num_opciones_visuales

    for grupo_opciones in opciones_visuales[opciones[CONFIG_LANGUAGE]]:
        for _ in grupo_opciones:
            num_opciones_visuales += 1    

    while bMenu:

        gestiona_eventos()
                   
        dibuja_menu_simple(pantalla)
        clock.tick(60)        
    return opciones
