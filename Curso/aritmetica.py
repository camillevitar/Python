#vamos a agregar atributos y metodos
class Aritmetica:
#Procedemos a iniciar nuestra clase con init y el primer parametro se recomienda que sea self aunque no es obligatorio
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    #Todos los parametros de la clase deben ser iniciados con self
    def sumar(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2

#Creamos un nuevo objeto de la clase
#En el objeto el atributo SELF lo pasa de manera automatica python
aritmetica = Aritmetica(2, 4)
print("Resultado de la suma:", aritmetica.sumar())