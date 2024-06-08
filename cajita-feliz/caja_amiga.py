import os
import pickle
from config import *
from utiles import *
# clase artículo

v = 0.2

print(f'{__name__} v{v}')

class Articulo():
    
    def __init__(self, nombre, categoria, precio):
        
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        
class Pedido():
    
    def __init__(self,unidades,articulos):
        self.unidades = unidades
        self.articulos = articulos

    def calcula_precio(self):

        precio_total = 0
        log(f'Artículo\tCantidad\tPrecio/Unidad\tPrecio\n{LINEA_STR}')
        for producto, unidades in zip(self.articulos, self.unidades):
            log(f'{producto.nombre}\t\t{unidades:3.2f}\t\t{producto.precio:{FORMATO_PRECIO}}{MONEDA}\t\t{producto.precio*unidades:{FORMATO_PRECIO}}{MONEDA}')
            precio_total += producto.precio * unidades
            
        #print('tu compra ha costado',precio_total)
        return precio_total
    
class caja_amiga():
    def __init__(self,fichero_articulos):
        self.articulos = []
        self.fichero_articulos = fichero_articulos
        self.categorias = []
        self.carga_articulos()
    
    def add_articulo(self,articulo):
        self.articulos.append(articulo)
        if articulo.categoria not in self.categorias:
            self.categorias.append(articulo.categoria)
            
    def guarda_articulos(self):
        if os.path.exists(self.fichero_articulos): # si existe el fichero lo renombramos
            log(f'Renombrando el fichero {self.fichero_articulos}')
            os.rename(self.fichero_articulos,self.fichero_articulos+'.bak')
        with open(self.fichero_articulos,'wb') as fichero:
            for articulo in self.articulos:
                pickle.dump(articulo, fichero) # ¿Hay que guardar las categorias?
                
    def carga_articulos(self):
        if os.path.exists(self.fichero_articulos): # existe el fichero
            log(f'Cargando artículos del fichero "{self.fichero_articulos}"')
            with open(self.fichero_articulos,'rb') as fichero:
                try: 
                    while True:
                        articulo = pickle.load(fichero)
                        self.add_articulo(articulo)
                except EOFError: # hemos llegado al final del fichero
                    pass
            log(f'Cargados {len(self.articulos)} artículos')
        else:
            log('Creando artículos "a mano"')
            self.add_articulo(Articulo('Patata','verdura',1.4))
            self.add_articulo(Articulo('Leche','lacteo',1))
            self.add_articulo(Articulo('Yogurt','lacteo',0.8))
            self.add_articulo(Articulo('Galleta', 'bolleria', 0.6))
            self.add_articulo(Articulo('Nestea', 'refrescos', 1.5))
            self.add_articulo(Articulo('Tomate','verdura',1.6))
            self.guarda_articulos()


    def test_pedido(self):
        import random # lo hacemos aquí porque es sólo para el tes
        articulos = []
        cantidades = []
        print('Creando pedido aleatorio\n\n')
        numero_productos = random.randint(5,10) # tendrá entre 5 y 10 artículos
        for _ in range(numero_productos): 
            articulo = random.choice(self.articulos) # artículo aleatorio
            if articulo not in articulos: # Para que no se repita
                articulos.append(articulo)
                cantidad = random.random()*10+0.1 # entre 0.1 y 10.1
                cantidades.append(cantidad)
        mi_pedido = Pedido(cantidades,articulos)
        precio_total = mi_pedido.calcula_precio()
        print(LINEA_STR)
        print(f'Precio total del pedido \t\t\t\t{precio_total:{FORMATO_PRECIO}}{MONEDA}')
        
if  __name__ == '__main__':
    caja = caja_amiga(FICHERO_ARTICULOS)
    caja.test_pedido()