""" Se desea un programa que pueda evaluar polinomios de la forma:

a1xn+an−12xn−1+an−23xn−2......an.

Por ejemplo si queremos evaluar polinomio  1x2+2x+3
con x=1 toma el valor de 6 

En la entrada existen varios casos de prueba. La primera línea tiene el valor 0≤M≤20
que es el número de elementos del polinomio. Separada por un espacio está el número 0≤v≤50
que es donde queremos evaluar el polinomio.

Por cada caso de prueba imprima una línea con un número que representa evaluar el polinomio en el punto dado.

Ejemplo Entrada
3 1
1 2 3
# queremos un polimio con 3 coeficientes y que se evalue con x=1 == 6
#  1*x^2 + 2*x^1 + 3*x^0 == 1*x² + 2*x + 3
#  cuando x vale 1 x=1 => 6

4 2
1 0 0 1
# segundo caso queremos 4 coheficientes
# 1*x³+ 0*x² + 0*x¹ +1*x⁰ == 1*x³ + 1  x=2=> 1*2² +1  ==9

4 3
1 0 1 1

4 3
1 1 1 1 
#4 coheficientes 
# 1*x³ + 1* x² +1*x¹ + 1*x⁰ = 1*x³ + 1* x² +1*x¹ + 1 x=3  == 40
Ejemplo Salida
6.0
9.0
31.0
40.0
"""
#necesitamos que corra hasta que acabe de leer datos podemos hacer un while infinito while True: o importar libreria del sistema
import sys 
for line in sys.stdin: #lee una linea del estandar input infinitamente ctrl + d le digo a la terminal que llegue al final del standar input EOF end of file
#stdin, stdout, stderr: entrada estandar cuando ingresamos datos, cuando hacemos print estamos usando el estandar output, estandar error llo usa la pc para mostrar errores

#grado y valor de x numero de coeficientes y x
    """ 
n, x = list(map(int, input().split())) # lee 3, 1 
coefs= list(map(int, input().split())) # lee 1,2,3

res = 0
for i in range(len(coefs)):
    #print(str(coefs[i])+"x^"+str(n-1-i)+")")# iterar sobre los coheficientes
    res += coefs[i]*x**(n-1-i)
print(float(res))
 """
#otra solucion seria
    n, x = list(map(int, line.split())) # lee 3, 1 
    coefs= list(map(int, input().split())) # lee 1,2,3

    res = 0
    exp = n-1
    for c in coefs:
        res += c*x**exp
        exp -= 1
    print(float(res))