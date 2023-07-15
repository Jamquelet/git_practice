def find_volume(length=1,width=1,depth=1): #tamaño o altura, ancho y profundidad
    return length*width*depth, width, 'hi!' #devuelve una tupla con esos valores

result = find_volume(width=10)#solo le asigno un valor explicitamente
#asignar variables result, width, text = find_volume(width=10)
#print(result, width, text)

print(result[0])#retorna solo el primer indice de la tupla