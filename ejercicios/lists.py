numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'hello']
print(types)

print(numbers[0])
print(tasks[0])
print(types[1])

""" text = 'hello'
text[0] = 'w' """  #los strings son inmutables no puedo cambiar tengo q utilizar otro metodo como replace una lista si puedo hacer esto

tasks[0] = 'watch platzi courses' # cambio la posicion 1 de la lista tasks
print(tasks)

#seleccionar parte de los elementos de la lista
print(numbers[:3])
print(True in types)
print('hello' in types)