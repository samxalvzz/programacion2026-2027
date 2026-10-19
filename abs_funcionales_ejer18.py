"""
18. La función quita tiene la siguiente especificación:
Pre : True
quita(𝑒, 𝑡: tuple) -> tuple
Post : quita(𝑒, 𝑡) = una tupla igual que t pero sin los e
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
a) recursivo.
b) iterativo.
"""

# a) Recursivo
quita = lambda e, t: () if t == () else \
    quita(e, t[1:]) if t[0] == e else \
    (t[0],) + quita(e, t[1:])

# b) Iterativo
quita_it = lambda e, t, acc: acc if t == () else \
    quita_it(e, t[1:], acc) if t[0] == e else \
    quita_it(e, t[1:], acc + (t[0],))
quita = lambda e, t: quita_it(e, t, ())