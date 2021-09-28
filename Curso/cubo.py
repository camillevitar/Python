class Cubo:
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def volumen(self):
        return self.largo * self.ancho * self.alto

largo = int(input("Propociona el largo: "))
ancho = int(input("Proporciona el ancho: "))
alto = int(input("Proporciona la altura: "))

cubo = Cubo(largo, ancho, alto)
print("El volumen del cubo es:", cubo.volumen(), "metros cubicos")2