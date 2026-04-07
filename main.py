from clases.herencia2.puente import Puente

def main():
    pt=Puente("Estructura: Puente,", "Material: Acero,", "Altura: 25 mts,", "Estado: Funcionando,", "Longitud: 50000 mts.")
    print(pt)
    pt.alojarPersonas()
    
if __name__ == '__main__':
    main()
    

# 1. yo digo que el atributo de nombre, material, altura y estado, en si todas, ya que para todo se ocupa o tiene lo las cosas para responder esas preguntas 
# 2. la ventaja es que no es necesario repetir mucho codigo ya que lo hereda y nos ahorramos tiempo
# 3. tendria los mismo que estructura, solo le añadiria produnfidad tal vez y resistencia en metodos 
# 4. creo que en el uso de un objeto para orientar a los otros, de esta manera estamos generalizando 