print(10 // 3) #entero
print (10 % 3)# 10 modulo 3 - 10 entre 3
print(2 ** 3) #2 exponent 3
print(2 ** 3 + 3 - 7 / 1 // 4) # operadores aritmeticos P - paréntesis E - exponentes M - multiplicación D - división A - adición S - sutracción
print('hello' + 'world')
print('hello ' * 3)

# operadores de comparacion - comparators
print(7 > 3)
print(3 > 7)
print(7 > 7) #False
print(5 < 6) # True
print(2>=1)
print(2>=3) 
print(2>=2)
print(1<=2)

# == extrictamente de igualdad
print(3 == 3)
print(5 == 2)
# !=
print(3 != 3)
print(6 != 10)

print("Apple" == 'Apple') #True
print("Apple" == 'apple') #False
print("1" == 1)#False

age = 14
print(age >= 18)

#float
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y) # False

y_str = format(y, ".2g")#que solo tenga 2 digitos
print("str -->", y_str)
print(y_str == str(x)) #True

#de una forma matematica
print('x' * 10) # línea divisoria para separar xD

print(y, x)

tolerance = 0.00001 # margen de error
print(abs(x - y) < tolerance) #sacar el valor absoluto no pueden haber numeros negativos tienen q ser positivos
#restando el x - y para sacar la diferencia 

#operadores lógicos - logic
print('AND')
print('True and True =>', True and True) #True
print('True and False =>', True and False)
print('False and False =>', False and False)
print('False and True =>', False and True)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = input('ingress stock =>')
stock = int(stock)

print(stock >= 100 and stock <= 1000)

print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or False =>', False or False) #False
print('False or True =>', False or True)

role = input('Digita el rol => ')
print( role == 'admin' or role == 'seller')

#not
print(not True) #False
print(not False) #True

print('not True and True =>', not (True and True))
print('not True and False =>', not (True and False))
print('not False and False =>', not(False and False))
print('not False and True =>', not(False and True))

stock = input('ingress stock =>')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))