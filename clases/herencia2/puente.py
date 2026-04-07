from clases.herencia1.estructura import Estructura
class Puente(Estructura):
    def __init__(self, nombre, material, altura, estado, longitud):
        super().__init__(nombre, material, altura, estado)
        self.longitud = longitud
        
    def __str__(self):
        return super().__str__()+" "+str(self.longitud)
    
    def alojarPersonas():
        print("El puente está soportando carga")
        
