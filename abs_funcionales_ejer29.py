"""
29. La función finales tiene la siguiente especificación:
Pre : 𝑛 ≥ 0
finales(𝑛: int, 𝑡: tuple) -> tuple
Post : finales(𝑛, 𝑡) = la tupla que contiene los 𝑛 elementos finales de 𝑡
Por ejemplo: finales(2, (1, 2, 3, 4)) == (3, 4).
Escribir una función recursiva que satisfaga dicha especificación.
"""
finales = lambda n, t: t if len(t) <= n else finales(n, t[1:])