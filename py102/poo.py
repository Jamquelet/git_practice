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

