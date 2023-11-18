#---------------------------------#')
###   Alberto Vega - NOV 2023   ###')
###       explodeGlobes v1      ###')
#---------------------------------#')

"""Juego de explotar globos moviendo el punto
de mira con el ratón y disparando con el botón
izquierdo o con la barra espaciadora. Faltaría
poner un tiempo, controlar nº de aciertos, .."""

import pygame
import random
# pip3 install pygame o instalar paquete desde el entorno ( Thonny por ejemplo )
# https://www.pygame.org/docs/ -> DOCUMENTACIÓN

print('---------------------------------')
print('##   Alberto Vega - NOV 2023   ##')
print('##       explodeGlobes v1      ##')
print('---------------------------------\n')

ancho = 640           # Ancho de la ventana
alto = 640            # Alto de la ventana
xPosGlobo = ancho/2   # Posición X del globo
yPosGlobo = alto      # Posición Y del globo
velGlobo = 2          # Velocidad del globo 
xPosMira = ancho/2    # X del centro del punto de mira
yPosMira = alto/2     # Y del centro del punto de mira
imgFondo = pygame.image.load('./data/fondo.jpg') # 640 x 640 px -> Fondo
imgGlobo = pygame.image.load('./data/globo.png') # 85 x 128 px -> Globo
black = (0,0,0)       # negro RGB
red = (255,0,0)       # rojo RGB
velGlobo = 5          # Velocidad del globo
reloj = pygame.time.Clock() # reloj para controlar los fps
fps = 30*velGlobo     # frames por segundo

# Audio
# mixer = módulo para cargar y reproducir sonidos
pygame.mixer.init()
pygame.mixer.music.load('./data/disparo.ogg') # Audio .ogg
pygame.mixer.music.set_volume(0.5 ) # volumen entre 0 y 1.0

def nuevoGlobo():
    # Nueva posición aleatoria del globo
    # Imagen de 85 x 128 px
    global xPosGlobo, yPosGlobo
    xPosGlobo = random.randrange(0, ancho-85,1) # Posición X del globo
    yPosGlobo = alto-20

def puntoMira(color):
    # Capturamos la posición X e Y del ratón
    global xPosMira, yPosMira
    xPosMira, yPosMira = pygame.mouse.get_pos() 
    # Nueva posición del punto de mira
    pygame.draw.circle(pantalla, color, (xPosMira, yPosMira), 25,3)
    # circle -> pantalla, color RGB, centro, radio, grosor
    pygame.draw.line(pantalla, color, (xPosMira-30, yPosMira), (xPosMira+30,yPosMira), 3) # Horizontal
    pygame.draw.line(pantalla, color, (xPosMira, yPosMira-30), (xPosMira,yPosMira+30), 3) # Vertical
    # line -> pantalla, color, inicio, fin, grosor px
    
def disparo():
    # Sonido del disparo
    pygame.mixer.music.play()
    # Actualizamos el punto de mira
    puntoMira(red) # Al disparar -> rojo
    pygame.display.flip() # Refrescamos la pantalla
    pygame.time.delay(20) # Retardo de 20 mseg
    # Comprobamos si hubo puntería
    if ((xPosMira>=xPosGlobo) and (xPosMira<=xPosGlobo+85)): # Ancho globo 85 px
        if ((yPosMira>=yPosGlobo) and (yPosMira<=yPosGlobo+128)): # Alto globo 128 px
            # Tiro dentro del globo
            # puntos+=1; // Puntuación en el juego..
            nuevoGlobo()

# Inicializa el entorno de pygame
pygame.init() 

# Creamos la ventana
pantalla = pygame.display.set_mode((ancho, alto)) # Crea la ventana
pygame.display.set_caption('explodeGlobes v1.0')  # Cambia el título

# Ocultamos el cursor del ratón (usamos un punto de mira)
pygame.mouse.set_visible(0)

running = True
while running: # Bucle infinito
    
    # El globo siempre asciende ..
    yPosGlobo-=velGlobo # Podíamos usar una variable
    if (yPosGlobo<0):
        nuevoGlobo()
    
    # Control de eventos   
    for event in pygame.event.get():
        
        # Cierre de la ventana
        if event.type == pygame.QUIT:
            running = False
        
        # Pulsaciones del ratón
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Botón izquierdo pulsado
                disparo()

        # Pulsaciones del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Barra espaciadora
                disparo()
     
    # Posicionamos elementos
    pantalla.blit(imgFondo,(0, 0)) # Fondo
    pantalla.blit(imgGlobo,(xPosGlobo, yPosGlobo)) # Globo
    puntoMira(black) # Punto de mira en negro
    
    # Refrescamos la pantalla
    reloj.tick(fps) # fps
    pygame.display.flip()

pygame.quit()