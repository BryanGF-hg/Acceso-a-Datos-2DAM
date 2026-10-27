import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="lector",
    password="lector123",
    database="biblioteca"
)

cursor = conexion.cursor()
cursor.execute("UPDATE clientes SET nombre = 'Ana Maria' WHERE id = 1;")
conexion.commit()

print("Registro actualizado correctamente.")
cursor.close()
conexion.close()
