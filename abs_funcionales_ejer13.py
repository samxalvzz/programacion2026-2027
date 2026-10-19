"""
13. La función voltea le da la vuelta a un número entero:
voltea(423) = 324
voltea(7) = 7
Se pide:
a) Escribir su especificación.
b) Indicación: Usar la función digitos que devuelve la cantidad de dígitos que tiene un
entero. Usar además la indicación del ejercicio anterior.
"""

# a) Escribir su especificación
"""
pre: a ≥ 0
voltea(n: int) -> int
post: voltea(n) = el numero n con sus dígitos en orden inverso

"""

# b) Implementar una función recursiva que satisfaga dicha especificación.

digitos = lambda n: n if n < 10 else n % 10 + digitos(n // 10)
voltea = lambda n: n if n < 10 else (n % 10) * 10 ** (digitos(n) - 1) + voltea(n // 10)
