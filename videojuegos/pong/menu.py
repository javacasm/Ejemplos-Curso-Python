# Sistema de menús para pygame
from pygame import *

from config import *
from utiles import draw_text, reproducir_sonido
from recursos import *

v = 1.5

print(f'{__name__} v{v}')

opciones_visuales = ['Sonido On','Sonido Off',
                     '0 Jugadores','1 Jugador','2 Jugadores',
                     'Jugar','Salir']

opciones = {CONFIG_MUTE:False,CONFIG_N_JUGADORES:0}

def show_menu(pantalla, clock):

    bMenu = True

    opcion_seleccionada = 0

    while bMenu:

        for evento in event.get():
            if evento.type == QUIT:
                bMenu = False
                # Pulso la tecla ESC bJugando = False
                # TODO: detectar la tecla pulsada
            elif evento.type == KEYDOWN:
                if evento.key == K_DOWN:
                    opcion_seleccionada += 1
                    if opcion_seleccionada >= len(opciones_visuales):
                        opcion_seleccionada = 0
                    reproducir_sonido(SONIDO_MENU,opciones[CONFIG_MUTE])
                elif evento.key == K_UP:
                    opcion_seleccionada -= 1
                    if opcion_seleccionada < 0:
                        opcion_seleccionada = len(opciones_visuales) - 1
                    reproducir_sonido(SONIDO_MENU,opciones[CONFIG_MUTE])
                elif evento.key in ( K_RETURN, K_SPACE):
                    reproducir_sonido(SONIDO_MENU_SELECCION,opciones[CONFIG_MUTE])                    
                    if opcion_seleccionada == 0:
                        opciones[CONFIG_MUTE] = False
                    elif opcion_seleccionada == 1:
                        opciones[CONFIG_MUTE] = True
                    elif opcion_seleccionada == 2:
                        opciones[CONFIG_N_JUGADORES] = 0
                    elif opcion_seleccionada == 3:
                        opciones[CONFIG_N_JUGADORES] = 1
                    elif opcion_seleccionada == 4:
                        opciones[CONFIG_N_JUGADORES] = 2                        
                    elif opcion_seleccionada == 5:
                        bMenu=False # Jugamos
                    elif opcion_seleccionada == 6:
                        quit() # pygame quit
                        exit()
                   
        # dibujando menú
    

        pantalla.fill(COLOR_FONDO_MENU)  # rellenamos el fondo de la pantalla de negro
     
        altura_opcion = alto_pantalla//(len(opciones_visuales)+1)
        for indice,texto_opcion in enumerate(opciones_visuales):
            draw_text(pantalla, texto_opcion,
                      altura_opcion//2, 200, 50 + indice*altura_opcion,
                      COLOR_OPCION_SELECCIONADA if indice == opcion_seleccionada else COLOR_OPCION,
                      FUENTE_MENU)              

        pantalla.blit(icono_mute if opciones[CONFIG_MUTE] else icono_sound, (ancho_pantalla-ICONOS_SIZE-5, alto_pantalla-ICONOS_SIZE))
        pantalla.blit(iconos_n_jugadores[opciones[CONFIG_N_JUGADORES]], ( 5, alto_pantalla-ICONOS_SIZE-5))
        clock.tick(60)
        display.flip()
        
    return opciones
