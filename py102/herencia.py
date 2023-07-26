from dataclasses import dataclass

@dataclass
class Persona:
    nombre:str
    edad:int

@dataclass
class Trabajador(Persona):
    sueldo:float

@dataclass
class Cliente(Persona):
    nro:int

t= Trabajador('Pepito', 25, 1000)
c= Cliente('Maria', 30,111)

print(t)
print(c)

#reimplementando sin dataclass
class Persona1:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre #__ lo vuelve seudo privado
        self.__edad = edad 

    """ def get_nombre(self):
        return self.__nombre
    def set_nombre(self, value:str):
        self._nombre = value """

    @property #permite utilizar .nombre directamente llama al getter sin definir la funcion 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str):
        if isinstance(value,str):
            raise ValueError('el nombre debe ser de tipo cadena')
        
        self.__nombre = value
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value: int):
        if isinstance(value,int):
            raise ValueError('la edad debe ser de tipo entero')
        
        self.__edad = value

    def __str__(self) -> str:
        return f"nombre={self.nombre}, edad={self.edad}"
        

p = Persona1('pepe', 15)

#print(dir(p)) 
""" print(p.nombre)
p.nombre = 'menganito'
print(p.nombre) """

class Trabajador1(Persona1):
    def __init__(self, nombre:str, edad:int, salario:float):
        super().__init__(nombre, edad) #para no darle self.nombre... superclase clase padre invoca el constructor de persona
        self.salario = salario

    def __str__(self) -> str:
        return super().__str__() + f", salario={self.salario}"
    
t= Trabajador1('memo', 50, 1000)
print(t)
    
