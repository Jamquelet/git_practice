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