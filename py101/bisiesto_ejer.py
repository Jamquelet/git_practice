#los años bisiestos tienen 366 dias y son aquellos que son multiplos de 4 y no terminan con dos ceros o aquellos que despues de quitar los dos ceros del final son divisibles por 4(divisibles por 400). por ejemplo 1800 y 1900 no son años bisiestos, sin embargo el año 2000 si lo fue
n = int(input())

if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("Si")
else:
    print("no")