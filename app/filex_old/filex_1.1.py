# App filex: visor de imágenes
'''
TODO: seleccionar carpeta - Queralt (https://lawsie.github.io/guizero/alerts/ Example: Get a file name)
# TODO: botón imagen anterior - Carlos
# TODO: botón imagen siguiente - Carlos
# TODO: agrupar los controles en filas - José Antonio
# TODO: interface - Luis
# TODO: mostrar imágenes - Lucía
# TODO: abrir nueva ventana para imagen - Luis (https://lawsie.github.io/guizero/multiple_windows/#multiple-windows)
# TODO: refrescar - Lucía
# TODO: añadir comentarios - Lucía
# TODO: buscar nombre - Carlos
# TODO: paquetes que se necesitan - José Antonio

# v 2.0

# TODO: seleccionar el aspecto/tema
# TODO: optimizar imágenes - Luis
# TODO: crear fuentes o imágenes

# v 3.0

# TODO: control por voz - Carlos
# TODO: IA para seleccionar estilo - Luis

'''

#  by team @EJI

# documentación
# guizero: "https://github.com/lawsie/guizero"

# import guizero docs:
# https://lawsie.github.io/guizero/layout/



v = '1.1'

print('V:',v)

import guizero
guizero.App

from guizero import *


# Arrays

color = ["black", "white", "red", "green", "blue", "purple", "gray31"]

#end Arrays

# app declare

# TODO: ajustar el tamaño a la pantalla
filexapp = App(layout="grid", title="Filex", width=1400, height=1000)
# investigar
# filexapp.full_screen = True

# end declare

# begin app

# begin line 1

# iconos de https://boxicons.com/?query=

text = Text(filexapp, text="carpeta:", grid=[0, 0])
directory = TextBox(filexapp, text="fichero", grid=[1, 0], width=100)
p1 = Text(filexapp, text=" ", grid=[2, 0])
reloadBtn = PushButton(filexapp, text="Recargar", image = 'icons/3936688.png',command="", grid=[3, 0], width=30, height=30, align="right")
textColorFnt = Text(filexapp, text="Color fuente:", grid=[4, 0])
fontCmb = Combo(filexapp, options=color, command="", selected=filexapp.text_color, grid=[5, 0], align="right")
textColorBack = Text(filexapp, text="Color fondo:", grid=[6, 0])
themeCmb = Combo(filexapp, options=color, command="", selected=filexapp.bg, grid=[7, 0], align="right")

# end

# begin line 2

prevBtn = PushButton(filexapp, text="Anterior", image="icons/left-arrow-alt-regular-24.png", command="", grid=[0,1])

try:
    vsimg = Picture(filexapp, grid=[1, 1], image="../imagenes/nyancat.gif", width=500, height=500)
except :
    print('No se ha encontrado la imagen')
    
nextBtn = PushButton(filexapp, text="Siguiente", image="icons/right-arrow-alt-regular-24.png", command="", grid=[3,1], align="right")

#end

filexapp.display()

#end app