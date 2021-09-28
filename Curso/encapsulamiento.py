#En python para definir una variable privada se utiliza __ como prefijo 
#Para acceder al elemento y seguirlo modificando se utiliza GET y SET
#GET es el metodo que vamos a crear de manera publica para leer el valor del atributo
#y SET es el metodo que vamos a crear para poder modificar el valor del atributo
#Las palabras GET y SET son opcionales, puede ser cualquier otro nombre, sin embargo por buenas practicas se utilizan estas
#No es necesario pasar mas parametros al INIT, basta con definirlos en la clase
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = 18
#Se pueden agregar mas atributos a la clase (edad), pero de ser privados hay que definir GET y SET para todos
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad


p1 = Persona("Juan", 18)
#print(p1.__nombre) esto marca un error
print(p1.get_nombre())
print(p1.get_edad())

#p1.__nombre = "Karla" esto marca error
p1.set_nombre("Karla")
p1.set_edad(20)
print(p1.get_nombre())
print(p1.get_edad())