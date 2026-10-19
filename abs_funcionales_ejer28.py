"""
28. La función menor_mayor tiene la siguiente especificación:
Pre : 𝑡 ≠ ()
menor_mayor(𝑡: tuple[𝛼]) -> tuple[𝛼]
Post : menor_mayor(𝑡) = una tupla con dos elementos
que contiene el menor y el mayor elemento de 𝑡,
en ese orden
Por ejemplo: menor_mayor((3, 2, 5, 7)) == (2, 7).
Escribir una función recursiva que satisfaga dicha especificación.
"""
actualiza = lambda x, p: (min(x, p[0]), max(x, p[1]))
menor_mayor = lambda t: (t[0], t[0]) if t[1:] == () else actualiza(t[0], menor_mayor(t[1:]))