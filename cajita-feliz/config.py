# config
import os

v = 0.2

print(f'{__name__} v{v}')

# ficheros
CARPETA_DATOS  = 'datos'

FICHERO_ARTICULOS = CARPETA_DATOS + os.sep + 'articulos.data'


# depuración

verbose = True

# formato
LINEA_STR = '-'*55
MONEDA = '€'
FORMATO_PRECIO = '>5.2f'