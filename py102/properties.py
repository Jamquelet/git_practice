#ejemplo numeros complejos
#a + bi #a y b son numeros reales, son los flotantes
#con i² = -1

class Complejo:
    '''
    clase para manipular números complejos'''
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"{self.a} + {self.b}i"
    
    def __add__(self, other: "Complejo") -> "Complejo":
        return Complejo(self.a + other.a, self.b + other.b)
    
    def __mul__(self, other: "Complejo") -> "Complejo":
        '''
        multiplica dos complejos
        args: other complejo:otro operando 
        returns: complejo:retorna la multiplicacion
        '''
        return Complejo(self.a * other.a-self.b*other.b, self.a*other.b+self.b*other.a)

#numeros complejos se suman elementos a con a y b con b
c1= Complejo(3,8)
c2= Complejo(9,1)

#print(c1,c2)
print(c1)
print(c2)
print()
#sobrecarga de operadores modificando 
print(c1 + c2)
#print(c1.__add__(c2)) #c2 es el otro
print(c1 * c2)
#print(Complejo(c1.a + c2.a, c1.b + c2.b)) #crear el complejo con def __add__ evito crear esta logica
#print(Complejo(c1.a * c2.a, c1.b * c2.b)) 

