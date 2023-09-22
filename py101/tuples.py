#inmutables no se pueden modificar
numbers = (1,2,3,4,5,6,7,8,9,10)
strings = ('nico', 'zule', 'santi', 'jam')
print(numbers)
print('0=>', numbers[0])#ver el elemento que esta en esta posicion
print('-1=>', numbers[-1])#ver elemento de la ultima posicion
print(type(numbers))

tipos_datos = (12, 'santi', True)

#solo podemos declarar, no podemos insertar elementos, podemos buscar elementos dentro de la tupla
print(strings)
print(strings.index('nico'))
print(strings.count('nico'))#podemos ver cuantas veces esta un elemento dentro de la tupla

#si podemos hacer trasformaciones de tupla a lista

my_list= list(strings)#de tupla a list 
strings[1] = 'July' #si puedo modificar la lista la posicion 1 la cambio a July

my_tuple = tuple(my_list)