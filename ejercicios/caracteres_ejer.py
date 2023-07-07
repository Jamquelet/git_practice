#escriba un programa que lea una lista y diga si esta letra es minuscula, mayuscula y tambien debe indicar si es una vocal o una consonante

c = input()


if c.isupper():
    print("Mayuscula")
else:
    print("minuscula")

c = c.lower()
if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
    print("vocal")
else:
    print("consonante")