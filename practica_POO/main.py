"""
IMPORTANTE:
Al crear la clase Estudiante, agregar la siguiente función

def __hash__(self):
    return int(sha256(self.ru.encode()).hexdigest(), 16) #sha256 es un metodo de hashing

Esta permitirá que pueda ser utilizado en un diccionario
"""


from random import random
import pickle #para poder trabajar con archivos
from clases import * #importa todo
from collections import defaultdict
import os

def adicionar_materia_a_archivo(materia: Materia, filename="materias.dat"):
    with open(filename, "a+b") as f: #f es el puntero que guarda en el disco
        pickle.dump(materia, f) #dump= botar-tirar de forma binaria la materia al archivo f
    

def estudiante_en_dos_materias(filename="materias.dat"): #estudiante debe tener un hash ya que repetidos es un dict
    repetidos = defaultdict(int) # tipo de dato que va a tener el valor
    
    with open(filename, "rb") as f:
        while True:
            try: #intenta leer la materia una instancia de la materia
                materia: Materia = pickle.load(f)
                for paralelo in materia.paralelos:
                    for estudiante in paralelo.estudiantes:
                        repetidos[estudiante] += 1 # estamos utilizando el dicionario para contar instancias de estudiantes al leer todas las materias
            except EOFError:
                break

    for estudiante, conteo in repetidos.items(): #items permite devolver una tupla de llave valor
        if conteo == 2:
            print(estudiante)


def agregar_auxiliar(
    auxiliar: Auxiliar, 
    sigla_paralelo: str, 
    filename="materias.dat"
):
    with open(filename, "rb") as f, open("temp.dat", "wb") as temp:
        while True:
            try: #intenta leer la materia una instancia de la materia
                materia: Materia = pickle.load(f)
                for paralelo in materia.paralelos:
                    if paralelo.sigla == sigla_paralelo:
                        paralelo.auxiliar = auxiliar

                pickle.dump(materia, temp) #
            except EOFError:
                break
                #borrar todo lo de temporal, sobreescrito todo en mi archivo real
    with open(filename, "wb") as f, open("temp.dat", "rb") as temp: #sobreescribir el archivo original
        while True:
            try: #intenta leer la materia una instancia de la materia
                materia: Materia = pickle.load(temp)
                pickle.dump(materia, f) #
            except EOFError:
                break

    os.remove("temp.dat")

def mostrar_materias(filename = "materias.dat"):
     with open(filename, "rb") as f:
        while True:
            try: 
                materia: Materia = pickle.load(f)
                print(materia)
            except EOFError:
                break


def main():
    estudiantes = [
        Estudiante(nombre=f"E{i}", dni=f"{i}" * 3, ru=f"{i}" * 4) 
        for i in range(1, 7) #list comprehension para ir desde 1 hasta 7 e ir generando estudiantes con el nombre e1-e2...e7. dni el numero i*3 ru i*4. generar 7 datos artificiales 
    ]

    docentes = [
        Docente(
            nombre=f"D{i}", dni=f"{i}", sueldo=round(random() * 10000, 2), titular=True#crea  par de docentes con sueldos aleatorios
        )
        for i in range(8, 11)
    ]
#crea 3 paralelos, asignamos ciertos docentes a estos paralelos, un grupo de estudiantes y un grupo de notas
    paralelo_1 = Paralelo(
        sigla="p1", docente=docentes[0], estudiantes=estudiantes[:2], notas=[50, 20]
    )
    paralelo_2 = Paralelo(
        sigla="p2", docente=docentes[1], estudiantes=estudiantes[2:4], notas=[60, 100]
    )
    paralelo_3 = Paralelo(
        sigla="p3",
        docente=docentes[2],
        estudiantes=estudiantes[4:] + [estudiantes[0]],
        notas=[40, 30, 10],
    )
#creamos dos materias una con dos paralelos y una con un paralelo
    m1 = Materia(nombre="M1", sigla="M1", paralelos=[paralelo_1, paralelo_2])
    m2 = Materia(nombre="M2", sigla="M2", paralelos=[paralelo_3])

    # Adicionar todas las materias al archivo
    #adicionar_materia_a_archivo(m1)#porque sino se van adicionando materias al archivo y vamos a tener informacion duplicada
    #adicionar_materia_a_archivo(m2)

    # Mostrar los estudiantes que están en en ambas materias
    #estudiante_en_dos_materias()

    #agregar auxiliares a los parelelos
    #a1 = Auxiliar(nombre="a1", dni = "123", ru= 123, sueldo=1000, nro_item=1)
    #a2 = Auxiliar(nombre="a2", dni = "456", ru= 456, sueldo=1000, nro_item=2)
    #a3 = Auxiliar(nombre="a3", dni = "789", ru= 789, sueldo=1000, nro_item=3)
    #agregar_auxiliar(a1, "p1")
    #agregar_auxiliar(a2, "p2")
    #agregar_auxiliar(a3, "p3")

    #leyendo el archivo
    mostrar_materias()

    #descontar el 12% al auxiliar del paralelo de algun docente a eleccion(por el nombre)
    #para esto crear una funcion que reciba una lista de materias y el nombre del docente

if __name__ == "__main__":
    main()