"""
5. Escribir un programa que reciba dos datos de entrada y que
los ordene de menor a mayor, indicando cuál es el primero
y cuál el segundo.

Copyright (c) 2026 Samuel Álvarez

Este programa se distribuye bajo la liciencia GNU GPL v3.
"""

# Datos de entrada

dato1 = 7 
dato2 = 4

# Datos de salida

# Esto es en valor ternario, el otro ejemplo que hicimos estaba bien, era el siguiente, esta abajo.

primero = dato1 if dato1 < dato2 else dato2
segundo = dato1 if dato1 > dato2 else dato1
# segundo = dato1 if dato1 >= dato2 else dato2

"""
primero = min(dato1, dato2)
segundo = max(dato1, dato2)

"""

