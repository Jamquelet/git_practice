#el programa termina si ahy algun error
#print(0/0)) #SyntaxError: unmatched ')'
#print(0/0) # ZeroDivisionError: division by zero
#print(result) #NameError: name 'result' is not defined

""" suma = lambda x, y: x + y
assert suma(2,2)== 5 """#assert = verificacion sencilla . AssertionError

""" age = 10
if age < 18:
    raise Exception('No se permiten menores de edad') """#lanzar error propio

#manejo y control de excepciones _ errores
#capturar error
try: 
    print(0 / 0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad') 
except Exception as error:
    print(error)


#un solo try, al capturar un solo error los demas no se ejecutan y puedo seguir con mi codigo
try:
    print(0 / 0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad') 
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

##
def my_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "No se puede dividir por 0"
    return result

response = my_divide(10, 2)
print(response) #5
response = my_divide(10, 0)
print(response) #No se puede dividir por 0