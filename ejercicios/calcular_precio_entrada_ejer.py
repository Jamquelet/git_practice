#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.

#El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.

#Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5 monedas y si es mayor de 18 años, 10 monedas.

def calcular_precio_entrada(edad):
    if edad < 4:
        return 0
        
    elif edad >= 4 and edad <=18:
        return 5
        
    else:
        return 10
        

edad_cliente = int(input('Ingresa tu edad: '))

precio_entrada = calcular_precio_entrada(edad_cliente)

print("El precio de entrada es:", precio_entrada, "monedas.")