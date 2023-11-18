# Dibuja un damero y un triángulo

version = 1.6

print('Tablero de damero v',version)

# dibuja un damero de ancho x alto
def dibuja_damero(ancho,alto):
    for i in range(alto):
        print('# ' * ancho)
        print(' #' * ancho)    
    

def dibuja_triangulo(alto):
    for i in range(alto + 1):
        print('#' * i)
    
    

ancho_usuario = input('Dime el ancho del damero: ') # es una cadena
ancho_int = int(ancho_usuario)   # convierte la cadena a entero

alto_usuario = input('Dime el alto del damero: ') # es una cadena
alto_int = int(alto_usuario)   # convierte la cadena a entero


dibuja_damero(ancho_int,alto_int)

alto_usuario = input('Dime el alto del triángulo: ') # es una cadena
alto_int = int(alto_usuario)   # convierte la cadena a entero

dibuja_triangulo(alto_int)