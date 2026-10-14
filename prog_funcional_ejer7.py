"""
7. Escribir un programa que calcule el mínimo común múltiplo (mcm) de dos números
enteros, de dos formas diferentes:

a) Mediante la función lcm del módulo math.

b) Aprovechando la siguiente propiedad:
𝑎 · 𝑏 = 𝑚𝑐𝑑 (𝑎, 𝑏) · 𝑚𝑐𝑚(𝑎, 𝑏)

Copyright (c) 2026 Samuel Álvarez

Este programa se distribuye bajo la liciencia GNU GPL v3.
"""

from math import lcm, gcd

# Datos de entrada:
a = 12 # Primer número
b = 18 # Segundo número

# Datos de salida:
mcm_a = lcm(a, b)
mcm_b = abs(a * b) // gcd(a, b)
