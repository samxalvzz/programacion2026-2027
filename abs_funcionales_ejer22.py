"""
22. La función invertir tiene la siguiente especificación:
Pre : True
invertir(𝑡: tuple) -> tuple
Post : invertir(𝑡) = una tupla con los elementos de 𝑡 en orden contrario
Por ejemplo: invertir((1, 2, 3, 4)) == (4, 3, 2, 1).
Escribir una función recursiva que satisfaga dicha especificación.
"""
invertir = lambda t: if t == () else invertir(t[1:]) + (t[0],)