from clases.herencia2.puente import Puente

def main():
    pt=Puente("Golden gates", "Acero", "1000 mts", "funcionando", "50000 mts")
    print(pt)
    pt.construir()
    pt.inspeccionar()
    pt.mostrarInformacion()
    pt.alojarPersonas()
    

