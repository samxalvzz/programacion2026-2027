"""
11. Escribir un programa que diga si una cadena es un palíndromo.
Se ignoran tildes, mayúsculas y espacios en blanco.

Copyright (c) 2026 Samuel Álvarez

Este programa se distribuye bajo la liciencia GNU GPL #v3.
"""

# Datos de entrada:
cadena = "Anás usó tu auto, Susana" # Esto será la cadena original

# Datos que son intermedios:
tabla = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")
sin_espacios = cadena.replace(" ", "")
sin_tildes = sin_espacios.translate(tabla)
normalizada = sin_tildes.lower()

# Datos de salida:
es_palindromo = normalizada == normalizada[::-1]