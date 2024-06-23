# TPV
from clases_caja_amiga import *
from guizero import App, Box, Text, PushButton

v = 0.3


_width_productos = 800
_width_ticket = 400

_width = _width_productos + _width_ticket

_height = 800

tpvApp = App(layout='grid', title=f'Caja Amiga v{v}', width=_width, height=_height)

def init_app(caja):
    '''
    boxBotoneraTop = Box(tpvApp, align="top",width='fill')
    boxBotoneraTop.bg = 'red'
    textBotoneraTop = Text(boxBotoneraTop, text="Botones Top", align = "left")

    boxCentral = Box(tpvApp, height='fill',width='fill')
    boxCentral.bg = 'green'

    boxArticulos = Box(boxCentral, height='fill', width='fill')
    boxArticulos.layout = 'grid'
    boxArticulos.bg = 'yellow'
    '''  
    # 5 x 4 aritulos
    ancho = 3
    fila = 0
    columna = 0
    ancho_imagen = _width_productos // ancho
    for articulo in caja.articulos:
        button = PushButton(tpvApp,
                            grid=[columna,fila],
                            text=articulo.nombre,
                            image=articulo.imagen,
                            width=ancho_imagen,
                            height=ancho_imagen)
        print(f'{articulo.nombre} - ({fila},{columna})')
        columna += 1
        if columna >= ancho:
            columna = 0
            fila += 1
    '''
    boxPedido = Box(boxCentral, height='fill',width='right')
    boxPedido.bg = 'gray'



    boxBotoneraDown = Box(tpvApp,align="bottom")
    boxBotoneraDown.bg = 'blue'
    textBotoneraDown = Text(boxBotoneraDown, text="Botones Down", align = "left")
    ''' 
caja = Caja_Amiga()

init_app(caja)

tpvApp.display()