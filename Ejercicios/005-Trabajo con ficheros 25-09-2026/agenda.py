#EJERCICIO 1: agenda.py
import csv

class Agenda:
  def __init___(self,archivo):
    self.archivo = archivo

      
  def guardar(self,nombre,telefono):
    archivo = open(archivo, 'a')
    archivo.write(nombre + "," + telefono + "\n")
    archivo.close()
    
  def leer(self):
    archivo = open(archivo, 'r')
    archivo.close()
    
  def leer(self):
    archivo = open(archivo, 'r')
    for linea in archivo:
        datos = linea.strip().split(",")
        print("NOmbre:" , datos[0], "- Telefono:", datos[1])
        archivo.close()
          
          	
