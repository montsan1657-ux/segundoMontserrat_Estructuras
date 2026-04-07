class Estructura(object):
    def __init__(self, nombre, material, altura, estado):
        self.nombre = nombre
        self.material = material
        self.altura = altura
        self.estado = estado

    def __str__(self):
        return self.nombre +" "+self.material+" "+self.altura+" "+self.estado

    def construir(self):
        print("Construyendo")

    def inspeccionar(self):
        print("Inspeccionando")

    def mostrarInformacion(self):
        print("Mostrando información")