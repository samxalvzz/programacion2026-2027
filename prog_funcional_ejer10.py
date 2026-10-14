"""
10. Usando el método maketrans, escribir un programa que sustituya en
una cadena las vocales acentuadas por sus correspondientes sin acentuar.

Copyright (c) 2026 Samuel Álvarez

Este programa se distribuye bajo la liciencia GNU GPL #v3.
"""

# Datos de entrada:
cadena = "¡Pero bueno, como estás! ¡Qué tal! ¡Te echaré de menos!" # Esto será la cadena original

# Datos que serán intermedios:
tabla = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU") # Esto es la tabla

# Datos de salida:
sin_tildes = cadena.translate(tabla) # Nos devuelve la cadena, sin tildes.

