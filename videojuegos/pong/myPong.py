# Name: Pong by JLCQL
from pygame import *
# TODO: optimizar carga del modulo
# TODO: modo 1  jugador
from random import randint
from time import sleep

v = 0.9

# paleta en https://htmlcolorcodes.com/es/
BLACK = (0,0,0)
RED = (255,0,0)
PURPLE = (200,50,240)
GREEN = (55,236,0)
WHITE = (255,255,255)

numero_judadores = int(input('¿número de jugadores? (0/1/2) '))


init() # inicializamos pygame

# inicialización
ancho_pantalla = 640
alto_pantalla = 480

pantalla = display.set_mode( (ancho_pantalla, alto_pantalla) )

display.set_caption('Mi primer juego - Pong')


velocidad_pelota_x = 0
velocidad_pelota_y = 0

pelota_x = ancho_pantalla // 2
pelota_y = alto_pantalla // 2

# reinicia la posición de la pelota y le da una nueva velocidad aleatoria
def pelota_centro():
    global pelota_x, pelota_y, velocidad_pelota_x, velocidad_pelota_y
    pelota_x = ancho_pantalla // 2
    pelota_y = alto_pantalla // 2

    velocidad_pelota_x = velocidad_pelota_y = 0

    while velocidad_pelota_x == 0 or velocidad_pelota_y == 0:
        velocidad_pelota_x = randint(0,5)
        velocidad_pelota_y = randint(-5,5)    

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


clock = time.Clock()

# Sonido
mixer.init()

def reproducir_sonido(ruta):
    mixer.music.load(ruta)
    mixer.music.play()



    
bJugando = True # se repite el bucle mientras jugamos

while bJugando:
    
    # escuchar los eventos
    for evento in event.get():
        if evento.type == QUIT:
            bJugando = False
            # Pulso la tecla ESC bJugando = False
            # TODO: detectar la tecla pulsada
        elif evento.type == KEYDOWN: # se ha pulsado una tecla
            # print('Has pulsado:',evento.unicode)
            
            if evento.key == K_ESCAPE:
                print('Nos vamos...')
                bJugando = False
            # teclas raqueta 1 W & S
            elif numero_judadores> 0 and evento.key == K_w:
                velocidad_raqueta1_y = -10
            elif numero_judadores> 0 and evento.key == K_s:
                velocidad_raqueta1_y =  10
            # teclas raqueta 2 UP & DOWN
            elif numero_judadores == 2 and evento.key == K_UP:
                velocidad_raqueta2_y = -10
            elif numero_judadores == 2 and evento.key == K_DOWN:
                velocidad_raqueta2_y =  10
                
        elif evento.type == KEYUP: # se ha soltado una tecla
            # reseteamos las velocidades de las raquetas
            if numero_judadores == 2 and evento.key == K_UP or evento.key == K_DOWN :
                velocidad_raqueta2_y = 0
            elif numero_judadores> 0 and evento.key == K_w or evento.key == K_s :
                velocidad_raqueta1_y = 0

    if numero_judadores < 2:
        if velocidad_pelota_x > 0 and pelota_y > raqueta2_y + raqueta_alto//2:
            velocidad_raqueta2_y = 5
        elif velocidad_pelota_x > 0 and pelota_y < raqueta2_y + raqueta_alto//2:
            velocidad_raqueta2_y = -5
        else :
            velocidad_raqueta2_y = 0

    if numero_judadores == 0:
        if velocidad_pelota_x <0 and pelota_y > raqueta1_y + raqueta_alto//2:
            velocidad_raqueta1_y = 5
        elif velocidad_pelota_x <0 and pelota_y < raqueta1_y + raqueta_alto//2:
            velocidad_raqueta1_y = -5
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
        reproducir_sonido('boing-pared.mp3')        
        velocidad_pelota_y = -velocidad_pelota_y
       
    if pelota_y > alto_pantalla - radio_pelota:
        reproducir_sonido('boing-pared.mp3')
        velocidad_pelota_y = -velocidad_pelota_y
       

    # Detección de colisión en la izquierda
    # colision raqueta 1
    if pelota_x < raqueta_ancho + radio_pelota:
        if raqueta1_y < pelota_y < raqueta1_y + raqueta_alto: # rebota en la raqueta
            velocidad_pelota_x = -velocidad_pelota_x
            reproducir_sonido('boing-raqueta.mp3')

    if pelota_x < radio_pelota:  # hemos perdido
        # TODO: sonido perder
        pelota_centro()
        puntos_jugador2 += 1
        print(f'Jugador 1: {puntos_jugador1} - Jugador 2: {puntos_jugador2}')
        # TODO: mostrar puntos dibujados
        reproducir_sonido('sonido-punto.mp3')
        sleep(2)

    if pelota_x > ancho_pantalla - (raqueta_ancho + radio_pelota):
        if raqueta2_y < pelota_y < raqueta2_y + raqueta_alto: # rebota en la raqueta
            velocidad_pelota_x = -velocidad_pelota_x
            reproducir_sonido('boing-raqueta.mp3') # TODO: definir variables nombres de sonidos
    if pelota_x > ancho_pantalla - radio_pelota:  # hemos perdido
        # TODO: sonido perder
        pelota_centro()
        puntos_jugador1 += 1
        print(f'Jugador 1: {puntos_jugador1} - Jugador 2: {puntos_jugador2}')
        # TODO: mostrar puntos dibujados
        reproducir_sonido('sonido-punto.mp3')
        sleep(2)
            
    # dibujo la pantalla
    pantalla.fill(BLACK)  # rellenamos el fondo de la pantalla de negro
    
    draw.circle(pantalla, PURPLE, (pelota_x, pelota_y), radio_pelota)
    draw.rect(pantalla, RED, (raqueta1_x, raqueta1_y, raqueta_ancho, raqueta_alto) )
    draw.rect(pantalla, GREEN, (raqueta2_x, raqueta2_y, raqueta_ancho, raqueta_alto) )
    
    display.flip() # actualizamos la pantalla
    clock.tick(60)
    
quit() # cerramos pygame
print('Adiós')