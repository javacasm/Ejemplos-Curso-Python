# game

from pygame import *
from random import randint
from time import sleep

from config import *
from utiles import draw_text, reproducir_sonido
from recursos import *

v = 1.7

print(f'{__name__} v{v}')

# variables globales

pelota_x = 0
pelota_y = 0
velocidad_pelota_x = 0
velocidad_pelota_y = 0

velocidad_paleta = MAX_VELOCIDAD

radio_pelota = 15

puntos_jugador1 = 0
puntos_jugador2 = 0

velocidad_pelota_x = 0
velocidad_pelota_y = 0

pelota_x = ancho_pantalla // 2
pelota_y = alto_pantalla // 2

raqueta1_x = 0
raqueta1_y = alto_pantalla // 2

velocidad_raqueta1_y = 0
velocidad_raqueta2_y = 0

raqueta_ancho = 20
raqueta_alto = 120 

raqueta2_x = ancho_pantalla - raqueta_ancho
raqueta2_y = alto_pantalla // 2

bPausa = False
bShowHelp = False
bJugando = True # se repite el bucle mientras jugamos

numero_jugadores = 0
dificultad = 0
mute = False
idioma = 0

# reinicia la posición de la pelota y le da una nueva velocidad aleatoria
def pelota_centro():
    global pelota_x, pelota_y, velocidad_pelota_x, velocidad_pelota_y
    pelota_x = ancho_pantalla // 2
    pelota_y = alto_pantalla // 2

    velocidad_pelota_x = 0
    velocidad_pelota_y = 0

    while velocidad_pelota_x == 0 or velocidad_pelota_y == 0:
        velocidad_pelota_x = randint(0, velocidad_paleta)
        velocidad_pelota_y = randint(-velocidad_paleta, velocidad_paleta)    

