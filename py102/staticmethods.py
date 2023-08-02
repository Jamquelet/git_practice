#el self no es utilizado, una forma de no poner esto ser explicito que este metodo no va a depender de ningun atributo interno de la clase se utiliza staticmethods
#un metodo que no necesita self
#su uso es cuando quieren hacer un metodo que no dependa de nada de la clase 
class Aleatorio: 
    @staticmethod #que es un metodo que no va a cambiar el estado interno de la clase, no requiere una referencia a la clase 
    def generar_aleatorio_con_semillas(semilla):
        return semilla + 1
    
a = Aleatorio()
print(a.generar_aleatorio_con_semillas(42))