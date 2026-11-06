lista = ['a', 'b', 'c']

entrada = input('Introduzca un índice: ')

if ...:
    indice = int(entrada)
 
if (indice >= 0 and indice <= len(lista) - 1) or \
   (indice <= -1 and indice >= -len(lista)):
    print(lista[indice])