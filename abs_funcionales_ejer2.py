"""
2. Escribir una función que implemente la siguiente especificación:
Pre : 𝑛 ≥ 0
repite(𝑠: str, 𝑛: int) -> str
Post : repite(𝑠, 𝑛) = 𝑠 repetido 𝑛 veces
Dar un ejemplo de uso.
"""

from typing import Callable
repite = lambda s, n: s * n