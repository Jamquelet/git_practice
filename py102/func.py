def my_print(text):
    print(text*2)
my_print('Hello ')

def suma(a,b):
    print(a+b)
suma(int(input('a')),int(input('b')))

def suma2(a,b):
    my_print(a+b)
suma2(2,5)

#return
def sum_range(min,max): #suma de los numeros entre x,y
    print(min,max)
    sum = 0
    for x in range(min,max):
        sum += x
    return sum

result=sum_range(1,10)
print(result)
result2=sum_range(result,result+10)
print(result2)
sum_range(1,100)