try:
    x = int(input('Introduzca el primer número: '))
    y = int(input('Introduzca el segundo número: '))
    print('La suma es:', x + y)
except ValueError:
    print('Ha introducido un valor incorrecto.')
