suma = lambda x, y: x + y
producto = lambda x, y: x * y
combinada = lambda a, b: suma(a, b) - producto(a, b)
a = suma(2, 3)
b = combinada(4, 5)

# Primer ámbito es toda la expresión. Es el ámbito global.
# Segundo ámbito es x + y de suma.
# Tercer ámbito es x * y de producto.
# Cuarto ámbito es suma(a, b) - producto(a, b) de combinada