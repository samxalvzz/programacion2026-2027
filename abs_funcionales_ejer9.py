"""
9. La función potencia tiene la siguiente especificación:
Pre : 𝑏 ≥ 0
potencia(𝑎: int, 𝑏: int) -> int
Post : potencia(𝑎, 𝑏) = 𝑎
𝑏
a) Implementar la función de forma no recursiva.
b) Implementar la función de forma recursiva.
"""

# a) Forma recursiva
potencia = lambda a, b: a ** b

# b) Forma no recursiva
potencia = lambda a, b: 1 if b == 0 else a * potencia (a, b - 1)

