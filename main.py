from clases.herencia2.puente import Puente

def main():
    pt=Puente("Golden gates", "Acero", "1000 mts", "funcionando", "50000 mts")
    print(pt)
    pt.construir()
    pt.inspeccionar()
    pt.mostrarInformacion()
    pt.alojarPersonas()
    
if __name__ == "__init__":
    main()
    

# 1. yo digo que el atributo de nombre, material, altura y estado, en si todas, ya que para todo se ocupa o tiene lo las cosas para responder esas preguntas 
# 2. la ventaja es que no es necesario repetir mucho codigo ya que lo hereda y nos ahorramos tiempo
# 3. tendria los mismo que estructura, solo le añadiria produnfidad tal vez y resistencia en metodos 
# 4. creo que en el uso de un objeto para orientar a los otros, de esta manera estamos generalizando 