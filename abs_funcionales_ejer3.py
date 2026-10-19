"""
Escribir una función que implemente la siguiente especificación:
Pre : len(𝑐) = 1
es_vocal(𝑐: str) -> bool
Post : es_vocal(𝑐) = 𝑐 es una vocal, acentuada o no
Dar un ejemplo de uso
"""

es_vocal = lambda c: c.lower() in 'aeiouàèìòù'

# Si lo queremos con una anotación de tipos, seria:

"""
from typing import Callable

es_vocal: Callable[str], bool] = lambda c: c.lower() in 'aeiouàèìòù'

"""