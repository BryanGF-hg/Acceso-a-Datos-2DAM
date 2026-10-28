#pip install mysql-connector-python
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="app_biblioteca",
    password="Biblio_2026",
    database="biblioteca"
)
cursor = conexion.cursor()

# PASO 4: Listar todos los libros
cursor.callproc("listar_libros", ())

print("=== Listado de libros ===")

for resultado in cursor.stored_results():
    for id_libro, titulo, autor, ejemplares in resultado.fetchall():
        print(
            f"{id_libro} - {titulo} ({autor}) - "
            f"{ejemplares} ejemplares"
        )


# PASO 5: Buscar libros por autor
print()
print("=== Libros de Federico García Lorca ===")

cursor.callproc("buscar_por_autor", ("Federico García Lorca",))

for resultado in cursor.stored_results():
    for titulo, ejemplares in resultado.fetchall():
        print(f"{titulo} - {ejemplares} ejemplares")


# PASO 6: Contar libros
print()
print("=== Total de libros ===")

resultado = cursor.callproc("contar_libros", (0,))
print(f"Hay {resultado[0]} libros en la biblioteca")


# PASO 8: Prestar el libro 1
print()
print("=== Préstamo del libro 1 ===")

try:
    cursor.callproc("prestar_libro", (1,))
    conexion.commit()
    print("Préstamo registrado")

except mysql.connector.Error as e:
    conexion.rollback()
    print(f"Error: {e.msg}")


# Intentar prestar el libro 4, que no tiene ejemplares
print()
print("=== Préstamo del libro 4 ===")

try:
    cursor.callproc("prestar_libro", (4,))
    conexion.commit()
    print("Préstamo registrado")

except mysql.connector.Error as e:
    conexion.rollback()
    print(f"Error: {e.msg}")


# PASO 9: Comprobar los permisos
print()
print("=== Prueba de permisos ===")

try:
    cursor.execute("SELECT * FROM libros")
    print("La consulta directa se ha ejecutado")

except mysql.connector.Error as e:
    print(f"Acceso denegado: {e.msg}")


# Cierre de recursos: siempre al final
cursor.close()
conexion.close()

