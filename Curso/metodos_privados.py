#Si utilizamos un _ quiere decir que ese atributo es parcialmente privado o protegido


class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre
        self._apellido_paterno = ape_paterno
        self.__apellido_materno = ape_materno

    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)

p1 = Persona("Juan", "Lopez", "Perez")
