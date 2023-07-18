matriz = [
    [1,2,3],[4,5,6],[7,8,9]
    ]
print(matriz[0])
print(matriz[0][1])

for row in matriz:
    print(row)
    for column in row:
        print(column)

#

matriz_ada= []
#dimenciones filas y columnas
filas = 3
columnas = 4
#crear cada fila como una lista y agregarla a la matriz
for _ in range(filas):
    fila=[]
    print(fila)
    for _ in range(columnas):
        fila.append(0)
    matriz_ada.append(fila)

print(matriz_ada)
#utilizando list comprehension
matriz2 = [
    [0 for j in range (columnas)]
    for i in range(filas)
    ]
#fila,columna
matriz_ada[0][0] = 1
print(matriz_ada) 