# game

from pygame import *
from random import randint
from time import sleep

from config import *
from utiles import draw_text, reproducir_sonido
from recursos import *

v = 1.5

print(f'{__name__} v{v}')

# variables globales

pelota_x = 0
pelota_y = 0
velocidad_pelota_x = 0
velocidad_pelota_y = 0

# reinicia la posición de la pelota y le da una nueva velocidad aleatoria
def pelota_centro():
    global pelota_x, pelota_y, velocidad_pelota_x, velocidad_pelota_y
    pelota_x = ancho_pantalla // 2
    pelota_y = alto_pantalla // 2

    velocidad_pelota_x = 0
    velocidad_pelota_y = 0

    while velocidad_pelota_x == 0 or velocidad_pelota_y == 0:
        velocidad_pelota_x = randint(0, MAX_VELOCIDAD)
        velocidad_pelota_y = randint(-MAX_VELOCIDAD, MAX_VELOCIDAD)    


def play_game(pantalla,clock, numero_jugadores, mute):
    global pelota_x, pelota_y, velocidad_pelota_x, velocidad_pelota_y    

    bJugando = True # se repite el bucle mientras jugamos

    velocidad_pelota_x = 0
    velocidad_pelota_y = 0

    pelota_x = ancho_pantalla // 2
    pelota_y = alto_pantalla // 2

    pelota_centro()

    raqueta1_x = 0
    raqueta1_y = alto_pantalla // 2

    velocidad_raqueta1_y = 0
    velocidad_raqueta2_y = 0

    raqueta_ancho = 20
    raqueta_alto = 120 

    raqueta2_x = ancho_pantalla - raqueta_ancho
    raqueta2_y = alto_pantalla // 2

    radio_pelota = 15

    puntos_jugador1 = 0
    puntos_jugador2 = 0


    while bJugando:
        
        # escuchar los eventos
        for evento in event.get():
            if evento.type == QUIT:
                bJugando = False
                # Pulso la tecla ESC bJugando = False
            elif evento.type == KEYDOWN: # se ha pulsado una tecla
                # print('Has pulsado:',evento.unicode)
                
                if evento.key == K_ESCAPE:
                    print('Nos vamos...')
                    bJugando = False
                # TODO: Tecla P para pausa
                # TODO: Tecla Q para salir
                # TODO: Tecla H para mostrar ayuda
                # tecla m mute sound
                elif evento.key == K_m:
                    mute = not mute
                    print(f'Mute {mute}')
                # teclas raqueta 1 W & S
                elif numero_jugadores > 0 and evento.key == K_w:
                    velocidad_raqueta1_y = -MAX_VELOCIDAD
                elif numero_jugadores > 0 and evento.key == K_s:
                    velocidad_raqueta1_y =  MAX_VELOCIDAD
                # teclas raqueta 2 UP & DOWN
                elif numero_jugadores == 2 and evento.key == K_UP:
                    velocidad_raqueta2_y = -MAX_VELOCIDAD
                elif numero_jugadores == 2 and evento.key == K_DOWN:
                    velocidad_raqueta2_y =  MAX_VELOCIDAD
                    
            elif evento.type == KEYUP: # se ha soltado una tecla
                # reseteamos las velocidades de las raquetas
                if numero_jugadores == 2 and evento.key == K_UP or evento.key == K_DOWN :
                    velocidad_raqueta2_y = 0
                elif numero_jugadores > 0 and evento.key == K_w or evento.key == K_s :
                    velocidad_raqueta1_y = 0

        if numero_jugadores < 2:
            if velocidad_pelota_x > 0 and pelota_y > raqueta2_y + raqueta_alto//2:
                velocidad_raqueta2_y = MAX_VELOCIDAD
            elif velocidad_pelota_x > 0 and pelota_y < raqueta2_y + raqueta_alto//2:
                velocidad_raqueta2_y = -MAX_VELOCIDAD
            else :
                velocidad_raqueta2_y = 0

        if numero_jugadores == 0:
            if velocidad_pelota_x <0 and pelota_y > raqueta1_y + raqueta_alto//2:
                velocidad_raqueta1_y = MAX_VELOCIDAD
            elif velocidad_pelota_x <0 and pelota_y < raqueta1_y + raqueta_alto//2:
                velocidad_raqueta1_y = -MAX_VELOCIDAD
            else :
                velocidad_raqueta1_y = 0

        # actualizamos la posición de la raqueta 1
        raqueta1_y += velocidad_raqueta1_y
        
        # Comprobamos límites raqueta 1
        if raqueta1_y < 0:
            raqueta1_y  = 0
        if raqueta1_y > alto_pantalla - raqueta_alto:
            raqueta1_y = alto_pantalla - raqueta_alto
            
        # actualizamos la posición de la raqueta 2
        raqueta2_y += velocidad_raqueta2_y
        
        # Comprobar límites raqueta 2
        if raqueta2_y < 0:
            raqueta2_y  = 0
        if raqueta2_y > alto_pantalla - raqueta_alto:
            raqueta2_y = alto_pantalla - raqueta_alto
        
        # calculamos y actualizamos
        
        # Actualizamos la posición de la pelota  
        pelota_x += velocidad_pelota_x
        pelota_y += velocidad_pelota_y
        
        # comprobamos rebotes de la pelota con las paredes de arriba y abajo
           
        if pelota_y < radio_pelota:
            reproducir_sonido(SONIDO_REBOTE_PARED,mute)        
            velocidad_pelota_y = -velocidad_pelota_y
           
        if pelota_y > alto_pantalla - radio_pelota:
            reproducir_sonido(SONIDO_REBOTE_PARED,mute)
            velocidad_pelota_y = -velocidad_pelota_y
           
        # Detección de colisión en la izquierda
        # colision raqueta 1
        if pelota_x < raqueta_ancho + radio_pelota:
            if raqueta1_y < pelota_y < raqueta1_y + raqueta_alto: # rebota en la raqueta
                velocidad_pelota_x = -velocidad_pelota_x
                reproducir_sonido(SONIDO_REBOTE_RAQUETA,mute)
                #esquina de arriba
            elif pelota_y < raqueta1_y and raqueta1_y - pelota_y   < radio_pelota:
                velocidad_pelota_x = -velocidad_pelota_x
                velocidad_pelota_y = -velocidad_pelota_y
                # esquina de abajo
            elif pelota_y > raqueta1_y and pelota_y - raqueta1_y   < radio_pelota:
                velocidad_pelota_x = -velocidad_pelota_x
                velocidad_pelota_y = -velocidad_pelota_y
        
        if pelota_x < radio_pelota:  # hemos perdido
            pelota_centro()
            puntos_jugador2 += 1
            print(f'Jugador 1: {puntos_jugador1} - Jugador 2: {puntos_jugador2}')

            reproducir_sonido(SONIDO_PUNTO,mute)
            sleep(2)

        if pelota_x > ancho_pantalla - (raqueta_ancho + radio_pelota):
            if raqueta2_y < pelota_y < raqueta2_y + raqueta_alto: # rebota en la raqueta
                velocidad_pelota_x = -velocidad_pelota_x
                reproducir_sonido(SONIDO_REBOTE_RAQUETA,mute) 
        if pelota_x > ancho_pantalla - radio_pelota:  # hemos perdido
            pelota_centro()
            puntos_jugador1 += 1
            print(f'Jugador 1: {puntos_jugador1} - Jugador 2: {puntos_jugador2}')

            reproducir_sonido(SONIDO_PUNTO,mute)
            sleep(2)
                
        # dibujo la pantalla
        pantalla.fill(BLACK)  # rellenamos el fondo de la pantalla de negro
        

        pantalla.blit( icono_mute if mute else icono_sound, (ancho_pantalla -ICONOS_SIZE-5, alto_pantalla-ICONOS_SIZE))
 
        pantalla.blit(iconos_n_jugadores[numero_jugadores], ( 5, alto_pantalla-ICONOS_SIZE-5))
        draw.rect(pantalla, WHITE, (ancho_pantalla // 2, 0, 10, alto_pantalla))
        
        draw.circle(pantalla, COLOR_BALL, (pelota_x, pelota_y), radio_pelota)
        draw.rect(pantalla, COLOR_PLAYER1 , (raqueta1_x, raqueta1_y, raqueta_ancho, raqueta_alto) )
        draw.rect(pantalla, COLOR_PLAYER2, (raqueta2_x, raqueta2_y, raqueta_ancho, raqueta_alto) )

        draw_text(pantalla, f'Player 1  {puntos_jugador1}', 30, ancho_pantalla // 6, FONT_SIZE*2//3, COLOR_PLAYER1, font_name = FUENTE_JUGADOR1)
        draw_text(pantalla, f'Player 2  {puntos_jugador2}', 30, ancho_pantalla * 3 // 5, FONT_SIZE, COLOR_PLAYER2, font_name = FUENTE_JUGADOR2)
        
        display.flip() # actualizamos la pantalla
        clock.tick(120)
