from  caja_amiga import * 
from config import *

nombre = 'Caja amiga'
v = 0.2

print(f'{nombre} v{v}')

caja = caja_amiga(FICHERO_ARTICULOS)

caja.test_pedido()