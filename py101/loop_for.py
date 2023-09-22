""" for element in range(1, 21):
    print(element) """
my_list = [23, 45, 89, 43, 2]
my_list.sort()
for element in my_list:
    print(element)

my_tuple = ('ja', 'an', 'bi', 'co', 'de', 'em')
for element in my_tuple:
    print(element)

product = {
    'name': 'Shirt',
    'price': 100,
    'stock': 80
}

""" for element in product:
    print(element) """ #imprime solo las llaves

""" for element in product:
    print(product[element]) """ #imprime solo los valores
for key in product:
    print(key, '=>', product[key])
#otra forma de obtener la llave valor seria:
for key, value in product.items(): #genera un array que lo vuelve tupla
    print(key, '=>', value)

people = [
    {
        'name': 'John',
        'age': 21
    },
    {
        'name': 'Zule',
        'age': 29
    },
    {
        'name': 'Santi',
        'age': 44
    }
]
#recorrer esta lista de personas que trae varios diccionarios
for person in people:
    print(person)

for person in people:
    print('name =>', person['name'])
    
#recorrer lista y seleccionar solo los numeros positivos y agregarlos a un nuevo array

my_list = [20,-30,50,8,-8,1,-1,2,-2,3,-3,4,-4]
new_list = []


for n in my_list:
    if not n < 0:
        new_list.append(n)
new_list.sort()
print(new_list)