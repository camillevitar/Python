#Por buenas practicas se usa SELF al iniciar la clase
#Pero como vemos a continuacion podemos definir otro parametro de inicio de la clase
#En este caso lo haremos con this
#Para incluir una tupla en esta lista se puede hacer con * y llamando a la lista de valores
#Para incluir un diccionario podemos usar **
# * y ** Se usa para paramteros opcionales
class Persona:
    def __init__(this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d

    def desplegar(this):
        print("Nombre: ", this.nombre)
        print("Edad: ", this.edad)
        print("Valores (Tupla): ", this.valores)
        print("Diccionario: ", this.diccionario)

p1 = Persona("Juan", 28)
p1.desplegar()
print()

p2 = Persona("Karla", 30, 2,5,8)
p2.desplegar()
print()

p3 = Persona("Paola", 33, 4,9, m="manzana", p="pera", j="jicama")
p3.desplegar()
