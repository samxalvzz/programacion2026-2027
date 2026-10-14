"""
9. Escribir un programa que diga si dos cadenas son iguales sin tener en cuenta las
mayúsculas y minúsculas. Por ejemplo, el programa debería decir que las cadenas
"Hola" y "hoLa" son iguales

Copyright (c) 2026 Samuel Álvarez

Este programa se distribuye bajo la liciencia GNU GPL #v3.
"""

# Datos de entrada:
cadena1 = "Hola"
cadena2 = "hoLa"

# Datos de salida:
son_iguales: bool = cadena1.lower() == cadena2.lower() # Serán iguales o no, con esto nos devolverá un bool.
