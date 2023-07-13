# d, m, a = list(map(int, text.split()))
# lista = list(map(int, text.split()))
""" 
Un municipio ha tomados exámenes a los estudiantes del colegios y ha obtenido los resultados de sus habilidades verbales y numéricas. Le piden decir cuantos estudiantes están por debajo del promedio.

Para hallar el promedio se deben sumar los resultados de Las habilidades numéricas y verbales de cada estudiante.

Por ejemplo tenemos cuatro estudiantes con habilidades verbales 200,250,700,700 y habilidades numéricas 400,400,400,400, el promedio es 600+650+1100+1100/4 = 862.5 por lo que dos estudiantes están por debajo del promedio. 
output
Por cada caso de prueba escriba en numero de estudiantes que están por debajo del promedio.
"""


def estudiante_por_debajo_del_promedio(hab_verbales, hab_numericas):
    n = len(hab_verbales)
    prome = (sum(hab_verbales) + sum(hab_numericas)) / n
    estudiantes_bajo_promedio = 0

    for i in range(n):
        habilidades_totales = hab_verbales[i] + hab_numericas[i]
        if habilidades_totales < prome:
            estudiantes_bajo_promedio += 1
        
    return estudiantes_bajo_promedio

text1 = input('ingrese notas habilidades verbales separadas por espacios ')
lista1 = list(map(int, text1.split()))
text2 = input('ingrese notas habilidades númericas separadas por espacios ')
lista2 = list(map(int, text2.split()))

hab_verbales = lista1
hab_numericas = lista2

estudiante_por_debajo_del_promedio = estudiante_por_debajo_del_promedio(hab_verbales, hab_numericas)
print(estudiante_por_debajo_del_promedio)

''' solucion test
def calcular_promedios(verbales: str, numericas: str) -> int:
    verbales = list(map(int, verbales.split()))
    numericas = list(map(int, numericas.split()))
    n = len(verbales)
    prome = (sum(verbales) + sum(numericas)) / n
    estudiantes_bajo_promedio = 0
    
    for i in range(n):
        habilidades_totales = verbales[i] + numericas[i]
       
        if habilidades_totales < prome:
            estudiantes_bajo_promedio += 1
   
    return estudiantes_bajo_promedio


'''