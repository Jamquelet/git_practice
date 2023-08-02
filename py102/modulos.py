#from collections import defaultdict
#import this   
#from typing import Tuple, List  #python < 3.9
#from dataclasses import dataclass
#import functools
#import random
#from abc import ABC #Abstrac Base Class
#import pickle # serializacion

import sys #preguntar sobre el sistema operativo
print(sys.path)#en que ubicacion estoy trabajando este archivo

import re #expresiones regulares

text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero favorito es el 7'
#obtener solo los string que coincidan con un numero de este texto
result = re.findall('[0-9]+', text)
print(result)

import time # manejo de horas y fechas
timestamp = time.time()#formato de la hora actual
print(timestamp) #1690598505.4475825 lo que representa la hora actual para el pc

local = time.localtime()#formato de humanos
result = time.asctime(local)
print(result)

import collections # util para manejar listas 
numbers = [1,1,2,2,3,3,3,3,3,4,4,5,5,6,9,8,7]
counter = collections.Counter(numbers)#frecuencia de un numero en la lista
print(counter)

