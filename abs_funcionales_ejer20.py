"""
20. La función ultimo tiene la siguiente especificación:
Pre : 𝑡 ≠ ()
ultimo(𝑡: tuple) -> Any
Post : ultimo(𝑡) = el último elemento de t
Escribir una función recursiva que satisfaga dicha especificación.
"""

ultimo = lambda t: t[0] if t[1:] == () else ultimo(t[1:])