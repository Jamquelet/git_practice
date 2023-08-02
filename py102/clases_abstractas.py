#patrones de diseño
#es la plantilla de donde se van a sacar copias
#interfaz- sino tiene esta estructura no sirve

from abc import ABC, abstractmethod  #Abstrac Base Class

class Auth(ABC): # ej autenticacion

    @abstractmethod
    def login(self, credenciales):
        ...

    @abstractmethod
    def logout(self):
        ...

class Google(Auth):
    def login(self, credenciales):
        print("Te autenticaste con Google")

    def logout(self):
        print("Adios Google")

class Facebook(Auth):
    def login(self, credenciales):
        print("Te autenticaste con Facebook")

    def logout(self):
        print("Adios Facebook")

def autenticar(arg1=None, arg2=None, autenticador: Auth=None):
    autenticador.login("hola")

autenticar(autenticador=Facebook())