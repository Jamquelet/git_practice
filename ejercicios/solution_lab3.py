#Se le pide escribir un programa para validar fechas del calendario Gregoriano. Es decir él que utilizamos comúnmente. Los años bisiestos tienen 366 días. y son aquellos que son múltiplos de 4 y no terminan con dos ceros, ó que después de quitar los dos ceros del final son divisibles por 4. Por ejemplo 1800, y 1900 no son años bisiestos, sin embargo el año 2000 si lo fue.
#31 dias: enero, marzo, mayo, julio, agosto, octubre y diciembre
# 30 dias : abril, junio, septiembre y noviembre
# 28 dias: febrero
#29 dias : febrero solo si es biciesto

""" date = input()
d, m, a = list(map(int, date.split()))
print(d, m, a)  """

def biciesto(a):
    if a % 4 == 0 and str(a)[-2:] != '00': #[-2:] muestre los ultimos dos caracteres 
        return True
    elif int(str(a)[:-2])%4 == 0: #[:-2] saca los primeros dos primeros elementos
        return True
    return False

resultado = biciesto(1900)
print(resultado)

