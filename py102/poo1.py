# atributos principales de un obj : tipo, conteo de referencias,resto de contenido: 
#instance attributes: 
#class atributes: se definen variables fuera del init, se dan variables a nivel de clase
#f-strings
carpeta1 = 'archivos'
carpeta2 = 'importantes'
carpeta3 = 'files'
archivo ='foto.png'

""" direccion = carpeta1 + "/" + carpeta2 + "/" + carpeta3 + "/" + archivo 
print(direccion)
 """

direccion2 = f"{carpeta1}/{carpeta2}/{carpeta3}/{archivo}"
print(direccion2)
edad=10
nombre='Jam'
text = f"Hola {nombre} tienes {edad} años" 
print(text)

#class - instance - attribute/field - method
""" class NameofClass(SuperClass): #formato camel case
    def __init__(self): """
        #atributos aqui

    #metodos aqui #snake clase
class Persona:
    def __init__(self,nombre,edad,dni) -> None:
        self.nombre = nombre
        self.edad= edad
        self.dni = dni

    def __str__(self) -> str :
        return f"Persona({self.nombre}, {self.edad}, {self.dni})"
    '''
    def__len__(self) -> int:
    '''
    def comer(self, plato):
        print(f"Que rico {plato}")

p1 =Persona('Laura', 20,'111111')
#print(p1) dirige a un puntero num hexagesimal
""" print(p1.nombre)
print(p1.edad)
print(p1.dni) """
texto = f"Hello {p1}"
print(texto)

str(p1)
print(p1.__str__())

p1.comer('beef')

# paso por referencias
p5 = Persona('adsl', 16, '9855588')
p6= Persona ('Olaf', 22, '15448545451')

p7= p1 # no estoy haciendo una copia de p1, python guarda un conteo de referencias de cada objeto, de cuantas variables estan apuntando, la variableapunta a un espacio en memoria
#esto crea una referencia mas para el mismo bloque de memoria, ambos verian los cambios reflejados porq apuntan al mismo espacio

#monkey patching = python permite crearle atributos de manera dinamica a las instancias una vez han sido creadas
class Prueba:
    conteo=0

pr1 = Prueba()
pr2=Prueba()

pr1.conteo
pr2.conteo

pr1.conteo += 1
print(pr1.conteo)
print(pr2.conteo)


pr1.patito =':D'
pr2.asdasdad=':('
print(pr1.patito)
print(pr2.asdasdad)

Prueba().conteo += 1


class Tupla3:
    def __init__(self, v1,v2,v3)->None:
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

##Dataclases:permiten crear clases con una sintaxis class atributes, crea el init solo crea elprint solo
from dataclasses import dataclass

#Implementar una clase Tupla3, tupla de 3 valores, método suma que devuelva la suma de los 3 valores
@dataclass
class  Trica:
    v1: int | float
    v2: int | float
    v3: int | float

    def __add__(self,other):
        return Trica(self.v1+other.v1,self.v2+other.v2,self.v3+other.v3)

t1 = Trica(1,2,3)
t2 = Trica(4,5,6)
print(t1)
print(t2)
print(t1+t2)

t3= Trica(1,2,3)
print(t3==t1) #True

#pydantic dataclass con 'esteroides
#Agregación : rombo-es una relacion debil -los componentes pueden ser compartidos -la destruccion del componente no destruye el compuesto
#Composición: representado por rombo oscuro -Es una relacion fuerte - Los componentes no pueden ser compartidos - la detruccion del componente conlleva la destruccion del compuesto