def dibuja_pantalla(pantalla):
    # global pelota_x, pelota_y, bPausa
    
    # dibujo la pantalla
    #pantalla.fill(BLACK)  # rellenamos el fondo de la pantalla de negro
    pantalla.blit(fondo, (0,0))

    pantalla.blit(icono_mute if mute else icono_sound, (ancho_pantalla -ICONOS_SIZE-5, alto_pantalla-ICONOS_SIZE))

    pantalla.blit(iconos_n_jugadores[numero_jugadores], ( 5, alto_pantalla-ICONOS_SIZE-5))
    pantalla.blit(iconos_idiomas[idioma], (ancho_pantalla*3//4, alto_pantalla-ICONOS_SIZE+22))
    pantalla.blit(iconos_dificultad[dificultad], (ancho_pantalla*4//7, alto_pantalla-ICONOS_SIZE-5))

    # línea central
    draw.rect(pantalla, WHITE, (ancho_pantalla // 2, 0, 10, alto_pantalla))
    
    # pelota
    draw.circle(pantalla, COLOR_BALL, (pelota_x, pelota_y), radio_pelota)
    
    # raquetas
    #draw.rect(pantalla, COLOR_PLAYER1 , (raqueta1_x, raqueta1_y, raqueta_ancho, raqueta_alto) )
    pantalla.blit(icono_raqueta1,(raqueta1_x,raqueta1_y))
    #draw.rect(pantalla, COLOR_PLAYER2, (raqueta2_x, raqueta2_y, raqueta_ancho, raqueta_alto) )
    pantalla.blit(icono_raqueta2,(raqueta2_x,raqueta2_y))
    
    # marcador
    draw_text(pantalla, f'{str_Player[idioma]} 1  {puntos_jugador1}', 30, ancho_pantalla // 6, FONT_SIZE*2//3, COLOR_PLAYER1, font_name = FUENTE_JUGADOR1)
    draw_text(pantalla, f'{str_Player[idioma]} 2  {puntos_jugador2}', 30, ancho_pantalla * 3 // 5, FONT_SIZE, COLOR_PLAYER2, font_name = FUENTE_JUGADOR2)

    if bPausa:
        draw_text(pantalla, f'{str_pausa[idioma]}', alto_pantalla//3, 0, FONT_SIZE*2, COLOR_PLAYER2, font_name = FUENTE_JUGADOR2)

    if bShowHelp:
        
        altura_opcion = alto_pantalla//(len(ayuda_str[idioma])+1 +4)
        draw_text(pantalla, f'{str_ayuda_titulo[idioma]}', altura_opcion*3, FONT_SIZE*5, FONT_SIZE*2, COLOR_AYUDA, font_name = FUENTE_JUGADOR2)
        indice = 0
        for texto_ayuda in ayuda_str[idioma]:
            draw_text(pantalla, texto_ayuda,
                      altura_opcion//2, ancho_pantalla//3, (indice+4)*altura_opcion,
                      COLOR_AYUDA,
                      FUENTE_MENU)
            indice += 1        

    display.flip() # actualizamos la pantalla

def actualiza_estado():
    
    global pelota_x, pelota_y, velocidad_pelota_x, velocidad_pelota_y, velocidad_paleta
    # global mute, numero_jugadores, dificultad, idioma
    global raqueta1_y, raqueta2_y
    global puntos_jugador1, puntos_jugador2
    global velocidad_pelota_x, velocidad_pelota_y
    global velocidad_raqueta1_y , velocidad_raqueta2_y
    
    if dificultad == 2:
        velocidad_paleta = MAX_VELOCIDAD
    elif dificultad == 1:
        velocidad_paleta = MAX_VELOCIDAD // 2
    else:
        velocidad_paleta = MAX_VELOCIDAD // 4
     
    if numero_jugadores < 2:
        if velocidad_pelota_x > 0 and pelota_y > raqueta2_y + raqueta_alto//2:
            velocidad_raqueta2_y = velocidad_paleta
        elif velocidad_pelota_x > 0 and pelota_y < raqueta2_y + raqueta_alto//2:
            velocidad_raqueta2_y = -velocidad_paleta
        else :
            velocidad_raqueta2_y = 0

    if numero_jugadores == 0:
        if velocidad_pelota_x <0 and pelota_y > raqueta1_y + raqueta_alto//2:
            velocidad_raqueta1_y = velocidad_paleta
        elif velocidad_pelota_x <0 and pelota_y < raqueta1_y + raqueta_alto//2:
            velocidad_raqueta1_y = -velocidad_paleta
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
    
def gestiona_eventos():
    global bJugando, bPausa, bShowHelp
    global mute, numero_jugadores, dificultad, idioma
    global velocidad_raqueta1_y, velocidad_raqueta2_y
   # escuchar los eventos
    for evento in event.get():
        if evento.type == QUIT:
            bJugando = False
            # Pulso la tecla ESC bJugando = False
        elif evento.type == KEYDOWN: # se ha pulsado una tecla
            # print('Has pulsado:',evento.unicode)
            
            if evento.key in (K_ESCAPE, K_q):
                print('Nos vamos...')
                bJugando = False
            if evento.key == K_p:
                bPausa = not bPausa
            elif evento.key == K_h:
                bShowHelp = not bShowHelp
            elif evento.key == K_0:
                numero_jugadores = 0
            elif evento.key == K_1:
                numero_jugadores = 1
            elif evento.key == K_2:
                numero_jugadores = 2
            elif evento.key == K_f:
                dificultad = 0
            elif evento.key == K_d:
                dificultad = 1
            elif evento.key == K_g:
                dificultad = 2
            elif evento.key == K_e:
                idioma = 0
            elif evento.key == K_n:
                idioma = 1
            elif evento.key == K_a:
                idioma = 2
            # TODO: Tecla God Mode
            # tecla m mute sound
            elif evento.key == K_m:
                mute = not mute
                print(f'Mute {mute}')
            # teclas raqueta 1 W & S
            elif numero_jugadores > 0 and evento.key == K_w:
                velocidad_raqueta1_y = -velocidad_paleta
            elif numero_jugadores > 0 and evento.key == K_s:
                velocidad_raqueta1_y =  velocidad_paleta
            # teclas raqueta 2 UP & DOWN
            elif numero_jugadores == 2 and evento.key == K_UP:
                velocidad_raqueta2_y = -velocidad_paleta
            elif numero_jugadores == 2 and evento.key == K_DOWN:
                velocidad_raqueta2_y =  velocidad_paleta
                
        elif evento.type == KEYUP: # se ha soltado una tecla
            # reseteamos las velocidades de las raquetas
            if numero_jugadores == 2 and evento.key == K_UP or evento.key == K_DOWN :
                velocidad_raqueta2_y = 0
            elif numero_jugadores > 0 and evento.key == K_w or evento.key == K_s :
                velocidad_raqueta1_y = 0


def play_game(pantalla,clock):      

    print(f'Jugadores:{numero_jugadores} idioma:{idioma} nivel:{dificultad} mute:{mute}')

    pelota_centro()

    while bJugando:
        
        gestiona_eventos()
 
        if not bPausa and not bShowHelp:
            actualiza_estado()
                
        dibuja_pantalla(pantalla)
        
        clock.tick(120)
