#Se le pide escribir un programa para validar fechas del calendario Gregoriano. Es decir él que utilizamos comúnmente. Los años bisiestos tienen 366 días. y son aquellos que son múltiplos de 4 y no terminan con dos ceros, ó que después de quitar los dos ceros del final son divisibles por 4. Por ejemplo 1800, y 1900 no son años bisiestos, sin embargo el año 2000 si lo fue.
#31 dias: enero, marzo, mayo, julio, agosto, octubre y diciembre
# 30 dias : abril, junio, septiembre y noviembre
# 28 dias: febrero
#29 dias : febrero solo si es biciesto

""" date = input()
d, m, a = list(map(int, date.split()))
print(d, m, a)  """

def bisiesto(a):
    if a % 4 == 0 and str(a)[-2:] != '00': #[-2:] muestre los ultimos dos caracteres 
        return True
    elif int(str(a)[:-2])%4 == 0: #[:-2] saca los primeros dos primeros elementos
        return True
    return False

""" resultado = biciesto(1900)
print(resultado) 

mes_31 = [1, 3, 5, 7, 8, 10, 12]
mes_30 = [4, 6, 9, 11]
mes_28 = [2]
"""
def validate_date(date):
    d, m, a = list(map(int, date.split()))
    if m in [1, 3, 5, 7, 8, 10, 12] and (d >= 1 and d <= 31):
        return "Fecha correcta"
    elif m ==2 and bisiesto(a) and (d >= 1 and d <= 29):
        return "Fecha correcta"
    if m in [4, 6, 9, 11] and (d >= 1 and d <=30):
        return "Fecha correcta"
    elif m == 2 and bisiesto(a) and (d >=1 and d <=28):
        return "Fecha correcta"
    else:
        return "Fecha incorrecta"

print(validate_date("6 7 531"))
print(validate_date("4 13 4668"))
print(validate_date("29 2 2000"))

""" bot si pasa, la de la clase no pasa
def es_bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    return False

def validar_fecha(date):
    d, m, a = list(map(int, date.split()))

    # Validar el rango del año
    if a < 1 or a > 9999:
        return "Fecha incorrecta"

    # Validar el rango del mes
    if m < 1 or m > 12:
        return "Fecha incorrecta"

    # Validar el rango del día
    if d < 1 or d > 31:
        return "Fecha incorrecta"

    # Validar febrero en años no bisiestos
    if m == 2 and d > 28 and not es_bisiesto(a):
        return "Fecha incorrecta"

    # Validar febrero en años bisiestos
    if m == 2 and d > 29 and es_bisiesto(a):
        return "Fecha incorrecta"

    # Validar meses con 30 días
    if (m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
        return "Fecha incorrecta"

    return "Fecha correcta"

# Ejemplos de uso
fecha1 = "30 11 1971"
resultado1 = validar_fecha(fecha1)
print(resultado1)

fecha2 = "29 2 2001"
resultado2 = validar_fecha(fecha2)
print(resultado2)
 """