"""
24. La función rota tiene la siguiente especificación:
Pre : 𝑛 ≥ 0
rota(𝑛: int, 𝑡: tuple) -> tuple
Post : rota(𝑛, 𝑡) = la tupla obtenida poniendo los 𝑛 primeros
elementos de 𝑡 al final
Por ejemplo:
rota(1, (3, 2, 5, 7)) == (2, 5, 7, 3)
rota(2, (3, 2, 5, 7)) == (5, 7, 3, 2)
rota(3, (3, 2, 5, 7)) == (7, 3, 2, 5)
Escribir una función recursiva que satisfaga dicha especificación.

"""
rota1 = lambda t: () if t == () else t[1:] + (t[0],)
rota = lambda n, t: t if n == 0 else rota(n - 1, rota1(t))