
""" def func(entrada: tipo): #restringimos el tipo
    #procesamiento
    return salida #por defect None

def name(parametro):
    """
    #docstring:documentacion de la funcion
"""
    instrucciones
    return
"""
#
def suma(a, b):
    suma = a + b
    return suma
#
def saludar():
    print('hello')
saludar()
#
def saludar(name:str='Ada'):
    print('hello')
saludar()
#
def saludar(name:str='Jam', last_name = 'Perez'):
    print('hello', name, last_name)
saludar('Juan', 'Josp')
#explicita
def saludar(name, last_name='Kent'):#valor por defecto
    print('hello',name,last_name)
saludar(last_name='Juan', name='School')
#devolver valores desde una funcion
def suma(a:int, b:int):
    suma=a+b
    return suma
respuesta=suma(2,3)
print(respuesta)
#
def es_par(a:int):

    """
    función devuelveun booleano que indica si a es par o no.
    a: solo debe ser entero
    """

    if a % 2 == 0:
        return True
    else:
        return False
    
n=5
n_es_par = es_par(n)
print("{} es par?\nRespuesta: {}".format(n, n_es_par))
#print(f"{n} es par?\nRespuesta: {n_es_par}")

#funciones con multiples parametros
def saludar_con_mensaje(name, mensaje1):
    print("Hello", name, ",", mensaje1)
saludar_con_mensaje("Alejandro", "how are you?")
#
def saludar_con_mensaje(name, mensaje1):
    mensaje = "Hello " + name + "," + mensaje1
    return mensaje
resultado = saludar_con_mensaje("Alejandro", "how are you?")
print(resultado)

#pass quiere decir que pasa

#named arguments el orden de los argumentos es importante
def exponencial(base, exponente):
    return base ** exponente #operador de potencia 2 elevado a la 3
print(exponencial(2,3))
# implicito explicito
print(exponencial(base=2,exponente=3))
#o
print(exponencial(exponente=3, base=2))

#argumentos arbitrarios: no sabemos cuantos argumentos tenemos los iteramos
def saludo(*args):#recive una tupla de valores
    print(type(args))
    for nombre in args:
        print("Hello", nombre)
saludo("Ximena","Joel","jamin", 1, 2, 3)
#
def suma2(*args):
    print(args)
    return sum(list(args))
resultado = suma2(2,3,4,5,6)
print(resultado)

#kwargs: argumentos de clave valor almacenados como diccionario
def funcion(*args, **kwargs):
    print(args)
    print(kwargs)
    for arg in args:
        print("arg", arg)
    for llave in kwargs.keys():#diccionario
        print(f"llave: {llave} tiene el valor: {kwargs[llave]}")

funcion("arg1", "arg2", "arg3", kwarg1="Hola", kwarg2="Mundo", reddy="reddy tintaya")
#
def suma(**kwargs):
    if 'a' in kwargs.keys():
        print(True)
    else:
        print(False)
suma(a=1, b=2)
#
def suma(**kwargs):
    if 'a' in kwargs.keys():
        if 'b' in kwargs.keys():
            suma = kwargs['a']+kwargs['b']
            return suma
    return 'no argumentos suficientes'
       
resultado = suma(a=1, b=2)
print(resultado)
# o
def suma(**kwargs):
    """
    funcion para sumar dos numeros a,b
    a:int requerido
    b:int requerido
    """
    print(kwargs)
    if 'a' in kwargs.keys() and 'b' in kwargs.keys():
        suma = kwargs['a'] + kwargs['b']
        return suma
    return 'no argumentos suficientes'

resultado = suma(a=1, b=2)
print(resultado)
#
def suma1(**kwargs):

    valores = kwargs.values()
    return sum(list(valores))

resultado = suma1(a=1, b=2, c=3, d=4)
print(resultado)

#funciones anonimas: no se declara como def
#lambda argumentos: instrucciones
cuadrado = lambda n: n**2
print(cuadrado(4))
print(type(cuadrado))
#
f1 = lambda: print("funcion sin argumentos")
f1()

f2=lambda a,b: a+b
print(f2(2,4))