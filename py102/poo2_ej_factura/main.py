from poo2_facturas import Factura, Producto

def main():
    papas = Producto('papitas', 10.85)
    pollo = Producto('pollo', 18.0)
    pepsi = Producto('pepsi', 10.5)
    pizza = Producto('pizza', 23.5)

    f= Factura(123, 'Pepito')
    f.adicionar(papas, 3)
    f.adicionar(pizza, 5)
    f.adicionar(pollo, 2)
    f.adicionar(pepsi, 1)
    f.adicionar(pepsi, 1)

    print(f"{f.buscar('papitas')=}") #el = imprime la expreccion y su valor

    print(f)

if __name__ == '__main__':
    main()