"""
Escribir un programa que muestre por la salida todo lo que el
usuario introduzca por la entrada, hasta que escriba FIN.
"""

while True:
    entrada = input('Introduzca algo (FIN para salir): ')
    if entrada == 'FIN':
        break
    print(entrada)