#Funcion de orden superior  HOF, una funcion dentro de una funcion
def increment(x):#recibe un parametro le aumentamos un mas 1 y esa operacion la retornamos
    return x + 1

def higher_o_f(x, func):#recibe un parametro q es x el segundo parametro es una funcion y como es una funcion se ejecuta 
    return x +func(x)

result = higher_o_f(2,increment)#no necesito ejecutarla
"2+(2+1)"
print(result)

#lambda function
increment_v2 = lambda x:x+1
higher_order_function = lambda x, func: x+func(x)
result2= higher_order_function(2,increment_v2)
print(result2)
#
result3= higher_order_function(2, lambda x:x+1)
print(result3)
result4= higher_order_function(5, lambda x:x*5)
print(result4)