import types
from typing import Any

class Vector:
    def __init__(self, data: list) -> None: # *data añade una cantidad arbitraria de datos
        #self.data: list[int | float] = []
        "cada elemento de data que me mandan por parametro debe ser un numero"
        #for e in data: 
        #    if not isinstance(e,(int,float)): #isinstance es si el tipo de dato es int o float
        #        raise ValueError("La entrada debe ser numerica")
            
        #    self.data.append(e)#estas lineas de codigo son opcionales para validar el tipo de dato con que se agregue la siguiente linea funciona
        self.data = data

    def __add__ (self, other:"Vector") -> "Vector": #otro valor
        #iterar dos elementos a la vez, hay varias formas
        """ 
        OPCION 1:
        res = []
        for i in range(len(self.data)):
            res.append(self.data[i] + other.data[i])

        return Vector(res) """

        """   
        OPCION 2:
        res = [
            self.data[i] + other.data[i]
            for i in range(len(self.data))
            ]
        return Vector(res) """

        #OPCION 3:
        res = [
            a+b
            for a, b in zip(self.data, other.data)
        ]
        return Vector(res)

    
#print((Vector([1,2,3]) + Vector([4,5,6])).data)


    def __sub__ (self, other:"Vector") -> "Vector": 
        
        res = [
            a-b
            for a, b in zip(self.data, other.data)
        ]
        return Vector(res)

    def __mul__ (self, other:"Vector") -> "Vector": 
        
        res = [
            a*b
            for a, b in zip(self.data, other.data)
        ]
        return Vector(res)

#@
#[1,2,3]
#[4,5,6]
#1*4 + 2*5 + 3*6 ->
    def __matmul__(self, other: "Vector") -> float:
     res = self * other
     return sum(res.data)

#para indexar o para acceder a un valor debemos implementar get item y set item

    def __getitem__(self, key):
      return self.data[key]

#asignar setitem
    def __setitem__(self, key, value):
      self.data[key] = value

    def __str__(self) -> str:
      return str(self.data)

    def __eq__(self, other: "Vector"):
        """
        itero los dos si alguno de los elementos es diferente del otro retorno falso
        """
        for a, b in zip(self.data, other.data):
           if a != b:
            return False
        
        return True


v = Vector([1,2,3])
print(v[2]) #3
v[1] = 10
print(v)
#libreria LangChain

""" #zip: toma los elementos y lo retorna como una tupla
for e1, e2 in zip(["a", "b", "c"],["d", "e", "f"]):



#list comprehension
l1 = []
for i in range(10):
    l1.append(i)

l2= [i for i in range(10)] """