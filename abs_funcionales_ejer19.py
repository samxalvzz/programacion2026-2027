"""
19. La función sustituye tiene la siguiente especificación:1
Pre : True
sustituye(𝑎, 𝑏, 𝑡: tuple) -> tuple
Post : sustituye(𝑎, 𝑏, 𝑡) = una tupla igual que t pero
sustituyendo los a por b
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
a) recursivo.
b) iterativo.
"""

# a) Recursivo
sustituye = lambda a, b, t: () if t == () else \
    ((b,) if t[0] == a else (t[0],)) + sustituye(a, b, t[1:])

# b) Iterativo
sustituye_it = lambda a, b, t, acc: acc if t == () else \
    sustituye_it(a, b, t[1:], acc + ((b,) if t[0] == a else (t[0],)))
sustituye = lambda a, b, t: sustituye_it(a, b, t, ())