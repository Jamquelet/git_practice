orders = {}

def store_order(client_name, products):
    if client_name in orders:
        return False  # La orden ya ha sido registrada previamente

    orders[client_name] = products
    return True  # La orden se almacenó correctamente

# Ejemplo de uso
order1 = ("Cliente 1", ["Producto A", "Producto B"])
order2 = ("Cliente 2", ["Producto C", "Producto D"])

print(store_order(*order1))  # True
print(store_order(*order1))  # False (orden duplicada)
print(store_order(*order2))  # True

## test_lab
#archivo solution 
""" from typing import Tuple


db = set()


def almacenar_orden(orden: Tuple[str, ...]) -> bool:
    if orden in db:
        return False # La orden ya ha sido registrada previamente
    db.add(orden)
    return True # La orden se almaceno correctamente
    pass 

 """
 #archivo test-lab-4
"""  from solution import almacenar_orden, db


def test_almacenar_orden_nueva():
    orden_nueva = ("Cliente A", "Pizza", "Refresco", "Helado")
    assert almacenar_orden(orden_nueva) == True


def test_almacenar_orden_existente():
    orden_existente = ("Cliente B", "Hamburguesa", "Papas Fritas")
    db.add(orden_existente)
    assert almacenar_orden(orden_existente) == False


def test_almacenar_orden_misma_persona():
    orden_misma_persona = ("Cliente A", "Hamburguesa", "Refresco")
    db.add(orden_misma_persona)
    assert almacenar_orden(orden_misma_persona) == False
 """