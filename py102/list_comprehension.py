#[element for element in iterable] [element for element in iterable if condition]
numbers = []
for element in range(1,11):
    numbers.append(element)
print(numbers)

numbers = [element*2 for element in range(1,11)]
print(numbers)

numbers2 = []
for i in range(1,11):
    if i%2==0:
        numbers2.append(i*2)
print(numbers2)

numbers2 = [i*2 for i in range(1,11) if i%2==0]
print(numbers2)

