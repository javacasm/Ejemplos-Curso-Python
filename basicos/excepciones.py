# cuenta hasta un número...

import time

try:

    numero_final_str = input('Dime el número hasta el que quieres que cuente: ')

    numero_final = int(numero_final_str) # convertimos de texto a entero
    
    tiempo_inicial = time.time() # guarda en la variable el tiempo inicial
    
    for n in range(1,numero_final + 1): # desde 1 hasta numero_final
        pass
        # print(n)
        
    tiempo_final = time.time() # guarda el tiempo final
    
    duracion = int ( 1000 * (tiempo_final - tiempo_inicial) ) # número entero de milisegundos
    
    #print('Ha tardado:', duracion, ' milisegundos')
    print(f'Ha tardado: {duracion} milisegundos') # formato con f-string 
    
except Exception as e:
    print('Se ha producido un error: ',e)