""" Implementar una clase Vector que contiene un vector en el sentido matemático, sobrecargar los operadores +, -, *, @ y [] de la siguiente forma:

+ corresponde a la función reservada __add__ y nos permite sumar dos vectores elemento a elemento
- resta elemento a elemento, corresponde a __sub__
producto elemento a elemento con __mul__
@ es un operador especial de Python usado para multiplicaciones matriciales, en este caso implementar el producto punto de dos vectores, de la siguiente manera
sea un vector [a1, a2, ..., an] y otro [b1, b2, ..., bn] su producto punto es a1_b1 + a2b2 + ... + an_bm*
El operador [] tiene dos funciones, asignar un valor a la posición i, y obtener el valor en esa posición
Para obtener el valor se implementa la función __getitem__
Para asignar se usa la función __setitem__ """
#Sobrecargar operadores:
#return Vector(*result)

##con esta implementacion hemos creado una clase Vector que permite realizar diversas operaciones matematicas

class Vector:

    def __init__(self, *args):
        '''
        este es el contructor de la clase. Permite crear un objeto Vector pasando los elementos del vector como argumentos separados por comas'''

        self.vector = list(args)

    def __repr__ (self):
        '''
        Es una función especial que devuelve una representacion legible de la clase en forma de cadena. Se utiliza para mostrar el vector cuando imprimimos un objeto Vector'''

        return f"Vector({', '.join(str(x) for x in self.vector)})"

    def __add__ (self, other):
        '''
        Sobrecarga el operador de suma + para realizar la suma elemento a elemento de dos vectores'''

        if len(self.vector) != len(other.vector):
            raise ValueError("Los vectores deben tener la misma longitud para sumarlos.")
        result = [a+b for a,b in zip(self.vector, other.vector)]
        return Vector(*result)
    
    def __sub__(self, other):
        '''
        Sobrecarga el operador resta - para realizar la resta elemento a elemento de dos vectores.'''

        if len(self.vector)!= len(other.vector):
            raise ValueError("Los vectores deben tener la misma longitud para restarlos.")
        result = [a-b for a,b in zip(self.vector,other.vector)]
        return Vector(*result)
    
    def __mul__(self, other):
        '''
        Sobrecarga el operador de multiplicacion * para realizar el producto elemento a elemento de dos vectores o la multiplicacion escalar de un vector por un numero'''

        if isinstance(other,Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Los vectores deben tener la misma longitud para multiplicarlos elemento a elemento.")
            result = [a*b for a,b in zip(self.vector,other.vector)]
            return Vector(*result)
        elif isinstance(other,(int,float)):
            result = [a*other for a in self.vector]
            return Vector(*result)
        else:
            raise TypeError("unsupported vector type - el tipo de dato no es compatible con la multiplicación.")
        
    def __matmul__(self, other):
        '''
        Sobrecarga el operador @ para realizar el producto  punto a punto entre dos vectores'''

        if not isinstance(other, Vector):
            raise TypeError("El operador @ solo es valido para multiplicacion punto a punto entre vectores.")
        if len(self.vector) != len(other.vector):
            raise ValueError("Los vectores deben tener la misma longitud para realizar el producto  punto.")
        result = sum(a*b for a,b in zip(self.vector, other.vector))
        return result
    
    def __getitem__(self,index):
        '''
        permite tener el valor en una posicion especifica del vector utilizando la sintaxis vector[i]'''
        return self.vector[index]
    
    def __setitem__(self,index, value):
        '''
        Permite asignar un valor a  una posicion especifica del vector utilizando la sintaxis vector[i]=value.'''
        self.vector[index] = value

#Con esta implementacion podemos crear objetos 'Vector' y utilizar los operadores sobrecargados de la siguiente manera:
#crearlos
v1 = Vector(1,2,3)
v2 = Vector(4,5,6)

#suma de vectores
suma = v1 +v2 #Vector(5,7,9)

resta = v1-v2 #Vector(-3,-3,-3)
print(resta)

#producto elemento a elemento de vectores
producto_elemento_a_elemento = v1 * v2 #Vector(4,10,18)

#multiplicacion escalar
multiplicacion_escalar = v1*2#Vector(2,4,6)

#producto punto de vectores
producto_punto =v1 @ v2 #Resultado:32 los multiplica y luego suma los productos

#obtener un valor en una posicion
valor = v1[1]#resultado 2

#asignar valor en una posicion especifica
v1[1] = 10 
print(v1) #resultado Vector(1,10,3)



##refactoring para pasar pytest
class Vector:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Los vectores deben tener la misma longitud para la suma.")
        result = [a + b for a, b in zip(self.data, other.data)]
        return Vector(result)

    def __sub__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Los vectores deben tener la misma longitud para la resta.")
        result = [a - b for a, b in zip(self.data, other.data)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Los vectores deben tener la misma longitud para el producto elemento a elemento.")
        result = [a * b for a, b in zip(self.data, other.data)]
        return Vector(result)

    def __matmul__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Los vectores deben tener la misma longitud para el producto punto.")
        result = sum(a * b for a, b in zip(self.data, other.data))
        return result

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return f"Vector({self.data})"



####
#from solution import Vector


def test_vector_suma():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    resultado = v1 + v2
    assert resultado == Vector([5, 7, 9])

def test_vector_resta():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    resultado = v1 - v2
    assert resultado == Vector([-3, -3, -3])

def test_vector_producto_elemento_a_elemento():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    resultado = v1 * v2
    assert resultado == Vector([4, 10, 18])

def test_vector_producto_punto():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    resultado = v1 @ v2
    assert resultado == 32
