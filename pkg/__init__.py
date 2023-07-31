#version anterior a la 3.3 este archivo es obligatorio para que funcionen los paquetes. en las versiones posteriores se utiliza para inicializar alguna variable o importaciones a ese paquete.
# cada vez que se llame al paquete automaticamente se va a inicializar y va crear esa variable 
print('se inicio paquete')

URL = 'platzi.com'

#namespaces
import pkg.mod_1, pkg.mod_2