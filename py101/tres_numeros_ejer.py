#Escribe un programa que lee tres numeros enteros separados por un espacio y los imprime en una linea separados por un espacio en  forma ordenada de menor a mayor.
#pattern matching
#a, b, c = 3, 1, 2
#a, b, c = 3, 1, 2

# a >= b and b >= c
# si x esta en el rango (a, b)
# if a <= x and x <= b ... if a <= x <= b
""" if a > b >= c:
    print(c, b, a)
if a >= c >= b:
    print(b, c, a) """

a, b, c = list(map(int, input().split()))
print(a, b, c)

""" print(type(a))
print(type(b))
print(type(c)) """