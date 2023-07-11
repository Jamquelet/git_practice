#CRUD: Create - Read - Update - Delete

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Create
print (numbers[1]) # Read
numbers[-1] = 10 #actualizar la ultima posicion
print(numbers)

numbers.append(700) #agrega elemento al final de la lista
print(numbers)
numbers.insert(0, 'hello') #recive dos parametros la posicion y cual es mi elemento
print(numbers)

numbers.insert(3, 'hice un cambio') #corre los demas a la derecha no elimina
print(numbers)

#fucionar listas,unir una lista a otra 
tasks = ['todo 1', 'todo 2', 'todo 3'] 
new_list = numbers + tasks
print(new_list) 

#metodo index para preguntar en que posicion esta un elemento
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

#metodos para eliminar elementos de la lista
new_list.remove('todo 1')
print(new_list)

new_list.pop()# ,pop elimina el ultimo elemento de la lista
print(new_list)

new_list.pop(0) #tambien se le puede dar la posicion del elemento
print(new_list)

new_list.reverse() #metodo para voltiar todo el array trasforma el array y lo cambia de posicion
print(new_list)

#sort ordenar
numbers_a = [1, 4, 6, 3]
numbers_a.sort() #ordena del menor al mayor
print(numbers_a)

strings = ['re', 'ab', 'ed'] 
strings.sort() #ordena en el nombre del abecedario, si tiene tipos de datos mezclados no funciona
print(strings)


""" 
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor. 
"""