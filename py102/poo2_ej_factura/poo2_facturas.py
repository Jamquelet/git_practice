#ejecutar main de esta carpeta
from dataclasses import dataclass, field

@dataclass
class Producto:
    nombre: str
    precio_u: float

@dataclass
class Factura:
    nro: int
    cliente: str 
    productos: list[tuple[int, Producto]] = field(default_factory=list) # cada vez que se instancie un nuevo tipo de factura crea una lista de productos desde 0

    def adicionar(self, producto: Producto, cantidad: int):
        self.productos.append((cantidad, producto))

    def buscar(self, nombre_producto:str) -> int:
        '''
        busca un producto dado su nombre
        Args: nombre_producto (str): Nombre del producto
        Returns:
        int: indice del producto si se encuentra, caso contrario -1'''
    
        for i,(_,producto) in enumerate(self.productos): #en cada interaccion voy a tener un producto. #() enumerate voy a tener un desempaquetado anidado. enumerate retorna una tupla
            if producto.nombre == nombre_producto:
                return i
    
        return -1
    
    def total(self):
        ...
        '''
        calcular el precio total de los productos de la factura.
        correr un for sobre los productos y acumular. donde cada iteraccion valide precio * q y acumular eso'''