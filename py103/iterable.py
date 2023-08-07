for i in range(1, 11):
    print(i)

my_iter = range(1, 11)
print(my_iter)#range(1, 11)

my_iter = iter(range(1, 11))
print(my_iter)#<range_iterator object at 0x7f7d75392fd0>

print(next(my_iter))#1 iterar manualmente progresivamente el recurso en memoria no es tan alto
print(next(my_iter))#2
print(next(my_iter))#3

my_iter = iter(range(1, 4))
print(my_iter)
