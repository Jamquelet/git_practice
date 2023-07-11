#Crear una función que verifique que una cadena está contenida en otra (Sin usar la instrucción in)

#Esta función verificar_contenido toma dos cadenas como parámetros: cadena1 y cadena2. Compara la subcadena de cadena2 que tiene la misma longitud que cadena1 con cadena1 en cada iteración del bucle while. Si la subcadena coincide con cadena1, devuelve True. Si no se encuentra ninguna coincidencia después de recorrer toda cadena2, devuelve False.

def verificar_contenido(cadena1, cadena2):
    indice = 0
    while indice < len(cadena2):
        if cadena2[indice:indice + len(cadena1)] == cadena1:
            return True
        indice += 1
    return False


""" La función toma dos parámetros: cadena1 y cadena2. Estas son las dos cadenas que deseas comparar.

La función inicializa una variable llamada indice con el valor 0. Esta variable se utilizará para iterar a través de los caracteres de cadena2.

La función entra en un bucle while que se ejecuta mientras el indice sea menor que la longitud de cadena2.

Dentro del bucle, la función compara la subcadena de cadena2 que comienza en el índice actual (indice) y tiene la misma longitud que cadena1. Para hacer esto, utiliza la sintaxis de rebanado de cadenas en Python: cadena2[indice:indice + len(cadena1)].

Si la subcadena obtenida es igual a cadena1, significa que cadena1 está contenida en cadena2. En ese caso, la función devuelve True.

Si no se encuentra ninguna coincidencia después de recorrer toda cadena2, es decir, el bucle while se ha ejecutado completamente, la función sale del bucle y devuelve False.

En resumen, la función verificar_contenido recorre cada posible subcadena de cadena2 con la misma longitud que cadena1 y las compara con cadena1. Si alguna de las subcadenas coincide con cadena1, la función devuelve True, indicando que cadena1 está contenida en cadena2. Si no se encuentra ninguna coincidencia, devuelve False. """