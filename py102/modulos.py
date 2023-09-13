#from collections import defaultdict
#import this   
#from typing import Tuple, List, Optional #python < 3.9
#from dataclasses import dataclass, field #para listas 
#import functools
#import random
#from abc import ABC #Abstrac Base Class
#import pickle # serializacion- archivos. comunicacion entre programa, que estan ejecuando en paralelo y se necesitan sincronizar
#from hashlib import sha256
#import os
#from typing import Callable
#import time 
#import cv2 #open cv  para trabajar con procesamiento de img
#import matplotlib.pyplot as plt #generar graficas, mostrar imagenes
#from math import ceil
#import csv #leer csv
#joblib

#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker, declarative_base
#from sqlalchemy import Column, Integer, String
#import sqlite3

#from tortoise import Tortoise, fields, run_async
#from tortoise.models import Model
#from tortoise.expressions import Q  #Filtrar con operadores de comparación
#from tortoise.functions import Count import Sum import Avg



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

