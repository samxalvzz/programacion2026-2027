"""
10. La función repite tiene la siguiente especificación:
Pre : 𝑛 ≥ 0
repite(𝑠: str, 𝑛: int) -> str
Post : repite(𝑠, 𝑛) = 𝑠 * 𝑛
Implementar la función de forma recursiva.
"""

repite = lambda s, n: '' if n == 0 else s + repite(s, n - 1)
