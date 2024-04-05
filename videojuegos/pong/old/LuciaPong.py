# PONG by JLCQL

from pygame import *
# TODO: optimizar carga del modulo
# TODO: modo multijugador o contra-ordenador
from random import randint
from time import sleep
v = 0.2

bJugando = True


# inicializaciónWarning

ancho_x = 640
alto_y = 480

# paleta en https://htmlcolorcodes.com/es/

NEGRO = (0,0,0)
ROJO = (255,0,0)
MORADO = (250,50,240)
VERDE = (55,236,0)
BLANCO = (255,255,255)

init()

pantalla = display.set_mode((ancho_x, alto_y))

display.set_caption('Mi primer juego - PONG')

# RELOJ
clock = time.Clock()

# PUNTOS
puntos_jugador1 = 0
puntos_jugador2 = 0

# PELOTA
pelota_x = ancho_x // 2
pelota_y = alto_y // 2
radio = 15

velocidad_pelota_x = 0
velocidad_pelota_y = 0

def pelota_centro ():
    global pelota_x, pelota_y, velocidad_raqueta1_y, velocidad_pelota_x, velocidad_pelota_y
    pelota_x = ancho_x // 2
    pelota_y = alto_y // 2
    velocidad_pelota_x = 0
    velocidad_pelota_y = 0
    while velocidad_pelota_x == 0 or velocidad_pelota_y == 0:
        velocidad_pelota_x = randint (5,7)
        velocidad_pelota_y = randint (-5,7)
    print(velocidad_pelota_y)

pelota_centro()

#RAQUETAS
raqueta_ancho= 20
raqueta_alto= 110

raqueta1_x = 0
raqueta1_y = alto_y//2

raqueta2_x = ancho_x - raqueta_ancho
raqueta2_y = alto_y//2

velocidad_raqueta1_y = 0
velocidad_raqueta2_y = 0

# MÚSICA
mixer.init()
def reproducir_sonido (ruta):
    mixer.music.load(ruta)
    mixer.music.play()

# JUGADORES
numero_players = int(input('Número de jugadores? (1/2): '))
if numero_players == 1:
    print('Función no implementada ahora mismo. Estamos trabajando en ello')
    exit()


while bJugando:
    # escuchar eventos
    for evento in event.get():
        if evento.type == QUIT:
            bJugando = False
            # si pulso la tecla ESC bJugando = False
        elif evento.type == KEYDOWN: # se ha pulsado un tecla
            if evento.key == K_ESCAPE:
                print('Nos vamos...')
                bJugando = False
               
            elif  evento.key == K_UP: # FLECHA ARRIBA
                velocidad_raqueta1_y = -10
               
            elif  evento.key == K_DOWN:# FLECHA ABAJO
                velocidad_raqueta1_y = 10
               
            elif  evento.key == K_w: # TECLA ARRIBA (w)
                velocidad_raqueta2_y = -10
               
            elif  evento.key == K_s: # TECLA ABAJO (s)
                velocidad_raqueta2_y = 10
        elif evento.type == KEYUP: #se suelta la tecla
           
            if evento.key == K_UP or evento.key == K_DOWN:
                velocidad_raqueta1_y = 0
            elif evento.key == K_w or evento.key == K_s:
                velocidad_raqueta2_y = 0
   
    pelota_x += velocidad_pelota_x
    pelota_y += velocidad_pelota_y
   
# Comprobando
    # MOVIMIENTO RAUQUETA 1
    raqueta1_y += velocidad_raqueta1_y
    if raqueta1_y < 0:
        raqueta1_y = 0
    if raqueta1_y > alto_y - raqueta_alto:
        raqueta1_y = alto_y - raqueta_alto
   
    # MOVIMIENTO RAUQUETA 2
    raqueta2_y += velocidad_raqueta2_y
    if raqueta2_y < 0:
        raqueta2_y = 0
    if raqueta2_y > alto_y - raqueta_alto:
        raqueta2_y = alto_y - raqueta_alto
   
   
    # calculamos y actualizamos
    if pelota_x < radio:
        reproducir_sonido('boing_pared.mp3')
        velocidad_pelota_x = -velocidad_pelota_x
       
    if pelota_y < radio:
        reproducir_sonido('boing_pared.mp3')
        velocidad_pelota_y = -velocidad_pelota_y
       
    if pelota_x > ancho_x - radio:
        reproducir_sonido('boing_pared.mp3')
        velocidad_pelota_x = -velocidad_pelota_x
       
    if pelota_y > alto_y - radio:
        reproducir_sonido('boing_pared.mp3')
        velocidad_pelota_y = -velocidad_pelota_y
   
   
# DETECCIÓN DE COLISIÓN
    # colisión raqueta 1
    if pelota_x < raqueta_ancho + radio:
        if raqueta1_y < pelota_y < raqueta1_y + raqueta_alto:
            velocidad_pelota_x = - velocidad_pelota_x
            reproducir_sonido('boing-raqueta.mp3')
       
        else : # hemo perdido :(
            #TODO: sonido perdedor
            pelota_centro()
            puntos_jugador2 += 1
            print (f'JUGADOR 1 : {puntos_jugador1}  |  JUGADOR 2: {puntos_jugador2}')
            reproducir_sonido('sonido-punto.mp3')
            sleep(2)
           
    # colisión raqueta 2      
    if pelota_x > ancho_x - (raqueta_ancho + radio):
        if raqueta2_y < pelota_y < raqueta2_y + raqueta_alto:
            velocidad_pelota_x = - velocidad_pelota_x
            reproducir_sonido('boing-raqueta.mp3')
       
        else : # hemo perdido :(
            #TODO: sonido perdedor
            pelota_centro()
            puntos_jugador2 += 1
            print (f'JUGADOR 1 : {puntos_jugador1}  |  JUGADOR 2: {puntos_jugador2}')
            reproducir_sonido('sonido-punto.mp3')
            sleep(2)
       
    # dibujo la pantalla
    pantalla.fill(NEGRO)
    draw.circle(pantalla,BLANCO, (pelota_x, pelota_y), radio)
    draw.rect(pantalla, ROJO, (raqueta1_x, raqueta1_y, raqueta_ancho, raqueta_alto))
    draw.rect(pantalla, VERDE, (raqueta2_x, raqueta2_y, raqueta_ancho, raqueta_alto))

    #TODO: ajustar FPS
    display.flip()
    clock.tick(60)

quit() #cerramos el programa
print('Adiós')