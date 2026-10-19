"""
26. La función menor tiene la siguiente especificación:
Pre : 𝑡 ≠ ()
menor(𝑡: tuple[𝛼]) -> 𝛼
Post : menor(𝑡) = el menor elemento de 𝑡
Por ejemplo: menor((3, 2, 5, 7)) == 2.
Escribir una función recursiva que satisfaga dicha especificación
"""
menor = lambda t: t[0] if t[1:] == () else min(t[0], menor(t[1:]))