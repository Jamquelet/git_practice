""" La desviación estándar es una medida estadística que indica cuánto se dispersan los valores de un conjunto de datos con respecto a la media o promedio. En otras palabras, mide la dispersión o variabilidad de los valores individuales con respecto a la media de esos valores. Cuanto mayor sea la desviación estándar, mayor será la dispersión de los datos; cuanto menor sea, más cercanos estarán los valores a la media.

El margen de error, en este contexto, se refiere a la precisión con la que se redondea el resultado final. Se establece un margen de error de ±0.1 para indicar que el resultado final debe redondearse a un decimal y permitir una variación máxima de ±0.1 en el valor redondeado. """

""" Dada una lista,X, de N enteros, calcule e imprima la desviación estándar. La respuesta debe estar redondeada a sólo un decimal con un margen de error de 
±0.1.

input
Se proveerá la lista de números como una cadena

output
retornar la desviación estándar

input sample 1
10 40 30 50 20
output sample 1
14.1 """

""" 
1.Parsear la entrada para obtener una lista de enteros. Convertimos la cadena de entrada en una lista de números enteros utilizando la función map para aplicar la conversión int a cada elemento.
2.Calcular la media (promedio) de los números en la lista. Se suma todos los números en la lista y se divide entre la cantidad total de números para obtener la media.
3.Calcular la suma de los cuadrados de las diferencias entre cada número y la media.Para calcular la varianza, primero necesitamos las diferencias entre cada número y la media. Al elevar al cuadrado estas diferencias, obtenemos los términos que se sumarán para calcular la varianza. Esto se realiza utilizando la función map.
4.Calcular la varianza dividiendo la suma de los cuadrados entre la cantidad total de elementos. La varianza se calcula sumando los cuadrados de las diferencias calculadas en el paso anterior y dividiendo el resultado entre la cantidad total de números. Esto se hace utilizando la función reduce.
5.Calcular la desviación estándar tomando la raíz cuadrada de la varianza.La desviación estándar es simplemente la raíz cuadrada de la varianza calculada en el paso anterior.
6.Redondear el resultado a un decimal con un margen de error de ±0.1. redondeamos el valor de la desviación estándar a un decimal con el margen de error especificado.

La suma de los cuadrados de las diferencias y el cálculo de la varianza son pasos necesarios para determinar la dispersión y variabilidad de los datos con respecto a la media. La varianza nos dice cuánto se extienden los valores individuales con respecto a la media, y la desviación estándar es simplemente la raíz cuadrada de la varianza, lo que la convierte en una medida más interpretable en las mismas unidades que los datos originales.
"""


from functools import reduce
import math

def calculate_std_dev(nums):
    # Paso 1: Parsear la entrada para obtener una lista de enteros
    num_list = list(map(int, nums.split()))

    # Paso 2: Calcular la media (promedio)
    mean = sum(num_list) / len(num_list)

    # Paso 3: Calcular la suma de los cuadrados de las diferencias entre cada número y la media
    squared_diff = list(map(lambda x: (x - mean) ** 2, num_list))

    # Paso 4: Calcular la varianza dividiendo la suma de los cuadrados entre la cantidad total de elementos
    variance = reduce(lambda x, y: x + y, squared_diff) / len(num_list)

    # Paso 5: Calcular la desviación estándar tomando la raíz cuadrada de la varianza
    std_dev = math.sqrt(variance) #la varianza tiene la particularidad de estar en unidades al cuadrado.math.sqrt:raiz cuadrada de un numero

    # Paso 6: Redondear el resultado a un decimal con un margen de error de ±0.1
    rounded_std_dev = round(std_dev, 1) #redondear un número decimal al número entero más cercano. Puedes especificar la cantidad de decimales a la que deseas redondear. es el número de decimales al que deseas redondear. Si no se proporciona este argumento, round() redondeará al número entero más cercano.

    return rounded_std_dev

# Entrada de ejemplo
input_nums = "10 40 30 50 20"
# Calcular y mostrar la desviación estándar
result = calculate_std_dev(input_nums)
print(result)

