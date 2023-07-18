items=[
    {
        'product': 'camisa',
        'price': 100,
    },
    {
        'product': 'pantalon',
        'price': 200
    },
    {
        'product': 'hat',
        'price': 500
    }]

def add_taxes(item):
    item['taxes']=item['price']*.19
    return item

new_items = list(map(add_taxes,items))
print(new_items)