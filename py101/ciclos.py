# for

for i in range(1,4):
    print(i)

""" for(int i = 0; i<n; i++){
    #codigo
} """
    
print("numbers of 1-10")
for i in range(1,11):
    print(i)

print("numeros del 1 al 10 2da version")
for i in range(0,10):
    print(i+1)

print("cuenta de 2 en 2")
for i in range(0, 12, 2):
    print(i)

print("cuenta regrasiva")
for i in range(10, -1, -1):
    print(i)

for num in reversed(range(10)):
    print(num, end=" ")

for i in range(0, 10):
    print("procesando...")
    if i % 2 == 1:
        continue
    print(i, " ", end="")
    print("es un numero par.")

#impriman los números primos del 2 al 1000
for n in range(2, 1000):
    primo = True
    for div in range(2, n):
        if n%div == 0:
            primo = False
            break
    if primo:
        print(n, end=" ")

#
cad = "hola"
for char in reversed(cad):
    print(char)

#
frase = "anita lava la tina"
contador= 0

for c in frase:
    if c == "a":
        contador = contador +1
print("Cantidad de a:", contador)

#cantidad de vocales
frase = "hola como estas"
contador = 0
for f in frase:
    if f=='a' or f=='e' or f=='i' or f=='o' or f=='u':
        contador = contador +1
print("Cantidad de vocales", contador)
print(frase[14]) #s

#calcular la suma de todos los numeros pares hasta n
n = int(input("ingrese un número: "))
suma = 0
for i in range(2,n+1,2):
    suma+=i
print("la suma de todos los numeros pares hasta", n, "es:", suma)


#while

num=0
print("comenzando impresion")
while num<10:
    print(num, end=" ")
    num+=1
print("finaliza")

num=0
while True:
    print(num, end=" ")
    num+=1
    if num == 10:
        break

n = 0
while n<10:
    #n = n + 1
    n +=1
    print(n)

n = 10
while n > 0:
    n-=1
    print(n)

n = 0
while n < 100:
    n+=2
    print(n)

