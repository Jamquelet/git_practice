text = 'Ella sabe programar en Python'
print('JavaScript' in text) #False
print('Python' in text) #verifica si un subtexto esta dentro del string

if 'python' in text:
    print('Elegiste bien!!')
else:
    print('no esta en el string')

size = len('amor') #evaluar el tamaño de un string - examina el tamño en el numero de caracteres 
print(size)


print(text)
print(text.upper()) #pasa todo a mayusculas
print(text.lower()) #pasa todo a minusculas 
print(text.count('a'))# contar el numero de veces hay una letra o alg dentro del texto
print(text.swapcase())#trasforma cualquier caracteres, si esta en minus lo pasa a mayus y si esta en mayus lo pasa a minuscula
print(text.startswith('Ella'))#contesta en forma booleana si el texto inicia con algo en especifico
print(text.endswith('Rust')) # nuestra palabra final es ' '
print(text.replace('Python', 'Go')) #reemplazar cambiar una cosa por otra

texto_2 = 'este es un titulo'
print(texto_2)
print(texto_2.capitalize()) #poner el primer caracter en mayuscula
print(texto_2.title()) #poner el inicio de cada una de las palabras que hay en mayuscula
print(texto_2.isdigit()) #si este texto es un digito
print("121213".isdigit()) #True