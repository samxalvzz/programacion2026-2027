"""
15. La función par determina si un número entero (positivo o negativo) es par:
par(0) = True
par(1) = False
par(-27) = False
Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.
c) ¿Cómo se podría implementar una función impar a partir de la función par?
"""

# a) Escribir su especificación
"""
pre: True
par(n: int) -> bool
post: par(n) = true si n es par, false en caso contrario

"""

# b) Implementar una función recursiva que satisfaga dicha especificación y
# ¿Cómo se podría implementar una función impar a partir de la función par?

par = lambda n: true if n == 0 else not par(abs(n) - 1)
impar = lambda n: not par(n)
