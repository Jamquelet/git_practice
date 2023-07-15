#local scope => enclosing scope => global scope => built-in 

price = 100 #alcance global 

""" def increment():
    price = 200
    price = price + 10
    print(price)
    return price

print(price)
price2 = increment()
print(price2) """
def increment():
    price = 200
    result = price + 10
    print(result)
    return result

print(price)
price2 = increment()
print(price2) 
