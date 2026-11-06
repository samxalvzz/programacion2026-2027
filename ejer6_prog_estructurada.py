"""
6. Escribir un programa que muestre por pantalla la tabla
de multiplicar de un número comprendido entre 0 y 10,
introducido por teclado.
"""

try:
    numero = int(input('Introduzca el número de la tabla deseada: '))
    i = 0
    while i <= 10:
        print(numero, 'x', i, '=', numero * i)
        i += 1
except ValueError:
    print('Ha introducido un valor incorrecto.')
