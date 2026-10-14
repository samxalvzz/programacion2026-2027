"""
1. Los médicos forenses utilizan la longitud de los huesos para determinar la altura de una
persona, cuando la persona estaba viva.
Por ejemplo, para los varones:

altura (en cm) = 69.089 + 2.232 × longitud de la tibia

Para las mujeres, el valor es el siguiente:

altura (en cm) = 61.412 + 2.317 × longitud de la tibia

A partir de los 30 años (inclusive), la altura de una persona decrece a una tasa de 0.06
cm por año.

Escribir un programa que, dados los valores de la longitud de la tibia, el sexo y la edad
del paciente, nos calcule la altura aproximada.

Copyright (c) 2026 Samuel Álvarez

Este programa se distribuye bajo la liciencia GNU GPL v3.
"""

# Datos de entrada:
tibia = 40.0 # Longitud de la tibia
sexo = "mujer" # "Varon o mujer"
edad = 24 # Edad en años 

# Datos que tenemos de intermedio:
altura_base: float = (69.089 + 2.232 * tibia) if sexo == "varon" \
    else (61.412 + 2.317 * tibia) # Aqui se dice la altura según el sexo
anios_descenso: int = max(0, edad - 30) # Aqui te dice si los años desde los 30 o si es más joven

# Datos de salida:
altura: float = altura_base - 0.06 * anios_descenso # Aquí te dice la altura máxima

