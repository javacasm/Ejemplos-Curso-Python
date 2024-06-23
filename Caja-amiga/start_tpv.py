# https://lawsie.github.io/guizero/app
from  guizero import App, PushButton, TextBox
from config import *
import pickle
from clases_caja_amiga import *

articulos = []

with open('articulos.list',"rb") as fichero:
    try:
        while True:
            articulo = pickle.load(fichero)
            articulos.append(articulo)
            
    except EOFError:
        pass
    
tpvApp = App(title='Caja amiga', layout='grid', width=1200, height=800)

mi_pedido = Pedido()

def add_articulo(articulo):
    print(f'añadido artículo {articulo.nombre}')
    mi_pedido.add(articulo,1)
    ticket_text.value = mi_pedido.get_ticket()

# TODO: creamos botones para los articulos
fila = 0
columna = 0

for articulo in articulos:
    try:
        boton = PushButton(tpvApp,
                           grid=[columna,fila],
                           text=articulo.nombre,
                           image=DIRECTORIO_IMAGENES+articulo.nombre+'.png',
                           width=ANCHO_IMAGEN,
                           height=ANCHO_IMAGEN,
                           command=add_articulo,
                           args=[articulo])
        columna += 1
        if columna >= ANCHO_COLUMNAS:
            columna = 0
            fila += 1
    except Exception as e:
        print(e)

ticket_text = TextBox(tpvApp,text='Pedido', grid=[4,0,6,4],
                      width='fill', height='fill',
                      multiline=True)
ticket_text.text_size = 20

tpvApp.display()

