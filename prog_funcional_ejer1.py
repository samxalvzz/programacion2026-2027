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

long_tibia: float = 35.0
sexo: str = 'M' # 'H' = Hombre, 'M' = Mujer
edad: int = 22

# Datos intermedios

altura_previa_hombre = lambda l: 69.089 + 2.332 * l
altura_previa_mujer = lambda l: 61.412 + 2.317 * l

altura_previa: float = 69.089 + 2.332 * long_tibia if sexo == 'H' else \
                       61.412 + 2.317 * long_tibia

correccion = lambda ap, e: ap - 0.06 * (e - 29)


# Datos de salida:

altura: float = correcion(altura_previa, edad) if edad >= 30 else \
                altura_previa

"""
Arriba haré la forma que ricardo lo va a hacer, pego aqui lo que yo hice...

# Datos de entrada:
tibia = 40.0 # Longitud de la tibia
sexo = "mujer" # "Varon o mujer"
edad = 24 # Edad en años 

# Datos que tenemos de intermedio:
altura_base: float = (69.089 + 2.232 * tibia) if sexo == "varon" else
                     (61.412 + 2.317 * tibia) # Aqui se dice la altura según el sexo
anios_descenso: int = max(0, edad - 30) # Aqui te dice si los años desde los 30 o si es más joven

# Datos de salida:
altura: float = altura_base - 0.06 * anios_descenso # Aquí te dice la altura máxima
"""