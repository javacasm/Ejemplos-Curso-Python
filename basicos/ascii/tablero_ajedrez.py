# Dibuja un tablero de damero

version = 1.6

print('Tablero de damero v',version)

# dibuja un damero de ancho x alto
def dibuja_damero(ancho,alto):
    for i in range(alto):
        print('# ' * ancho)
        print(' #' * ancho)    
    

def dibuja_triangulo(alto):
    for i in range(alto):
        print('#' * i)
    
    

ancho_usuario = input('Dime el ancho del tablero: ') # es una cadena
ancho_int = int(ancho_usuario)   # convierte la cadena a entero

alto_usuario = input('Dime el alto del tablero: ') # es una cadena
alto_int = int(alto_usuario)   # convierte la cadena a entero


dibuja_damero(ancho_int,alto_int)

dibuja_triangulo(alto_int)