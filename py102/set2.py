set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_types = {'col', 12, 12.12, True}

#salida {'h', 'o', 'l', 'a'}
set_from_string = set('hola')
print(set_from_string)

set_from_tuple = set(('abc', 'cbv', 'ad' ))
print(set_from_tuple) #{'abc', 'cbv', 'ad'}

numbers = [1,2,3,4,5,6,7,2,3,4,5,6,7]
set_numbers = set(numbers)
print(set_numbers) #{1, 2, 3, 4, 5, 6, 7}
#puedo pasar un dict a una lista
unique_numbers = list(set_numbers)
#CRUD
size = len(set_countries)
print(size) # 3
print('col' in set_countries) #True
# add
set_countries.add('per')
# update: los agrega al conjunto
set_countries.update({'arg', 'ecu', 'per'})
# remove
set_countries.remove('per')
# si remuevo un elemento que no esta saca error se utiliza .discard para queno estalle el programa
set_countries.discard('ven')
#limpiar el conjunto elimina los elementos
set_countries.clear()

## operaciones entre conjuntos
# union
set_a = {'col','mex','bol'}
set_b = {'pe', 'bol'}
set_c = set_a.union(set_b) # o set_a | set_b
print(set_c) # {'col', 'bol', 'mex', 'pe'}

# intersection: elementos en comun
set_c = set_a.intersection(set_b) # o set_a & set_b

#difference elementos de a sin los elementos de b
set_c = set_a.difference(set_b) # o set_a - set_b

#symetric difference: sin los elementos en comun
set_c = set_a.symmetric_difference(set_b) # o set_a ^ set_b
