# llave valor
my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'Jam',
    'last_name': 'Quelet',
    'age': '29'
}
print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['name'])
print(my_dict.get('name')) #es lo mismo pero si no esta la llave muestra None, [] muestra error si no esta la llave

print('last_name' in my_dict)
print('avion' in my_dict)

person = {
    'name': 'Manu',
    'last_name': 'Rust',
    'langs': ['python', 'javascript'],
    'age': 26
}

print(person)
#actualizar o cambiar llave
person['name'] = 'John' 
person['age'] -= 6
person['langs'].append('rust')
print(person)

#eliminar un atributo de esos pares clave valor
del person['last_name']
person.pop('age')
print(person)

print('items:')
print(person.items())

print('keys:')
print(person.keys())

print('values:')
print(person.values())

person['media'] = 'fb' #agregar elemento 
print(person) 

print(list(person.keys())) #imprime una lista

