"""
25. La función rota1 tiene la siguiente especificación:
Pre : True
rota1(𝑡: tuple) -> tuple
Post : rota1(𝑡) = la tupla obtenida poniendo el primer
elemento de 𝑡 al final
Por ejemplo: rota1((3, 2, 5, 7)) == (2, 5, 7, 3).
Escribir una función recursiva que satisfaga dicha especificación.
"""
rota1 = lambda t: () if t == () else t[1:] + (t[0],)