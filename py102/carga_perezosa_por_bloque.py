import cv2 #open cv  para trabajar con procesamiento de img. se debe instalar
import matplotlib.pyplot as plt #generar graficas, mostrar imagenes. se debe instalar

#cargando imagen individualmente
import os

def to_rgb(img): return cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #funct que convierte las img a rgb, que la img se vea bn

def cargar_imagenes_lazy(directory, function):
  '''
  cargar las imagenes de forma perezosa. Generador que recive un directorio(una carpeta en disco) donde quiero cargar imagenes, y una funccion que le quiera aplicar a esas imagenes. voy a iterar sobre los archivos. list dir lista todos los archivos y carpetas. que hay en esa carpeta, lista con los archivos. '''
  for filename in filter(lambda f: ".png" in f, os.listdir(directory)): # esta funcion lambda lista el directorio y si tiene .png es un archivo que yo quiero. conforme los pido, esta funcion saca todos los archivos .png y se los va devolviendo pero no de golpe
    yield function(cv2.imread(f'{directory}/{filename}'))#concede los imread me carga el archivo del directorio, lo convierte 

for img in cargar_imagenes_lazy("imgs", to_rgb):#para todas las imagenes en esta carpeta quiero ir leyendo, imagen que leo la muestro y la borra de la ram
  print(type(img))
  plt.imshow(img)
  plt.show()

#Ahora toca implementar cargar en bloques. La lógica para esto es usar el operador slicing
# Por ejemplo si tenemos
letras = ['a', 'b', 'c', 'd', 'e']

# queremos extraerlas en bloques de 2
bloque_1 = letras[0:2]
print(bloque_1)

bloque_2 = letras[2:4]
print(bloque_2)

bloque_3 = letras[4:6]
print(bloque_3)

#el operador slicing no tiene problemas si el extremo derecho del rango es mayor al tamaño de la lista, cuando llega al final, se detiene.Para iterar de bloque en bloque sólo debemos seguir la regla

#datos[tamaño_bloque*n_bloque: tamaño_bloque*(n_bloque+1)]

#y para cada bloque, debemos iterar de manera perezosa para retornar las imagenes "leídas"
from math import ceil

def carga_perezosa_bloques(directory: str, batch_size: int):
    filenames = list(filter(lambda f: ".png" in f, os.listdir(directory))) #cargo todos los nombres de archivos

    for i in range(ceil(len(filenames)/batch_size)):
        yield [
            to_rgb(cv2.imread(f'{directory}/{filename}'))
            for filename in filenames[batch_size*i: batch_size*(i+1)] #se los voy devolviendo pero solo los bloques
        ]

for imgs in carga_perezosa_bloques("imgs", 4):#que me cargue de 4 en 4 leyendo del disco y devuelve una lista de 4 imagenes
  print(len(imgs))
