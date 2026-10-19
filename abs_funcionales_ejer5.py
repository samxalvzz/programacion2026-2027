"""
5. Escribir una función que calcule la distancia euclídea entre dos puntos (𝑥1, 𝑦1) y (𝑥2, 𝑦2),
descrita por la siguiente especificación:

Pre : True
distancia(𝑥1: float, 𝑦1: float, 𝑥2: float, 𝑦2: float) -> float
Post : distancia(𝑥1, 𝑦1, 𝑥2, 𝑦2) = √︁ (𝑥1 − 𝑥2) 2 + (𝑦1 − 𝑦2) 2
Dar un ejemplo de uso.

"""

distancia = lambda x1, y1, x2, y2: ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5