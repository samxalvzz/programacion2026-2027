"""
6. Escribir un programa que reciba tres datos de entrada y que los ordene de menor a
mayor, indicando cuál es el primero, cuál el segundo y cuál el tercero.

Copyright (c) 2026 Samuel Álvarez

Este programa se distribuye bajo la liciencia GNU GPL v3.
"""

# Datos de entrada:
dato1 = 8 # Primer dato
dato2 = 3 # Segundo dato
dato3 = 5 # Tercer dato

# Datos de salida:
primero = min (dato1, dato2, dato3) # El primero
tercero = max (dato1, dato2, dato3) # El tercero
segundo = dato1 + dato2 + dato3 - primero - tercero # El que estaría en medio


