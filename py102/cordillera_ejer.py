""" Dada los puntos de altura de una imagen simplificada, contar cuantas picos existen en la imagen

Dado que todos los números consecutivos son diferentes tenemos los siguientes casos:

a) 1 2 3
b) 3 2 1
c) 1 3 2
d) 2 1 3

En los casos a y b, tenemos una recta pendiente, así­ que no podemos contar como un pico en la imagen.
El el caso c si tenemos un pico.

  /\
 /  \
/


En el caso d, no tenemos un pico, sino otra montaña que comienza, así­ que no lo podemos contar como un pico.


     /
 \  /
  \/

La entrada consiste de varios casos de prueba Q. Cada caso de prueba tiene:
El numero de puntos N(N≤1000000),
el primero y ultimo tienen el valor 0. SiguenN
 alturas hi≥0≤1000.
Dos alturas consecutivas son diferentes

Ejemplo Entrada
1
9
0 10 0 8 0 3 4 5 0

Salida
Cuantos picos hay en el gráfico
ejemplo Salida
3

 """
 # 3  /
 # 2 /
 # 1/
 # posicion 012


#estructura de datos
q = int(input()) # cuantos casos de prueba voy a ejecutar
for _ in range(q):
    n = int(input()) # cuantos elementos voy a leer
    alturas = [int(a) for a in input().split()] #todos los elementos en este caso alturas
    picos = 0
    for i in range(1, n-1):
        a = alturas[i]
        if alturas[i-1] < a and a > alturas[i+1]:
            picos += 1

    print(picos)