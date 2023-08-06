#programacion funcional = inmutabilidad, funciones
#decoradores

def suma(a: float, b: float):
    return a + b
print(suma(3, 5))


#
from typing import Callable

def externa()-> Callable:
    '''
    llamable, imbocable, la funct ext devuelve algo '''
    def interna():
        print('Hola!')
    return interna

f = externa()
f()

#

from typing import Callable

def externa(init: int)-> Callable[[int], int]: #recive un entero y retorna un retorna un entero
    '''
    llamable, imbocable, la funct ext devuelve algo '''
    def interna(to_add: int): #recive entero retorna entero
        return init + to_add
    return interna

f = externa(3)
print(f(5))#8
print(f(8))#3+8=11

#anonymous functions = cerradura

#decorador: recive funcion como arg
from typing import Callable
def decorador(func: Callable):
    def wrapper(): #envoltorio sobre la func, antes y despues durante la func
        print("Antes")

        resultado = func()

        print("Despues")
        return resultado
    return wrapper

##
def saludar():
    print("Hola")

envuelto = decorador(saludar)
envuelto()

#syntactic sugar: decoradores : ayuda de sintaxis
@decorador
def saludar2():
    print("Hello there 2")

saludar2()

##
#argumentos arbitrarios 
def func_arbitrarios(*args):#devuelve una tupla
    print(args)

func_arbitrarios(1,2,3,4,'a')
#
def func_arbitrario(*args):
    a,b = args
    print(a)
    print(b)
func_arbitrarios(1,2)
#
def func_arbitrario(*args):
    print(args) #devuelve tupla
    print()
    print(*args) #devuelve los valores
func_arbitrario(1,'a', 2, 'dad')
print(1,'a', 2, 'dad')
#argumentos nombrados keyword arguments **kward - arroja un dict
def func_kwords(a:int, b:int):
    return a,b

func_kwords(b=2,a=1)
#
def func_kwords(**kwargs):
    print(kwargs)

func_kwords(patito=2, var_1=3, var_2="hello")

#permite sintaxis declarativa. 
#cuando no se ejecuta hasta que se necesita

for i in range(10):
    print(i)

range(10) #es un objeto prezoso no se evalua hasta q se lo pida

it= iter(range(10))
print(next(it))