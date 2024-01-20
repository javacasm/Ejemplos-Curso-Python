'''
   /*!
    * author: by

    * using:
    * guizero: "https://github.com/lawsie/guizero"

    * import guizero docs:
    * https://lawsie.github.io/guizero/layout/

    * version: 1.1b-prev1
    */
'''
# properties


from guizero import *

import os

v = "1.1b-prev3"

_width = 9050
_height = 1050

numero_imagen = 0
lista_imagenes = []

print ("Version: ", v)


# end
################################################
# def functions
def update_bg():
    filexapp.bg = themecmb.value
    debug()

def update_text():
    filexapp.text_color = fontcmb.value
    debug()

def debug():
    if(filexapp.text_color == filexapp.bg):
        if(filexapp.bg == "black"):
            filexapp.text_color = "white"
        else:
            filexapp.text_color = "black"

def update():
    global lista_imagenes, numero_imagen # usamos la variable lista_imagenes como global
    # reincializamos el aspecto del interface
    filexapp.bg = "white"
    filexapp.text_color = "black"
    # recargamos la lista de imágenes
    lista_imagenes = os.listdir(directory.value)
    print(lista_imagenes)

def showImage():     # actualizar la imagen
    global lista_imagenes, numero_imagen # usamos la variable lista_imagenes como global
    vsimg.image = directory.value + lista_imagenes[numero_imagen]
    
def next_image():
    global numero_imagen
    numero_imagen = numero_imagen + 1
    # comprobar si nos hemos pasado
    showImage()
    

def prev_image():
    global numero_imagen
    numero_imagen = numero_imagen - 1
    # comprobar si nos hemos pasado
    showImage()
    
#end def
###############################################
# Arrays

color = ["black", "white", "red", "green", "blue", "purple", "gray31"]

#end Arrays
###############################################
# app declare

filexapp = App(layout="grid", title="Filex", width=_width, height=_height)


#end declare
###############################################
#app properties


# end
###############################################
#begin app
###############################################
# begin line 1

text = Text(filexapp, text="carpeta:      ", grid=[0, 0])
directory = TextBox(filexapp, text="images/", grid=[1, 0], width=100)
p1 = Text(filexapp, text="         ", grid=[2, 0])
rcbtn = PushButton(filexapp, image="iconos/recargar.png", command=update, grid=[3, 0], align="right")

p2 = Text(filexapp, text="         Color fuente:", grid=[4, 0])
fontcmb = Combo(filexapp, options=color, command=update_text, selected=filexapp.text_color, grid=[5, 0], align="right")
p3 = Text(filexapp, text="         Color fondo:", grid=[6, 0])
themecmb = Combo(filexapp, options=color, command=update_bg, selected=filexapp.bg, grid=[7, 0], align="right")

# end
###############################################
# begin line 2
try:
    update() # recargamos la lista de imágenes
    
    prevbtn = PushButton(filexapp, image="iconos/left-arrow.png", command=prev_image, grid=[0,1])

    vsimg = Picture(filexapp, grid=[1, 1], image=directory.value+lista_imagenes[numero_imagen], width=500, height=500)

    nextbtn = PushButton(filexapp, image="iconos/right-arrow.png", command=next_image, grid=[3,1], align="right")
except Exception as e:
    print("error 001: can't find image:",e)
    filexapp.warn('Error:',str(e))

#end
###############################################
filexapp.display()
###############################################
#end app


