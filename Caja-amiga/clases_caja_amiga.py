import os
import pickle

NOMBRE_FICHERO_ARTICULOS = 'articulos.list'


CARPETA_IMAGENES = 'imagenes' + os.sep

# clase artículo

class Articulo ():
    
    def __init__(self, nombre, categoria, precio, imagen):
        
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.imagen = CARPETA_IMAGENES + imagen
        if not os.path.exists(self.imagen):
            print(f'No se ha encontrado el fichero {self.imagen}')
    
    def __str__(self):
        return f'{self.nombre} - {self.precio} - {self.imagen}'
# clase pedido
# formato
LINEA_STR = '-'*45
MONEDA = '€'
FORMATO_PRECIO = '>5.2f'

class Pedido ():
    
    def __init__(self):
        self.unidades = []
        self.articulos = []
    
    def add(self, article, cant):
        self.articulos.append(article)
        self.unidades.append(cant)
        
    ## V 5
    def add_articulo(self,articulo,cantidad):
        indice = 0
        bEsta = False 
        for producto in self.articulos:
            if producto.nombre == articulo.nombre: # ya está
                bEsta = True
                self.unidades[indice] += cantidad
                print(f'Añadida la cantidad {cantidad} de {articulo.nombre}')
                break
            indice += 1
        if bEsta == False: # lo añadiomos
            self.articulos.append(articulo)
            self.unidades.append(cantidad)
            print(f'Añadido {articulo.nombre}')

    def calcula_precio (self):
        
        precio_total = 0

        for producto, cantidad in zip(self.articulos, self.unidades):
            print('· Artículo:', producto.nombre, ', precio:',producto.precio)
            precio_total += producto.precio * cantidad
            
        return precio_total
    
    def get_ticket(self):
        
        precio_total = 0
        str = f'Artículo\tCantidad\tPrecio/Unidad\tPrecio\n{LINEA_STR}\n'
        for producto, unidades in zip(self.articulos, self.unidades):
            str += f'{producto.nombre}\t{unidades:3.2f}\t{producto.precio:{FORMATO_PRECIO}}{MONEDA}\t\t{producto.precio*unidades:{FORMATO_PRECIO}}{MONEDA}\n'
            precio_total += producto.precio * unidades
        str += f'{LINEA_STR}\nPRECIO TOTAL\t\t\t\t{precio_total:{FORMATO_PRECIO}}{MONEDA}'
        return str

    def __str__(self):
        return self.get_ticket()
    
class Caja_Amiga():
    def __init__(self,fichero_artiuclos = NOMBRE_FICHERO_ARTICULOS):
        self.fichero_articulos = fichero_artiuclos
        self.articulos = []
        # si hay fichero de datos 
        if os.path.exists(self.fichero_articulos):
            self.carga_articulos()
        else: # si no exite creamos los articulos
            self.crea_articulos()
            self.guarda_articulos() # los guardamos
        self.show_articules()
        self.pedido = Pedido()
        
    def crea_articulos(self):
        # creamos los articulos
        patata = Articulo('Patata','verdura',1.4,'patata.png')
        self.articulos.append(patata)
        leche = Articulo('Leche','lacteo',1,'leche.png')
        self.articulos.append(leche)
        yogurt = Articulo('Yogurt','lacteo',0.8,'yogurt.png')
        self.articulos.append(yogurt)
        galletas = Articulo('Galleta', 'bolleria', 0.6,'galletas.png')
        self.articulos.append(galletas)
        agua = Articulo('Agua', 'refrescos', 1,'agua.png')
        self.articulos.append(agua)
        nestea = Articulo('Nestea', 'refrescos', 1.5,'nestea.png')
        self.articulos.append(nestea)
        tomate = Articulo('Tomate','verdura',1.6,'tomate.png')
        self.articulos.append(tomate)
        pan = Articulo('Pan', 'bolleria', 0.2,'pan.png')
        self.articulos.append(pan)

    def guarda_articulos(self):
        # abrimos el fichero para escritura
        with open(self.fichero_articulos, 'wb') as fichero:
            for articulo in self.articulos:
                pickle.dump(articulo, fichero)

    def carga_articulos(self):
        with open(self.fichero_articulos, 'rb')  as fichero:
            try:
                while True:
                    articulo = pickle.load(fichero)
                    self.articulos.append(articulo)
                    # print('cargado',articulo.nombre)
            except EOFError: # hemos llegado al final del fichero
                pass

    def show_articules(self):  
        print('Listado')
        for articulo in self.articulos:
            print(articulo.nombre, articulo.precio, articulo.imagen)


