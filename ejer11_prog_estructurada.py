"""
11. Escribir un programa que determine si un número entero introducido por teclado es
primo o compuesto.
Indicación: Un número primo es aquel que sólo puede dividirse exactamente por sí
mismo y por 1.
"""

numero = int(input("Introduzca un número: "))

if numero < 2:
    print("El número no es ni compuesto ni primo")
    