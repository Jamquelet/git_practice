#existen ciertos metodos que estan ligados a una clase, se utiliza mucho en test, en pandas se utiliza
#es un metodo que puede llamarse sin necesidad de instanciar la clase, por que es un metodo a nivel de clase no a nivel de objeto o instancia
#metodo pensado par ser utilizado sin tener que instanciar la clase

#ejemplo 
from dataclasses import dataclass

@dataclass
class Date: 
    day: int
    month: int
    year: int
    
    @staticmethod
    def to_string(day, month, year):#no depende de la clase, simplemente hace algo y ya
        return f"{day}-{month}-{year}"
    
    @classmethod
    def to_format(cls, day, month, year):
        return cls.to_string(cls,day,month,year)
    
    def __str__(self) -> str:
        return self.to_string(self.day, self.month, self.year)

fecha = Date.to_format(20, 7, 2023)
print(fecha)
    
