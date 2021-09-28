#Este archivo va a almacenar la clase 'persona'
#Por buenas practicas las primeras letras de las clases deben estar en mayuscula y los objetos en minuscula

#Con esto estamos definiendo el TIPO PERSONA y pass hace referencia a 'pasar' o 'saltar' 
#Todos los metodos que agreguemos dentro de una clase en python deben recibir como argumento 'self'
class Persona:
 #Vamos a definir los valores de nuestros atributos utilizando la palabra reservada def con un metodo especial que se conoce como init
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

Persona.nombre = 'Camille'
Persona.edad = 26

#Acceder a los valores
print(Persona.nombre)
print(Persona.edad)
#Esto unicamente se ense;a para entender que una clase tambien es un objeto
#Este caso no es comun pero sirve para ver como funcionan los valores y como se asignan

#Creacion de un objeto
persona = Persona('Mariana', 29)
print(persona.nombre)
print(persona.edad)
print(id(persona))

#Creando un segundo objeto
persona2 = Persona('Carlos', 40)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))