#Escribir una función factorial y utilizarla para calcular combinaciones de objetos n!/((n-k)!k!)
#el factorial de 5 se calcula como: 5! = 5 * 4 * 3 * 2 * 1 = 120

""" La función factorial calcula el factorial de un número dado utilizando una llamada recursiva. La función combinaciones utiliza el factorial para calcular las combinaciones de n objetos tomados de k en k. Verifica primero si n es menor que k, y si es así, devuelve un mensaje de error. De lo contrario, utiliza la fórmula de combinaciones n!/((n-k)!k!) para calcular el resultado. """

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combinaciones(n, k):
    if n < k:
        return "Error: n debe ser mayor o igual a k"
    else:
        numerador = factorial(n)
        denominador = factorial(n - k) * factorial(k)
        combinaciones = numerador / denominador
        return combinaciones


n = 5
k = 2
resultado = combinaciones(n, k)
print("El resultado es:", resultado)

""" En matemáticas y estadísticas, las combinaciones representan una forma de seleccionar objetos de un conjunto sin tener en cuenta el orden. La fórmula para calcular el número de combinaciones de "n" objetos tomados de "k" en "k" se expresa como:

n! / ((n-k)! * k!)

Donde "n!" es el factorial de "n", "(n-k)!" es el factorial de la diferencia entre "n" y "k", y "k!" es el factorial de "k".

La función factorial nos permite calcular el factorial de un número dado. Por ejemplo, el factorial de 5 sería:

5! = 5 * 4 * 3 * 2 * 1 = 120

La función factorial se puede utilizar para calcular el factorial de "n", "(n-k)", y "k" en la fórmula de las combinaciones. Al dividir el factorial de "n" entre el producto de los factoriales de "(n-k)" y "k", obtenemos el resultado de las combinaciones de "n" objetos tomados de "k" en "k". """

##calcular el factorial de n
from functools import reduce
reduce(lambda x, y: x *y,range(1,5))

