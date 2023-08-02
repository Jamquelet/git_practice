#libreria PyTorch: AI- modelos - buffers
#abrir archivo - lectura Texto Plano
f = open("datos.txt") #implitamente es "r" de lectura   #abrir un buffer

#print(f.read()) #lee todo el texto de golpe como si fuera una sola cadena
#print(repr(f.read())) #que me muestre por las comillas. representacion 
""" print(f.readline())#solo lee una linea de un archivo
print(f.readline())
print(f.readline())
 """
linea = None
while linea != "":  # ya no hay espacios vacios
    linea = f.readline() 
    print(linea.strip())

f.close() #siempre cerrarlo  #cerrar un buffer

#escritura Texto Plano

f=open("datos.txt", "w") # write borra todo lo q hay en el archivo y escribe lo que yo le mande al buffer

f.write("patito\n") #se debe poner explicitamente salto de linea o sale pegado
f.write("aaa") #puedo escribir linea a linea

f.close() 

#para escribir y no me borre
f = open("datos.txt", "a+") #append- "a" cada vez que esncuentre el archivo le va agregando una nueva linea y si no existe el archivo me lo creas

f.write("\nbbbbb")

f.close()

#context managers = manipulador de contexto
#no tengo q hacer un close, ciera el canal de comunicacion

with open("datos.txt") as f: #abrir el archivo y dale el nombre de f
    print(f.readlines()) #lee el archivo en una lista, termina y cierra el archivo

#pickles 

from dataclasses import dataclass

@dataclass
class Persona: 
    name: str
    age: int

p1=Persona("Pepito", 20)
p2=Persona("Juan","Gallego")

print(p1,p2)

import pickle #concepto de serializacion, convierte un objeto a datos binarios y los va a guardar en el archivo como si fuera imformacion compactada. comprime pesa menos

with open("personas.dat", "w+b") as f: #personas.dat lo crea si no existe. a+ = adiccionar b = bytes. quiero que mantengas el protocolo de crear el archivo si no existe y si ya existe existe hazle un append pero quiero que escribas en formato binario en bytes
    pickle.dump(p1, f)# voy a guardar una persona y quiero mandarselo a un archivo f
    pickle.dump(p2, f)

#para leerlo
with open("personas.dat", "rb") as f:
    while True: #leer hasta que se termine el archivo
        try: #intenta leer, si ya no puedes 
            obj = pickle.load(f)
            print(obj)
        except EOFError: #
            print("Fin de archivo")
            break #rompe el bucle mientras no de error sigue leyendo

 