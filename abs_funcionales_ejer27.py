"""
27. La función mayor tiene la siguiente especificación:
Pre : 𝑡 ≠ ()
mayor(𝑡: tuple[𝛼]) -> 𝛼
Post : mayor(𝑡) = el mayor elemento de 𝑡
Por ejemplo: mayor((3, 2, 5, 7)) == 7.
Escribir una función recursiva que satisfaga dicha especificación
"""
mayor = lambda t: t[0] if t[1:] == () else max(t[0], mayor(t[1:]))