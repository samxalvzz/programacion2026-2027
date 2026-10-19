"""
16. La función elem tiene la siguiente especificación:
Pre : True
elem(𝑒, 𝑡: tuple) -> bool
Post : elem(𝑒, 𝑡) =
{︄
True si e está en t
False en caso contrario
Escribir una función recursiva que satisfaga dicha especificación
"""
elem = e, t: False if t == () else True if t[0] == e else elem(e, t[1:])
