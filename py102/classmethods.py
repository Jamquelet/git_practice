#existen ciertos metodos que estan ligados a una clase, se utiliza mucho en test, en pandas se utiliza
#es un metodo que puede llamarse sin necesidad de instanciar la clase, por que es un metodo a nivel de clase no a nivel de objeto o instancia

#ejemplo 
from dataclasses import dataclass

@dataclass
class Date: 
    day: int
    month: int
    year: int

    def to_string(self, day, month, year):
        return f""
