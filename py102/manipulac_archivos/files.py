""" file = open('./text.txt')

#print(file.read()) #leer archivo completo
print(file.readline())#leerlo linea a linea
print(file.readline())#linea 2

file.close()
 """
#como no sabemos cuantas lineas tiene el archivo lo ingresamos a un for
""" file = open('./text.txt')

for line in file:
    print(line)

file.close() """

""" with open('./text.txt') as f: #cierra el archivo automaticamente
    for line in f:
        print(line) """

#escribir en el archivo
""" with open('./text.txt', 'r+') as f: #permisos de lectura y de escritura rplus agrega lineas
    for line in f:
        print(line)
    f.write('nuevas cosas en este archivo\n')# lo agrega al final del archivo toca agregarle salto de linea
    f.write('otra linea\n') """
#sobreescribe 'w+' reescribe el archivo
with open('./text.txt', 'w+') as f: #permisos de lectura y de escritura rplus agrega lineas
    for line in f:
        print(line)
    f.write('nuevas cosas en este archivo\n')# reemplaza todo el contenido
    f.write('otra linea\n')