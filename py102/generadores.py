def primeros_n(n):
    num = 0
    while num < n:
        yield num
        num += 1
    print(num)
suma = sum(primeros_n(3))
print(suma)


##ejemplo: función que imprime la secuencia fibonacci

def fibo_1(n):
    a, b = -1, 1
    for _ in range(n):
        c = a + b
        print(c)
        a, b = b, c

fibo_1(10)#0,1,1,2,3,5,8,13,21,34

#reimplementar con yield
def fibo_2(n):
    a, b = -1, 1
    for _ in range(n):
        c = a + b 
        a, b = b, c
        yield c

f = fibo_2(10)
next(f)

for fib in fibo_2(10):
    print(fib)


# ada
# generar mis primeros n
def primeros_n(n: int):
    num = 0 
    while num < n:
        print(num)
        num +=1
primeros_n(10) # del 0 al 9

#
def primeros_n(n: int):
    num = 0 
    while num < n:
        yield num #generador
        num +=1

for n in primeros_n(10):
    print(n)
print(list(primeros_n(10)))
assert list(primeros_n(10)) == list(range(10))

##secuencia fibonacci . #aureo 0,1,1,2,3,5,8,13,21,34....
def fibo1(n: int):
    a, b = -1, 1
    for _ in range(n):
        c = a + b
        print(c)
        a, b = b, c

fibo1(10)
#generar
def fibo_gen(n:int):
    a, b = -1, 1
    for _ in range(n):
        c = a + b
        a, b = b, c
        yield c

print(list(filter(lambda x: x % 2 == 0, fibo_gen(20))))