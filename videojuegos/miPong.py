# Name: Pong by JLCQL

from pygame import *
# TODO: optimizar carga del modulo

v = 0.1



bJugando = True

# inicialización


ancho = 640
alto = 480

# paleta en https://htmlcolorcodes.com/es/

black = (0,0,0)
red = (255,0,0)
purple = (200,50,240)
green = (55,236,0)

init() # inicializamos pygame

pantalla = display.set_mode( (ancho, alto) )

display.set_caption('Mi primer juego - Pong')

pelota_x = ancho // 2
pelota_y = alto // 2

radio = 15

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
            elif evento.key == K_LEFT:
                pelota_x = pelota_x - 10
            elif evento.key == K_RIGHT:
                pelota_x +=  10
            elif evento.key == K_UP:
                pelota_y -=  10
            elif evento.key == K_DOWN:
                pelota_y +=  10                
    # print(pelota_x,pelota_y)
    
    # calculamos y actualizamos
    if pelota_x < radio:
       pelota_x = radio 
    if pelota_y < radio:
       pelota_y = radio
    if pelota_x > ancho - radio:
       pelota_x = ancho - radio
    if pelota_y > alto - radio:
       pelota_y = alto - radio

    # dibujo la pantalla
    pantalla.fill(black)
    
    draw.circle(pantalla, purple, (pelota_x, pelota_y), radio) 
    
    # TODO: ajustar FPS
    
    display.flip() # actualizamos la pantalla
    
quit() # cerramos pygame
print('Adiós')
