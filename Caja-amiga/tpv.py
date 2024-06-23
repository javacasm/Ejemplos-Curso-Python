# TPV
from clases_caja_amiga import *
from guizero import App, Box, TextBox, PushButton

v = 0.3


_width_productos = 800
_width_ticket = 600

_width = _width_productos + _width_ticket

_height = 800

tpvApp = App(layout='grid', title=f'Caja Amiga v{v}', width=_width, height=_height)

caja = Caja_Amiga()

ticket_text = None

def actualiza_ticket():
    if ticket_text != None:
        ticket_text.value = caja.pedido.get_ticket()
    
def add_articulo(articulo):
    print(f'Clic en {articulo}')
    caja.pedido.add_articulo(articulo,1)
    actualiza_ticket()

def init_app(caja):
    global ticket_text
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
                            height=ancho_imagen,
                            command=add_articulo,
                            args=[articulo])
        #print(f'{articulo.nombre} - ({fila},{columna})')
        columna += 1
        if columna >= ancho:
            columna = 0
            fila += 1
    ticket_text = TextBox(tpvApp, text='Pedido', grid=[4,0,6,4],
                          width='fill',height='fill',
                          multiline=True,enabled=False)
    ticket_text.text_size = 20
    

init_app(caja)

tpvApp.display()