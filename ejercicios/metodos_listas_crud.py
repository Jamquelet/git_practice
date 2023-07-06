#CRUD: Create - Read - Update - Delete

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Create
print (numbers[1]) # Read
numbers[-1] = 10 #actualizar la ultima posicion
print(numbers)

numbers.append(700) #agrega elemento al final de la lista
print(numbers)
numbers.insert(0, 'hello') #recive dos parametros la posicion y cual es mi elemento
print(numbers)

numbers.insert(3, 'hice un cambio')