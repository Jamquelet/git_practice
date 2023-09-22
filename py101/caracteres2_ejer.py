#códigos ascci = ord("")

c = input()

if len(c) == 1 and c.isalpha():
    if c.isuppe():
        print("Mayuscula")
    else:
        print("minuscula")

    c   = c.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        print("vocal")
    else:
        print("consonante")
else:
    print("entrada invalida")