def dibujar_triangulo(tipo, altura, caracter_relleno, caracter_borde):
    if tipo == "equilatero":
        print(" " * (altura + 1) + caracter_borde)
        for i in range(1, altura + 1):
            espacio = ' '+" " * (altura - i)
            relleno = caracter_relleno * (2 * i - 1)
            linea = caracter_borde + relleno + caracter_borde
            print(espacio + linea)
        print( caracter_borde * ( 2 * (altura +1) +1)  )
    elif tipo == "escaleno":
        print(' ' + caracter_borde)
        for i in range(1, altura + 1):
            relleno = caracter_relleno * i
            linea = caracter_borde + relleno + caracter_borde
            print(linea)
        print(caracter_borde * (altura+3))
    else:
        print("Tipo de triángulo no válido")

def main():
    tipo_triangulo = input("Elige el tipo de triángulo (equilatero, escaleno): ").lower()
    altura_triangulo = int(input("Introduce la altura del triángulo: "))
    caracter_relleno = input("Introduce el carácter de relleno: ")
    caracter_borde = input("Introduce el carácter de borde: ")

    dibujar_triangulo(tipo_triangulo, altura_triangulo, caracter_relleno, caracter_borde)

if __name__ == "__main__":
    main()