# fichero de utilidades
from config import *

v = 0.2

print(f'{__name__} v{v}')

def log(mensaje):
    if verbose: print(mensaje)