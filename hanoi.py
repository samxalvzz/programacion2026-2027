"""
Escribir una función recursiva que resulta la torre de Hanoi
Pre: 𝑛 ≥ 0
    hanoi(a, b, c, n) -> tuple[str]
Post: ...

"""

hanoi = lambda a, b, c, n: () if n == 0 else \
                           hanoi(a, c, b, n - 1) + \
                           ("Muevo un disco de " + a + " hacia " + b,) + \
                           hanoi(c, b, a, n - 1)
