# Name: Pong
# By Group: JLCQL (Jose, Lucia, Carlos, Queralt, Luis)
# Version: 0.1
version = 0.1

# print version
print(version)

# includes libraries: pygame
from pygame import *
# TODO: optimize module charge

# declare play as True
play = True

# begin

# declare width as 640
width = 640
# declare height as 480
height = 480

init() # init pygame

#define colors
#color pallete by https://htmlcolorcodes.com/es/
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (125, 0, 125)
yellow = (125, 125, 0)
white = (255, 255,255)

#declare window as display mode as width, height
window = display.set_mode( (width, height) )

# set title: Pong
display.set_caption('Pong')

# declare ballx as width // 2
pin1x = 4
pin2x = width-24
ballx = width//2;
# declare bally as height // 2
pin1y = height//2
pin2y = height//2
bally = height//2;
# declare radio as size
radio = 90

pulsedKU1 = False
pulsedKD1 = False
pulsedKU2 = False
pulsedKD2 = False
canEneable = True
mov = 1/10
dif = 1

# loop
while play:
    # listen the events
    for eventListener in event.get():
        if eventListener.type == QUIT:
            play = False
        elif eventListener.type == KEYDOWN:
            if eventListener.key == K_ESCAPE:
                play = False
            elif eventListener.key == K_UP:
                pulsedKU1 = True
            elif eventListener.key == K_DOWN:
                pulsedKD1 = True
        elif eventListener.type == KEYUP:
            if eventListener.key == K_UP:
                pulsedKU1 = False
            elif eventListener.key == K_DOWN:
                pulsedKD1 = False 
        
    if pulsedKU1:
        pin1y -= mov
    elif pulsedKD1:
        pin1y += mov
    
    if pulsedKD1 or pulsedKU1:
        canEneable = not canEneable
    # calculate and update
    if pin1y < 0:
        pin1y += mov
    if pin1y > height - mov * height * 1.75:
        pin1y -= mov
    ballx -= mov/3
    # TODO: ballx adjustament to border not pass
    # draw the window
    window.fill(black)
    #draw bar
    draw.rect(window, white, Rect(pin1x, pin1y, 20, radio))
    draw.rect(window, white, Rect(pin2x, pin2y, 20, radio))
    draw.circle(window, white, (ballx, bally), radio/9)
    #update window
    display.flip()
    #TODO: ACTUALIZAR FPS

quit()