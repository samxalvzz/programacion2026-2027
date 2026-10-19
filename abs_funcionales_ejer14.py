"""
14. La función par_positivo determina si un número entero positivo es par:
par_positivo(0) = True
par_positivo(1) = False
par_positivo(27) = False
par_positivo(82) = True
Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.
"""

# a) Escribir su especificación
"""
pre: a ≥ 0
par(n: int) -> bool
post: par(n) = true si n es par, false en caso contrario

"""

# b) Implementar una función recursiva que satisfaga dicha especificación.

par positivo = lambda n: true if n == 0 else not par_positivo(n - 1)


