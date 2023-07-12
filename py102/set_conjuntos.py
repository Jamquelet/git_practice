#se puede modificar, no tienen un orden, no permite elementos duplicados no lo toma en cuenta
#conjunto vacio
conjunto = set()
conjunto.add(2)# add element
a = {1,2,3}
b = {3,4,5}

#igualdad
print(a == b) #False
#
print(len(a))
#union
c = a | b
#intercesion : son elementos q estan en ambos conjuntos
c = a & b #3
#diferencia: elementos de a que no estan en b
c = a - b
#diferencia simetrica:elementos que estan en a y en b pero que no estan en ambos no sale el 3
c = a ^ b
#si u conjunto es un subconjunto de otro, si un conjunto esta dentro de otro deben estar todos los elementos
c = {1,2,3,4,5}
print(a.issubset(c)) #si a es un subconjunto del conjunto c #True
print(b.issubset(c)) #True
#superconjunto
print(c.issuperset(a)) #si c es el superconjunto de a.True.en c estan todos los elementos de a
#si ambos conjuntos son disconexos. que no comparten ningun elemento en comun
print(a.isdisjoint(b)) #False conjunto a y b comparten elemento de 3 no son disconexos
#conjuntos inmutables
a = frozenset({1,2,3})
# remove
a.remove(3)

