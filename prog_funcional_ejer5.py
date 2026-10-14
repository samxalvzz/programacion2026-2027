"""
5. Escribir un programa que reciba dos datos de entrada y que
los ordene de menor a mayor, indicando cuál es el primero
y cuál el segundo.

Copyright (c) 2026 Samuel Álvarez

Este programa se distribuye bajo la liciencia GNU GPL v3.
"""

# Datos de entrada:
dato1 = 7
dato2 = 4

# Datos de salida:
primero = dato1 if dato1 < dato2 else dato2 # Esto seria ternario, se puede hacer asi también, pero es fácil como lo que dejaré en lo último
segundo = dato1 if dato1 > dato2 else dato1
# segundo = dato1 if dato1 >= dato2 else dato1

"""
primero = min(dato1, dato2)
segundo = max(dato1, dato2)

"""

