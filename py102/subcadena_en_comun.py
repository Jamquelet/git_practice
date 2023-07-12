#dadas dos cadenas determine si comparten una subcadena en comun, una subcadena puede ser tan pequeña como un caracter

## convertilo en con conjunto para iterarlo
def twoStrings (s1, s2):
    conjunto = set() # cada elemento de la cadena lo mandamos a un conjunto
    for c in s1: # 
        conjunto.add(c) # metiendole todos los caracteres de s1 al conjunto

    for c in s2:
        if c in conjunto:
            return "YES"
    return "NO"

## solucion 2 ahora la solucion como un diccionario c:caracter d:diccionario
#d.get("a",0)  dame a y si a no exite dame un 0 
#defaultdict 

def twoString(s1, s2):
    d = {}
    for c in s1: #para cada caracter en la cadena
        d[c] = d.get(c,0) +1 #a esta pocision o a este caracter, cuantas veces ya la vi antes si ya existe dame el conteo de veces que lo vi sino retorna 0 y aumentale 1, estoy contando cuantas veces vi este caracter

    for c in s2:
        if d.get(c,0) > 0:#si este caracter ya lo vi antes, debe ser 0 caso contrario dame 0
            return "YES"
    
    return "NO"