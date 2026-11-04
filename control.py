numero = int(input('Introduzca un número: '))

es_par = lambda n: n % 2 == 0

if es_par(numero):
    print('El número', numero, 'es par')
else:
    print('El número', numero, 'es impar')