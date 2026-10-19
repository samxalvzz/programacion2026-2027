"""
7. Escribir una función que reciba dos instantes de tiempo en forma de horas y minutos y
que cumpla con la siguiente especificación:
Pre : ℎ𝑜𝑟𝑎1 ≥ 0 ∧ 𝑚𝑖𝑛𝑢𝑡𝑜1 ≥ 0 ∧ ℎ𝑜𝑟𝑎2 ≥ 0 ∧ 𝑚𝑖𝑛𝑢𝑡𝑜2 ≥ 0
distancia(ℎ𝑜𝑟𝑎1: int, 𝑚𝑖𝑛𝑢𝑡𝑜1: int, ℎ𝑜𝑟𝑎2: int, 𝑚𝑖𝑛𝑢𝑡𝑜2: int) -> int
Post : distancia(ℎ𝑜𝑟𝑎1, 𝑚𝑖𝑛𝑢𝑡𝑜1, ℎ𝑜𝑟𝑎2, 𝑚𝑖𝑛𝑢𝑡𝑜2) =
la cantidad de minutos que existen de diferencia entre los dos instantes
Dar un ejemplo de uso
"""

distancia = lambda hora1, minuto1, hora2, minuto2: abs((hora2 * 60 + minuto2) - (hora1 * 60 + minuto1))
