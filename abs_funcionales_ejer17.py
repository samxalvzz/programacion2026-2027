"""
17. La función cuantos tiene la siguiente especificación:
Pre : True
cuantos(𝑒, 𝑡: tuple) -> int
Post : cuantos(𝑒, 𝑡) = el número de veces que aparece e en t
Escribir una función recursiva que satisfaga dicha especificación y que genere un
proceso:
a) recursivo.
b) iterativo
"""

# a) Recursivo
cuantos = lambda e, t: 0 if t == () else (1 if t[0] == e else 0) + cuantos(e, t[1:])

# b) Iterativo
cuantos_it = lambda e, t, acc: acc if t == () else cuantos_it(e, t[1:], acc + (1 if t[0] == e else 0))
cuantos = lambda e, t: cuantos_it(e, t, 0)
