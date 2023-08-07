#organizados por filas y columnas
#datos de poblacion mundial en ciertos años
import csv #leer archivos

""" def read_csv(path):
    '''
    leemos cada una de las filas y cada una de ellas viene como un array de datos'''
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #lector. delimiter:es la forma en la que vienen separados los datos ',' ';'
        for row in reader: #iterador para leer fila a fila
            print('***' * 5)
            print(row) #fila

if __name__ == '__main__':
    read_csv('./app/data.csv')
 """
#para que quede en formato diccionario, en donde se pueda acceder con la clave de la columna. Trasformar a una lista de dict, la llave del dict es el nombre de la columna
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #reader es un iterable, la primer fila es el nombre de las columnas
        header = next(reader)
        #print(header)#array con las llaves de la columna

        data = []

        #con zip para unir el header con la row que se esta iterando
        for row in reader: #iterador para leer fila a fila
            iterable = zip(header, row)#union del header con el row, convierte todo el header y el row los une en uno solo uniondolos en un array de tuplas en donde la primer posicion la columna y en la segunda el row 

            #print(list(iterable))

            #generar un dict apartir del iterable
            country_dict = {key: value for key, value in iterable}#tenemos el dict
            #print(country_dict)
            data.append(country_dict)#lista de dict donde tengo clave valor
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    #print(data)
    print(data[0])