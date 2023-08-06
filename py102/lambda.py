#tambien llamadas funciones anonimas
#lambda argumentos:valor retorno
def increment (x):
    return x+1

result = increment(10)
print(result)
#
increment_v2 = lambda x: x+1
result2 = increment_v2(20)
print(result2)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}' #title primeras letras de la palabra en mayuscula

text = full_name('nicolas', 'perez casas')
print(text)

###
cubo = lambda n: n**3

print(cubo(3))#27

##cubos del 1 al 20
cubos = list(map(lambda n: n**3, range(1,10)))
print(cubos)#[1, 8, 27, 64, 125, 216, 343, 512, 729]

#con un for seria:
for c in map(lambda n: n**3, [1,2,3]):
    print(c)

