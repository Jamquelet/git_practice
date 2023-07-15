# {key:value for var in iterable} {key:value for var in iterable if condition} 
dict = {}
for i in range(1,5):
    dict[i] = i*2
print(dict)

dict = {i:i*3 for i in range(1,5)}
print(dict)

import random

countries = ['col','mex','bol','per']
population = {}
for country in countries:
    population[country] = random.randint(1,50)
print(population)

population2 = {country:random.randint(1,60) for country in countries}
print(population2)
#
names = ['nico','zule','santi']
ages = [12,25,32]
print(list(zip(names,ages)))#zip unir lista con otra

new_dict = {name: age for (name,age) in zip(names,ages)}
print(new_dict)
#conditional
import random
countries = ['col','mex','us','bol']
population1 = {country:random.randint(1,100) for country in countries}
result = {country: population for (country, population) in population1.items() if population>55}
print(result)

text = 'Hello, i am fine'
unique={c:c.upper() for c in text if c in 'aeiou'}
print(unique) 


