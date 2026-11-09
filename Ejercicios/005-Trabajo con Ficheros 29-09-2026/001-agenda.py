import csv

class Agenda:
  archivo = "agenda.csv"
  def __init__(self,archivo):
    self.archivo = archivo
  def guardar(self,nombre,telefono):
    archivo = open("self.archivo","a")
    archivo.write(nombre + "," + telefono + "\n")
    archivo.close()
  def leer(self):
    archivo = open("self.archivo","r")
    for i in archivo:
      datos = i.strip().split(",")
      print("Nombre:",datos[0],"-Telefono:",datos[1])
    archivo.close()  
  def contar(self):
    total = 0
    archivo = open("self.archivo","r")
    for i in archivo:
      total += 1
    archivo.close()   
    return total
    
      
def main():
  print("--MI AGENDA--")
  agenda = Agenda("agenda.csv")
  agenda.guardar("Marta", "611222333")
  agenda.guardar("Pablo", "622333444")
  agenda.guardar("Lucia", "633444555")
  agenda.leer()
  print("Tengo", agenda.contar(), "amigos")
  
if __name__ == "__main__":
  main()    
