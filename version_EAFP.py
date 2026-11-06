try:    
    lista = ['a', 'b', 'c']
    indice = int(input('Introduzca un índice: '))
    print(lista[indice])
except ValueError:
    print('Ha introducido algo que no es un número.')
except IndexError:
    print('El índice no es correcto porque se sale de los límites.')