def precios(edad: int):
    # Cambiar el valor de esta variable como corresponde
    if edad < 4:
        return 0
    elif edad >=4 and edad <=18:
        return 5
    else:
        return 10

def triangulo(n: int):
   res = ""

   # Concatenar cada linea a la variable `res`
   for i in range(1, n + 1):
       res += "*" * i + "\n"

   return res

