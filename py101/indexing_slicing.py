#indexing= los textos tienen un indicador posiciones
text = "Ella sabe Python"
print(text[0]) #E
print(text[1]) #segunda posicion l
#print(text[9999]) error fuera del rango
size = len(text) # evauar el tamaño del texto
print('size => ', size) #tamaño es de 16
#print(text[size]) #el tamaño es de 16 caracteres pero para ingresar a ellos es desde laposicion 0-15
print(text[size - 1]) # la ultima es la 15
print(text[-1]) # seria lo mismo que indicar size -1 va hasta la ultima posicion tambien -2 -3

#slicing: basados en las posiciones podemos sacar ciertas partes del texto

print(text[0:5]) #sacar la posicion dentro la posicion 0 hasta la 5
print(text[10:16]) #quiero sacar este rango
print(text[:10]) # es como 0:10 desde la posicion 0 hasta la 10
print(text[5:-1]) # desde la posicion 5 hasta el final pero no incluye el ultimo caracter
print(text[5:]) # desde el 5 hasta el final de la cadena
print(text[:]) # va desde el inicio hasta el final
print(text[10:16:2]) # saltos, va desde la 10 a la 16 con dos caracteres de salto
print(text[::2]) #va desde el inicio hasta el final y quiero saltar de a 2 elementos