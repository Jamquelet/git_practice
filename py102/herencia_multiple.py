#ejemplo problema del diamante: b y c heredan de a, y d hereda de b y c, a cual le damos prioridad: python prioriza la clase de izq a derecha

class A:
    def __init__(self, a) -> None:
        self.a = a

class B:
    def __init__(self, b) -> None:
        self.b = b

class C(A, B):
    def __init__(self, a,b,c) -> None:
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c 

    def __str__(self) -> str:
        return f"{self.a=}, {self.b=}, {self.c=}"
    
obj = C(1,2,3)
print(obj)

##
class A:
    def __init__(self, a) -> None:
        self.a = a

class B(A):
    def __init__(self,a, b) -> None:
        A.__init__(self,a)
        self.b = b

class C(A):
    def __init__(self, a,c) -> None:
        A.__init__(self, a)
        self.c = c 
    
class D(B, C):
    def __init__(self, a,b,c) -> None:
        B.__init__(self, a, b)
        C.__init__(self, a, c)
        self.c = c 

    def __str__(self) -> str:
        return f"{self.a=}, {self.b=}, {self.c=}"
    
obj = D(1,2,3)
print(obj)

'''
class Clase:
    def metodo(self,a,b,c):
        ...
        
Cuando se invoca
obj = Clase()
obj.metodo(a,b,c)

es equivalente 
metodo(obj, a, b, c) # no funcionara en python el self se inyecta
'''

class A:
    def func(self):
        print('A')

class B(A):
    def func(self):
        print('B')

class C(A):
    def func(self):
        print('C')

class D(C,B):
    pass

#python lo resuelve priorizando el orden de herencia
d= D()
d.func()
# retorna C

#ejemplo vehiculo
from dataclasses import dataclass
@dataclass
class Vehiculo:
    nro_ruedas: int
    capacidad: int

class VehiculoGasolina(Vehiculo):
    def __init__(self,nro_ruedas,capacidad,tipo_motor):
        Vehiculo.__init__(self,nro_ruedas,capacidad)#llamamos el constructor de vehiculo
        self.tipo_motor = tipo_motor

class VehiculoElectrico(Vehiculo):
    def __init__(self,nro_ruedas,capacidad,potencia):
        Vehiculo.__init__(self,nro_ruedas,capacidad)
        self.potencia = potencia

class VehiculoHibrido(VehiculoGasolina,VehiculoElectrico):
    def __init__(self, nro_ruedas,capacidad,tipo_motor,potencia, so):
        VehiculoGasolina.__init__(self, nro_ruedas, capacidad,tipo_motor)
        VehiculoElectrico.__init__(self, nro_ruedas, capacidad,potencia)
        self.so = so

    def __str__(self) -> str:
        return ", ".join([str(self.nro_ruedas), str(self.capacidad), str(self.tipo_motor), str(self.potencia), str(self.so)])
    
vh = VehiculoHibrido(nro_ruedas=4, capacidad=2, tipo_motor="V6", potencia="720 KWh", so="Android Auto")
print(vh)

#Composition over inheritance: utilizar mas composicion que herencia ya que es engorroso la herencia multiple

#seria reescribir el vehiculo hibrido
class VehiculoHibrido:
    def __init__(self, nro_ruedas,capacidad,tipo_motor,potencia, so):
        vg = VehiculoGasolina(nro_ruedas, capacidad,tipo_motor)
        ve = VehiculoElectrico(nro_ruedas, capacidad,potencia)
        self.so = so

    def __str__(self) -> str:
        return ", ".join([str(self.nro_ruedas), str(self.capacidad), str(self.tipo_motor), str(self.potencia), str(self.so)])
    
