""" debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el total de gastos del año.
Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. """
import csv

def read_csv(path):
    total = 0
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            total += int(row[1])
        return total

response = read_csv('./py103/data.csv')
print(response)