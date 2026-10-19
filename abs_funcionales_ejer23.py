"""
23. La función palindromo tiene la siguiente especificación:
Pre : True
palindromo(𝑡: tuple) -> bool
Post : palindromo(𝑡) =
True si 𝑡 es un palíndromo
(se lee igual en un sentido que en otro)
False en caso contrario
Por ejemplo: palindromo((1, 2, 3, 4, 3, 2, 1)) == True.
Escribir una función recursiva que satisfaga dicha especificación.

"""
palindromo = lambda t: True if len(t) < 2 else t[0] == t[-1] and palindromo(t[1:-1])