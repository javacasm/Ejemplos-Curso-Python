'''
   /*!
    * author: by Luis, Carlos, Lucía, Queralt & JAVacasM

    * using:
    * guizero: "https://github.com/lawsie/guizero"

    * import guizero docs:
    * https://lawsie.github.io/guizero/layout/

    * version: 1.3
    */
'''
# properties


from guizero import *

import os

v = "1.3"

_width = 1400
_height = 800

numero_imagen = 0
lista_imagenes = []

print ("Version: ", v)


# end
################################################
# def functions
def update_bg():
    filexapp.bg = themecmb.value
    check_color()

def update_text():
    filexapp.text_color = fontcmb.value
    check_color()

# comprueba que los colores sean válidos
def check_color():
    if(filexapp.text_color == filexapp.bg):
        if(filexapp.bg == "black"):
            filexapp.text_color = "white"
        else:
            filexapp.text_color = "black"
    # TODO: comprobar iconos blanco o negros
    
# reincializamos el aspecto del interface
def update_theme():
    filexapp.bg = "white"
    filexapp.text_color = "black"

valid_extensions = ('.gif','.jpg','.png','.jpeg')
# recargamos la lista de imágenes
def update_images():
    global lista_imagenes, numero_imagen # usamos la variable lista_imagenes como global
    
    lista_imagenes = []
    for file in os.listdir(directory.value):
        filename,extension = os.path.splitext(file)
        if extension in valid_extensions:
            lista_imagenes.append(file)
        else:
            print(f'{file} is not a valid image')
    print(lista_imagenes)

# Actualiza la lista de imágenes y tema
def update():
    update_images()
    update_theme()

# actualizar la imagen que se muestra
def show_image():     
    global lista_imagenes, numero_imagen # usamos la variable lista_imagenes como global
    try:
        vsimg.image = directory.value + "/" + lista_imagenes[numero_imagen]
        textImagenName.value = lista_imagenes[numero_imagen]
    except Exception as e:
        print("Error:",e)
        filexapp.error('Error:',str(e))

# muestra la imagen siguiente
def next_image():
    global numero_imagen, lista_imagenes
    numero_imagen = numero_imagen + 1
    if numero_imagen >= len(lista_imagenes):
        numero_imagen = 0
    show_image()
    
# muestra la imagen anterior
def prev_image():
    global numero_imagen
    numero_imagen = numero_imagen - 1
    if numero_imagen < 0:
        numero_imagen = len(lista_imagenes) - 1
    show_image()
    
# muestra la primera imagen
def first_image():
    global numero_imagen
    numero_imagen = 0
    show_image()
    
# muestra la última imagen
def last_image():
    global numero_imagen
    numero_imagen = len(lista_imagenes)-1
    show_image()

def select_folder():
    directory.value = filexapp.select_folder("Seleccione el directorio",directory.value)
    update_images()
    show_image()
    
#end def
###############################################
# Arrays

color = ["black", "white", "red", "green", "blue", "purple", "gray31"]

#end Arrays
###############################################
# app declare

filexapp = App(layout="auto", title="Filex", width=_width, height=_height)


#end declare
###############################################
#app properties


# end
###############################################
#begin app
###############################################
# begin line 1

separadorStr = "     "

boxBotonera = Box(filexapp, align="top",width='fill')

text = Text(boxBotonera, text="Carpeta:"+separadorStr, align = "left")
directory = TextBox(boxBotonera, text="images", align = "left", width="fill")

# Orden invertido para la derecha

themecmb = Combo(boxBotonera, options=color, command=update_bg, selected=filexapp.bg, align="right")
themetext = Text(boxBotonera, text=separadorStr+"Color fondo:",  align="right")
separador1 = Text(boxBotonera, text=separadorStr,  align="right" )
fontcmb = Combo(boxBotonera, options=color, command=update_text, selected=filexapp.text_color,  align="right")
fonttext = Text(boxBotonera, text=separadorStr+"Color fuente:",  align="right")
reloadbtn = PushButton(boxBotonera, image="iconos/recargar.png", command=update,  align="right")
separador2 = Text(boxBotonera, text=separadorStr,  align="right" )
selectDirbtn = PushButton(boxBotonera,image="iconos/file.png",command=select_folder,align='right')
separador3 = Text(boxBotonera, text=separadorStr,  align="right" )

# end
###############################################
# begin line 2


boxImagen = Box(filexapp,height='fill',width='fill')

vsimg = Picture(boxImagen, width=700, height=700, align="top")

boxBotoneraImagen = Box(filexapp,align="bottom")

firstbtn = PushButton(boxBotoneraImagen, image="iconos/arrow-to-left.png", command=first_image, align="left")
prevbtn = PushButton(boxBotoneraImagen, image="iconos/left-arrow.png", command=prev_image, align="left")
separador4 = Text(boxBotoneraImagen, text=separadorStr,  align="left")

textImagenName = Text(boxBotoneraImagen,"Imagen",align="left")

# Orden inverso a la derecha
lastbtn = PushButton(boxBotoneraImagen, image="iconos/arrow-to-right.png", command=last_image, align="right")
nextbtn = PushButton(boxBotoneraImagen, image="iconos/right-arrow.png", command=next_image, align="right")
separador4 = Text(boxBotoneraImagen, text=separadorStr,  align="right")

# Actualizamos el aspecto
update_theme()
boxBotonera.bg = 'blue' # DEBUG para zona box
boxBotoneraImagen.bg = "green" # DEBUG para zona box
boxImagen.bg='red' # DEBUG para zona box
update_images() # recargamos la lista de imágenes
show_image()
    


#end
###############################################
filexapp.display()
###############################################
#end app


