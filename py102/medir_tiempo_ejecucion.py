import time #crear un decorador que diga cuanto demora en ejecutar nuetra funct
from typing import Callable

def medir_tiempo(func: Callable):
    def wrapper(*args, **kwargs):#argumentos arbitrarios y argumentos nombrados: la funcion recibe lo que sea como elemento posicional
        start = time.perf_counter()#tiempo trascurrido hasta ahora. retorna el valor en seg fraccionales, poder calcular a nanosegundos a mucho mas detalle la diferencia en seg
        output = func(*args, **kwargs)

        end = time.perf_counter()#tiempo trascurrido
        print(f"Tiempo trascurrido: {end-start}")

        return output
    return wrapper

""" s = time.perf_counter()
time.sleep(3) # le digo a la app  q se duerma por 3 seg
e = time.perf_counter()

print(e-s) """

""" @medir_tiempo
def dormir():
    print("ME DORMIRé")
    time.sleep(1)
    print("Desperté")

dormir()
 """
@medir_tiempo
def sumar_pesado(n: int):
    '''
    sume los primeros n elementos'''
    res = 0
    for i in range(n):
        res += i

    return res

res = sumar_pesado(10000000)
print(f"el resultado de la suma es: {res}")

