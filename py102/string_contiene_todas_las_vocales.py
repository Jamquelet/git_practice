def contiene_todas_las_vocales(palabra):
    palabra = palabra.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    for v in vocales:
        if v not in palabra:
            return False
    return True

palabra = input('ingrese la palabra ')
if contiene_todas_las_vocales(palabra):
    print('contiene todas las vocales')
else:
    print('no contiene todas las vocales')