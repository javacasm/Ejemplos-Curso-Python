# Dibuja el triangulo que quieras, ¡pruebalo ya!

v = 2
print(f'Triángulos con bordes v{v}')
 
def dibujar_triangulo(tipo, altura, caracter_relleno, caracter_borde):
    if tipo == "equilatero" or tipo == '1':
        print(" " * (altura + 1) + caracter_borde)
        for i in range(1, altura + 1):
            espacio = " " * (altura - i)
            relleno = caracter_relleno * (2 * i - 1)
            linea = caracter_borde + relleno + caracter_borde
            print(espacio + linea)
        print(caracter_borde*(2*(altura+1)-1))
   
    elif tipo == "isosceles" or tipo =='2':
        print(" " * altura + caracter_borde)
        for i in range(1, altura + 1):
            espacio = " " * (altura - i)
            relleno = caracter_relleno * (2 * i - 1)
            linea = caracter_borde + relleno + caracter_borde
            print(espacio + linea)
        print(caracter_borde*(2*(altura+1)-1))
   
    elif tipo == "escaleno" or tipo == '3' :
        for i in range(1, altura + 1):
            espacio =""*(altura -i)
            relleno = caracter_relleno * (2 * i-1)
            linea = (caracter_borde + relleno + caracter_borde)
            print(linea)
        print(caracter_borde * (2*(altura +1 )- 1))
    else:
        print("Tipo de triángulo no válido")

def main():
#    try:
       
        tipo_triangulo = input("Elige el tipo de triángulo (1. Equilatero,2. Isosceles, 3. Escaleno): ").lower()
        altura_triangulo = int(input("Introduce la altura del triángulo: "))
        if altura_triangulo <=0:
            print('La altura tiene que ser mayor que 0')
            exit()
        if altura_triangulo > 25:
            print('La altura no puede ser mayor de 25')
            return
        caracter_relleno = input("Introduce el carácter de relleno: ")
        if caracter_relleno == '':
            caracter_relleno = '#'
        caracter_borde = input("Introduce el carácter de borde: ")
        if caracter_borde == "":
            caracter_borde = '·'
        dibujar_triangulo(tipo_triangulo, altura_triangulo, caracter_relleno, caracter_borde)
       
#    except Exception as e:
#       print(f'Se ha producido un error: {e}')
   
if __name__ == "__main__":
    main()