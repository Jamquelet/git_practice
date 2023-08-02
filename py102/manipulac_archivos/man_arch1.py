#abrir archivo
f = open("datos.txt")

#print(f.read()) #lee todo el texto de golpe como si fuera una sola cadena
#print(repr(f.read())) #que me muestre por las comillas. representacion 
""" print(f.readline())#solo lee una linea de un archivo
print(f.readline())
print(f.readline())
 """
linea = None
while linea != "":  # ya no hay espacios vacios
    linea = f.readline() 
    print(linea.strip())

f.close() #siempre cerrarlo
