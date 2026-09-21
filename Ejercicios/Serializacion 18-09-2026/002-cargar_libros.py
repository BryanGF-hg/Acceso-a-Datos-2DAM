import json
RUTA_FICHERO = "basededatos.dat"
  
def leer_fichero():
  archivo = open(RUTA_FICHERO,'r')
  lineas = archivo.readlines()
  linea = lineas[0]
  archivo.close()
  return linea
  
def deserializar_libros(linea):
  lista = json.loads(linea) 
  return lista   

def main():
  texto_json = leer_fichero()
  print(texto_json)
  print("tipo de dato: ", type(texto_json))
  
  libros = deserializar_libros(texto_json)
  print(libros)
  print("tipo de dato: ",type(libros))

if __name__ == "__main__":
    main()
