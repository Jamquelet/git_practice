#Escribir un programa que pida al usuario un número entero y retorne un triángulo rectángulo como el ejemplo de abajo, de altura que sea el número introducido. Imprimir la cadena retornada por la función.

def generar_triangulo_rectangulo(numero):
    triangulo = ""
    for i in range(1, numero + 1):
        triangulo += "* " * i + "\n"
    return triangulo

numero_entero = int(input("Ingrese un número entero: "))
triangulo_resultante = generar_triangulo_rectangulo(numero_entero)

print(triangulo_resultante)

